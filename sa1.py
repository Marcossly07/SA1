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