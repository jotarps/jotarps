# JOTARPS — Cybersecurity Toolkit

```
       ____     ____     _______      /\       _____     _____      _____  
       |  |    /    \   |__   __|    /  \     |  __ \   |  __ \    / ____| 
       |  |   |      |     | |      / /\ \    | |__) |  | |__) |  | (___   
   /|  |  |    \    /      | |     /_/  \_\   |  _  /   |  ___/    \___ \  
   \|__|__|     \__/       |_|                |_| \_\   |_|        ____) | 
```

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blueviolet?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Android%20%7C%20Windows-black?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Termux-Compatible-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Dependencies-Zero-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Tools-34-blueviolet?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge"/>
</p>

<p align="center">
  <b>Ferramenta all-in-one de cybersecurity para terminal — roda ate no celular via Termux.</b><br/>
  34 ferramentas. Zero dependencias. 100% Python puro.
</p>

---

## Instalacao Rapida

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

> Nenhuma biblioteca externa necessaria. Funciona com Python 3.6+

---

## O que e o JOTARPS?

JOTARPS e um toolkit de cybersecurity feito inteiramente em Python puro, sem nenhuma dependencia externa. Foi desenvolvido para rodar em qualquer ambiente — do Linux tradicional ao Termux no Android — sem precisar instalar nada alem do Python.

O projeto nasceu com o objetivo de reunir as ferramentas mais usadas em CTF, pentest e aprendizado de seguranca em um unico arquivo interativo, acessivel pelo terminal com um menu simples numerado.

Ideal para:
- Estudantes de cybersecurity e iniciantes em pentest
- Participantes de CTF (Capture The Flag)
- Profissionais que precisam de ferramentas rapidas no terminal
- Usuarios de Termux que querem um toolkit completo no celular

---

## Menu de Ferramentas

```
  [ REDE & SCAN ]
  [1] Port Scanner TCP    [2] Ping Sweep         [3] Traceroute
  [4] DNS Lookup          [5] WHOIS Manual        [6] Banner Grabber
  [7] HTTP Headers        [8] Subnet Calc

  [ ANALISE DE WEB ]
  [9] Subdomain Finder    [10] Dir Brute Force    [11] URL Fuzzer
  [12] Tech Fingerprint   [13] Link Extractor

  [ CRIPTO & HASH ]
  [14] Hash Generator     [15] Hash Cracker       [16] Base64
  [17] ROT13              [18] XOR Cipher         [19] Caesar Cipher

  [ SENHAS & WORDLIST ]
  [20] Password Gen       [21] Wordlist Gen       [22] Pass Strength
  [23] Leet Speak

  [ FORENSE & INFO ]
  [24] System Info        [25] Public IP          [26] MAC Lookup
  [27] File Analyzer      [28] Active Conns

  [ MISC & TOOLS ]
  [29] Payload B64        [30] IP Geolocation     [31] Ping Flood
  [32] Rev Shell Gen      [33] URL Encoder        [34] JWT Decoder
  [35] EXIT

  jotarps@menu >
```

---

## Descricao Detalhada das Ferramentas

### Rede & Scan

#### [1] Port Scanner TCP
Scanner de portas multithread com deteccao de servico. Suporta ranges grandes rapidamente usando centenas de threads simultaneas.
- Entrada: host/IP + range de portas (ex: 1-65535)
- Saida: portas abertas + nome do servico
- Velocidade: multithread (ate 200 threads simultaneas)

#### [2] Ping Sweep / Host Discovery
Descobre hosts ativos em uma rede inteira usando CIDR.
- Entrada: notacao CIDR (ex: 192.168.1.0/24)
- Saida: lista de IPs ativos com resposta ao ping
- Multithread para varredura rapida

#### [3] Traceroute
Rastreia o caminho dos pacotes ate o destino, mostrando cada salto na rota.
- Usa o traceroute nativo do sistema
- Compativel com Linux, macOS e Windows

#### [4] DNS Lookup & Reverso
Resolve dominios para IPs (IPv4 e IPv6) e faz lookup reverso de IPs para hostnames.
- Suporta resolucao direta e reversa
- Mostra todos os registros encontrados

#### [5] WHOIS Manual
Consulta informacoes de registro de dominios diretamente via socket, sem depender de ferramentas externas.
- Conecta ao servidor WHOIS da IANA automaticamente
- Segue referencias para o WHOIS correto do dominio

#### [6] Banner Grabber
Captura banners de servicos em portas especificadas para identificar versoes e softwares rodando.
- Util para fingerprinting de servicos
- Suporta multiplas portas de uma vez

#### [7] HTTP Header Inspector
Analisa os cabecalhos HTTP de qualquer URL, destacando headers de seguranca importantes.
- Destaca: Server, X-Powered-By, X-Frame-Options, CSP
- Ignora erros de certificado SSL

#### [8] Subnet Calculator
Calcula todos os dados de uma sub-rede a partir de uma notacao CIDR.
- Mostra: rede, broadcast, mascara, wildcard, primeiro/ultimo host, total de hosts

---

### Analise de Web

#### [9] Subdomain Finder
Descobre subdominios de um dominio usando uma wordlist. Usa threads para maior velocidade.
- Wordlist padrao embutida com 25 subdominios comuns
- Suporta wordlists externas
- Resolve e mostra o IP de cada subdominio encontrado

#### [10] Directory Brute Force
Testa caminhos em um servidor web para encontrar diretorios e arquivos ocultos.
- Wordlist padrao com paths comuns (admin, login, wp-admin, .git, etc)
- Suporta wordlists externas
- Mostra codigo HTTP de cada resposta

#### [11] URL Fuzzer
Substitui a palavra FUZZ em uma URL por valores de uma wordlist ou range numerico.
- Modo numerico: testa IDs sequenciais
- Modo wordlist: testa qualquer lista de payloads
- Util para encontrar parametros vulneraveis

#### [12] Tech Fingerprinter
Identifica as tecnologias usadas em um site analisando o HTML e cabecalhos HTTP.
- Detecta: WordPress, Joomla, Drupal, Laravel, Django, React, Vue, Angular, jQuery, Bootstrap, PHP, ASP.NET, Nginx, Apache, Cloudflare e mais

#### [13] Link Extractor
Extrai todos os links (href e src) de uma pagina web.
- Remove duplicatas automaticamente
- Util para mapeamento de superficie de ataque

---

### Criptografia & Hash

#### [14] Hash Generator
Gera hashes de textos ou arquivos em multiplos algoritmos simultaneamente.
- Algoritmos: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SHA3-256, BLAKE2b
- Suporta texto direto ou caminho de arquivo

#### [15] Hash Cracker
Tenta quebrar um hash comparando com uma wordlist.
- Suporta: MD5, SHA1, SHA256 e qualquer algoritmo do hashlib
- Mostra progresso a cada 5000 tentativas

#### [16] Base64 Encoder/Decoder
Codifica e decodifica strings em Base64.

#### [17] ROT13
Aplica a cifra ROT13 em um texto. Como e simetrica, serve para encode e decode.

#### [18] XOR Cipher
Aplica XOR entre um texto e uma chave string.
- Saida em hexadecimal e Base64
- Chave ciclica

#### [19] Caesar Cipher
Cifra de Cesar com suporte a encode, decode e brute force completo (25 shifts).

---

### Senhas & Wordlists

#### [20] Password Generator
Gera senhas criptograficamente seguras usando SystemRandom.
- Configuravel: tamanho, quantidade, incluir simbolos

#### [21] Wordlist Generator
Cria wordlists personalizadas com mutacoes automaticas.
- Adiciona anos, numeros, simbolos, leet speak
- Salva em arquivo .txt

#### [22] Password Strength
Analisa uma senha em 9 criterios e da uma pontuacao de forca.
- Niveis: MUITO FRACA / FRACA / MEDIA / FORTE
- Entrada oculta

#### [23] Leet Speak Mutator
Aplica 3 estilos diferentes de substituicao leet speak em uma palavra.

---

### Forense & Info

#### [24] System Info
Exibe informacoes completas do sistema: hostname, IP, OS, CPU, usuario, interfaces de rede.

#### [25] Public IP
Descobre o IP publico da maquina consultando servicos externos.

#### [26] MAC Lookup
Identifica o fabricante de um dispositivo a partir do MAC address via API.

#### [27] File Analyzer
Analisa qualquer arquivo: tamanho, magic bytes, MD5, SHA256, hex dump e strings.

#### [28] Active Connections
Mostra todas as conexoes de rede ativas usando netstat.

---

### Misc & Tools

#### [29] Payload Base64
Gera payloads encodados prontos para CTF e pentest autorizado.
- Suporte a Bash, Python3 e PHP

#### [30] IP Geolocation
Geolocalizacao de qualquer IP: pais, cidade, ISP, timezone, coordenadas.

#### [31] Ping Flood Tester
Envia pings rapidos para teste de estabilidade em ambiente controlado.
- Requer confirmacao de uso responsavel

#### [32] Reverse Shell Generator
Gera reverse shells prontos para CTF e pentest autorizado.
- Tipos: Bash, Python3, Netcat, Perl, PHP, PowerShell

#### [33] URL Encoder/Decoder
Codifica e decodifica strings para uso em URLs.

#### [34] JWT Decoder
Decodifica tokens JWT mostrando header e payload.
- Converte timestamps para data legivel
- Avisa que assinatura nao e verificada

---

## Estrutura do Projeto

```
jotarps/
  jotarps.py    -- tudo em um unico arquivo
  README.md     -- documentacao
```

---

## Compatibilidade

| Plataforma | Status |
|-----------|--------|
| Linux (Debian/Ubuntu/Arch) | OK |
| Android (Termux) | OK |
| macOS | OK |
| Windows | OK |
| Python 3.6+ | OK |

---

## Aviso Legal

Esta ferramenta foi desenvolvida exclusivamente para fins educacionais, pratica em CTF e pentest com autorizacao expressa do proprietario do sistema alvo.

**O uso desta ferramenta em sistemas sem autorizacao e crime.**

O autor nao se responsabiliza por qualquer uso indevido.

---

## Contribuindo

Pull requests sao bem-vindos!

1. Fork o projeto
2. Crie sua branch: `git checkout -b minha-feature`
3. Commit: `git commit -m "Adiciona nova ferramenta"`
4. Push: `git push origin minha-feature`
5. Abra um Pull Request

---

## Roadmap

- [ ] Scanner UDP
- [ ] SMTP Enumerator
- [ ] Analisador de pcap
- [ ] Escaner de vulnerabilidades web basico
- [ ] Exportar resultados para arquivo
- [ ] Modo verboso/silencioso

---

## Autor

Feito por **jpp** — [@jotarps](https://github.com/jotarps)

Se o projeto te ajudou, deixa uma estrela!

---

## Licenca

MIT License — Copyright (c) 2026 jotarps
