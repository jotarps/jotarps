# JOTARPS — Cybersecurity Toolkit

```
     ##   #####  ######  #   #  ####   ####    ####
      #  #    #    #     #   #  #   #  #   #  #
      #  #    #    #     #####  ####   ####    ###
  #   #  #    #    #     #   #  #   #  #          #
   ###    ####     #     #   #  #   #  #      ####
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

Ao rodar o JOTARPS voce vera um menu assim:

```
  [ REDE & SCAN ]
   [ 1] Port Scanner TCP
   [ 2] Ping Sweep / Host Discovery
   [ 3] Traceroute
   [ 4] DNS Lookup & Reverso
   [ 5] WHOIS Manual (via socket)
   [ 6] Banner Grabber
   [ 7] HTTP Header Inspector
   [ 8] Subnet Calculator

  [ ANALISE DE WEB ]
   [ 9] Subdominio Finder (wordlist)
   [10] Directory Brute Force
   [11] URL Fuzzer
   [12] Tech Fingerprinter
   [13] Extrator de Links

  [ CRIPTOGRAFIA & HASH ]
   [14] Gerador de Hash (MD5/SHA)
   [15] Hash Cracker (wordlist)
   [16] Encoder/Decoder Base64
   [17] ROT13 Cipher
   [18] XOR Cipher
   [19] Caesar Cipher

  [ SENHAS & WORDLISTS ]
   [20] Gerador de Senhas Fortes
   [21] Gerador de Wordlist
   [22] Verificador de Forca de Senha
   [23] Mutacao Leet Speak

  [ FORENSE & INFO ]
   [24] Info do Sistema Local
   [25] Capturador de IP Publico
   [26] MAC Address Lookup
   [27] Analisador de Arquivo (hex/strings)
   [28] Log de Conexoes Ativas

  [ MISC & TOOLS ]
   [29] Gerador de Payload Base64
   [30] IP Geolocation
   [31] Ping Flood Tester (CTF/lab)
   [32] Reverse Shell Generator
   [33] Encoder/Decoder de URL
   [34] Decoder JWT
   [35] SAIR

  jotarps@menu >
```

Digite o numero da ferramenta e pressione ENTER.

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
Rastreia o caminho dos pacotes ate o destino, mostrando cada salto (hop) na rota.
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

#### [9] Subdominio Finder
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
- Analisa corpo da pagina + headers simultaneamente

#### [13] Extrator de Links
Extrai todos os links (href e src) de uma pagina web.
- Remove duplicatas automaticamente
- Util para mapeamento de superficie de ataque

---

### Criptografia & Hash

#### [14] Gerador de Hash
Gera hashes de textos ou arquivos em multiplos algoritmos simultaneamente.
- Algoritmos: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SHA3-256, BLAKE2b
- Suporta texto direto ou caminho de arquivo

#### [15] Hash Cracker
Tenta quebrar um hash comparando com uma wordlist.
- Suporta: MD5, SHA1, SHA256 e qualquer algoritmo do hashlib
- Mostra progresso a cada 5000 tentativas

#### [16] Base64 Encoder/Decoder
Codifica e decodifica strings em Base64.
- Modo encode e decode
- Saida limpa sem espacos extras

#### [17] ROT13
Aplica a cifra ROT13 em um texto. Como ROT13 e simetrica, a mesma operacao serve para encode e decode.

#### [18] XOR Cipher
Aplica XOR entre um texto e uma chave string.
- Saida em hexadecimal e Base64
- Chave ciclica (repete automaticamente)

#### [19] Caesar Cipher
Cifra de Cesar com suporte a encode, decode e brute force.
- Modo encode: cifra com shift escolhido
- Modo decode: decifra com shift escolhido
- Modo brute force: testa todos os 25 shifts possiveis

---

### Senhas & Wordlists

#### [20] Gerador de Senhas Fortes
Gera senhas criptograficamente seguras usando `random.SystemRandom`.
- Configuravel: tamanho, quantidade, incluir simbolos
- Usa SystemRandom (criptograficamente seguro)

#### [21] Gerador de Wordlist
Cria wordlists personalizadas baseadas em uma palavra-base com mutacoes automaticas.
- Adiciona anos, numeros, simbolos
- Aplica variacoes de capitalizacao
- Gera versoes leet speak automaticamente
- Salva em arquivo .txt

#### [22] Verificador de Forca de Senha
Analisa uma senha em 9 criterios e da uma pontuacao de forca.
- Criterios: comprimento, maiusculas, minusculas, numeros, simbolos, diversidade, repeticoes
- Niveis: MUITO FRACA / FRACA / MEDIA / FORTE
- Entrada oculta (nao aparece na tela)

#### [23] Mutacao Leet Speak
Aplica diferentes estilos de substituicao leet speak em uma palavra.
- 3 estilos diferentes de leet
- Util para gerar variantes de senhas em wordlists

---

### Forense & Info

#### [24] Info do Sistema Local
Exibe informacoes completas do sistema onde o JOTARPS esta rodando.
- Hostname, IP local, OS, CPU, versao Python, usuario, data/hora, diretorio atual
- Lista interfaces de rede com IPs

#### [25] Capturador de IP Publico
Descobre o IP publico da maquina consultando servicos externos.
- Tenta multiplos servicos em sequencia
- Mostra qual servico respondeu

#### [26] MAC Address Lookup
Identifica o fabricante de um dispositivo a partir do seu endereco MAC.
- Extrai o OUI (primeiros 3 octetos)
- Consulta a API macvendors.com

#### [27] Analisador de Arquivo
Analisa qualquer arquivo mostrando informacoes forenses.
- Tamanho, magic bytes, MD5, SHA256
- Hex dump dos primeiros 256 bytes
- Extrai strings legiveis (minimo 6 chars)

#### [28] Log de Conexoes Ativas
Mostra todas as conexoes de rede ativas no sistema.
- Usa netstat nativo
- Destaca conexoes ESTABLISHED e portas em LISTEN

---

### Misc & Tools

#### [29] Gerador de Payload Base64
Gera payloads encodados em Base64 prontos para uso em CTF e pentest autorizado.
- Suporte a Bash, Python3 e PHP
- Mostra o payload completo para execucao

#### [30] IP Geolocation
Geolocalizacao de qualquer IP usando a API ip-api.com.
- Mostra: pais, estado, cidade, ISP, organizacao, timezone, latitude/longitude
- Funciona com IPv4 publico

#### [31] Ping Flood Tester
Envia pings rapidos para testar estabilidade de rede em ambiente controlado.
- Requer confirmacao explicita de uso responsavel
- Apenas para redes proprias ou com autorizacao

#### [32] Reverse Shell Generator
Gera reverse shells prontos para copiar e usar em CTF e pentest autorizado.
- Tipos: Bash, Python3, Netcat, Netcat mkfifo, Perl, PHP, PowerShell
- Mostra tambem o comando de listener (nc -lvnp)

#### [33] Encoder/Decoder de URL
Codifica e decodifica strings para uso em URLs.
- Modo encode: URL encode e URL encode completo
- Modo decode: decodifica %XX de volta para texto

#### [34] Decoder JWT
Decodifica tokens JWT mostrando header e payload sem verificar assinatura.
- Decodifica Base64url automaticamente
- Converte timestamps (exp, iat, nbf) para data legivel
- Avisa que a assinatura nao e verificada

---

## Estrutura do Projeto

```
jotarps/
  jotarps.py    -- arquivo principal (tudo em um unico arquivo)
  README.md     -- documentacao
```

Tudo em um unico arquivo Python para facilitar distribuicao e uso rapido.

---

## Compatibilidade

| Plataforma | Status |
|-----------|--------|
| Linux (Debian/Ubuntu/Arch) | OK |
| Android (Termux) | OK |
| macOS | OK |
| Windows | OK |
| Python 3.6+ | OK |
| Python 2.x | NAO suportado |

---

## Aviso Legal

Esta ferramenta foi desenvolvida exclusivamente para fins educacionais, pratica em CTF e pentest com autorizacao expressa do proprietario do sistema alvo.

**O uso desta ferramenta em sistemas sem autorizacao e crime.**

O autor nao se responsabiliza por qualquer uso indevido. Use com responsabilidade.

---

## Contribuindo

Pull requests sao bem-vindos!

1. Fork o projeto
2. Crie sua branch: `git checkout -b minha-feature`
3. Commit: `git commit -m "Adiciona nova ferramenta"`
4. Push: `git push origin minha-feature`
5. Abra um Pull Request

Ideias de novas ferramentas? Abre uma Issue!

---

## Roadmap

- [ ] Scanner UDP
- [ ] SMTP Enumerator
- [ ] Brute force SSH (com autorizacao)
- [ ] Decodificador de QR Code
- [ ] Analisador de pcap
- [ ] Gerador de certificado SSL autoassinado
- [ ] Escaner de vulnerabilidades web basico
- [ ] Interface colorida melhorada
- [ ] Exportar resultados para arquivo

---

## Autor

Feito por **jpp** — [@jotarps](https://github.com/jotarps)

Se o projeto te ajudou, deixa uma estrela! Ajuda o projeto a crescer.

---

## Licenca

```
MIT License

Copyright (c) 2026 jotarps

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
