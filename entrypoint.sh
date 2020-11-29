#!/bin/bash
set -e

source venv/bin/activate
# shellcheck disable=SC2145
echo "echo python3 main.py"
# shellcheck disable=SC2068
exec python3 main.py