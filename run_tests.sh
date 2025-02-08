#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Optional: Print commands and their arguments as they are executed.
# set -x

# 1. Create (or recreate) a Python virtual environment named 'venv'
if [ -d "venv" ]; then
  echo "Removing existing virtual environment 'venv'..."
  rm -rf venv
fi

echo "Creating a new virtual environment..."
python3 -m venv venv

# 2. Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# 3. Upgrade pip and install dependencies
echo "Upgrading pip and installing Black, Flake8, and Pytest..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Define the directories or files to check
#    You can modify these paths as needed.
SRC_DIR="./src"   # where your Python files might live
TEST_DIR="./tests" # separate directory for tests (if you have one)

# 5. Run Black (auto-formatting)
echo "Running Black on $SRC_DIR..."
black --line-length 79 "$SRC_DIR"

# 6. Run Flake8 (linting)
echo "Running Flake8 on $SRC_DIR..."
flake8 "$SRC_DIR"

# 7. Run Tests with pytest
#    You can point pytest directly to a tests directory or just run `pytest`
#    to detect tests automatically. If your tests live in `src/`, just change the directory path.
echo "Running tests with pytest..."
pytest "$TEST_DIR"

# 8. Deactivate the virtual environment (optional)
echo "Deactivating virtual environment..."
deactivate

echo "All done!"
