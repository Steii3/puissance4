from os import system


#definition d'une fonction qui enleve tout le texte du terminal
def clear():
    '''clear console'''
    return system('cls')

w, h = 7, 6
case_vide = '.'
espacement_cases_v = ' '

Matrix = [[case_vide for x in range(w)] for y in range(h)] 
Matrix[5][0] = 'O'
pion = 'X'


while True:

    colonne_choisit = int(input("quelle colonne ? \nentrer un nombre de 1 à 7:   "))-1
    clear()

    for i in range(0,6):

        #print(" le i est " , i, 'et le matrix[i][col est ]',Matrix[i][colonne_choisit])
        if Matrix[i][colonne_choisit] == case_vide and i == 5:
            Matrix[5][colonne_choisit] = pion
            break
        
        if Matrix[0][colonne_choisit]  == pion: 
            print('you can\'t overflow the board, that\'s rude >:(')
            break
        
        if Matrix[i][colonne_choisit] != case_vide:
            Matrix[i-1][colonne_choisit] = pion
            break


#affiche le tableau        
    for i in range(6):
        print(espacement_cases_v.join(map(str, Matrix[i])),) #convertie chaque caractere de matrix en str et le regroupe en une ligne séparé par 2espaces 
