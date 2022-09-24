import os
import json

def setFixIP():
    getstatus = os.system('netsh interface ip show config "Ethernet" | findstr /c:"DHCP" | findstr /c:"Não"' )
    if getstatus == 0:
        print("O modo DHCP está desativado!")
        print("Ativando DHCP...")
        os.system('cmd /c netsh interface ip set address name="Ethernet" dhcp')
        print("DHCP Ativado!")
        input("Pressione Enter para sair")
    elif getstatus == 1:
        print("O modo DHCP está Ativado!")
        print("Realizando configuração estática...")
        with open('config.txt') as config:
            configJson = json.load(config)

            IP = configJson["IP"]
            MASK = configJson["MASK"]
            GATEWAY = configJson["GATEWAY"]
            DNS = configJson["DNS"]

        os.system(f'cmd /c netsh interface ip set address name="Ethernet" static {IP} {MASK} {GATEWAY}')
        print(f'IP Setado: :{IP}')
        print(f'MASCARA Setado: :{MASK}')
        print(f'GATEWAY Setado: :{GATEWAY}')
        print(f'DNS Setado: :{DNS}')
        input("Pressione Enter para sair")
if __name__ == '__main__':
    setFixIP()