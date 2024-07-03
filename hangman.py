import random
import os
import re

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

def hangmanHeader():
    os.system('cls')
    print('JOGO DA FORCA')
    print('Tema: Campeões de League of Legends\n-----------------------------------\n')


def validate_letter():
    while True:

        print(f'Letras já utilizadas: {repeated_letters}')

        chosen_letter = input('\nEscolha uma letra (caso seja uma palavra, será considerada apenas a primeira letra): ').strip().upper()[:1]

        check_letter = lambda letter: bool(re.match(r'^[a-zA-Z]+$', letter))
        already_use = lambda letter: letter in repeated_letters

        if check_letter(chosen_letter):
            if not already_use(chosen_letter):
                repeated_letters.append(chosen_letter)
                break
            else:
                hangmanHeader()
                print(f"'{chosen_letter}' já foi utilizada, favor escolher outra")
                print(f'Você ainda tem {max_attempts} tentativas\n')
        else:
            hangmanHeader()
            print(f"'{chosen_letter}' não é uma letra válida, favor escolher outra")
            print(f'Você ainda tem {max_attempts} tentativas\n')
    return chosen_letter

def guess_word():
    right_letters = []
    for caractere in selected_champion:
        if caractere.isalpha():
            right_letters.append('_')
        else:
            right_letters.append(caractere)
    return right_letters

define_champion = list(championSelect())
selected_champion = define_champion[0]
tip = define_champion[1]
repeated_letters = []

selected_champion = selected_champion.upper()

max_attempts = 6

while max_attempts > 0:
    hangmanHeader()
    print(f'Você tem {max_attempts} tentativas')
    word = guess_word()
    verify_letter = validate_letter()
    max_attempts -= 1
