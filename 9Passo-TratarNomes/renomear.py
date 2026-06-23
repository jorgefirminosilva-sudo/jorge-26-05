OBS1: puxe todas as pastas do passo 8 para este passo 9
OBS2: você vai atualizar o nome das imagens para seguir um padrão, mas você vai fazer isso pasta por pasta
OBS3: atualize a linha 15 com o nome da pasta das questões que você vai arrumar
OBS4: ENTENDA muito bem o for da linha 25!!!!!!!!!!!
OBS4: ENTENDA muito bem o for da linha 24!!!!!!!!!!!
"""
import os

def renomear_questoes_simples():
    pasta = "80-90"
    pasta = "80-90" # ATUALIZE O NOME DA PASTA QUE VOCÊ VAI ARRUMAR AQUI

    if not os.path.exists(pasta):
        print(f"Pasta {pasta} não encontrada!")
@@ -21,12 +21,17 @@ def renomear_questoes_simples():
    # Mapeamento direto dos nomes antigos para os novos
    mapeamento = {}

    # Exemplo: parte_00x a parte_00y -> questao-x a questao-y
    for i in range(81, 91+1):    # atualize seu for com o número da primeira imagem "parte_AlgumaCoisa.png" até o número da última imagem "parte_AlgumaCoisa.png" mais 1 da pasta
    # Aqui você vai renomear seguindo o padrão: parte_00x.png a parte_00y.png -> questao-a.png a questao-b.png
    # atualize seu for com o número da primeira imagem "parte_AlgumaCoisa.png" até o número da última imagem "parte_AlgumaCoisa.png" mais 1 da pasta
    for i in range(81, 91+1):
        # f-string do nome antigo
        antigo = f"parte_{i:03d}.png"
        #novo = f"questao-{i+78}-espanhol.png"  # faça uma conta: se a primeira pagina for 

        # f-string dos novos nomes. Faça a conta para transformar o número do antigo no número do novo
        # faça uma conta: se o i do teu for está em 2, e precisa virar questão 35, como você transforma 2 em 35? faça a conta e coloque dentro da concatenação
        novo = f"questao-{i+78}-espanhol.png"  # faça uma conta: se a primeira pagina for 
        #novo = f"questao-{i+78}-ingles.png"
        novo = f"questao-{i-1}.png" # faça uma conta: se o i do teu for está em 2, e precisa virar questão 35, como você transforma 2 em 35? faça a conta e coloque dentro da concatenação
        #novo = f"questao-{i-1}.png" 

        mapeamento[antigo] = novo
