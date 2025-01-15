# The code is written by Shibo Li, @Miqroera in Shanghai.
# Date: 2025-01-09
# The code is the main entry of the application.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .executor import ScriptExecutor
import os
import logging

# Initialize FastAPI
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define the directory to store scripts
MOUNT_DIR = "/usr/src/app/host_code"
if not os.path.exists(MOUNT_DIR):
    os.makedirs(MOUNT_DIR, exist_ok=True)

# Initialize ScriptExecutor
executor = ScriptExecutor(python_executable='python3', timeout=10)

# Define the input model
class CodeInput(BaseModel):
    code: str

@app.post("/submit_code")
async def submit_code(input: CodeInput):
    file_path = os.path.join(MOUNT_DIR, "user_script.py")

    # Save the submitted code to a file
    try:
        with open(file_path, "w") as f:
            f.write(input.code)
        logging.info(f"User script saved to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save user script: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to save the script.")

    # Execute the script
    try:
        result = executor.execute(file_path)
        return {
            "status": "success" if result['success'] else "failure",
            "output": result['output'],
            "error": result['error'],
            "return_code": result['return_code'],
            "timeout": result['return_code'] == -1
        }
    except Exception as e:
        logging.error(f"Error executing user script: {str(e)}")
        raise HTTPException(status_code=500, detail="Error executing the script.")


