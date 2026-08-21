import socket
from cyber_easy.tools.base_tool import Tool


COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 443: "HTTPS", 3306: "MySQL",
    5432: "PostgreSQL", 8080: "HTTP-Alt"
}

class PortScanner(Tool):
    def __init__(self):
        super().__init__(
            toolName="Port Scanner",
            toolDescription="Scans common ports on a target IP"
        )

    def scan_port(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0  # 0 means open
        except:
            return False

    def run(self):
        self.display_info()
        ip = input("Enter IP to scan (try 127.0.0.1 for localhost): ")
        print(f"\nScanning {ip}...\n")
        open_ports = []
        for port, service in COMMON_PORTS.items():
            if self.scan_port(ip, port):
                print(f"  [OPEN] Port {port} — {service}")
                open_ports.append(port)
        if not open_ports:
            print("  No common ports found open.")
        print(f"\nScan complete. {len(open_ports)} open port(s) found.")

if __name__ == "__main__":
    scanner = PortScanner()
    scanner.run()