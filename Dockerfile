FROM debian:12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    socat \
    python3 \
    python3-pip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /

COPY rusty_clock .
COPY flag.txt .
COPY generate_flag.py .

RUN chmod +x ./rusty_clock ./generate_flag.py

ENV PORT=8080

CMD ["sh", "-c", "exec socat TCP-LISTEN:${PORT},reuseaddr,fork EXEC:'./generate_flag.py,stderr'"]
