# Multi-Threaded-Port-Scanner-with-Banner-Grabbing-python-

This Python script performs a **multi-threaded TCP port scan** on one or more IP addresses or hostnames over a specified range of ports. It attempts to identify open ports and grab the service banner from each open port. All scan results are saved in a CSV file.

---

## 🚀 Features

- ✅ Scans multiple IP addresses or hostnames
- ⚡ Multi-threaded for faster scanning
- 📡 Attempts to **grab banners** from open ports
- 🗃️ Saves results to `scan_results.csv`
- 🧠 Graceful error handling with hostname resolution

---

## 🧰 Requirements

- Python 3.x  
- No external libraries required (uses built-in `socket`, `threading`, and `csv` modules)

---

## 📦 How to Use

1. **Clone the repository or copy the script:**
   ```bash
   git clone https://github.com/your-username/advanced_port_canner.git
   cd port-scanner
   ```

2. **Run the script:**
   ```bash
   python3 port_scanner.py
   ```

3. **Provide input when prompted:**
   ```
   Enter comma-separated IP addresses or hostnames: 192.168.1.1,example.com
   Enter start port: 20
   Enter end port: 100
   ```

---

## 📝 Sample Output

```
🔍 Scanning 192.168.1.1 from port 20 to 100...
[+] 192.168.1.1 (router.local) - Port 80 is OPEN - Banner: HTTP/1.1 200 OK

✅ Scan complete. Results saved in 'scan_results.csv'
```

---

## 📄 Output File (`scan_results.csv`)

| IP Address     | Hostname     | Port | Status | Banner                |
|----------------|--------------|------|--------|------------------------|
| 192.168.1.1    | router.local | 80   | OPEN   | HTTP/1.1 200 OK        |

---

## 🛡️ Disclaimer

This tool is intended for **educational and ethical testing purposes only**. Do not scan networks or devices without **proper authorization**.

---

## 👨‍💻 Author

**Goddey Ocheme**  
Cybersecurity Educator | Ethical Hacker | Developer

- 🔗 LinkedIn: [www.linkedin.com/in/goddey-ocheme-498349176](https://www.linkedin.com/in/goddey-ocheme-498349176)  
- 📧 Email: ochemicglobalresources@gmail.com

---
