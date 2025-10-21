# Start from Debian slim
FROM debian:12-slim

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    socat \
    python3 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /

# Copy your binary and Python wrapper
COPY rusty_clock .
COPY generate_flag.py .

# Make them executable
RUN chmod +x ./rusty_clock ./generate_flag.py

# Use Railway-provided PORT environment variable
ENV PORT=8080

# Run socat to forward TCP connections to the Python wrapper
CMD ["sh", "-c", "exec socat TCP-LISTEN:${PORT},reuseaddr,fork EXEC:'./generate_flag.py,stderr'"]
