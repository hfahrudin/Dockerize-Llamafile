from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import torch
from concurrent.futures import ThreadPoolExecutor
import json
import requests

app = FastAPI(redirect_slashes=False)

BASE_URL = "http://llamafile_service:8080"

# Initialize the thread pool executor
executor = ThreadPoolExecutor()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# STREAMING

@app.post("/stream")
async def stream(request: Request):
    # Clear CUDA cache
    torch.cuda.empty_cache()

    # Parse the incoming JSON payload
    try:
        data = await request.json()
    except Exception as err:
        return JSONResponse(content={"status": "error", "message": f"Invalid JSON: {err}"}, status_code=400)

    full_url = BASE_URL+"/v1/chat/completions" # Replace with your actual endpoint
    headers = {"Content-Type": "application/json"}  # Add any required headers here

    async def stream_response():
        try:
            # Send the POST request to the external API
            response = requests.post(full_url, headers=headers, data=json.dumps(data), stream=True)
            response.raise_for_status()

            # Stream the response data
            for chunk in response.iter_lines():
                if await request.is_disconnected():
                    response.close()
                    break

                # Decode the chunk and yield it
                yield chunk.decode("utf-8") + "\n"

            response.close()
        except requests.exceptions.RequestException as err:
            # Yield an error message if the request fails
            yield f"Error occurred: {str(err)}"

    # Return a StreamingResponse
    return StreamingResponse(stream_response(), media_type="text/event-stream")



@app.get("/health_check")
async def health_check():
    hc_endpoint = f"{BASE_URL}/health"
    try:
        response = requests.get(hc_endpoint)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return {"status": "success", "data": json.loads(response.text)}
    except requests.exceptions.RequestException as err:
        return JSONResponse(content={"status": "error", "message": str(err)}, status_code=500)
