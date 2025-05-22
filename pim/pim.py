#Importacoes
import getpass ##Nao torna a senha visivel na hora de digitar
import hashlib ##Transforma a senha em hexadecimal
import json ## Salva os arquivos em Json, pode carregar ou salvar
import os
import uuid ##Gera os id de usuarios no momento da criação.

# Função pra gerar o hash da senha
def gerar_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()
#carregar os usuarios salvos em json
caminho_json = r"C:\Users\ramos\Desktop\PythonProjects\Aula 3\pim\usuarios.json"
#def para salvar em json os usuarios criados 
def salvar_usuarios(susuariosjson):
    with open(caminho_json, "w") as dados_usuarios:
        json.dump(usuarios, dados_usuarios, indent=4)
def carregar_usuarios(cusuariosjson):
    if os.path.exists(caminho_json):
        if os.path.getsize(caminho_json) > 0:  # Verifica se o arquivo NÃO está vazio
            with open(caminho_json, "r") as dados:
                return json.load(dados)
        else:
            return {}  
    return {}  

def tela_login(): #funcao inicial para acesso ao sistema
    while True:
        print("---BEM-VINDO!--- \n (1) - Primeiro acesso \n (2) - Login \n (3) - Esqueci a senha \n (4) - Sair")
        try:
            opcoes_login = int(input("Digite uma opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue
        match opcoes_login:
            case 1: #Valida se é um novo acesso ou se é um acesso já existente
                nome_usuario = (input("Informe seu nome de usuário: (nome.sobrenome)"))
                senha = getpass.getpass ("Informe sua senha de acesso: ")
                senha_confirm = getpass.getpass("Confirme sua senha: ")
                pergunta1 = (input("Informe o nome do seu PET: "))
                pergunta2 = (input("Informe os 4 ultimos digitos do seu CPF: "))
                pergunta3 = (input("Informe o nome da escola em que você estudou: "))
                if nome_usuario not in usuarios:
                    if senha == senha_confirm:
                        usuarios[nome_usuario] = {
                            "id" : str(uuid.uuid1()), ## chama o uuid e transforma em hexadecimal no JSON
                            "usuario" :(nome_usuario),
                            "senha": gerar_hash(senha),
                            "Pergunta_1": gerar_hash(pergunta1),
                            "Pergunta_2": gerar_hash(pergunta2),
                            "Pergunta_3": gerar_hash(pergunta3),
                        }
                        salvar_usuarios(usuarios)
                        print("Usuário criado com sucesso!")
                    else:
                        print("As senhas não coincidem")
                else:
                    print("Este login já existe na base!")
            case 2:
                nome_usuario = input("Informe seu nome de usuário: (nome.sobrenome) ")
                senha = getpass.getpass("Informe sua senha de acesso: ")
                if nome_usuario in usuarios: # Verifica se o usuário existe
                    senha_hash = gerar_hash(senha)
                    if senha_hash == usuarios[nome_usuario]["senha"]:
                        print(f"\nBem-vindo, {nome_usuario}!")
                        print("Redirecionando até a página principal...\n")
                        home_sistema()
                    else:
                        print("Senha incorreta!")
                else:
                    print("Usuário não encontrado! ")
            case 3:
                with open (r"C:\Users\ramos\Desktop\PythonProjects\Aula 3\pim\usuarios.json", encoding="utf-8") as dados: #serve para 
                    dados = json.load(dados)
                    ##print(dados) serve para puxar os dados do json dentro do Case
                    nome_usuario = (input("Informe o nome do seu usuário: "))
                if  nome_usuario in usuarios:   
                    resposta1 = gerar_hash(input("Informe o nome do seu PET: "))
                    resposta2 = gerar_hash(input("Informe os 4 ultimos digitos do seu CPF: "))
                    resposta3 = gerar_hash(input("Informe o nome da escola em que você estudou: "))
                    usuarios = carregar_usuarios 
                    if  resposta1 == usuarios["Pergunta_1"] and resposta2 == usuarios["Pergunta_2"] and resposta3 == usuarios["Pergunta_3"]:
                        nova_senha = getpass.getpass("Crie a nova senha de acesso: ")
                        nova_senha_confirm = getpass.getpass("Repita a nova senha de acesso: ")
                        if nova_senha == nova_senha_confirm:
                            print ("Senha alterada com sucesso! ")
                            senha[senha] = {
                            "usuario" :(nome_usuario),
                            "senha": gerar_hash(senha),
                            }
                        else:
                            print("As senhas não coincidem")
                    else:
                        print("Informações não coincidem.")
                else:
                    print("Usuáario não localizado!")
            case 4 :
                break
def home_sistema (): #Essa DEF DEFINE QUAL CURSO O USUÁRIO VAI QUERER ACESSAR 
    while True:
        print("---INFORME O CURSO QUE DESEJA ACESSAR--- \n (1) - Infraestrutura Computacional \n (2) - Programação em Python \n (3) - Segurança Digital \n (4) - Sair")
        try:
            opcoes_cursos = int(input("Digite uma opção: ")) # Solicita ao usuário qual curso escolher
        except ValueError:
            print("Digite um número válido.")
            continue
tela_login()