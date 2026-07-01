<<<<<<< HEAD
from random import randint
from datetime import datetime
lista_cadastros=[]
lista_produtos=[]
lista_vendas=[]
vendas={"vendas":[]}
brindes=["Calendario", "Pano de prato", "tupperware", "Chaveiro", "Unhex", "Abridor de Garrafa", "Camisa do Brasil", "Capa de bujão"]


def cadastrar(lista_de_usuarios):
    valido=True
    print("=-=-=-CADASTRAR CLIENTE-=-=-=")
    nome=input("Nome: ").upper()
    while True:
        if nome.isalpha()==True:
            break
        else:
            print("Digite um nome válido!")
            nome=input("Nome: ")
    cpf=input("Cpf: ")
    while True:
        if len(cpf)==11 and int(cpf).is_integer()==True:
            break
        else:
            print("Digite um cpf válido!")
            cpf=input("Cpf: ")
    for cadastros in lista_cadastros:
        if cadastros[1]==cpf:
            valido=False
    senha=input("Senha: ")
    senha_2=input("Repita a senha: ")
    while senha!=senha_2:
        print("As senhas não coincidem!")
        senha=input("Senha: ")
        senha_2=input("Repita a senha: ")
    if valido ==True:
        lista_de_usuarios.append([nome,cpf,senha])
        print("CADASTRO REALIZADO COM SUCESSO!")
        print(f"=-=-=-=-=-=-=--=-=-=")
        input("APERTE ENTER PARA CONTINUAR...")
    else:
        print("NÃO FOI POSSÍVEL FAZER O CADASTRO, O CPF JÁ ESTÁ SENDO UTILIZADO!")
        print(f"=-=-=-=-=-=-=--=-=-=")
        input("APERTE ENTER PARA CONTINUAR...")

def listar_cadastros(lista):
    if len(lista)>=1:
        contador=1
        for cadastro in lista:
            print(f"\n=-=-=-Cliente {contador}=-=-=-")
            print("Nome: ",cadastro[0])
            print("Cpf: ",cadastro[1])
            print(f"=-=-=-=-=-=-=--=-=-=")
            contador+=1
    else:
        print("SEM CLIENTES CADASTRADOS!")
    input("APERTE ENTER PARA CONTINUAR...")

def alterar_cadastros(lista):
    if len(lista)>=1:
        cpf=input("CPF: ")
        for cadastro in lista:
            if cadastro[1]==cpf:
                print("CLIENTE ENCONTRADO!")
                print("Digite 1 para alterar o nome")
                print("Digite 2 para alterar o cpf")
                print("Digite 3 para alterar a senha")
                print("Digite 4 para cancelar a operação")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                resposta=input("Sua resposta: ")
                if resposta=="1":
                    novo_nome=input("Novo nome: ")
                    novo_nome2=input("Digite novamente: ")
                    if novo_nome==novo_nome2:
                        cadastro[0]=novo_nome.upper()
                        print("NOME ALTERADO COM SUCESSO!")
                    else:
                        print("OS NOMES NÃO COINCIDEM!")
                elif resposta=="2":
                    novo_cpf=input("Cpf: ")
                    while True:
                        if len(novo_cpf)==11 and int(novo_cpf).is_integer()==True:
                            valido=True
                            print("TEM CERTEZA QUE DESEJA ALTERAR O CPF?")
                            resposta=input("Digite 1 para SIM e 2 para NÃO\nSua resposta: ")
                            if resposta=="1":
                                for cliente in lista:
                                    if cliente[1]==novo_cpf:
                                        valido=False
                                if valido==True:
                                    cadastro[1]=novo_cpf
                                    print("CPF ALTERADO COM SUCESSO!")
                                else:
                                    print("OPERAÇÃO INVÁLIDA, O CPF JÁ ESTÁ EM USO!")
                                    break
                            else:
                                print("OPERAÇÃO CANCELADA!")
                            break
                        else:
                            print("CPF INVÁLIDO!")
                            novo_cpf=input("Cpf: ")
                elif resposta=="3":
                    nova_senha=input("Nova senha: ")
                    nova_senha2=input("Digite novamente: ")
                    if nova_senha!=nova_senha2 or nova_senha==cadastro[2]:
                        while True:
                            print("AS SENHAS PRECISAM SER IGUAIS E DIFERENTES DA SENHA ANTERIOR!")
                            nova_senha=input("Nova senha: ")
                            nova_senha2=input("Digite novamente: ")
                            if nova_senha==nova_senha2 and nova_senha!=cadastro[2]:
                                cadastro[2]=nova_senha
                                print("SENHA ALTERADA COM SUCESSO!")
                                break
    else:
        print("NENHUM CADASTRO FOI REALIZADO!")
    input("APERTE ENTER PARA CONTINUAR...")

def deletar_cadastro(lista):
    if len(lista)>0:
        listar_cadastros(lista)
        input("APERTE ENTER PARA CONTINUAR...")
        num_cadastro=int(input(("\nDigite o número do cadastro para ser deletado: ")))
        if num_cadastro<=len(lista) and num_cadastro>=1:
            print(f"Tem certeza que deseja excluir o cadastro: \nCliente:{lista[num_cadastro-1][0]} \nCpf: {lista[num_cadastro-1][1]}")
            print("Digite 1 para SIM\n-=-=-=-=-=-=-=-=-=-=-=")
            resposta=input("Sua resposta: ")
            if resposta=="1":
                lista.pop(num_cadastro-1)
                print("CADASTRADO DELETADO COM SUCESSO!")
            else:
                print("O CADASTRO NÃO FOI DELETADO, OPERAÇÃO CANCELADA!")
        else:
            print("NÚMERO INVÁLIDO, OPERAÇÃO CANCELADA!")
    else:
        print("NÃO EXISTE CADASTROS!")
    input("APERTE ENTER PARA CONTINUAR...")
=======
def alterar_produtos(lista):
    if len(lista)>0:
        listar_produtos(lista)
        codigo_produto=int(input("Digite o código do produto: "))
        codigo_produto=codigo_produto-1
        nome_produto=input("Digite o nome do produto: ").upper()
        if codigo_produto<=len(lista):
            if nome_produto==lista[codigo_produto][0]:
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Digite 1 para alterar o  nome")
                print("Digite 2 para alterar o preço")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                resposta=input("Sua resposta: ")
                if resposta=="1":
                    novo_nome=input("Novo nome: ").upper()
                    resposta=input("Digite 1 para confirmar o novo nome: ")
                    if resposta=="1":
                        lista[codigo_produto][0]=novo_nome.upper()
                        print("NOME EDITADO COM SUCESSO!")
                    else:
                        print("OPERAÇÃO CANCELADA!")
                elif resposta=="2":
                    novo_preco=float(input("Digite o novo preço: "))
                    while True:
                        if novo_preco<=0:
                            print("Digite um preço válido!")
                            novo_preco=float(input("Preço: "))
                        else:
                            break
                    resposta=input("Digite 1 para confirmar o novo preço: ")
                    if resposta=="1":
                        lista[codigo_produto][1]=novo_preco
                        print("PREÇO EDITADO COM SUCESSO!")
                    else:
                        print("OPERAÇÃO CANCELADA!")
            else:
                print("PRODUTO INVÁLIDO!")
        else:
            print("PRODUTO INVÁLIDO!")
    else:print("NENHUM PRODUTO ENCONTRADO!")
    input("APERTE ENTER PARA CONTINUAR...")
    

def deletar_produto(lista):
    if len(lista)>0:
        listar_produtos(lista)
        num_produto=int(input(("\nDigite o número do produto para ser deletado: ")))
        if num_produto<=len(lista) and num_produto>=1:
            print(f"Tem certeza que deseja excluir o produto: \nNome:{lista[num_produto-1][0]} \nPreço: {lista[num_produto-1][1]}")
            print("Digite 1 para SIM\n-=-=-=-=-=-=-=-=-=-=-=")
            resposta=input("Sua resposta: ")
            if resposta=="1":
                lista.pop(num_produto-1)
                print("PRODUTO DELETADO COM SUCESSO!")
            else:
                print("O PRODUTO NÃO FOI DELETADO, OPERAÇÃO CANCELADA!")
        else:
            print("NÚMERO INVÁLIDO, OPERAÇÃO CANCELADA!")
    else:
        print("NÃO EXISTE PRODUTOS!")
    input("APERTE ENTER PARA CONTINUAR...")

def sortear_brinde(lista):
    print("Digite 1 para sortear um brinde")
    print("Digite 2 para cancelar")
    resposta=input("Sua resposta: ")
    while True:
        if resposta=="1" or resposta=="2":
            break
        else:
            print("Digite uma resposta válida!")
            resposta=input("Sua resposta: ")
    if resposta=="1":
        numero_sorteado=randint(0,len(brindes)-1)
        brinde_sorteado=brindes[numero_sorteado]
        return brinde_sorteado
    else:
        return "Sem brinde"

def vender(lista_de_vendas,lista_de_clientes,lista_de_produtos):
    valido=False
    contador=1

    for produto in lista_produtos:
        print(f"-=-=-=-=-= PRODUTO {contador}-=-=-=-=-=")
        print("Nome: ",produto[0])
        print("Preço: ",produto[1])
        print(f"Desconto máximo: {produto[2]}%")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        contador+=1
    if len(lista_de_produtos)>=1 and len(lista_de_clientes)>=1:
        produto_escolhido=int(input("Número do produto: "))
        while True:
            if produto_escolhido>=1 and produto_escolhido<contador or produto_escolhido==-1:
                break
            else:
                print("NÚMERO INVÁLIDO!")
                print("DIGITE -1 PARA CANCELAR A OPERAÇÃO!")
                produto_escolhido=int(input("Número do produto: "))
        if produto_escolhido!=-1:
            nome_cliente=input("Digite o nome do cliente: ").upper()
            cpf_cliente=input("Cpf: ")
            desconto=int(input("Desconto(%): "))
            for cadastro in lista_cadastros:
                if cadastro[0]==nome_cliente and cpf_cliente==cadastro[1]:
                    if desconto<=lista_produtos[produto_escolhido-1][2]:
                        valido=True
            if valido==False:
                print("DADOS INVÁLIDOS!")
                print("VENDA NÃO REALIZADA!")
            else:
                #o codigo abaixo adiciona uma lista dentro da biblioteca chamada vendas, a lista adicionada vai ter o nome do cliente, cpf, nome do produto, preço, brinde e data
                # já com o desconto caso tenha. 
                brinde=sortear_brinde(brindes)
                data=datetime.now()
                lista_de_vendas["vendas"].append({"Nome":nome_cliente,"Cpf":cpf_cliente,"Produto":lista_produtos[produto_escolhido-1][0],"Valor pago": lista_produtos[produto_escolhido-1][1]*((100-desconto)/100),"Brinde":brinde,
                                         "Data":data.strftime("%Y/%m/%d")})
                lista_produtos.pop(produto_escolhido-1)
                print("VENDA REALIZADA COM SUCESSO!\n")
    elif len(lista_de_produtos)>=1 and len(lista_de_clientes)==0:
        print("NENHUM CLIENTE FOI CADASTRADO!")
    elif len(lista_de_produtos)==0 and len(lista_de_clientes)>=1:
        print("NENHUM PRODUTO FOI CADASTRADO!")
    else:
        print("NÃO EXISTE PRODUTOS E CLIENTES!")
    input("APERTE ENTER PARA CONTINUAR...")

def listar_vendas(lista):
    contador=0
    if len(lista["vendas"])>=1:
        for venda in lista["vendas"]:
            print(f"-=-=-=-=-= {contador+1}º VENDA -=-=-=-=-=")
            print("Comprador: ",venda["Nome"])
            print("Cpf: ",venda["Cpf"])
            print("Produto: ",venda["Produto"])
            print("Preço junto com o desconto: R$",venda["Valor pago"])
            print("Brinde: ",venda["Brinde"])
            print("Data: ",venda["Data"])

            print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            contador+=1
    else:
        print("SEM VENDAS REALIZADAS!")
    input("APERTE ENTER PARA CONTINUAR...")




def menu():
    while True:
        print("------- MARCENARIA AFETO -------")
        print("-=-=-=-=ÁREA DO CLIENTE-=-=-=-=\n")
        print("1 - Cadastrar Cliente")
        print("2 - Ver Cadastros")
        print("3 - Alterar Cadastro")
        print("4 - Deletar Cadastro\n")
        print("=-=-=-=ÁREA DOS PRODUTOS-=-=-=-\n")
        print("5 - Cadastrar Produtos")
        print("6 - Ver Produtos")
        print("7 - Alterar Produtos")
        print("8 - Deletar Produto")
        print("\n-=-=-=-=-=-=VENDAS-=-=-=-=-=-=\n")
        print("9 - Vender")
        print("10 - Ver Vendas")
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("0 - Sair")
        opcao=input("Sua resposta: ")
        if opcao =="1":
            cadastrar(lista_cadastros)
        elif opcao=="2":
            listar_cadastros(lista_cadastros)
        elif opcao=="3":
            alterar_cadastros(lista_cadastros)
        elif opcao=="4":
            deletar_cadastro(lista_cadastros)
        elif opcao=="5":
            cadastrar_produtos(lista_produtos)
        elif opcao=="6":
            listar_produtos(lista_produtos)
        elif opcao=="7":
            alterar_produtos(lista_produtos)
        elif opcao=="8":
            deletar_produto(lista_produtos)
        elif opcao=="9":
            vender(vendas,lista_cadastros,lista_produtos)
        elif opcao=="10":
            listar_vendas(vendas)
        elif opcao=="0":
            break
        else:
            print("Número inválido!")
            input("APERTE ENTER PARA CONTINUAR...")
menu()
>>>>>>> 90f19fa (Atualiza arquivo sa1.py)
