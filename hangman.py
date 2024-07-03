import random

def championSelect():

    champions_txt = 'champions.txt'
    dict_champs = {}

    with open(champions_txt, 'r', encoding='utf-8') as file:
        for line in file:
            lineSize = line.strip().split()
            if len(lineSize) == 3:
                champ_name = lineSize[0]
                champ_class = lineSize[2]
                dict_champs[champ_name] = champ_class

    campeao_aleatorio = random.choice(list(dict_champs.items()))
    nome_aleatorio, classe_aleatoria = campeao_aleatorio
    return campeao_aleatorio

campeao_escolhido = list(championSelect())
print(campeao_escolhido)
