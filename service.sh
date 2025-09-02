#!/bin/bash

SERVICE="sysstat.service"

if systemctl is-active --quiet "$SERVICE"; then
    echo "running"
else
    echo "not running"
    
fi
