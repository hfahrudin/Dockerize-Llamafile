# Use NVIDIA CUDA base image (Ubuntu 22.04 and CUDA 12.3.2)
FROM nvidia/cuda:12.3.2-base-ubuntu22.04

# Set the working directory inside the container
WORKDIR /app

# Build-time arguments for model URL, model name, and other model parameters
ARG MODEL_URL
ARG MODEL_NAME
ARG MODEL_PORT
ARG MODEL_THREADS
ARG MODEL_BATCH
ARG MODEL_CONTEXT
ARG MODEL_NUM_PROCESSORS

# Set environment variables for runtime (can be overridden by docker-compose)
ENV MODEL_URL=${MODEL_URL}
ENV MODEL_NAME=${MODEL_NAME}
ENV MODEL_PORT=${MODEL_PORT}
ENV MODEL_THREADS=${MODEL_THREADS}
ENV MODEL_BATCH=${MODEL_BATCH}
ENV MODEL_CONTEXT=${MODEL_CONTEXT}
ENV MODEL_NUM_PROCESSORS=${MODEL_NUM_PROCESSORS}

# Install essential packages
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    curl \
    vim \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Download the model file from the specified URL and save it with the specified name
RUN wget ${MODEL_URL} -O /app/${MODEL_NAME}

# Make the downloaded file executable
RUN chmod +x /app/${MODEL_NAME}

# Copy an entrypoint script into the container
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Verify the downloaded model file and entrypoint script
RUN ls -la /app

# Expose port 8080 as per docker-compose configuration
EXPOSE ${MODEL_PORT}

# Set the entry point to run the downloaded model or custom script
ENTRYPOINT ["/app/entrypoint.sh"]
