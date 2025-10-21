#!/usr/bin/env python3
import os
import random
import string
import subprocess

# Generate a random 32-character hexadecimal string
random_hash = ''.join(random.choices('0123456789abcdef', k=32))
flag = f"uacCTF{{wh4t_do35_7h3_cl0ck_s4yyyy_{random_hash}}}"

# Write the flag to flag.txt so your binary can read it if needed
with open("flag.txt", "w") as f:
    f.write(flag + "\n")

# Print flag to stdout (optional, if you want user to see it)
print(flag)

# Run your original Rust binary
subprocess.run(["./rusty_clock"])
