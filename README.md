# 🔎 QUANTUM-TECH : An Network (Scanner) & Port (Scanner) using (PYTHON-PROGRAMMING + NMAP-TOOL)

This Project Provides a **Python Wrapper Around NMAP-TOOL** that allows you to easily perform:

- **Network Scanning** → Discover Live Hosts in a Subnet (Local Network or Internet).  
- **Port Scanning** → Scan `Open Ports`, `Detect Services`, `Run Scripts`, and more using all common **NMAP Flags**.  

It makes Nmap scanning interactive, customizable, and scriptable for learning, penetration testing, or system administration.

⚠️ **Note**: Always SCAN only Systems you **OWN** or have **Explicit Permission** to Test. Unauthorized Scanning may be `Illegal`.

---

## 📌 Features

### Network-Scanner
- Discover Live Hosts in a **Local Subnet** (e.g., `192.168.1.0/24`).  
- Automatically convert **Single IP Input** (`192.168.1.55`) → Full Subnet (`192.168.1.0/24`).  
- Supports **Internet Targets** (Domain/IP) for Reachability Checks.  
- Uses Nmap discovery flags:  
  - `-sn` → Ping scan (host discovery only, no port scan)  
  - `-sL` → List scan  
  - `-Pn` → Treat all hosts as online (skip discovery)  
  - Probe types: `-PS`, `-PA`, `-PU`, `-PE`, etc.  

### Port-Scanner
- Interactive **Flag Builder** for NMAP port scans.  
- Supports all Port-Specification options:  
  - `-p-` (all 65,535 ports)  
  - `-p 22,80,443` (custom ports)  
  - `-F` (fast scan common ports)  
  - `--top-ports N` (most common `N` ports)  
- Scan Techniques:  
  - `-sS` SYN scan (default, requires sudo)  
  - `-sT` TCP connect()  
  - `-sU` UDP scan  
  - `-sA`, `-sN`, `-sF`, `-sX`, `-sI`, etc.  
- Service & Version Detection: `-sV` with intensity options.  
- Script Scans: `-sC`, `--script`, `--script-args`.  
- OS Detection: `-O`, `--osscan-guess`.  
- Timing Templates: `-T0` (slow) → `-T5` (fast).  
- Firewall/IDS Evasion: `-f`, `-D`, `-S`, `--spoof-mac`, `--badsum`.  
- Output Control: `-oN`, `-oX`, `-oG`, `-oA`, append/resume.  

---

## 🛠 Installation

1. Install **Python 3** (>=3.8 recommended) :
   ```bash
   sudo apt install python3-pip
   ```
2. Install **Nmap** (>=7.95) :
   ```bash
   sudo apt update && sudo apt install nmap -y
   ```
3. 📦 Clone Git-Repository :
   ```bash
   git clone https://github.com/Neon-White-2002/QUANTUM-TECH_AN-Network-Scanner_AND_Port-Scanner.git
   cd QUANTUM-TECH_AN-Network-Scanner_AND_Port-Scanner/
   ```

## 🚀 Usage

```bash
python Quantum-Tech : Network (Scanner).py
```
```bash
python QUANTUM-TECH_AN-Network-Scanner_AND_Port-Scanner/Quantum-Tech : Network (Scanner).py
```

## 📂 Project Structure
```bash
.
├── NMAP-Outputs/                          # NMAP-Outputs (DIRECTORY) Here, NMAP-Commands are STORED based on the Command's
    ├── Network-Scan/
        ├── Internet-Target-Scan/
        ├── Local-Network-Scan/
    ├── Port-Scan
        ├── Quick-Command-Pattern/
        ├── Specific-Web-Port-Server/
├── Quantum-Tech : Network (Scanner).py    # Main-Python File (.py)
├── README.md                              # Project-Documentation
```
