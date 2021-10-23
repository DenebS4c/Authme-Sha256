# [+]==================[Creditos]==================[+]
#  #                                                #
#  #     Devs: Ghosty / xNullCode / Deneb           #
#  #     Discord:                                   #
#  #        Deneb007,#6666                          #
#  #     Derechos de Author:                        #
#  #         Ghosty / xNullCode / Deneb             #
# [+]==================[Creditos]==================[+]
#
#                        |\**/|
#                        \ == /
#                         |  |
#                         |  |
#                         \  /
#                          \/
#
# [+]==================[Start Code]==================[+]
#
# [+]==================[Imports]==================[+]

import hashlib, sys, colorama, os
from colorama import *

# [+]==================[Imports]==================[+]


# [+]==================[Extra]==================[+]

if os.name != "nt":
    os.system("clear")
else:
    os.system("title Developer » github.com/DenebS4c")
    os.system("cls")
    init(convert=True)

# [+]==================[Extra]==================[+]


# [+]==================[Banner]==================[+]

def banner(sexo):
    if sexo == "help":
        print(rf"""
                            {Fore.LIGHTCYAN_EX}ᶫᵒᵛᵉᵧₒᵤ
    {Fore.LIGHTMAGENTA_EX}╭────────────────━━━━━━━━━━━━━━━━━━━━━━━━━────────────────╮
    |{Fore.LIGHTCYAN_EX}              /\                                         {Fore.LIGHTMAGENTA_EX}|
    |{Fore.LIGHTCYAN_EX}  /vvvvvvvvvvvv \--------------------------------------, {Fore.LIGHTMAGENTA_EX}|
    |{Fore.LIGHTCYAN_EX}  `^^^^^^^^^^^^ /====================================="  {Fore.LIGHTMAGENTA_EX}|
    |{Fore.LIGHTCYAN_EX}              \/                                         {Fore.LIGHTMAGENTA_EX}|
    ╰────────────────━━━━━━━━━━━━━━━━━━━━━━━━━────────────────╯
                            {Fore.LIGHTCYAN_EX}ᶫᵒᵛᵉᵧₒᵤ
                               
        {Fore.LIGHTMAGENTA_EX}╭────────────────━━━━━━━━━━━━━━━────────────────╮
        | {Fore.LIGHTCYAN_EX}Use » python3 BreakPoint.py <hash> <wordlist> {Fore.LIGHTMAGENTA_EX}| 
        ╰────────────────━━━━━━━━━━━━━━━────────────────╯
                            {Fore.LIGHTCYAN_EX}ᶫᵒᵛᵉᵧₒᵤ
        """)
    else:
        print(rf"""{Fore.LIGHTMAGENTA_EX}
                            {Fore.LIGHTCYAN_EX}ᶫᵒᵛᵉᵧₒᵤ
    {Fore.LIGHTMAGENTA_EX}╭────────────────━━━━━━━━━━━━━━━━━━━━━━━━━────────────────╮
    |{Fore.LIGHTCYAN_EX}              /\                                         {Fore.LIGHTMAGENTA_EX}|
    |{Fore.LIGHTCYAN_EX}  /vvvvvvvvvvvv \--------------------------------------, {Fore.LIGHTMAGENTA_EX}|
    |{Fore.LIGHTCYAN_EX}  `^^^^^^^^^^^^ /====================================="  {Fore.LIGHTMAGENTA_EX}|
    |{Fore.LIGHTCYAN_EX}              \/                                         {Fore.LIGHTMAGENTA_EX}|
    ╰────────────────━━━━━━━━━━━━━━━━━━━━━━━━━────────────────╯
                            {Fore.LIGHTCYAN_EX}ᶫᵒᵛᵉᵧₒᵤ
        """)

# [+]==================[Banner]==================[+]


# [+]==================[Arguments]==================[+]

if len(sys.argv) != 3:
    banner(sexo="help")
    sys.exit(-1)

hash = sys.argv[1]
wordlist = sys.argv[2]
try:
    hash2 = hash.split("$", 16)
    hash = hash2[2]
    salt = hash2[1]
except:
    hash2 = hash.split("$", 10)
    hash = hash2[2]
    salt = hash2[1]

# [+]==================[Arguments]==================[+]


# [+]==================[Read WordList]==================[+]

banner(sexo="")
print(f'        {Fore.LIGHTMAGENTA_EX}[ {Fore.LIGHTCYAN_EX}BreakPoint {Fore.LIGHTMAGENTA_EX}] {Fore.LIGHTCYAN_EX}Cargando Contraseñas de {Fore.LIGHTMAGENTA_EX}» {Fore.LIGHTCYAN_EX}{wordlist}')
try:
    wordlist = [x.strip() for x in open(file=wordlist, encoding='utf-8', mode='r', errors='ignore').readlines()]
except:
    print(f'        {Fore.LIGHTMAGENTA_EX}[ {Fore.LIGHTCYAN_EX}BreakPoint {Fore.LIGHTMAGENTA_EX}] {Fore.LIGHTCYAN_EX}Error Cargando Wordlist.')
    sys.exit(-1)

# [+]==================[Read WordList]==================[+]


# [+]==================[Get Password]==================[+]

intentos = 0 
for password in wordlist:
    intentos += 1
    bruteforce = hashlib.sha256(hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8') + salt.encode('utf-8')).hexdigest()
    if bruteforce == hash:
        print(f'        {Fore.LIGHTMAGENTA_EX}[ {Fore.LIGHTCYAN_EX}BreakPoint {Fore.LIGHTMAGENTA_EX}] {Fore.LIGHTCYAN_EX}Contraseña Encontrada {Fore.LIGHTMAGENTA_EX}» {Fore.LIGHTCYAN_EX}{password}')
        sys.exit(-1)
print(f'        {Fore.LIGHTMAGENTA_EX}[ {Fore.LIGHTCYAN_EX}BreakPoint {Fore.LIGHTMAGENTA_EX}] {Fore.LIGHTCYAN_EX}Contraseña No Encontrada')

# [+]==================[Get Password]==================[+]
#
#
# [+]==================[End Code]==================[+]
#
#                          /\           
#                         /  \    
#                         |  |     
#                         |  |     
#                        / == \    
#                        |/**\|  
#    
# [+]==================[Creditos]==================[+]
#  #                                                #
#  #     Devs: Ghosty / xNullCode / Deneb           #
#  #     Discord:                                   #
#  #        Deneb007,#6666                          #
#  #     Derechos de Author:                        #
#  #         Ghosty / xNullCode / Deneb             #
# [+]==================[Creditos]==================[+]
