# JOTARPS
### Cybersecurity Toolkit by jpp

```
     ##   #####  ######  #   #  ####   ####    ####
      #  #    #    #     #   #  #   #  #   #  #
      #  #    #    #     #####  ####   ####    ###
  #   #  #    #    #     #   #  #   #  #          #
   ###    ####     #     #   #  #   #  #      ####
```

> Ferramenta de cybersecurity all-in-one feita para rodar no terminal — incluindo Termux (Android).

---

## Recursos

### Rede & Scan
| # | Ferramenta |
|---|-----------|
| 1 | Port Scanner TCP (multithread) |
| 2 | Ping Sweep / Host Discovery |
| 3 | Traceroute |
| 4 | DNS Lookup & Reverso |
| 5 | WHOIS Manual (via socket) |
| 6 | Banner Grabber |
| 7 | HTTP Header Inspector |
| 8 | Subnet Calculator |

### Analise de Web
| # | Ferramenta |
|---|-----------|
| 9  | Subdominio Finder (wordlist) |
| 10 | Directory Brute Force |
| 11 | URL Fuzzer |
| 12 | Tech Fingerprinter |
| 13 | Extrator de Links |

### Criptografia & Hash
| # | Ferramenta |
|---|-----------|
| 14 | Gerador de Hash (MD5/SHA1/SHA256/SHA512...) |
| 15 | Hash Cracker (wordlist) |
| 16 | Encoder/Decoder Base64 |
| 17 | ROT13 Cipher |
| 18 | XOR Cipher |
| 19 | Caesar Cipher + Brute Force |

### Senhas & Wordlists
| # | Ferramenta |
|---|-----------|
| 20 | Gerador de Senhas Fortes |
| 21 | Gerador de Wordlist |
| 22 | Verificador de Forca de Senha |
| 23 | Mutacao Leet Speak |

### Forense & Info
| # | Ferramenta |
|---|-----------|
| 24 | Info do Sistema Local |
| 25 | Capturador de IP Publico |
| 26 | MAC Address Lookup |
| 27 | Analisador de Arquivo (hex + strings) |
| 28 | Log de Conexoes Ativas |

### Misc & Tools
| # | Ferramenta |
|---|-----------|
| 29 | Gerador de Payload Base64 |
| 30 | IP Geolocation |
| 31 | Ping Flood Tester (CTF/lab) |
| 32 | Reverse Shell Generator |
| 33 | Encoder/Decoder de URL |
| 34 | Decoder JWT |

---

## Instalacao

### Termux (Android)
```bash
pkg install python git -y
git clone https://github.com/jotarps/jotarps.git
cd jotarps
python3 jotarps.py
```

### Linux / macOS
```bash
git clone https://github.com/jotarps/jotarps.git
cd jotarps
python3 jotarps.py
```

### Windows
```bash
git clone https://github.com/jotarps/jotarps.git
cd jotarps
python jotarps.py
```

> Zero dependencias externas — usa apenas bibliotecas padrao do Python 3.

---

## Uso

```
python3 jotarps.py
```

O menu interativo vai aparecer. Digite o numero da ferramenta e pressione ENTER.

---

## Aviso Legal

Esta ferramenta foi criada para fins educacionais, CTF e pentest **com autorizacao**.  
O uso em sistemas sem permissao e ilegal e de responsabilidade exclusiva do usuario.  
O autor nao se responsabiliza por uso indevido.

---

## Autor

**jpp** — [@jotarps](https://github.com/jotarps)

---

![Python](https://img.shields.io/badge/Python-3.x-purple?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Android%20%7C%20Windows-black?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blueviolet?style=flat-square)
