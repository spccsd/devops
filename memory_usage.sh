#!/bin/bash

echo "$(ps aux --sort=-%mem | head -n 11)" >> "memory_usage.log"