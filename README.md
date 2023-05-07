# arpspoof
Demonstração de ARP Spoofing utilizando a biblioteca SCAPY em Python

# Assuntos estudados
- Protocolo ARP
- Encapsulamento de pacotes de rede
- Manipulação de pacotes de rede com a biblioteca SCAPY

# Utilização
Altere a linha 7 colocando o IP alvo cujas tabelas ARP dos dispositivos da rede local passarão a registrar o endereço MAC escolhido na linha 8.
Configure a linha 9 de acordo com a faixa de IP da rede local.
```Python
spoof_ip = "192.168.0.1" #IP a ser falsificado (neste exemplo: Gateway da rede)
my_mac = get_if_hwaddr(conf.iface) #MAC Address da interface padrão
target_IP = "192.168.0.255" #broadcast
target_MAC = "FF:FF:FF:FF:FF:FF" #broadcast
```
