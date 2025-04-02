from scapy.all import ARP, Ether, srp

def varredura_arp(intervalo_ip):
    arp_request = ARP(pdst=intervalo_ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    pacote = broadcast/arp_request
    
    resposta = srp(pacote, timeout=3, verbose=False)[0]
    
    for _, resposta_arp in resposta:
        print(f"IP: {resposta_arp.psrc}, MAC: {resposta_arp.hwsrc}")

if __name__ == "__main__":
    intervalo = "192.168.1.0/24"
    varredura_arp(intervalo)
