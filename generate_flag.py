#!/usr/bin/env python3
import os
import secrets
import time
import tempfile

FLAG_TTL = 30           # seconds
FLAG_FILE = "flag.txt"  # file your Rust binary will read

def generate_flag():
    return f"uacCTF{{wh4t_do35_7h3_cl0ck_s4yyyy_{secrets.token_hex(16)}}}"

def write_atomic(path, text):
    """Atomically write text to path using a temporary file."""
    fd, tmp = tempfile.mkstemp(dir=".", prefix=".flagtmp_", suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)  # atomic rename
    finally:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except:
                pass

def update_flag():
    """Ensure flag.txt exists and is fresh; generate a new one if missing/expired."""
    if os.path.exists(FLAG_FILE):
        age = time.time() - os.path.getmtime(FLAG_FILE)
        if age < FLAG_TTL:
            return  # flag is still fresh; do nothing
    new_flag = generate_flag() + "\n"
    write_atomic(FLAG_FILE, new_flag)  # call the correctly defined function

if __name__ == "__main__":
    update_flag()                          # update flag.txt only

