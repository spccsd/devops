#!/bin/bash

SOURCE="/home/ajay/Desktop/shell code/sourc"
DESTINATION="/home/ajay/Desktop/shell code/dest"


mkdir -p "$DESTINATION/$(date)"
cp -r "$SOURCE" "$DESTINATION/$(date)" && echo "Backup completed on $(date)" || echo "Backup failed on $(date)"
