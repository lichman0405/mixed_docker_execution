# The code is writteng by Shibo Li, @Miqroera in Shanghai.
# Date: 2025-01-09
# The code is the main entry of the application.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from executor import execute_script
import os


# init FastAPI
app = FastAPI()

# mount the path
MOUNT_DIR = "/usr/src/app/host_code"

# Input script model
class CodeInput(BaseModel):
    code: str

@app.post("/submit_code")
async def submit_code(input: CodeInput):
    try:
        file_path = os.path.join(MOUNT_DIR, "user_script.py")
        with open(file_path, "w") as f:
            f.write(input.code)
            f.close()

        result = execute_script(file_path)

        return {
            "status": "success",
            "output": result['output'],
            "error": result['error'],
        }

    # throw error with specific status code and information
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
