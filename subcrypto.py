
import requests
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


try:
    url = sys.argv[1] ## site alvo
    wordlist = open(str(sys.argv[2])) ## Pegar input do usuario do dir do arquivo com a wordlist.


    for linha in wordlist: ## le cada linha da wordlist
        linha = linha.strip() ## tira os espacos da wordlist
        sub_to_check = f"https://{linha}.{url}" ### coloca o cada palavra da wordlist no subdominio do alvo.
        try:
            r = requests.get (sub_to_check ) ## cria uma requisicao com metodo GET, com os parametros da variavel dos subdominios.
            print(bcolors.OKGREEN + f"Subdominio Encontrado: {sub_to_check}") ## printa na tela os subdominios encontrados
            print(bcolors.OKCYAN+"###### Checking by crypto ######")
        except:
            print(bcolors.FAIL+ f"Opps nao existe {sub_to_check}") ## mostra na tela os subdominios nao foram encontrados ou algum erro da excessao.
            print(bcolors.OKCYAN+"###### Checking by crypto ######")
            continue

except:

    print(bcolors.OKCYAN+"███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗    ███████╗██╗   ██╗██████╗     ██████╗ ██╗   ██╗     ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗")
    print(bcolors.OKCYAN+"██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝    ██╔════╝██║   ██║██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗")
    print(bcolors.OKCYAN+"███████╗██║██╔████╔██║██████╔╝██║     █████╗      ███████╗██║   ██║██████╔╝    ██████╔╝ ╚████╔╝     ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║")
    print(bcolors.OKCYAN+"╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝      ╚════██║██║   ██║██╔══██╗    ██╔══██╗  ╚██╔╝      ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║")
    print(bcolors.OKCYAN+"███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗    ███████║╚██████╔╝██████╔╝    ██████╔╝   ██║       ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝ ")
    print(bcolors.OKCYAN+"╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝    ╚══════╝ ╚═════╝ ╚═════╝     ╚═════╝    ╚═╝        ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ")
    print(bcolors.WARNING+"#### github.com/CryptoSecurityx ####\nComo usar: subcrypto.py <dominio> <sua wordlist>\n")
    sys.exit() ## Finaliza caso o usuario nao coloque a input corretas no programa.


############ Crypto Security ###############
######## github.com/CryptoSecurityx ##########
############ Crypto Security ###############

