import requests

def pegar_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    
    dolar = float(dados["USDBRL"]["bid"])
    euro = float(dados["EURBRL"]["bid"])
    libra = float(dados["GBPBRL"]["bid"])

    return dolar, euro, libra

dolar, euro, libra = pegar_cotacao()

print(f"\nCotação atual:")
print(f"Dólar: R$ {dolar:.2f}")
print(f"Euro: R$ {euro:.2f}")
print(f"Libra: R$ {libra:.2f}")

while True:
    print("\n=== Conversor de Moedas ===")
    print("1 - Real para Dólar")
    print("2 - Real para Euro")
    print("3 - Real para Libra")
    print("4 - Atualizar cotação")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Saindo...")
        break
    elif opcao == "4":
        dolar, euro, libra = pegar_cotacao()
        print("\nCotação atualizada com sucesso!")
        print(f"Dólar: R$ {dolar:.2f}")
        print(f"Euro: R$ {euro:.2f}")
        print(f"Libra: R$ {libra:.2f}")
    elif opcao in ["1", "2", "3"]:
        valor_reais = float(input("Digite o valor em reais (R$): "))

        if opcao == "1":
            resultado = valor_reais/dolar
            print(f"R$ {valor_reais:.2f} = US$ {resultado:.2f}")
        elif opcao == "2":
            resultado = valor_reais/euro
            print(f"R$ {valor_reais:.2f} = € {resultado:.2f}")
        elif opcao == "3":
            resultado = valor_reais/libra
            print(f"R$ {valor_reais:.2f} = £ {resultado:.2f}") 
        else:
            print("Opção inválida!")          