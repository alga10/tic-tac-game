
#VARIABLES

lista = []
initial_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
winner = False

# FUNCION QUE DETERMINA EL SIGNO CON EL QUE JUGARA CADA USUARIO.

def user_choice(): 
    
    # Tomando valores por pantalla
    
    first_player = input("Quieres ser X or O?: ")
    first_player = first_player.upper()
   

    # Condiciones a revisar: los valores ingresados por el usuario deben ser X o O, de lo contrario, se solicitan 
    # los datos nuevamente. 
    
    while  first_player != "X" and first_player != "O":
        first_player = input("Disculpa, la opcion elegida esta fuera de rango, quieres ser X or O?: ")
        first_player = first_player.upper()
    
    # Dependiendo de la seleccion del jugador 1, se asigna el valor al jugador 2.
    
    if first_player == "X":
        second_player = "O"
    else:
        second_player = "X"
    
    return first_player, second_player

first_player, second_player = user_choice()

#FUNCION QUE IMPRIME EL TABLERO

def print_board(board):
    print(board[1] + "|" + board[2] + "|" +  board[3])
    print(board[4] + "|" + board[5] + "|" +  board[6])
    print(board[7] + "|" + board[8] + "|" +  board[9])
    
#FUNCION DE GANADOR1

def win_one(initial_board):
    
    global winner
    
    if initial_board[1] == initial_board[2] == initial_board[3] == first_player:
        print(f"El ganador es {first_player}")
        winner = True 
    elif initial_board[4] == initial_board[5] == initial_board[6] == first_player:
        print(f"El ganador es {first_player}")
        winner = True
    elif initial_board[7] == initial_board[8] == initial_board[9] == first_player:
        print(f"El ganador es {first_player}")
        winner = True
    elif initial_board[1] == initial_board[4] == initial_board[7] == first_player:
        print(f"El ganador es {first_player}")
        winner = True
    elif initial_board[2] == initial_board[5] == initial_board[8] == first_player:
        print(f"El ganador es {first_player}")
        winner = True
    elif initial_board[3] == initial_board[6] == initial_board[9] == first_player:
        print(f"El ganador es {first_player}")
        winner = True
    elif initial_board[7] == initial_board[5] == initial_board[3] == first_player:
        print(f"El ganador es {first_player}")
        winner = True
    elif initial_board[1] == initial_board[5] == initial_board[9] == first_player:
        print(f"El ganador es {first_player}")
        winner = True
    
    return winner

#FUNCION DE GANADOR2

def win_two(initial_board):
    
    global winner
    
    if initial_board[1] == initial_board[2] == initial_board[3] == second_player:
        print(f"El ganador es {second_player}")
        winner = True 
    elif initial_board[4] == initial_board[5] == initial_board[6] == second_player:
        print(f"El ganador es {second_player}")
        winner = True
    elif initial_board[7] == initial_board[8] == initial_board[9] == second_player:
        print(f"El ganador es {second_player}")
        winner = True
    elif initial_board[1] == initial_board[4] == initial_board[7] == second_player:
        print(f"El ganador es {second_player}")
        winner = True
    elif initial_board[2] == initial_board[5] == initial_board[8] == second_player:
        print(f"El ganador es {second_player}")
        winner = True
    elif initial_board[3] == initial_board[6] == initial_board[9] == second_player:
        print(f"El ganador es {second_player}")
        winner = True
    elif initial_board[7] == initial_board[5] == initial_board[3] == second_player:
        print(f"El ganador es {second_player}")
        winner = True
    elif initial_board[1] == initial_board[5] == initial_board[9] == second_player:
        print(f"El ganador es {second_player}")
        winner = True
    
    return winner

# FUNCION JUGADA

def jugadafinal():
    posicion_one = input("Jugador 1 seleccciona la posicion a jugar (1 - 9): ")
    posicion_one =int(posicion_one)
    
    while posicion_one not in range(1,10):
        print("Disculpa, opción seleccionada fuera de rango")
        posicion_one = input("Seleccciona la posicion a jugar (1 - 9): ")
        posicion_one =int(posicion_one)
    
    while posicion_one in lista:
        print("Esta posición ya esta jugada en el tablero")
        posicion_one = input("Seleccciona la posicion a jugar (1 - 9): ")
        posicion_one =int(posicion_one)
        
    if posicion_one not in lista:
        lista.append(posicion_one)
        initial_board[posicion_one] = first_player
        print_board(initial_board)
        win_one(initial_board)
    
    if winner == False:
        posicion_two = input("Jugador 2 seleccciona la posicion a jugar (1 - 9): ")
        posicion_two =int(posicion_two)
    
        while posicion_two not in range(1,10):
            print("Disculpa, opción seleccionada fuera de rango")
            posicion_two = input("Seleccciona la posicion a jugar (1 - 9): ")
            posicion_two =int(posicion_two)
    
        while posicion_two in lista:
            print("Esta posición ya esta jugada en el tablero")
            posicion_two = input("Seleccciona la posicion a jugar (1 - 9): ")
            posicion_two =int(posicion_two)
        
        if posicion_two not in lista:
            lista.append(posicion_two)
            initial_board[posicion_two] = second_player
            print_board(initial_board)
            win_two(initial_board)
        
            

# CORRER PROGRAMA

while winner != True:
    jugadafinal()
    
    if winner == True:
        repeat = input("Quieres Jugar de nuevo?: Y or N")
        if repeat == "Y":   
            winner = False
            lista = []
            initial_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        
    

