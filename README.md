# Mixed Docker Execution

A FastAPI-based service for securely executing Python code inside a Docker container. This project allows you to submit Python code dynamically, execute it in an isolated environment, and return the results.

## Features

* **Dynamic Code Submission**: Submit Python code via a REST API.
* **Secure Execution**: Code runs inside a Docker container to ensure isolation.
* **Rich Feedback**: Provides output, logs, and error messages for submitted code.
* **Script Timeout and Error Handling**: Handles execution timeouts, syntax errors, and runtime exceptions gracefully.
* **Structured Codebase**: Modularized for better maintainability and extensibility.

## Updates in this Version

* Replaced the old `execute_script` function with the `ScriptExecutor` class for enhanced flexibility and error handling.
* Added detailed logging for script execution and error scenarios.
* Docker integration using a lightweight `Python:3.10-slim` image.
* Updated project structure for better clarity and scalability.

## Project Structure

```
mixed_docker_execution/
├── Dockerfile                # Defines the Docker container
├── app/                      # Application code
│   ├── main.py               # FastAPI main application
│   ├── executor.py           # Code execution logic with ScriptExecutor
├── host_code/                # Mounted directory for user-submitted code
│   ├── sample_script.py      # Example Python script
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

## Prerequisites

* **Docker Installed**: [Download Docker](https://www.docker.com/)
* **Python 3.10+**: Optional, for local development or testing purposes.

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
   docker run --rm -v $(pwd)/host_code:/usr/src/app/host_code -p 8000:8000 mixed-docker-executor
   ```

## Usage

### Submit Code via `curl`

Submit Python code dynamically using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/submit_code" \
-H "Content-Type: application/json" \
-d '{"code": "print(\"Hello from FastAPI!\")"}'
```

### Submit Code via Python

You can also use Python to send a POST request:

```python
import requests

url = "http://127.0.0.1:8000/submit_code"
headers = {"Content-Type": "application/json"}
data = {"code": 'print("Hello from FastAPI!")'}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

### Example Output

#### Success Case:

```json
{
  "status": "success",
  "output": "Hello from FastAPI!\n",
  "error": "",
  "return_code": 0,
  "timeout": false
}
```

#### Error Case (e.g., Syntax Error):

```json
{
  "status": "failure",
  "output": "",
  "error": "SyntaxError: unexpected EOF while parsing",
  "return_code": 1,
  "timeout": false
}
```

#### Timeout Case:

```json
{
  "status": "failure",
  "output": "",
  "error": "TimeoutExpired: Command exceeded 10 seconds.",
  "return_code": -1,
  "timeout": true
}
```

## Configuration

* **Customizing the Python Interpreter**: The `ScriptExecutor` class in `executor.py` allows for specifying the Python interpreter (default: `python3`).
* **Timeout Setting**: You can customize the script execution timeout (default: `10 seconds`) by modifying the `timeout` parameter in `executor.py` or during deployment.
* **Docker Port Mapping**: By default, the service listens on port `8000`. This can be overridden during container execution:
  ```bash
  docker run --rm -p 8080:8000 mixed-docker-executor
  ```

## Testing

### Manual Testing

1. Start the Docker container.
2. Use the provided `curl` or Python examples to submit code and verify the responses.

### Automated Testing

Automated testing with `pytest` will be covered in future updates.

## Limitations

* Currently supports only Python scripts.
* Execution is limited to single-file Python code.
* No authentication implemented for API endpoints.

## Future Improvements

* Add support for other programming languages.
* Implement API authentication for security.
* Integrate CI/CD pipelines for testing and deployment.
* Enhance resource isolation with more robust sandboxing.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Feedback

If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request!
