#!/usr/bin/env python3

import socket
import argparse
import signal
import sys
from concurrent.futures import ThreadPoolExecutor

open_sockets = []

def def_handler(sig, frame):
    print(f"\n[!] Saliendo...")
    for s in open_sockets:
        s.close()
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("-t", "--target", dest="target", required=True, help="-t 127.0.0.1")
    parser.add_argument("-p", "--ports", dest="ports", required=True, help="-p 1-1000 or -p 22,80,443,8080")
    options = parser.parse_args()
    return options.target, options.ports

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    open_sockets.append(s)
    return s    

def port_scanner(port, host):
    s = create_socket()
    try:
        s.connect((host, port))
        s.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
        response = s.recv(1024)
        response = response.decode(errors="ignore").split('\n')

        if response:
            print(f"[+] Puerto {port} abierto")
            for line in response:
                print(line)
        else:
            print(f"[-] Puerto {port} abierto")
    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        s.close()

def scan_ports(ports, target):
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda port: port_scanner(port, target), ports)

def parse_ports(ports_str):
    if "-" in ports_str:
        start_port, end_port = ports_str.split("-")
        return range(int(start_port), int(end_port) + 1)
    elif "," in ports_str:
        return [int(p) for p in ports_str.split(",")]
    else:
        return [int(ports_str)]

def main():
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target)

if __name__ == "__main__":
    main()
