#Importacoes
import getpass ##Nao torna a senha visivel na hora de digitar
import hashlib ##Transforma a senha em hexadecimal
import json ## Salva os arquivos em Json, pode carregar ou salvar
import os

# Função pra gerar o hash da senha
def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()
#carregar os usuarios salvos em json
caminho_json = r"C:\Users\ramos\Desktop\PythonProjects\Aula 3\pim\usuarios.json"
#def para salvar em json os usuarios criados 
def salvar_usuarios(usuarios):
    with open(caminho_json, "w") as dados_usuarios:
        json.dump(usuarios, dados_usuarios, indent=4)
def carregar_usuarios():
    if os.path.exists(caminho_json):
        if os.path.getsize(caminho_json) > 0:  # Verifica se o arquivo NÃO está vazio
            with open(caminho_json, "r") as dados_usuarios:
                return json.load(dados_usuarios)
        else:
            return {}  
    return {}  

def tela_login(): #funcao inicial para acesso ao sistema
    while True:
        usuarios = carregar_usuarios()  # Carrega os usuários do arquivo JSON
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
                nome_usuario = input("Informe seu nome de usuário: (nome.sobrenome) ").strip()
                senha = getpass.getpass("Informe sua senha de acesso: ")
                if nome_usuario in usuarios: # Verifica se o usuário existe
                    senha_hash = gerar_hash(senha)
                    if senha_hash == usuarios[nome_usuario]["senha"]:
                        print(f"\nBem-vindo, {nome_usuario}!")
                        print("Redirecionando até a página principal...\n")
                        
                        # Aqui você pode chamar a função da página principal se quiser
                        # Exemplo: pagina_principal(nome_usuario)
                    else:
                        print("Senha incorreta!")
                else:
                    print("Usuário não encontrado! ")
tela_login()