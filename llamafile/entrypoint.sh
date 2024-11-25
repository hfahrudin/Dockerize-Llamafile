#!/bin/bash

# Debugging: Print environment variables
echo "MODEL_URL: ${MODEL_URL}"
echo "MODEL_NAME: ${MODEL_NAME}"
echo "MODEL_PORT: ${MODEL_PORT}"
echo "MODEL_THREADS: ${MODEL_THREADS}"
echo "MODEL_BATCH: ${MODEL_BATCH}"
echo "MODEL_CONTEXT: ${MODEL_CONTEXT}"
echo "MODEL_NUM_PROCESSORS: ${MODEL_NUM_PROCESSORS}"

# Set default values for environment variables if they are not provided
MODEL_PORT=${MODEL_PORT:-8080}               # Default port to 8080 if not set
MODEL_THREADS=${MODEL_THREADS:-4}           # Default threads to 4 if not set
MODEL_BATCH=${MODEL_BATCH:-4}               # Default batch size to 4 if not set
MODEL_CONTEXT=${MODEL_CONTEXT:-36000}       # Default context size to 36000 if not set
MODEL_NUM_PROCESSORS=${MODEL_NUM_PROCESSORS:-4} # Default number of processors to 4 if not set

# Run the model with the provided or default parameters
exec /bin/bash /app/${MODEL_NAME} \
  --server \
  --nobrowser \
  --host 0.0.0.0 \
  --port ${MODEL_PORT} \
  -ngl 9999 \
  -c ${MODEL_CONTEXT} \
  -np ${MODEL_NUM_PROCESSORS} \
  -cb \
  -t ${MODEL_THREADS} \
  -tb ${MODEL_BATCH}
