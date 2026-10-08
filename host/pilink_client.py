#!/usr/bin/env python3
"""PiLink host client: send data to aesdsocket on the Pi and print the response."""

import argparse
import socket
import sys

DEFAULT_HOST = "192.168.4.1"
DEFAULT_PORT = 9000


def send(host, port, data):
    # The server keeps the connection open after responding (it's waiting
    # for more packets), so it never signals "done" by closing the socket.
    # Read until a short idle gap instead of waiting for a clean close.
    with socket.create_connection((host, port), timeout=5) as sock:
        sock.sendall(data)

        chunks = []
        sock.settimeout(1)
        while True:
            try:
                chunk = sock.recv(4096)
            except socket.timeout:
                break
            if not chunk:
                break
            chunks.append(chunk)
        return b"".join(chunks)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default=DEFAULT_HOST, help=f"Pi address (default: {DEFAULT_HOST})")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"aesdsocket port (default: {DEFAULT_PORT})")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-m", "--message", help="send this string and exit")
    group.add_argument("-f", "--file", help="send the contents of this file and exit")
    args = parser.parse_args()

    if args.message is not None:
        data = args.message.encode() if args.message.endswith("\n") else (args.message + "\n").encode()
        response = send(args.host, args.port, data)
        sys.stdout.buffer.write(response)
        return

    if args.file is not None:
        with open(args.file, "rb") as f:
            data = f.read()
        response = send(args.host, args.port, data)
        sys.stdout.buffer.write(response)
        return

    print(f"Connected to {args.host}:{args.port}. Type a line and press Enter to send it; Ctrl-D to quit.")
    for line in sys.stdin:
        response = send(args.host, args.port, line.encode())
        sys.stdout.buffer.write(response)


if __name__ == "__main__":
    main()
