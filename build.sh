#!/bin/bash
# Check if Python version is at least 3.7

REQUIRED_MAJOR=3
REQUIRED_MINOR=7

PYTHON_VERSION_RAW=$(python3 --version 2>&1)
PYTHON_VERSION=$(echo $PYTHON_VERSION_RAW | awk '{print $2}')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if (( PYTHON_MAJOR > REQUIRED_MAJOR )) || { (( PYTHON_MAJOR == REQUIRED_MAJOR )) && (( PYTHON_MINOR >= REQUIRED_MINOR )); }; then
  echo "Python version OK: $PYTHON_VERSION_RAW"
else
  echo "Error: Python 3.7 or higher is required. Detected version: $PYTHON_VERSION_RAW"
  exit 1
fi

echo "Build complete (No dependencies required, standard library only)."
