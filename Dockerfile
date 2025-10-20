FROM debian:12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    socat \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Everything will live in the root
WORKDIR /

# Copy files from your repo (same level as Dockerfile)
COPY rusty_clock .
COPY flag.txt .

RUN chmod +x ./rusty_clock

# Railway provides the PORT environment variable automatically
ENV PORT=8080

# Listen on PORT and run the binary for each connection
CMD ["sh", "-c", "exec socat TCP-LISTEN:${PORT},reuseaddr,fork EXEC:'./rusty_clock,stderr'"]
