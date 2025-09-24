# --------------------------------------------------
# HELLO, & WELCOME TO 'QUANTUM-TECH : AN NETWORK (SCANNER) & PORT (SCANNER) !'
# --------------------------------------------------

# ----- PYTHON (MODULES & LIBRARY) ----- 
import os
import re
import sys
import signal
import pyfiglet
import subprocess
import ipaddress

# --------------------------------------------------
# CLASS @ NSAPS (NETWORK-SCANNER AND PORT-SCANNER)
# --------------------------------------------------
class NSAPS:
    # --------------------
    # RUN-COMMAND (FUNCTION) :
    # --------------------
    @staticmethod
    def run_command(command, outfile=None):
        print(f"\n[+] CURRENT-COMMAND : {command}")
        # ---------- CHECK, OUT-FILE ----------
        if outfile:
            with open(outfile, "w") as f:
                subprocess.run(command, shell=True, stdout=f, stderr=subprocess.STDOUT)
        
        else:
            subprocess.run(command, shell=True)
            
    # --------------------
    # LOCAL-NETWORK (SCANNER) - (FUNCTION) : 
    # --------------------
    @staticmethod
    def local_network_scanner():
        # LOCAL-NETWORK (IP-ADDRESS)
        local_network_ip = str(input(f"\n>>> ENTER YOUR, 'LOCAL-NETWORK' : IP-ADDRESS (e.g : 192.168.1.0-255) : "))
                                
        if len(local_network_ip) == "":
            # ---------- BANNER-NAME (ERROR) ---------- :
            ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
            print(f"\033[97m {ascii_banner} \033[0m")
                                    
        else:
            # VALIDATE (IP-ADDRESS) : 
            if ipaddress.ip_address(local_network_ip):
                # HERE, WE WILL 'BUILD' AN 'IP-ADDRESS' : DIRECTORY TO STORE (NMAP-RESULT'S) : 
                print(f"\n[+] CURRENT-TASK : GENERATE AN 'IP-ADDRESS' (DIRECTORY), TO STORE RESULT ...")
                os.makedirs(f"NMAP-Outputs/Network-Scan/Local-Network-Scan/{local_network_ip}", exist_ok=True)
                
                # LOCAL-NETWORK (SCANNER) : MENU
                while True:
                    print(f"\n---------- WELCOME TO, #'LOCAL-NETWORK' (WI-FI/LAN) - SCAN : (MENU) ----------", end="\n\n")
                    print(f">>> PRESS (1) : LIST-HOSTS")
                    print(f">>> PRESS (2) : DISCOVER LIVE HOSTS (ARP)")
                    print(f">>> PRESS (3) : ICMP-DISCOVERY")
                    print(f">>> PRESS (4) : FAST-SCAN")
                    print(f">>> PRESS (5) : SERVICES & OS-DETECTION")
                    print(f">>> PRESS (6) : AGGRESSIVE-SCAN")
                    print(f">>> PRESS (7) : VULNERABILITY-SCAN (SCRIPT'S)")
                    print(f">>> PRESS (0) : EXIT")
                    
                    choice = str(input(f"\n>>> ENTER YOUR, [LOCAL-NETWORK] CHOICE : "))
                    
                    # LIST-HOSTS :
                    if int(choice) == 1:
                        print(f"\n[+] CURRENT-TASK : LIST-HOSTS")
                        NSAPS.run_command(f"nmap -v -sn -PR {local_network_ip}/24 -oN NMAP-Outputs/Network-Scan/Local-Network-Scan/{local_network_ip}/list-hosts.txt")
                        
                    # DISCOVERY-LIVE-HOSTS :
                    elif int(choice) == 2:
                        print(f"\n[+] CURRENT-TASK : DISCOVER LIST-HOSTS (ARP)")
                        NSAPS.run_command(f"nmap -v -sn -PE {local_network_ip}/24 -oN NMAP-Outputs/Network-Scan/Local-Network-Scan/{local_network_ip}/discover-live-hosts.txt")
                        
                    # ICMP-DISCOVERY :
                    elif int(choice) == 3:
                        print(f"\n[+] CURRENT-TASK : ICMP-DISCOVERY")
                        NSAPS.run_command(f"nmap -v -sL {local_network_ip}/24 -oN NMAP-Outputs/Network-Scan/Local-Network-Scan/{local_network_ip}/icmp-discovery.txt")
                        
                    # FAST-SCAN :
                    elif int(choice) == 4:
                        print(f"\n[+] CURRENT-TASK : FAST-SCAN")
                        NSAPS.run_command(f"nmap -v -F {local_network_ip}/24 -oN NMAP-Outputs/Network-Scan/Local-Network-Scan/{local_network_ip}/fast-scan.txt")
                        
                    # SERVICES & OS-DETECTION :
                    elif int(choice) == 5:
                        print(f"\n[+] CURRENT-TASK : SERVICES & OS-DETECTION")
                        NSAPS.run_command(f"nmap -v -sS -sV -O {local_network_ip}/24 -oN NMAP-Outputs/Network-Scan/Local-Network-Scan/{local_network_ip}/services-and-os-detection.txt")
                         
                    # ADDRESSIVE-SCAN :
                    elif int(choice) == 6:
                        print(f"\n[+] CURRENT-TASK : AGGRESSIVE 'LAN' SCAN")
                        NSAPS.run_command(f"nmap -v -A {local_network_ip}/24 -oN NMAP-Outputs/Network-Scan/Local-Network-Scan/{local_network_ip}/aggressive-scan.txt")
                         
                    # VULNERABILITY-SCAN (SCRIPT) : 
                    elif int(choice) == 7:
                        print(f"\n[+] CURRENT-TASK : NMAP 'NSE' SCRIPTS")
                        NSAPS.run_command(f"nmap --script=vuln {local_network_ip}/24 -oN NMAP-Outputs/Network-Scan/Local-Network-Scan/{local_network_ip}/vuln-script.txt")
                        
                    # EXIT (FUNCTION) :
                    elif int(choice) == 0:
                        # ---------- BANNER-NAME (EXIT) ---------- :
                        ascii_banner = pyfiglet.figlet_format("EXIT ! [LOCAL-NETWORK] : SCAN ...", font="slant")
                        print(f"\033[97m {ascii_banner} \033[0m")
                        break
                    
            else:
                # ---------- BANNER-NAME (ERROR) ---------- :
                print(f"\n[!] CURRENT-TASK : 'FAILED' ! THE 'IP-ADDRESS' : {local_network_ip} IS NOT-VALID ...")
                ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                print(f"\033[97m {ascii_banner} \033[0m")
                sys.exit()
    
    # --------------------
    # INTERNET-TARGET [REMOTE IP-ADDRESS / DOMAIN-NAME] - SCAN (FUNCTION) : 
    # --------------------
    @staticmethod
    def internet_target_menu_scanner(target, file_path):
        while True:
            print(f"\n----- WELCOME TO, INTERNET [REMOTE IP-ADDRESS / DOMAIN-NAME] - SCAN : (MENU) -----", end="\n\n")
            print(f">>> PRESS (1) : HOST-DISCOVERY")
            print(f">>> PRESS (2) : SKIP PING-REQUEST")
            print(f">>> PRESS (3) : SYN-SCAN")
            print(f">>> PRESS (4) : TCP-CONNECT")
            print(f">>> PRESS (5) : FULL-PORT RANGE")
            print(f">>> PRESS (6) : SERVICE-DETECTION")
            print(f">>> PRESS (7) : OS-DETECTION")
            print(f">>> PRESS (8) : AGGRESSIVE-SCAN")
            print(f">>> PRESS (9) : UDP-SCAN")
            print(f">>> PRESS (10) : IDS-EVASION")
            print(f">>> PRESS (11) : VULNERABILITY-SCAN (SCRIPT's)")
            print(f">>> PRESS (0) : EXIT ! 'INTERNET' [REMOTE I-ADDRESS / DOMAIN-NAME]")
            
            choice = str(input("\n>>> ENTER YOUR, INTERNET [REMOTE IP-ADDRESS / DOMAIN-NAME] CHOICE : "))
            
            if len(choice) == "":
                # ---------- BANNER-NAME (ERROR) ---------- :
                ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                print(f"\033[97m {ascii_banner} \033[0m")
            
            else:
                try:
                    # HOST-DISCOVERY :
                    if int(choice) == 1:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (HOST-DISCOVERY) ...")
                        NSAPS.run_command(f"nmap -v -sn {target} -oN {file_path}/host-discovery.txt")
                        
                    # SKIP PING-REQUEST :
                    elif int(choice) == 2:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (SKIP PING-REQUEST : ICMP) ...")
                        NSAPS.run_command(f"nmap -v -Pn {target} -oN {file_path}/skip-ping-request.txt")
                        
                    # SYN-SCAN :
                    elif int(choice) == 3:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (SYN-SCAN) ...")
                        NSAPS.run_command(f"nmap -v -sS {target} -oN {file_path}/syn-scan.txt")
                        
                    # TCP-CONNECT :
                    elif int(choice) == 4:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (TCP-CONNECT) ...")
                        NSAPS.run_command(f"nmap -v -sT {target} -oN {file_path}/tcp-connect.txt")
                        
                    # FULL-PORT RANGE :
                    elif int(choice) == 5:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (FULL-PORT RANGE) ...")
                        NSAPS.run_command(f"nmap -v -p- {target} -oN {file_path}/full-port-range.txt")
                        
                    # SERVICE-DETECTION :
                    elif int(choice) == 6:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (SERVICE-DETECTION) ...")
                        NSAPS.run_command(f"nmap -v -sS -sV {target} -oN {file_path}/service-detection.txt")
                         
                    # OS-DETECTION :
                    elif int(choice) == 7:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (OS (OPERATING-SYSTEM) DETECTION) ...")
                        NSAPS.run_command(f"nmap -v -O {target} -oN {file_path}/os-detection.txt")
                        
                    # AGGRESSIVE-SCAN :
                    elif int(choice) == 8:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (AGGRESSIVE-INTERNET-SCAN) ...")
                        NSAPS.run_command(f"nmap -v -A {target} -oN {file_path}/aggressive-scan.txt")
                        
                    # UDP-SCAN :
                    elif int(choice) == 9:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (UDP-SCAN) ...")
                        NSAPS.run_command(f"sudo nmap -v -sU {target} -oN {file_path}/udp-scan.txt")
                        
                    # IDS-EVASION :
                    elif int(choice) == 10:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (IDS-EVASION) ...")
                        NSAPS.run_command(f"nmap -v -sS -Pn -T5 -f {target} -oN {file_path}/ids-evasion.txt")
                         
                    # VULNERABILITY-SCAN (SCRIPT) :
                    elif int(choice) == 11:
                        print(f"\n[+] CURRENT-TASK : INTERNET-TARGET (VULNERABILITY-SCAN : SCRIPT'S) ...")
                        NSAPS.run_command(f"nmap -v --script=vuln {target} -oN {file_path}/vulnerability-scan.txt")
                         
                    # EXIT :
                    elif int(choice) == 0:
                        # ---------- BANNER-NAME (EXIT) ---------- :
                        ascii_banner = pyfiglet.figlet_format("EXIT ! INTERNET-TARGET [REMOTE IP-ADDRESS / DOMAIN-NAME] ...", font="slant")
                        print(f"\033[97m {ascii_banner} \033[0m")
                        break
                    
                except ValueError:
                    # ---------- BANNER-NAME (ERROR) ---------- :
                    ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                    print(f"\033[97m {ascii_banner} \033[0m")
                    sys.exit()
    
    # --------------------
    # INTERNET-TARGET (SCANNER) - (FUNCTION) : 
    # --------------------
    @staticmethod
    def internet_target_scanner():
        print(f"\n----- WELCOME TO, #'INTERNET (TARGET) - SCAN' : MENU -----", end="\n\n")
        print(f">>> PRESS (1) : REMOTE 'IP-ADDRESS'")
        print(f">>> PRESS (2) : DOMAIN-NAME")
        print(f">>> PRESS (0) : EXIT (INTERNET-TARGET (SCANNER))")
        
        choice = str(input("\n>>> ENTER YOUR, [INTERNET-TARGET] CHOICE : "))
        
        if len(choice) == "":
            # ---------- BANNER-NAME (ERROR) ---------- :
            ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
            print(f"\033[97m {ascii_banner} \033[0m")
            
        else:
            try:
                # REMOTE 'IP-ADDRESS' :
                if int(choice) == 1:
                    print(f"\n[+] CURRENT-TASK : [INTERNET-TARGET] : REMOTE 'IP-ADDRESS' (SCAN) IN PROGRESS ...")
                    # REMOTE IP-ADDRESS : 
                    remote_ip_address = str(input("\n>>> ENTER ANY, [REMOTE IP-ADDRESS] e.g : (8.8.8.8) : "))
                    
                    if ipaddress.ip_address(remote_ip_address):
                        # NOW, HERE WE WILL 'GENERATE' AN IP-ADDRESS BASED (DIRECTORY) :
                        file_path = f"NMAP-Outputs/Network-Scan/Internet-Target-Scan/{remote_ip_address}"
                        os.makedirs(file_path, exist_ok=True)
                        
                        # CALL, INTERNET-TARGET-MENU-SCANNER (FUNCTION) :
                        NSAPS.internet_target_menu_scanner(remote_ip_address, file_path)
                    
                    else:
                        # ---------- BANNER-NAME (ERROR) ---------- :
                        print(f"\n[!] CURRENT-TASK : 'FAILED' ! THE REMOTE 'IP-ADDRESS' : {remote_ip_address} IS AN IN-VAILD ...")
                        ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                        print(f"\033[97m {ascii_banner} \033[0m")
                
                # DOMAIN-NAME :
                elif int(choice) == 2:
                    print(f"\n[+] CURRENT-TASK : [INTERNET-TARGET] : 'DOMAIN-NAME' (SCAN) IN PROGRESS ...")
                    # TARGET (DOMAIN-NAME) : 
                    target_domain_name = str(input("\n>>> ENTER ANY, [DOMAIN-NAME] e.g : (google.com) : "))
                    
                    if len(target_domain_name) == "":
                        ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                        print(f"\033[97m {ascii_banner} \033[0m")
                        
                    else:
                        # DOMAIN-NAME (PATTERN-VALIDATION) : 
                        domain_name_pattern = re.compile(r"^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
                        
                        if not domain_name_pattern.match(target_domain_name):
                            print(f"\n[-] CURRENT-TASK : 'FAILED' ! OOPS, LOOK'S LIKE YOU DIDN'T PROVIDE AN VALID [DOMAIN-NAME] : {target_domain_name}")
                            ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                            print(f"\033[97m {ascii_banner} \033[0m")
                            sys.exit()
                            
                        else:
                            print(f"\n>>> [DOMAIN-NAME] : {target_domain_name} IS SET AS AN TARGET !")
                            # NOW, HERE WE WILL 'GENERATE' AN IP-ADDRESS BASED (DIRECTORY) :
                            file_path = f"NMAP-Outputs/Network-Scan/Internet-Target-Scan/{target_domain_name}"
                            os.makedirs(file_path, exist_ok=True)
                            
                            # CALL, INTERNET-TARGET-MENU-SCANNER (FUNCTION) :
                            NSAPS.internet_target_menu_scanner(target_domain_name, file_path)
                
                # EXIT :  
                elif int(choice) == 0:
                    # ---------- BANNER-NAME (EXIT) ---------- :
                    ascii_banner = pyfiglet.figlet_format("EXIT ! [INTERNET-TARGET] : SCAN ...", font="slant")
                    print(f"\033[97m {ascii_banner} \033[0m")
                    sys.exit()
            
            except ValueError:
                # ---------- BANNER-NAME (ERROR) ---------- :
                ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                print(f"\033[97m {ascii_banner} \033[0m")
                sys.exit()
    
    # --------------------
    # QUICK-COMMAND-PATTERN (PORT-SCANNER) - (FUNCTION) : 
    # --------------------
    @staticmethod
    def quick_command_pattern_port_scanner():
        print(f"\n[+] CURRENT-TASK : [PORT-SCANNER : QUICK-COMMAND-PATTERN] : 'DOMAIN-NAME' (SCAN) IN PROGRESS ...")
        # TARGET (DOMAIN-NAME) : 
        target_domain_name = str(input("\n>>> ENTER ANY, [DOMAIN-NAME] e.g : (google.com) : "))
                    
        if len(target_domain_name) == "":
            # ---------- BANNER-NAME (ERROR) ---------- :
            ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
            print(f"\033[97m {ascii_banner} \033[0m")
                        
        else:
            # DOMAIN-NAME (PATTERN-VALIDATION) : 
            domain_name_pattern = re.compile(r"^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
                        
            if not domain_name_pattern.match(target_domain_name):
                print(f"\n[-] CURRENT-TASK : 'FAILED' ! OOPS, LOOK'S LIKE YOU DIDN'T PROVIDE AN VALID [DOMAIN-NAME] : {target_domain_name}")
                # ---------- BANNER-NAME (ERROR) ---------- :
                ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                print(f"\033[97m {ascii_banner} \033[0m")
                sys.exit()
                            
            else:
                print(f"\n>>> [DOMAIN-NAME] : '{target_domain_name}' IS SET AS AN TARGET !")
                # NOW, HERE WE WILL 'GENERATE' AN IP-ADDRESS BASED (DIRECTORY) :
                file_path = f"NMAP-Outputs/Port-Scan/Quick-Command-Pattern/{target_domain_name}"
                os.makedirs(file_path, exist_ok=True)
                
                # ----- QUICK-COMMAND-PATTERN : PORT-SCANNER ----- :
                while True:
                    print(f"\n----- WELCOME TO, #'QUICK-COMMAND-PATTERN (PORT-SCAN) : MENU -----'", end="\n\n")
                    print(f">>> PRESS (1) : SYN-SCAN + VERSION-DETECTION : ON COMMON-PORT")
                    print(f">>> PRESS (2) : TCP PORT-SCAN + AGGRESSIVE-DETECTION : ON ALL PORTS")
                    print(f">>> PRESS (3) : UDP-SCAN (DNS / NTP) + SERVICE-DETECTION : ON (DNS / NTP)")
                    print(f">>> PRESS (4) : FAST, UN-PRIVILEGED : TCP CONNECT-SCAN")
                    print(f">>> PRESS (5) : SKIP HOST-DISCOVERY & ONLY SCAN LISTED-PORT")
                    print(f">>> PRESS (6) : VULNERABILITY-SCAN (SCRIPT'S) : AGAINST DISCOVERED SERVICES")
                    print(f">>> PRESS (0) : EXIT ! QUICK-COMMAND-PATTERN : PORT-SCAN")
                    
                    choice = str(input("\n>>> ENTER YOUR, [QUICK-COMMAND-PATTERN : PORT-SCAN] CHOICE : "))
                    
                    if len(choice) == "":
                        # ---------- BANNER-NAME (ERROR) ---------- :
                        ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                        print(f"\033[97m {ascii_banner} \033[0m")
                        
                    else:
                        try:
                            # SYN-SCAN + VERSION-DETECTION : ON COMMON-PORT :
                            if int(choice) == 1:
                                print(f"\n[+] CURRENT-TASK : [QUICK-COMMAND-PATTERN] : 'SYN-SCAN + VERSION-DETECTION (ON-COMMON-PORT) ...'")
                                NSAPS.run_command(f"sudo nmap -v -sS --top-ports 100 -sV -T5 {target_domain_name} -oN {file_path}/syn-scan-plus-version-detection.txt")
                            
                            # TCP PORT-SCAN + AGGRESSIVE-DETECTION : ON ALL-PORT :
                            elif int(choice) == 2:
                                print(f"\n[+] CURRENT-TASK : [QUICK-COMMAND-PATTERN] : 'TCP PORT-SCAN + AGGRESSIVE-DETECTION (ON-ALL-PORTS) ...'")
                                NSAPS.run_command(f"sudo nmap -v -sS -p- -A -O -T5 {target_domain_name} -oN {file_path}/tcp-port-scan-plus-aggressive-detection.txt") 
                            
                            # UDP-SCAN + SERVICE-DETECTION : ON (DNS / NTP) : 
                            elif int(choice) == 3:
                                print(f"\n[+] CURRENT-TASK : [QUICK-COMMAND-PATTERN] : 'UDP-SCAN + SERVICE-DETECTION (ON : DNS / NTP) ...'")
                                NSAPS.run_command(f"sudo nmap -v -sU -p 53,123 -sV -T3 {target_domain_name} -oN {file_path}/udp-scan-plus-service-detection.txt")
                                
                            # FAST, UN-PRIVILEDGE : TCP CONNECT-SCAN :
                            elif int(choice) == 4:
                                print(f"\n[+] CURRENT-TASK : [QUICK-COMMAND-PATTERN] : 'FAST, UN-PRIVLIEDGE (TCP-CONNECT-SCAN) ...'")
                                NSAPS.run_command(f"nmap -v -sT -F {target_domain_name} -oN {file_path}/fast-unpriviledge-tcp-connect-scan.txt")
                                 
                            # SKIP HOST-DISCOVERY & ONLY SCAN LISTED-PORT : 
                            elif int(choice) == 5:
                                print(f"\n[+] CURRENT-TASK : [QUICK-COMMAND-PATTERN] : 'SKIP HOST-DISCOVERY & ONLY SCAN LSITED-PORT' ...")
                                NSAPS.run_command(f"nmap -v -Pn -sS -p- {target_domain_name} -oN {file_path}/skip-host-discovery-and-only-scan-listed-ports.txt")
                            
                            # VULNERABILITY-SCAN (SCRIPT) : AGAINST DISCOVERED SERVICES : 
                            elif int(choice) == 6:
                                print(f"\n[+] CURRENT-TASK : [QUICK-COMMAND-PATTERN] : 'VULNERABILITY-SCAN : SCRIPTS (AGAINST-DISCOVERED-SERVICES) ...'")
                                NSAPS.run_command(f"sudo nmap -v -sS -sV --script=vuln -p- {target_domain_name} -oN {file_path}/vulnerability-scan.txt")
                            
                            # EXIT :
                            elif int(choice) == 0:
                                # ---------- BANNER-NAME (THANK-YOU) ---------- :
                                ascii_banner = pyfiglet.figlet_format("THANK-YOU & VISIT-AGAIN !", font="slant")
                                print(f"\033[97m {ascii_banner} \033[0m")
                                break
                        
                        except ValueError:
                            # ---------- BANNER-NAME (ERROR) ---------- :
                            ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                            print(f"\033[97m {ascii_banner} \033[0m")
    
    # --------------------
    # SPECIFIC-PORT-SCAN (WEB-SERVER PORT) - (FUNCTION) : 
    # --------------------
    @staticmethod
    def specific_web_server_port_scanner():
        print(f"\n[+] CURRENT-TASK : [PORT-SCANNER : SPECIFIC (WEB-SERVER PORT)] : 'DOMAIN-NAME' (SCAN) IN PROGRESS ...")
        # TARGET (DOMAIN-NAME) : 
        target_domain_name = str(input("\n>>> ENTER ANY, [DOMAIN-NAME] e.g : (google.com) : "))
                    
        if len(target_domain_name) == "":
            # ---------- BANNER-NAME (ERROR) ---------- :
            ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
            print(f"\033[97m {ascii_banner} \033[0m")
                        
        else:
            # DOMAIN-NAME (PATTERN-VALIDATION) : 
            domain_name_pattern = re.compile(r"^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
                        
            if not domain_name_pattern.match(target_domain_name):
                print(f"\n[-] CURRENT-TASK : 'FAILED' ! OOPS, LOOK'S LIKE YOU DIDN'T PROVIDE AN VALID [DOMAIN-NAME] : {target_domain_name}")
                # ---------- BANNER-NAME (ERROR) ---------- :
                ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                print(f"\033[97m {ascii_banner} \033[0m")
                sys.exit()
                            
            else:
                print(f"\n>>> [DOMAIN-NAME] : '{target_domain_name}' IS SET AS AN TARGET !")
                # NOW, HERE WE WILL 'GENERATE' AN IP-ADDRESS BASED (DIRECTORY) :
                file_path = f"NMAP-Outputs/Port-Scan/Specific-Web-Port-Server/{target_domain_name}"
                os.makedirs(file_path, exist_ok=True)
                
                print(f"\n[+] CURRENT-TASK : [NMAP-COMMAND] FOR '{target_domain_name}' TO FIND-OUT 'OPEN-PORT' & 'SERVICES' ...")
                NSAPS.run_command(f"nmap -v -sV -A {target_domain_name} -oN {file_path}/{target_domain_name}-nmap-command.txt")
                
                print(f"\n[?] NOW, FROM THE ABOVE [NMAP-RESULT] DO YOU WANT TO 'CONTINUE' [PORT-SCAN] : SPECIFIC (WEB-SERVER-PORT) ... ?")
                condition = str(input("\n>>> TO CONTINUE [PORT-SCAN], THEN PRESS [Y]ES OR [N]O : "))
                
                if len(condition) == "":
                    # ---------- BANNER-NAME (ERROR) ---------- :
                    ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                    print(f"\033[97m {ascii_banner} \033[0m")
                    
                else:
                    try:
                        # FOR : YES-CONDITION : 
                        if condition in ["YES", "Yes", "yes", "y", "Y"]:
                            # ----- SPECIFIC (WEB-SERVER) PORTS : PORT-SCANNER ----- :
                            while True:
                                print(f"\n----- WELCOME TO, #'SPECIFIC (WEB-SERVER) PORTS (SCANNER) : MENU -----'", end="\n\n")
                                print(f">>> PRESS (1) : FTP (20) -> FILE-TRANSFER-PROTOCOL (DATA-TRANSFER)")
                                print(f">>> PRESS (2) : FTP (21) -> FILE-TRANSFER-PROTOCOL (COMMAND-CONTROL)")
                                print(f">>> PRESS (3) : SSH (22) -> SECURE-SHELL")
                                print(f">>> PRESS (4) : TELNET (23) -> REMOTE-LOGIN-SERVICE, UN-ENCRYPTED-TEXT-MESSAGE")
                                print(f">>> PRESS (5) : SMTP (25) -> SIMPLE-MAIL-TRANSFER-PROTOCOL (E-MAIL ROUTING)")
                                print(f">>> PRESS (6) : DNS (53) -> DOMAIN-NAME-SYSTEM (DNS-SERVICES)")
                                print(f">>> PRESS (7) : DHCP (67, 68) -> DYNAMIC-HOST-CONFIGURATION-PROTOCOL (ASSIGN AN : IP-ADDRESS TO HOST)")
                                print(f">>> PRESS (8) : HTTP (80) -> HYPER-TEXT-TRANSFER-PROTOCOL (WWW : WORDL-WIDE-WEB)")
                                print(f">>> PRESS (9) : POP3 (110) -> POST-OFFICE-PROTOCOL (E-MAIL CLIENT TO RETRIEVE E-MAIL FROM SERVER)")
                                print(f">>> PRESS (10) : NTP (123) -> NETWORK-TIME-PROTOCOL (SYNCHRONIZES-SYSTEM-CLOCKS)")
                                print(f">>> PRESS (11) : HTTPS (443) -> HTTP SECURE (OVER TSL / SSL)")
                                print(f">>> PRESS (12) : MY-SQL (3306) -> MY-STRUCTURED-QUERY-LANGUAGE (DATABASE) : MARIA-DB")
                                print(f">>> PRESS (13) : POSTGRE-SQL (5432) -> POSTGRE-STRUCTURE-QUERY-LANGUAGE (DATABASE)")
                                print(f">>> PRESS (14) : MICROSOFT-SQL (1433) -> MICROSOFT-SQL-SERVER (DATABASE)")
                                print(f">>> PRESS (15) : ORACLE-DB (1521) -> ORACLE-DATABASE (TNS-LISTENER)")
                                print(f">>> PRESS (16) : MONGO-DB (27017) -> MONGO-DATABASE")
                                print(f">>> PRESS (0) : EXIT ! SPECIFIC [WEB-SERVER-PORTS] : PORT-SCAN")
                                
                                choice = str(input("\n>>> ENTER YOUR, [SPECIFIC : WEB-SERVER-PORT] CHOICE : "))
                                
                                if len(choice) == "":
                                    # ---------- BANNER-NAME (ERROR) ---------- :
                                    ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                                    print(f"\033[97m {ascii_banner} \033[0m")
                                    
                                else:
                                    try:
                                        # FTP (20) -> FILE-TRANSFER-PROTOCOL (DATA-TRANSFER) : 
                                        if int(choice) == 1:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => FTP (20) : FILE-TRANSFER-PROTOCOL (DATA-TRANSFER) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 20 {target_domain_name} -oN {file_path}/ftp-20.txt")
                                        
                                        # FTP (21) -> FILE-TRANSFER-PROTOCOL (COMMAND-CONTROL) : 
                                        elif int(choice) == 2:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => FTP (21) : FILE-TRANSFER-PROTOCOL (COMMAND-CONTROL) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 21 {target_domain_name} -oN {file_path}/ftp-21.txt")
                                            
                                        # SSH (22) -> SECURE-SHELL :
                                        elif int(choice) == 3:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => SSH (22) : SECURE-SHELL IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 22 {target_domain_name} -oN {file_path}/ssh-22.txt")
                                        
                                        # TELNET (23) -> REMOTE-LOGIN-SERVICE & UNENCRYPTED-TEXT-MESSAGE :
                                        elif int(choice) == 4:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => TELNET (23) : REMOTE-LOGIN-SERVICES & UNENCRYPTED-TEXT-MESSAGE IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 23 {target_domain_name} -oN {file_path}/telnet-23.txt")
                                            
                                        # SMTP (25) -> SIMPLE-MAIL-TRANSFER-PROTOCOL (E-MAIL ROUTING) : 
                                        elif int(choice) == 5:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => SMTP (25) : SIMPLE-MAIL-TRANSFER-PROTOCOL (E-MAIL ROUTING) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 25 {target_domain_name} -oN {file_path}/smtp-25.txt")
                                            
                                        # DNS (53) -> DOMAIN-NAME-SYSTEM (DNS-SERVICES) : 
                                        elif int(choice) == 6:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => DNS (53) : DOMAIN-NAME-SYSTEM (CONVERT 'DOMAIN-NAME (e.g : google.com)' INTO 'IP-ADDRESS (e.g : 142.251.42.78)') IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 53 {target_domain_name} -oN {file_path}/dns-53.txt")
                                            
                                        # DHCP (67, 68) -> DYNAMIC-HOST-CONFIGURATION-PROTOCOL (ASSIGN : IP-ADDRESS TO HOST) : 
                                        elif int(choice) == 7:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => DHCP (67, 68) : DYNAMIC-HOST-CONFIGURATION-PROTOCOL (ASSIGN AN : 'IP-ADDRESS' TO HOST) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 67,68 {target_domain_name} -oN {file_path}/dhcp-67-and-68.txt")
                                            
                                        # HTTP (80) -> HYPER-TEXT-TRANSFER-PROTOCOL (WWW : WORLD-WIDE-WEB) : 
                                        elif int(choice) == 8:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => HTTP (80) : HYPER-TEXT-TRANSFER-PROTOCOL (WWW : WORLD-WIDE-WEB) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 80 {target_domain_name} -oN {file_path}/http-80.txt")
                                        
                                        # POP-3 (110) -> POST-OFFICE-PROTOCOL (E-MAIL CLIENT TO RETRIEVE E-MAIL FROM SERVER) : 
                                        elif int(choice) == 9:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => POP-3 (110) : POST-OFFICE-PROTOCOL (E-MAIL CLIENT TO RETRIEVE E-MAIL'S FROM SERVER) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 110 {target_domain_name} -oN {file_path}/pop3-110.txt")
                                        
                                        # NTP (123) -> NETWORK-TIME-PROTOCOL (SYNCHRONIZES-SYSTEM-CLOCKS) : 
                                        elif int(choice) == 10:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => NTP (123) : NETWORK-TIME-PROTOCOL (SYNCHRONIZES-SYSTEM-CLOCK) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 123 {target_domain_name} -oN {file_path}/ntp-123.txt")
                                        
                                        # HTTPS (443) -> HTTP SECURE (OVER : TSL / SSL) : 
                                        elif int(choice) == 11:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => HTTPS (443) : HTTPS SECURE (OVER : TSL / SSL) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 443 {target_domain_name} -oN {file_path}/https-443.txt")
                                        
                                        # MY-SQL (3306) -> MY STRUCTURED-QUERY-LANGUAGE (DATABASE) | MARIA-DB : 
                                        elif int(choice) == 12:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => MY-SQL (3306) : MY-STRUCTURED-QUERY-LANGUAGE (DATABASE) | (MARIA-DB) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 3306 {target_domain_name} -oN {file_path}/my-sql-3306.txt")
                                        
                                        # POSTGRES-SQL (5432) -> POSTGRE-SQL (DATABASE) : 
                                        elif int(choice) == 13:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => POSTGRES-SQL (5432) : POSTGRES-SQL (DATABASE) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 5432 {target_domain_name} -oN {file_path}/postgres-sql-5432.txt")
                                        
                                        # MICROSOFT-SQL (1433) -> MIRCOSOFT-SQL-SERVER (DATABASE) :
                                        elif int(choice) == 14:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => MICROSOFT-SQL (1433) : MICROSOFT-SQL-SERVER (DATABASE) IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 1433 {target_domain_name} -oN {file_path}/microsoft-sql-1433.txt")
                                        
                                        # ORCALE-DB (1521) -> ORCALE-DATABASE (TNS-LISTENER) : 
                                        elif int(choice) == 15:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => ORCALE-DB (1521) : ORACLE-DATABASE IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 1521 {target_domain_name} -oN {file_path}/oracle-db-1521.txt")
                                        
                                        # MONGO-DB (27107) -> MONGO-DATABASE : 
                                        elif int(choice) == 16:
                                            print("\n[+] CURRENT-TASK : [PORT-SCAN] => MONGO-DB (27107) : MONGO-DATABASE IN PROGRESS ...")
                                            NSAPS.run_command(f"nmap -v -sV -A -O --script=vuln -p 27107 {target_domain_name} -oN {file_path}/mongo-db-27107.txt")
                                                                                    
                                        # EXIT :
                                        elif int(choice) == 0:
                                            # ---------- BANNER-NAME (EXIT) ---------- :
                                            ascii_banner = pyfiglet.figlet_format("EXIT ! [PORT-SCAN] => FOR, SPECIFIC (WEB-SERVER PORTS) ...", font="slant")
                                            print(f"\033[97m {ascii_banner} \033[0m")
                                            break
                                        
                                    except ValueError:
                                        # ---------- BANNER-NAME (ERROR) ---------- :
                                        ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                                        print(f"\033[97m {ascii_banner} \033[0m")
                                        sys.exit()
                      
                        # FOR : NO-CONDITION :
                        elif condition in ["NO", "No", "no", "n", "N"]:
                            # ---------- BANNER-NAME (EXIT) ---------- :
                            ascii_banner = pyfiglet.figlet_format("EXIT ! [PORT-SCAN] => FOR, SPECIFIC (WEB-SERVER PORTS) ...", font="slant")
                            print(f"\033[97m {ascii_banner} \033[0m")
                            
                    except ValueError:
                        # ---------- BANNER-NAME (ERROR) ---------- :
                        ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                        print(f"\033[97m {ascii_banner} \033[0m")
                        sys.exit()
    
    # --------------------
    # QUANTUM-TECH (TOOL) - (FUNCTION) : 
    # --------------------
    @staticmethod
    def quantum_tech_tool():
        print(f"\n----------- WELCOME TO, #'QUANTUM-TECH' (TOOL) ----------", end="\n\n")
        print(f">>> PRESS (1) : NETWORK-SCANNER")
        print(f">>> PRESS (2) : PORT-SCANNER")
        print(f">>> PRESS (0) : EXIT")
        
        choice = str(input("\n>>> ENTER YOUR, [QUANTUM-TECH] TOOL => CHOICE : "))
        
        if len(choice) == "":
            # ---------- BANNER-NAME (ERROR) ---------- :
            ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
            print(f"\033[97m {ascii_banner} \033[0m")
        
        else:
            try:
                # ----- NETWORK-SCANNER ----- :
                if int(choice) == 1:
                   while True:
                       # ---------- BANNER-NAME (NETWORK-SCANNER) ---------- :
                        ascii_banner = pyfiglet.figlet_format("NETWORK-SCAN : (MENU)", font="slant")
                        print(f"\033[95m {ascii_banner} \033[0m")
                        
                        # ----- # NETWORK-SCANNER : (MENU) -----
                        print(f"\n----- WELCOME TO, #'NETWORK-SCANNER' : MENU -----", end="\n\n")
                        print(f">>> PRESS (1) : LOCAL-NETWORK (SCAN)")
                        print(f">>> PRESS (2) : INTERNET-TARGET (SCAN)")
                        print(f">>> PRESS (0) : EXIT")
                        
                        choice = str(input("\n>>> ENTER YOUR CHOICE, FOR # 'NETWORK-SCANNER' : "))
                        
                        if len(choice) == "":
                            # ---------- BANNER-NAME (ERROR) ---------- :
                            ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                            print(f"\033[97m {ascii_banner} \033[0m")
                            
                        else:
                            try:
                                # ----- LOCAL-NETWORK (WI-FI / LAN) ----- :
                                if int(choice) == 1:
                                    # ---------- BANNER-NAME (LOCAL-NETWORK (SCANNER)) ---------- :
                                    ascii_banner = pyfiglet.figlet_format("LOCAL-NETWORK (WI-FI / LAN)", font="slant")
                                    print(f"\033[97m {ascii_banner} \033[0m")
                                    
                                    # FUNCTION-CALL (LOCAL-NETWORK-SCANNER) :
                                    NSAPS.local_network_scanner()
                                    
                                # ----- INTERNET (REMOTE IP's / DOMAIN's) ----- :
                                elif int(choice) == 2:
                                    # ---------- BANNER-NAME (INTERNET-TARGET (SCANNER)) ---------- :
                                    ascii_banner = pyfiglet.figlet_format("INTERNET-TARGET (REMOTE IP's / DOMAIN's)", font="slant")
                                    print(f"\033[97m {ascii_banner} \033[0m")
                                    
                                    # FUNCTION-CALL (INTERNET-TARGET-SCANNER) :
                                    NSAPS.internet_target_scanner()
                                    
                                # ----- EXIT ----- :
                                elif int(choice) == 0:
                                    # ---------- BANNER-NAME (THANK-YOU) ---------- :
                                    ascii_banner = pyfiglet.figlet_format("THANK-YOU & VISIT-AGAIN !", font="slant")
                                    print(f"\033[97m {ascii_banner} \033[0m")
                                    break
                                    
                            except ValueError:
                                # ---------- BANNER-NAME (ERROR) ---------- :
                                ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                                print(f"\033[97m {ascii_banner} \033[0m")
                                continue
                
                # ----- PORT-SCANNER ----- :   
                elif int(choice) == 2:
                    while True:
                       # ---------- BANNER-NAME (NETWORK-SCANNER) ---------- :
                        ascii_banner = pyfiglet.figlet_format("PORT-SCAN : (MENU)", font="slant")
                        print(f"\033[95m {ascii_banner} \033[0m")
                        
                        # ----- # NETWORK-SCANNER : (MENU) -----
                        print(f"\n----- WELCOME TO, #'PORT-SCANNER' : MENU -----", end="\n\n")
                        print(f">>> PRESS (1) : QUICK : PORT-SCANNER")
                        print(f">>> PRESS (2) : PORT-SCANNER (SPECIFIC : WEB-SERVER-PORT)")
                        print(f">>> PRESS (0) : EXIT")
                        
                        choice = str(input("\n>>> ENTER YOUR CHOICE, FOR #'PORT-SCANNER' : "))
                        
                        if len(choice) == "":
                            # ---------- BANNER-NAME (ERROR) ---------- :
                            ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                            print(f"\033[97m {ascii_banner} \033[0m")
                            
                        else:
                            try:
                                # ----- QUICK : PORT-SCANNER ----- :
                                if int(choice) == 1:
                                    # ---------- BANNER-NAME (LOCAL-NETWORK (SCANNER)) ---------- :
                                    ascii_banner = pyfiglet.figlet_format("PORT-SCAN : (QUICK-PATTERN)", font="slant")
                                    print(f"\033[97m {ascii_banner} \033[0m")
                                    
                                    # FUNCTION-CALL, PORT-SCANNER (QUICK-COMMAND-PATTERN) : 
                                    NSAPS.quick_command_pattern_port_scanner()
                                    
                                # ----- PORT-SCANNER (SPECIFIC-PORT) ----- :
                                elif int(choice) == 2:
                                    # ---------- BANNER-NAME (INTERNET-TARGET (SCANNER)) ---------- :
                                    ascii_banner = pyfiglet.figlet_format("PORT-SCAN : SPECIFIC (WEB-SERVER-PORT)", font="slant")
                                    print(f"\033[97m {ascii_banner} \033[0m")
                                    
                                    # FUNCTION-CALL, SPECIFIC (WEB-SERVER : PORT-SCANNER) : 
                                    NSAPS.specific_web_server_port_scanner()
                                    
                                # ----- EXIT ----- :
                                elif int(choice) == 0:
                                    # ---------- BANNER-NAME (THANK-YOU) ---------- :
                                    ascii_banner = pyfiglet.figlet_format("THANK-YOU & VISIT-AGAIN !", font="slant")
                                    print(f"\033[97m {ascii_banner} \033[0m")
                                    break
                                    
                            except ValueError:
                                # ---------- BANNER-NAME (ERROR) ---------- :
                                ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                                print(f"\033[97m {ascii_banner} \033[0m")
                                continue
                        
                # ----- EXIT (TOOL) ----- :
                elif int(choice) == 0:
                    # ---------- BANNER-NAME (THANK-YOU) ---------- :
                    ascii_banner = pyfiglet.figlet_format("THANK-YOU & VISIT-AGAIN #'QUANTUM-TECH' !", font="slant")
                    print(f"\033[97m {ascii_banner} \033[0m")
                
            except ValueError:
                # ---------- BANNER-NAME (ERROR) ---------- :
                ascii_banner = pyfiglet.figlet_format("ERROR ! SOME-THING WENT WRONG, TRY AGAIN ...", font="slant")
                print(f"\033[97m {ascii_banner} \033[0m")

# --------------------
# ERROR-HANDLER (FUNCTION) :
# --------------------
@staticmethod
def error_handler(sig, frame):
    print(f"\n[!] ERROR-HANDLER ! 'SIG' : {sig} AND 'FRAME' : {frame}")
    # ---------- BANNER-NAME (EXIT) ---------- :
    ascii_banner = pyfiglet.figlet_format("CRTL + C (EXIT)", font="slant")
    print(f"\n[!] ALERT ! LOOKS LIKE YOU PRESS '(CRTL + C)' TO #EXIT, THE #QUANTUM-TECH ! VISIT AGAIN ...")
    print(f"\033[90m {ascii_banner} \033[0m")
    sys.exit(f"\n***** THNAK YOU, VISIT AGAIN ! *****")

# USE, SIGNAL (MODULE) :
signal.signal(signal.SIGINT, error_handler)

# --------------------------------------------------
# PYTHON (MAIN-METHOD)
# --------------------------------------------------
if __name__ == "__main__":
    try:
        # ---------- BANNER-NAME (QUANTUM-TECH) ---------- :
        ascii_banner = pyfiglet.figlet_format("QUANTUM-TECH", font="slant")
        print(f"\033[93m {ascii_banner} \033[0m")

        # BANNER-NAME (WEB-APPLICATION VULNERABILITY SCANNER) :
        ascii_banner = pyfiglet.figlet_format("NETWORK (SCANNER) & PORT (SCANNER)", font="slant")
        print(f"\033[90m {ascii_banner} \033[0m")
        
        # CLASS (NSAPS) @OBJECT : 
        nsaps = NSAPS()
        
        # NSAPS (FUNCTION-CALL) -> INFORMATION-GATHER : 
        nsaps.quantum_tech_tool()

    except KeyboardInterrupt:
        print("\n[!] ALERT ! LOOKS LIKE YOU PRESS '(CRTL + C)' TO #EXIT, THE #QUANTUM-TECH ! VISIT AGAIN ...")
        # ---------- BANNER-NAME (EXIT) ---------- :
        ascii_banner = pyfiglet.figlet_format("THANK-YOU & VISIT AGAIN !", font="slant")
        print(f"\033[93m {ascii_banner} \033[0m")

        sys.exit("\n***** THNAK YOU, VISIT AGAIN ! *****")

    except Exception:
        print(f"\n[!] ERROR ! AN ERROR OCCURED : {Exception}")
        sys.exit("\n***** SOME-THING WENT WRONG, TRY AGAIN ! *****")    