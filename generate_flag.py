#!/usr/bin/env python3
import os
import secrets
import time
import subprocess

FLAG_TTL = 30  # seconds
FLAG_FILE = "flag.txt"

def generate_flag():
    random_hash = secrets.token_hex(16)  # 32 hex chars
    return f"uacCTF{{wh4t_do35_7h3_cl0ck_s4yyyy_{random_hash}}}"

def write_flag(flag):
    with open(FLAG_FILE, "w") as f:
        f.write(flag + "\n")

def get_flag():
    """Return cached flag if TTL not expired, else generate new."""
    if os.path.exists(FLAG_FILE):
        age = time.time() - os.path.getmtime(FLAG_FILE)
        if age < FLAG_TTL:
            with open(FLAG_FILE) as f:
                return f.read().strip()
    # generate new
    flag = generate_flag()
    write_flag(flag)
    return "HI"

if __name__ == "__main__":
    flag = get_flag()
    # Run the Rust binary
    subprocess.run(["./rusty_clock"])
