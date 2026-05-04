#!/usr/bin/with-contenv bashio
# ==============================================================================
# Home Assistant Add-on: File API
# Runs the Flask API server for file operations
# ==============================================================================

bashio::log.info "Starting File API Server..."

# Get configuration
LOG_LEVEL=$(bashio::config 'log_level')
bashio::log.info "Log level: ${LOG_LEVEL}"

# Run the Python server
exec python3 /server.py
