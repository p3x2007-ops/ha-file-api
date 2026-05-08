#!/usr/bin/with-contenv bashio
# ==============================================================================
# Home Assistant Add-on: File API
# Runs the Flask API server for file operations
# ==============================================================================

bashio::log.info "Starting File API Server..."

# Get configuration
LOG_LEVEL=$(bashio::config 'log_level')
bashio::log.info "Log level: ${LOG_LEVEL}"

# Hotpatch: use latest server.py from source if available
if [ -f /config/addons/file_api/server.py ]; then
    cp /config/addons/file_api/server.py /server.py
    bashio::log.info "Hotpatched server.py from /config/addons/file_api/"
fi

# Run the Python server
exec python3 /server.py
