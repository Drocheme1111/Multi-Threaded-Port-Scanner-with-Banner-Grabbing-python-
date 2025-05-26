import socket
import threading
import csv

# Output file
output_file = "scan_results.csv"
lock = threading.Lock()  # Prevents threads from writing at the same time

# Grab banner from open port
def grab_banner(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as banner_sock:
            banner_sock.settimeout(2)
            banner_sock.connect((ip, port))
            banner = banner_sock.recv(1024).decode(errors="ignore").strip()
            return banner
    except:
        return "N/A"

# Scan a single port
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                except:
                    hostname = "Unknown"
                banner = grab_banner(ip, port)

                # Log result
                print(f"[+] {ip} ({hostname}) - Port {port} is OPEN - Banner: {banner}")
                with lock:
                    with open(output_file, "a", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow([ip, hostname, port, "OPEN", banner])
    except:
        pass  # Handle unexpected errors gracefully

# Main scanner
def scan_ip_range(ip_list, start_port, end_port):
    threads = []

    # Prepare CSV headers
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP Address", "Hostname", "Port", "Status", "Banner"])

    for ip in ip_list:
        print(f"\n🔍 Scanning {ip.strip()} from port {start_port} to {end_port}...")
        for port in range(start_port, end_port + 1):
            t = threading.Thread(target=scan_port, args=(ip.strip(), port))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

# --- Main Program Execution ---
if __name__ == "__main__":
    ip_input = input("Enter comma-separated IP addresses or hostnames: ")
    ip_list = ip_input.split(",")

    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
    except ValueError:
        print("❌ Invalid port number.")
        exit()

    scan_ip_range(ip_list, start_port, end_port)

    print(f"\n✅ Scan complete. Results saved in '{output_file}'")
