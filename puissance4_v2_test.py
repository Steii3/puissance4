from os import system

#definition d'une fonction qui enleve tout le texte du terminal
def clear():
    '''clear console'''
    return system('cls')

w, h = 7, 6
Matrix = [[0 for x in range(w)] for y in range(h)] 
Matrix[5][0] = 'O'
pion = 'X'
pions = ['X','O']
gagné = False

while True:

    colonne_choisit = int(input("quel colonne ? \nentrer un nombre de 1 à 7:   "))-1
    clear()

    for i in range(0,6):

        #print(" le i est " , i, 'et le matrix[i][col est ]',Matrix[i][colonne_choisit])
        if Matrix[i][colonne_choisit] == 0 and i == 5:
            Matrix[5][colonne_choisit] = pion
            break
        test = Matrix[0][colonne_choisit] 
        if test == 'X': 
            print('you can\'t overflow the board, that\'s rude')
            break
        
        if Matrix[i][colonne_choisit] != 0:
            Matrix[i-1][colonne_choisit] = pion
            break
        
   
                    
    for i in pions:
    #recherche de gagné sur les colonnes
        for x in range(3):
            for y in range(6):
                if (Matrix[x][y]  and Matrix[x+1][y] and Matrix[x+2][y] and Matrix[x+3][y]) == i:
                    print("{} = {} = {} = {}".format(Matrix[x][y],Matrix[x+1][y],Matrix[x+2][y],Matrix[x+3][y]))
                    gagné = True

            #recherche de gagné sur les lignes
        for x in range(6):
            for y in range(3):
                if (Matrix[x][y]  and Matrix[x][y+1] and Matrix[x][y+2] and Matrix[x][y+3]) == i:
                    print("{} = {} = {} = {}".format(Matrix[x][y],Matrix[x][y+1],Matrix[x][y+2],Matrix[x][y+3]))
                    gagné = True
                
            
    if gagné == True:
        if i == i[0]:
            print('le joueur 1 a gagné')
            exit()
        if i == i[1]:
            print('le joueur 2 a gagné')
            exit()
         
    for i in range(6):
        print(' '.join(map(str, Matrix[i])),) #convertie chaque caractere de matrix en str et le regroupe en une ligne séparé par 2espaces 
    
