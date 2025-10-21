#!/usr/bin/env python3
import os
import secrets
import sys

# cryptographically secure 32 hex chars
random_hash = secrets.token_hex(16)
flag = f"uacCTF{{wh4t_do35_7h3_cl0ck_s4yyyy_{random_hash}}}"

# write ./flag.txt (keeps compatibility if rusty_clock reads flag.txt)
with open("flag.txt", "w") as f:
    f.write(flag + "\n")

# print to client immediately (flush so socat forwards)
print(flag, flush=True)

# replace this process with the binary so socat is connected to the binary
# preserving our stdout/stderr. Use exec so there's no extra Python parent.
os.execv("./rusty_clock", ["./rusty_clock"])
