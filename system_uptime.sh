#!/bin/bash

OUTPUT_FILE="system_uptime.log"

echo "$(date): $(uptime -p)" >> "$OUTPUT_FILE"
