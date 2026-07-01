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
def cadastrar_produtos(lista_de_produtos):
    valido=True
    print("-=-=-=Cadastrar Produtos=-=-=-")
    nome=input("Nome: ").upper()
    preco=float(input("Preço: "))
    while True:
        if preco<=0:
            print("Digite um preço válido!")
            preco=float(input("Preço: "))
        else:
            break
    desconto_maximo=float(input("Máximo desconto: "))
    while True:
        if desconto_maximo>100 or desconto_maximo<0:
            print("Digite um valor válido!")
            desconto_maximo=int(input("Máximo desconto: "))
        else:
            break
    for produto in lista_produtos:
        if produto[0]==nome and produto[1]==preco:
            valido=False
            print("O PRODUTO JA ESTÁ CADASTRADO!")
            print("OPERAÇÃO CANCELADA!")
    if valido==True:
        lista_de_produtos.append([nome,preco,desconto_maximo])
        print("Produto cadastrado com sucesso!")
        
    else:
        print("PRODUTO NÃO CADASTRADO!")
    input("APERTE ENTER PARA CONTINUAR...")


def listar_produtos(lista):
    contador=1
    if len(lista)>=1:
        for cadastro in lista:
            print(f"\n=-=-=-Produto {contador}=-=-=-")
            print("Nome: ",cadastro[0])
            print("Preço: ",cadastro[1])
            print(f"=-=-=-=-=-=-=--=-=-=")
            contador+=1
    else:
        print("SEM PRODUTOS CADASTRADOS!")
    input("APERTE ENTER PARA CONTINUAR...")

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