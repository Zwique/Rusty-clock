# Use a small runtime image
FROM debian:12-slim

# Required packages (if your binary depends on libc only, you can omit some)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy your compiled binary and the flag into the image
# Ensure 'rusty_clock' is statically linked or compatible with the base image.
COPY rusty_clock rusty_clock
COPY flag.txt flag.txt

# Make executable
RUN chmod +x rusty_clock

# Run the binary on container start
CMD ["./rusty_clock"]
