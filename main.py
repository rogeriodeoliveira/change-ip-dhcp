import subprocess
import json

with open('config.txt') as config:
    configJson = json.load(config)

    INTERFACE = configJson["INTERFACE"]
    IP = configJson["IP"]
    MASK = configJson["MASK"]
    GATEWAY = configJson["GATEWAY"]
    DNS = configJson["DNS"]


def setFixIP():
    getstatus = subprocess.call(f'netsh interface ipv4 show config name="Ethernet" | findstr /c:"DHCP" | findstr /c:"Não"',shell=True,stdout=subprocess.DEVNULL)
    if getstatus == 0:
        print(f'O modo DHCP está desativado na interface {INTERFACE}')
        print("Ativando DHCP...")
        subprocess.call(f'cmd /c netsh interface ipv4 set address name={INTERFACE} source=dhcp')
        subprocess.call(f'cmd /c netsh interface ipv4 set dnsservers name={INTERFACE} source=dhcp')
        print("DHCP Ativado!")
        input("Pressione Enter para sair")
    elif getstatus == 1:
        print(f'O modo DHCP está Ativado na interface {INTERFACE}')
        print("Realizando configuração estática...")
        subprocess.call(f'cmd /c netsh interface ip set address name={INTERFACE} static {IP} {MASK} {GATEWAY} store=persistent')
        subprocess.call(f'cmd /c netsh interface ipv4 set dnsservers name={INTERFACE}  source=static address={DNS} validate=no')
        print(f'IP Setado: :{IP}')
        print(f'MASCARA Setado: :{MASK}')
        print(f'GATEWAY Setado: :{GATEWAY}')
        print(f'DNS Setado: :{DNS}')
        input("Pressione Enter para sair")
if __name__ == '__main__':
    setFixIP()