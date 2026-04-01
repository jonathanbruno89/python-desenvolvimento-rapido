contribuintes={}
def adicionar_contribuinte():
    nome = input("Nome completo:").strip().title()
    cpf = input("CPF (somente números): ").strip()
    renda = float(input("Renda mensal (R$):"))
    contribuintes[cpf] = {"nome": nome, "renda": renda}
    print(f"{nome} cadastrado com renda de R$ {renda:.2f}.")
def calcular_ir(renda):
    if renda <= 2112:
        return 0
    elif renda <= 2826.65:
        return renda * 0.075 - 158.40
    elif renda <= 3751.05:
        return renda * 0.15 - 370.40
    elif renda <= 4664.68:
        return renda * 0.225 - 651.73
    else:
        return renda * 0.275 - 884.96
def ver_contribuintes():
    print("\n=== Lista de Contribuintes ===")
    if not contribuintes:
        print("Nenhum contribuinte cadastrado.")
    else:
        for cpf, dados in contribuintes.items():
            print(f"Nome: {dados['nome']} | CPF: {cpf} | Renda: R$ {dados['renda']:.2f}")
def calcular_ir_contribuinte():
    cpf = input("Digite o CPF do contribuinte: ").strip()
    if cpf in contribuintes:
        renda = contribuintes[cpf]["renda"]
        nome = contribuintes[cpf]["nome"]
        imposto = calcular_ir(renda)
        print(f"\nContribuinte: {nome}")
        print(f"\nRenda Mensal: R$ {renda:.2f}")
        print(f"Imposto de Renda devido: R$ {imposto:.2f}")
    else:
        print("CPF não encontrado no sistema.")
def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Adicionar contribuintes")
        print("2 - Ver lista de contribuintes")
        print("3 - Calcular imposto de renda de um contribuinte")
        print("4 - Sair")
        opcao = input("Escolha uma opção.")
        if opcao == '1':
            adicionar_contribuinte()
        elif opcao == '2':
            ver_contribuintes()
        elif opcao == '3':
            calcular_ir_contribuinte()
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tenta novamente.")

menu()
            