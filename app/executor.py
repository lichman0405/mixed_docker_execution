# The code is writteng by Shibo Li, @Miqroera in Shanghai.
# Date: 2025-01-09
# The code is to call subprocess to execute the script.

import subprocess

def execute_script(file_path):
    try:
        result = subprocess.run(
            ['python', file_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        return {'output': result.stdout, 'error': result.stderr}

    except subprocess.TimeoutExpired as e:
        return {'output': '', 'error': str(e)}