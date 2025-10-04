# generate_base36.py
import os
import sys
import argparse
import math

digits = "0123456789abcdefghijklmnopqrstuvwxyz"

def int_to_base36_fixed(n, width=6):
    arr = ['0']*width
    for i in range(width-1, -1, -1):
        arr[i] = digits[n % 36]
        n //= 36
    return ''.join(arr)

def generate(total, out_prefix, workers=1, worker_id=0):
    start = (total // workers) * worker_id
    end = start + (total // workers)
    if worker_id == workers - 1:
        end = total
    out_file = f"{out_prefix}_part{worker_id:02d}.txt"
    bufsize = 4 * 1024 * 1024  # 4MB
    with open(out_file, "wb") as f:
        buf = bytearray()
        for i in range(start, end):
            s = int_to_base36_fixed(i, 6)
            buf.extend(s.encode('ascii'))
            buf.append(0x0A)  # newline
            if len(buf) >= bufsize:
                f.write(buf)
                buf.clear()
        if buf:
            f.write(buf)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--total", type=int, default=10**9)
    parser.add_argument("--out", type=str, default="logins")
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--worker_id", type=int, default=0)
    args = parser.parse_args()
    generate(args.total, args.out, args.workers, args.worker_id)
