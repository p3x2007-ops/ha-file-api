ARG BUILD_FROM
FROM $BUILD_FROM

# Install Python and dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Install Flask and requests
RUN pip3 install --no-cache-dir flask flask-cors requests

# Copy application files
COPY run.sh /
COPY server.py /

# Make run script executable
RUN chmod +x /run.sh

# Expose port
EXPOSE 8100

# Set working directory
WORKDIR /

# Run the application
CMD ["/run.sh"]
