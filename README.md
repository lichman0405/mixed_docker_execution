# Mixed Docker Execution

A FastAPI-based service for securely executing Python code inside a Docker container. This project allows you to submit Python code dynamically, execute it in an isolated environment, and return the results.

## Features

- Dynamic Code Submission: Submit Python code via a REST API.
- Secure Execution: Code runs inside a Docker container to ensure isolation.
- Flexible Port Configuration: Port can be customized using environment variables.
- Rich Feedback: Provides output, logs, and error messages for submitted code.

## Project Structure

```
mixed_docker_execution/
├── Dockerfile                # Defines the Docker container
├── app/                      # Application code
│   ├── main.py               # FastAPI main application
│   ├── executor.py           # Code execution logic
├── host_code/                # Mounted directory for code execution
│   ├── sample_script.py      # Example Python script
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

## Prerequisites

- Docker installed ([Download Docker](https://www.docker.com/))
- Python 3.9+ (optional, for testing with the `requests` library)

## Installation

1. Clone the Repository:
   ```bash
   git clone <repository_url>
   cd mixed_docker_execution
   ```

2. Build the Docker Image:
   ```bash
   docker build -t mixed-docker-executor .
   ```

3. Run the Container:
   ```bash
   docker run --rm -v $(pwd)/host_code:/usr/src/app/host_code -p 22499:22499 mixed-docker-executor
   ```

## Usage

### Submit Code via `curl`

Submit Python code dynamically using `curl`:

```bash
curl -X POST "http://<host_ip>:22499/submit_code" \
-H "Content-Type: application/json" \
-d '{"code": "print(\"Hello from FastAPI!\")"}'
```

### Submit Code via Python

You can also use Python to send a POST request:

```python
import requests

url = "http://<host_ip>:22499/submit_code"
headers = {"Content-Type": "application/json"}
data = {"code": 'print("Hello from FastAPI!")'}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

### Example Output

If the code executes successfully, you should receive:

```json
{
  "status": "success",
  "output": "Hello from FastAPI!\n",
  "error": ""
}
```

If there's an error in the code:

```json
{
  "status": "success",
  "output": "",
  "error": "SyntaxError: unexpected EOF while parsing"
}
```

## Configuration

- **Customizing the Port**:
  The default port is `22499`. You can override it using the `PORT` environment variable:
  ```bash
  docker run --rm -e PORT=3000 -p 3000:3000 mixed-docker-executor
  ```

## Testing

To test the service:

1. Start the Docker container as described above.
2. Submit test cases using the provided `curl` or Python examples.

## Limitations

- The service currently supports only Python scripts.
- Execution is limited to single-file Python code.

## Future Improvements

- Add support for other programming languages.
- Implement authentication for API endpoints.
- Enhance logging and debugging capabilities.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Feedback

If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request!