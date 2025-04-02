import dns.resolver

def coletar_dns(domain):
    try:
        print(f"Registros A para {domain}:")
        respostas_a = dns.resolver.resolve(domain, 'A')
        for rdata in respostas_a:
            print(rdata.to_text())
        
        print(f"\nRegistros MX para {domain}:")
        respostas_mx = dns.resolver.resolve(domain, 'MX')
        for rdata in respostas_mx:
            print(rdata.to_text())
        
        print(f"\nRegistros NS para {domain}:")
        respostas_ns = dns.resolver.resolve(domain, 'NS')
        for rdata in respostas_ns:
            print(rdata.to_text())
    
    except dns.resolver.NoAnswer:
        print(f"Não foi possível encontrar registros DNS para {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"O domínio {domain} não existe.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    dominio = input("Digite o domínio para consultar: ")
    coletar_dns(dominio)
