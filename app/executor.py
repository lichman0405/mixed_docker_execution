# The code is written by Shibo Li, @Miqroera in Shanghai.
# Date: 2025-01-09
# The code is to call subprocess to execute the script.

import subprocess
import logging

class ScriptExecutor:
    def __init__(self, python_executable='python', timeout=10):
        self.python_executable = python_executable
        self.timeout = timeout

        # Configure logging
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def execute(self, file_path, args=None):
        if args is None:
            args = []

        try:
            logging.info(f'Executing script: {file_path} with {self.python_executable}')
            result = subprocess.run(
                [self.python_executable, file_path] + args,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )

            logging.info(f'Successfully executed: {file_path}')
            return {
                'output': result.stdout,
                'error': result.stderr,
                'return_code': result.returncode,
                'success': result.returncode == 0
            }

        except subprocess.TimeoutExpired as e:
            logging.error(f'TimeoutExpired: {file_path} exceeded {self.timeout} seconds.')
            return {
                'output': '',
                'error': f'TimeoutExpired: {str(e)}',
                'return_code': -1,
                'success': False
            }

        except FileNotFoundError:
            logging.error(f'File not found: {file_path}')
            return {
                'output': '',
                'error': f'File not found: {file_path}',
                'return_code': -1,
                'success': False
            }

        except PermissionError:
            logging.error(f'Permission denied: {file_path}')
            return {
                'output': '',
                'error': f'Permission denied: {file_path}',
                'return_code': -1,
                'success': False
            }

        except Exception as e:
            logging.error(f'Unexpected error while executing {file_path}: {str(e)}')
            return {
                'output': '',
                'error': f'Unexpected error: {str(e)}',
                'return_code': -1,
                'success': False
            }
