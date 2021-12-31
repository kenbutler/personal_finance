#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

java -jar plantuml.jar -o $SCRIPT_DIR/out -recursive src/* -recursive -checkmetadata