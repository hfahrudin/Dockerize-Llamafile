# Dockerize Llamafile

This repository provides a containerized version of the **LlamaFile** to making it easy to deploy and manage. It also includes an example **Controller Service** built with FastAPI, which demonstrates how to handle incoming logic processed by LlamaFile.

## Features

- **LlamaFile**: The main application, ready for containerized deployment.
- **Controller Service**: A FastAPI-based example service to handle incoming logic and integrate seamlessly with LlamaFile.
- **Docker Support**: Simplifies deployment using Docker Compose.
- **Environment Configuration**: Configurable using `.env` for easy customization.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hfahrudin/Dockerize-Llamafile.git
   cd Dockerize-Llamafile
   ```

2. Configure environment variables:

   - Create a `.env` file in the root directory.

3. Build and start the services:

   ```bash
   docker-compose up --build
   ```

4. Access the Controller Service at `http://localhost:8000` (default).

## Example Request 

Here’s an example request to the Controller Service:

```bash
curl -X GET "http://localhost:8000/health" \
     -H "Content-Type: application/json" \
```

## Customization

- **LlamaFile Configuration**: Update the application in the `llamafile/` directory as needed.
- **Controller Logic**: Modify the FastAPI code in the `controller/` directory to implement custom logic.
- **Docker Compose**: Adjust the `docker-compose.yml` file for your infrastructure requirements.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the [MIT License](https://github.com/hfahrudin/Dockerize-Llamafile/blob/main/LICENSE).

