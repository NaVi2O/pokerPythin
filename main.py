#Nombrar Preflop

jugadores = input("Cuantos jugadores sois en la mesa (contandote a ti) =")
jugadores = int(jugadores)

print("CORAZONES = C // PICAS = P // TREBOLES = T // DIAMANTES = D")

print("Dime las cartas que te han tocado en el Preflop: ")

preFlop1 = input("1º CARTA: ")
preFlop1 = preFlop1.strip().upper()


preFlop2 = input("2ª CARTA: ")
preFlop2 = preFlop2.strip().upper()


def validacionDatosPreflop():
    if(len(preFlop1) < 2 or len(preFlop2) < 2):
        print("Tamaño dado NO VALIDO")
        return False

    if(preFlop1 == preFlop2):
        print("Has dado las mismas cartas")
        return False
    
    if(preFlop1[1] not in ["D","C","P","T"]):
        print("Palo de carta 1 NO VALIDO")
        return False

    if(preFlop2[1] not in ["D","C","P","T"]):
        print("Palo de carta 2 NO VALIDO")
        return False

    valores_validos = ["A","2","3","4","5","6","7","8","9","J","Q","K"]

    if(preFlop1[0] not in valores_validos):
        print("Valor de carta 1 NO VALIDO")
        return False
    
    if(preFlop2[0] not in valores_validos):
        print("Valor de carta 2 NO VALIDO")
        return False

    return True

    
while(not validacionDatosPreflop()):
    preFlop1 = input("1º CARTA: ")
    preFlop1 = preFlop1.strip().upper()


    preFlop2 = input("2ª CARTA: ")
    preFlop2 = preFlop2.strip().upper()

print(preFlop1, preFlop2)

def resivarJugadoresQueCambia():
    print("Han abandonado la mesa alguien? (SI S / NO N)")
    eleccionJugadores = input("Escribalo acontinuacion= ")
    eleccionJugadores = eleccionJugadores.upper().strip()

        
    if(eleccionJugadores == "S" or eleccionJugadores == "SI"):
        numJugadoresAbandonan = input("Cuantos jugadores han abandonado = ")
        numJugadoresAbandonan = int(numJugadoresAbandonan)

        jugadores = jugadores - numJugadoresAbandonan
            

    elif(eleccionJugadores == "N" or eleccionJugadores == "NO"):
        print("oK continuamos entonces")

    return jugadores
            

resivarJugadoresQueCambia()






