#!/bin/bash

HOST="fsfsdfdsfsf.com"
OUTPUT_FILE="ping_results.log"


if ping -c 1 "$HOST" &> /dev/null; then
    echo "$(date): $HOST is reachable" >> "$OUTPUT_FILE"
else
    echo "$(date): $HOST is not reachable" >> "$OUTPUT_FILE"
fi
