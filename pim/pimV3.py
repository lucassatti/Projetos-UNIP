import getpass ##Nao torna a senha visivel na hora de digitar
import hashlib ##Transforma a senha em hexadecimal
import json ## Salva os arquivos em Json, pode carregar ou salvar
import os ## agiliza com os comandos do Windows no terminal
import uuid ##Gera os id de usuarios no momento da criação.
import time ##Serve para calcular o tempo que o sistema ficou aberto 
#import matplotlib
import platform  #Serve para identificar e localizar diretorios no Windows/MacOS/Linux



def gerar_hash(senha): # Função pra gerar o hash da senha em hexadecimal
    return hashlib.sha256(senha.encode()).hexdigest()

caminho_arquivo = r"C:\Users\lucas.ramos\Downloads\Projetos-UNIP-main\Projetos-UNIP-main\pim\usuarios.json"

def salvar_usuarios(lista_de_usuarios):# Função para salvar os dados dos usuários no arquivo JSON
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(lista_de_usuarios, arquivo, indent=4)

def carregar_usuarios(): # Função para carregar os dados dos usuários já salvos no arquivo
    if os.path.exists(caminho_arquivo):
        if os.path.getsize(caminho_arquivo) > 0:
            with open(caminho_arquivo, "r") as arquivo:
                return json.load(arquivo)  
            return {}  
caminho_pdfpp = r"C:\Users\lucas.ramos\Downloads\Projetos-UNIP-main\Projetos-UNIP-main\pim\PPconteudo.pdf" 
def abrir_pdf(caminho_pdf): #Função para abrir o PDF do curso de Programação Python
    if platform.system() == "Windows":
        os.startfile(caminho_pdf)
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open '{caminho_pdf}'")
    else:  # Linux
        os.system(f"xdg-open '{caminho_pdf}'")

caminho_pdfsi = r"C:\Users\lucas.ramos\Downloads\Projetos-UNIP-main\Projetos-UNIP-main\pim\SIconteudo.pdf" 
def abrir_pdf(caminho_pdf): #Função para abrir o PDF do curso de SI 
    if platform.system() == "Windows":
        os.startfile(caminho_pdf)
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open '{caminho_pdf}'")
    else:  # Linux
        os.system(f"xdg-open '{caminho_pdf}'")

caminho_pdfplc = r"C:\Users\lucas.ramos\Downloads\Projetos-UNIP-main\Projetos-UNIP-main\pim\PLCconteudo.pdf" 
def abrir_pdf(caminho_pdf): #Função para abrir o PDF do curso de PLC 
    if platform.system() == "Windows":
        os.startfile(caminho_pdf)
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open '{caminho_pdf}'")
    else:  # Linux
        os.system(f"xdg-open '{caminho_pdf}'")
#--------------------------------------------------------------------------------------------------------------------------------------
def primeiro_acesso(): #quando o usuário quiser fazer o primeiro acesso(Não possui login)
    print("----PRIMEIRO ACESSO----")
    arquivojsondef = carregar_usuarios() #esta variavel criada foi feita para validar os usuários cadastrados
    nome_usuario = (input("Informe seu nome de usuário: (nome.sobrenome) "))
    senha = getpass.getpass ("Informe sua senha de acesso: ")
    senha_confirm = getpass.getpass("Confirme sua senha: ")
    print ("\n---- Perguntas de Segurança ----\n")
    pergunta1 = (input("Informe o nome do seu PET: "))
    pergunta2 = (input("Informe os 4 ultimos digitos do seu CPF: "))
    pergunta3 = (input("Informe o nome da escola em que você estudou: "))
    if nome_usuario not in arquivojsondef:
        if senha == senha_confirm:
            arquivojsondef[nome_usuario] = { #nessa parte, foi feita a estrutura de como ficará o arquivo de usuários em json.
            "id": str(uuid.uuid4()),#Puxa o import uuid lá de cima e gera um id hexadecimal aleatório
            "usuario" :(nome_usuario),
            "senha": gerar_hash(senha),
            "Pergunta_1": gerar_hash(pergunta1),
            "Pergunta_2": gerar_hash(pergunta2),
            "Pergunta_3": gerar_hash(pergunta3),
            }
            salvar_usuarios(arquivojsondef) #puxei a função para salvar os dados que foram criados logo acima.
            print("Usuário criado com sucesso!")
        else: 
            print("As senhas não coincidem!")
    else: 
        print(f"O login {nome_usuario} já está em uso!")

#--------------------------------------------------------------------------------------------------------------------------------------

def esqueci_a_senha(): #Quando o usuário esquecer a senha na tela inicial
    print("----RECUPERAÇÃO DE SENHA----")
    arquivojsondef = carregar_usuarios()
    nome_usuario = (input("Informe o nome do seu usuário: "))

    dados_usuario = arquivojsondef[nome_usuario]
    
    if nome_usuario in arquivojsondef:
        resposta1 = gerar_hash(input("Informe o nome do seu PET: "))
        resposta2 = gerar_hash(input("Informe os 4 ultimos digitos do seu CPF: "))
        resposta3 = gerar_hash(input("Informe o nome da escola em que você estudou: "))
        #if resposta1 == arquivojsondef[dados_usuario]["Pergunta_1"] and resposta2 == [dados_usuario]["Pergunta_2"] and resposta3 == [dados_usuario]["Pergunta_3"]: fiz errado, precisei criar uma variavel nova chamando o usuario que pede pra continuar
        if resposta1 == dados_usuario["Pergunta_1"] and resposta2 == dados_usuario["Pergunta_2"] and resposta3 == dados_usuario["Pergunta_3"]:
            nova_senha = getpass.getpass("Crie a nova senha de acesso: ")
            nova_senha_confirm = getpass.getpass("Repita a nova senha de acesso: ")
            if nova_senha == nova_senha_confirm:
                dados_usuario["senha"] = gerar_hash(nova_senha)  #atualiza diretamente a senha
                salvar_usuarios(arquivojsondef)  # salva a alteração no arquivo
                print("Senha alterada com sucesso! Retornando a página principal...")
               # dados_usuario[nome_usuario] = {
               # "senha": gerar_hash(nova_senha) 
               # }  Isso aqui não precisava
            else:
                print("As senhas não coincidem.")
        else:
            print("Informações de recuperação incorretas! \n Retornando a página inicial. ")

#--------------------------------------------------------------------------------------------------------------------------------------

def selecao_cursos(nome): # Após o user fazer login no case 2 da def de login, ele será direcionado para esta etapa.

    arquivojsondef = carregar_usuarios()
    dados_usuario = arquivojsondef.get(nome)

    while True:
        print("|HOME| TEC-PARA-TODOS \n(1) - Pensamento Lógico Computacional \n(2) - Segurança Digital \n(3) - Programação em Python \n(4) - Informações do Aluno \n(5) - Logout")
        select_home = int(input("Informe o Curso que deseja acessar: "))
        match select_home:
            case 1:
                curso_plc(nome)
            case 2:
                curso_sg(nome)
            case 3:
                curso_pp(nome)
            case 4:
                dados_usuario = arquivojsondef.get(nome)
                nota_plc = dados_usuario.get("nota_pensamentolc", 0)
                nota_sg = dados_usuario.get("nota_sg", 0)
                nota_py = dados_usuario.get("nota_python", 0)
                media = (nota_plc + nota_sg + nota_py) / 3
                melhor_curso = ""
                maior_nota = max(nota_plc, nota_sg, nota_py)

                if maior_nota == nota_plc and maior_nota != 0:
                    melhor_curso = "Pensamento Lógico Computacional"
                elif maior_nota == nota_sg and maior_nota != 0:
                    melhor_curso = "Segurança Digital"
                elif maior_nota == nota_py and maior_nota != 0:
                    melhor_curso = "Programação em Python"
                elif maior_nota == 0:
                    maior_nota == 'Sem provas realizadas'
                print("\n| INFORMAÇÕES DO ALUNO |\n")
                print(f"{'Usuário:':<15} {nome}")
                print(f"{'ID:':<15} {dados_usuario.get('id', 'Sem ID')}")

                print(f"{'Curso':<35} {'Nota':<5}")
                print("-" * 42)
                print(f"{'Pensamento Lógico Computacional':<35} {nota_plc:<5}")
                print(f"{'Segurança Digital':<35} {nota_sg:<5}")
                print(f"{'Programação em Python':<35} {nota_py:<5}")
                print("-" * 42)
                print(f"{'MÉDIA FINAL':<35} {media:.2f}")
                print(f"Curso com melhor desempenho: {melhor_curso}\n")
            case 5:
                print("Logout efetuado com sucesso.")
                tela_inicial()

def curso_plc(nome_usuario):
    print("----BEM VINDO AO CURSO DE PENSAMENTO LÓGICO COMPUTACIONAL!----")
    while True:
        opcao_curso = input("Selecione a opção desejada:\n (1) - Acessar o conteúdo do curso \n (2) - Fazer a prova \n (3) - Voltar para a tela inicial \n :")
        match opcao_curso:
            case "1":
                abrir_pdf(caminho_pdfplc)
            case "2":
                print("---- PROVA DE PENSAMENTO LÓGICO COMPUTACIONAL ----")
                nota = 0
                print(
                    "1. O que é pensamento lógico computacional?\n"
                    "1) Um método exclusivo de programar computadores\n"
                    "2) A arte de criar computadores lógicos\n"
                    "3) A habilidade de organizar ideias e resolver problemas com apoio da lógica e da computação\n"
                    "4) Um tipo de raciocínio matemático usado apenas em engenharia"
                )
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 1

                print(
                    "\n2. Qual das alternativas a seguir representa um exemplo de algoritmo?\n"
                    "1) Uma planilha de gastos\n"
                    "2) Uma receita de bolo\n"
                    "3) Um gráfico de barras\n"
                    "4) Um cabo USB"
                )
                resposta = input("Sua resposta: ")
                match resposta:
                    case "2":
                        nota += 1

                print(
                    "\n3. Em lógica, o que significa a proposição “se A então B”?\n"
                    "1) Que A e B são sempre verdadeiros\n"
                    "2) Que B depende da veracidade de A\n"
                    "3) Que A só é verdadeiro se B for falso\n"
                    "4) Que A não influencia B"
                )
                resposta = input("Sua resposta: ")
                match resposta:
                    case "2":
                        nota += 1

                print(
                    "\n4. Qual é o operador lógico correspondente ao “E” lógico?\n"
                    "1) OR\n"
                    "2) NOT\n"
                    "3) AND\n"
                    "4) XOR"
                )
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 1

                print(
                    "\n5. Em programação, qual estrutura usamos para tomar decisões?\n"
                    "1) Variável\n"
                    "2) Loop\n"
                    "3) Condicional (if/else)\n"
                    "4) Função"
                )
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 1

                print(
                    "\n6. O que é um fluxograma?\n"
                    "1) Um código de programação\n"
                    "2) Um gráfico de desempenho\n"
                    "3) Um mapa de ideias para sites\n"
                    "4) Uma representação visual de um algoritmo"
                )
                resposta = input("Sua resposta: ")
                match resposta:
                    case "4":
                        nota += 1

                print(
                    "\n7. Qual dessas alternativas é um tipo de dado?\n"
                    "1) Verdadeiro/Falso\n"
                    "2) Loop\n"
                    "3) Fluxograma\n"
                    "4) Condicional"
                )
                resposta = input("Sua resposta: ")
                match resposta:
                    case "1":
                        nota += 1

                print(
                    "\n8. Um laço de repetição é usado quando…\n"
                    "1) Queremos guardar um valor\n"
                    "2) Precisamos repetir uma ação várias vezes\n"
                    "3) Precisamos comparar dois valores\n"
                    "4) Queremos desenhar um gráfico"
                )
                resposta = input("Sua resposta: ")
                match resposta:
                    case "2":
                        nota += 1

                print(
                    "\n9. Qual conceito está relacionado à divisão de um problema em partes menores?\n"
                    "1) Generalização\n"
                    "2) Abstração\n"
                    "3) Decomposição\n"
                    "4) Pseudocódigo"
                )
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 1

                print(
                    "\n10. O que é pseudocódigo?\n"
                    "1) Um código que só funciona em Python\n"
                    "2) Um desenho de fluxograma\n"
                    "3) Um tipo de dado avançado\n"
                    "4) Uma forma de descrever algoritmos com linguagem simples"
                )
                resposta = input("Sua resposta: ")
                match resposta:
                    case "4":
                        nota += 1

                print(f"\nVocê acertou {nota} de 10 perguntas.")

                # Salvar a nota no JSON dos usuários
                usuarios = carregar_usuarios()
                if nome_usuario in usuarios:
                    usuarios[nome_usuario]["nota_plc"] = nota
                    salvar_usuarios(usuarios)
                    input("Pressione Enter para continuar...")
            case "3":
                tela_inicial()
                break
            case _:
                print("Valor inválido!")

def curso_sg(nome_usuario):
    while True:
        print("----BEM VINDO AO CURSO DE SEGURANÇA DIGITAL!----")
        opcao_curso = input("Selecione a opção desejada:\n (1) - Acessar o conteúdo do curso \n (2) - Fazer a prova \n (3) - Voltar para a tela inicial \n :")
        match opcao_curso:
            case "1":
                abrir_pdf(caminho_pdfsi)
            case "2":
                print("---- PROVA DE SEGURANÇA DIGITAL ----")
                nota = 0


                print("\n1. O que é phishing?\n"
                      "1 - Um tipo de firewall.\n"
                      "2 - Uma técnica de criptografia.\n"
                      "3 - Uma tentativa de enganar alguém para obter dados confidenciais.\n"
                      "4 - Um programa antivírus.")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 2

                print("\n2. Qual é a função de uma VPN?\n"
                      "1 - Aumentar a velocidade da internet.\n"
                      "2 - Proteger a identidade e dados do usuário ao navegar.\n"
                      "3 - Atualizar automaticamente softwares.\n"
                      "4 - Realizar backup de arquivos.")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "2":
                        nota += 2

                print("\n3. O que caracteriza uma senha forte?\n"
                      "1 - Apenas números.\n"
                      "2 - Apenas letras minúsculas.\n"
                      "3 - Uma combinação de letras, números e caracteres especiais.\n"
                      "4 - Nome do usuário e data de nascimento.")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 2

                print("\n4. Qual dessas atitudes é mais segura ao usar redes Wi-Fi públicas?\n"
                      "1 - Acessar contas bancárias com cuidado.\n"
                      "2 - Usar VPN para criptografar o tráfego.\n"
                      "3 - Desligar o antivírus temporariamente.\n"
                      "4 - Compartilhar arquivos livremente.")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "2":
                        nota += 2

                print("\n5. O que é autenticação em dois fatores?\n"
                      "1 - Acesso com login e senha apenas.\n"
                      "2 - Um método de backup automático.\n"
                      "3 - Verificação em duas etapas para aumentar a segurança.\n"
                      "4 - Um tipo de antivírus com duas camadas.")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 2

                print(f"\nVocê acertou {nota} de 5 perguntas.")

                # Salvar a nota no JSON dos usuários
                usuarios = carregar_usuarios()
                if nome_usuario in usuarios:
                    usuarios[nome_usuario]["nota_sg"] = nota
                    salvar_usuarios(usuarios)
                    input("Pressione Enter para continuar...")
            case "3":
                tela_inicial()
                break
            case _:
                print("Valor inválido!")
    
def curso_pp(nome_usuario):
    print("----BEM VINDO AO CURSO DE PROGRAMAÇÃO EM PYTHON!----")
    while True:
        opcao_curso = input("Selecione a opção desejada:\n (1) - Acessar o conteúdo do curso \n (2) - Fazer a prova \n (3) - Voltar para a tela inicial \n :")
        match opcao_curso:
            case "1":
                abrir_pdf(caminho_pdfpp)
            case "2":
                print("---- PROVA DE PROGRAMAÇÃO EM PYTHON! ----")
                nota = 0

                print("\n1. O que é uma variável em Python?\n"
                      "1) Um tipo de dado fixo\n"
                      "2) Um comando para imprimir valores\n"
                      "3) Um espaço para armazenar valores\n"
                      "4) Uma função matemática")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 1

                print("\n2. Qual comando usamos para mostrar algo na tela?\n"
                      "1) input()\n"
                      "2) echo()\n"
                      "3) output()\n"
                      "4) print()")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "4":
                        nota += 1

                print("\n3. Qual comando usamos para receber um dado do usuário?\n"
                      "1) print()\n"
                      "2) input()\n"
                      "3) get()\n"
                      "4) scan()")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "2":
                        nota += 1

                print("\n4. Qual das opções representa um número com ponto decimal?\n"
                      "1) int\n"
                      "2) str\n"
                      "3) float\n"
                      "4) bool")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 1

                print("\n5. O que o operador ** faz em Python?\n"
                      "1) Soma dois números\n"
                      "2) Mostra o resto da divisão\n"
                      "3) Faz a potência de um número\n"
                      "4) Divide dois números")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 1

                print("\n6. O que este código faz?\n\n"
                      "if idade >= 18:\n"
                      "    print(\"Maior de idade\")\n"
                      "else:\n"
                      "    print(\"Menor de idade\")\n\n"
                      "1) Sempre mostra \"Maior de idade\"\n"
                      "2) Verifica se a idade é maior ou igual a 18\n"
                      "3) Compara dois textos\n"
                      "4) Soma duas idades")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "2":
                        nota += 1

                print("\n7. Qual a diferença entre os laços for e while?\n"
                      "1) for repete infinitamente, while não\n"
                      "2) while percorre listas, for não\n"
                      "3) for repete um número conhecido de vezes, while depende de uma condição\n"
                      "4) Não há diferença")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 1

                print("\n8. Como criar uma lista em Python?\n"
                      "1) lista = list()\n"
                      "2) lista = {1, 2, 3}\n"
                      "3) lista = [1, 2, 3]\n"
                      "4) lista = <1, 2, 3>")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "3":
                        nota += 1

                print("\n9. O que é uma função em Python?\n"
                      "1) Um tipo de dado especial\n"
                      "2) Um código que roda apenas uma vez\n"
                      "3) Um comando para criar variáveis\n"
                      "4) Um bloco de código reutilizável")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "4":
                        nota += 1

                print("\n10. O que este código faz?\n\n"
                      "for i in range(1, 4):\n"
                      "    print(\"Olá\", i)\n\n"
                      "1) Imprime \"Olá\" uma vez\n"
                      "2) Repete \"Olá\" 3 vezes com os números 1, 2 e 3\n"
                      "3) Mostra um erro\n"
                      "4) Cria uma variável chamada Olá")
                resposta = input("Sua resposta: ")
                match resposta:
                    case "2":
                        nota += 1

                print(f"\nVocê acertou {nota} de 10 perguntas.")

                # Salvar a nota no JSON dos usuários
                usuarios = carregar_usuarios()
                if nome_usuario in usuarios:
                    usuarios[nome_usuario]["nota_python"] = nota
                    salvar_usuarios(usuarios)
            case "3":
                tela_inicial()
                break
            case _:
                print("Valor inválido!")

#--------------------------------------------------------------------------------------------------------------------------------------  
def login(): #Quando o user já tiver acesso e quiser logar
    print("----LOGIN----")
    arquivojsondef = carregar_usuarios()
    nome_usuario = (input("Informe seu usuário: (nome.sobrenome) "))
    if nome_usuario in arquivojsondef:
        senha_acesso = getpass.getpass("Informe sua senha de acesso: ")
        senha_acesso = gerar_hash(senha_acesso)
        if senha_acesso == arquivojsondef[nome_usuario]["senha"]:
            print(f"\nBem-vindo, {nome_usuario}!\nRedirecionando a página principal...")
            
            selecao_cursos(nome_usuario)
            return nome_usuario
        else:
            print("Senha inválida.")
            return None
    else:
        print("Usuário não encontrado!")
        return None
#--------------------------------------------------------------------------------------------------------------------------------------

def tela_inicial(): #Função principal do sistema, servirá para puxar as demais DEFS, precisa ficar por ultimo para reconhecer as defs que estão nos cases
    while True:
        print("BEM-VINDO A PLATAFORMA DE ENSINO \n TEC-PARA-TODOS!\n--------------------------\n (1) - Primeiro acesso \n (2) - Login \n (3) - Esqueci a senha \n (4) - Sair")
        try:
            opcoes_login = int(input("Digite uma opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue
        match opcoes_login:
            case 1:
                primeiro_acesso()
            case 2:
                login()
            case 3:
                esqueci_a_senha()
            case 4:
                break

if __name__ == "__main__":
    tela_inicial()