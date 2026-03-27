#Nombrar Preflop

print("CORAZONES = C // PICAS = P // TREBOLES = T // DIAMANTES = D")

print("Dime las cartas que te han tocado en el Preflop: ")

preFlop1 = input("1º CARTA: ")
preFlop1 = preFlop1.strip().upper()


preFlop2 = input("2ª CARTA: ")
preFlop2 = preFlop2.strip().upper()


def validacionDatosPreflop():
    validacion = False

    if(len(preFlop1) < 2 or len(preFlop2) < 2):
        print("Tamaño dado NO VALIDO")
        validacion =False

    if(preFlop1 == preFlop2):
        print("Has dado las mismas cartas")
        validacion =False
    
    if(preFlop1[1] not in ["D","C","P","T"]):
        print("Has dado un valor de carta NO VALIDO")
        validacion =False

    if(preFlop2[1] not in ["D","C","P","T"]):
        print("Has dado un valor de carta NO VALIDO")
        validacion =False

    if (preFlop1[0] != "A" and preFlop1[0] != "2" and preFlop1[0] != "3" and preFlop1[0] != "4"
        and preFlop1[0] != "5" and preFlop1[0] != "6" and preFlop1[0] != "7" and preFlop1[0] != "8"
        and preFlop1[0] != "9" and preFlop1[0] != "J" and preFlop1[0] != "K" and preFlop1[0] != "Q"):
        
        print("Has dado un valor de carta NO VALIDO")
        validacion =False
    
    if (preFlop2[0] != "A" and preFlop2[0] != "2" and preFlop2[0] != "3" and preFlop2[0] != "4"
        and preFlop2[0] != "5" and preFlop2[0] != "6" and preFlop2[0] != "7" and preFlop2[0] != "8"
        and preFlop2[0] != "9" and preFlop2[0] != "J" and preFlop2[0] != "K" and preFlop2[0] != "Q"):

        print("Has dado un valor de carta NO VALIDO")
        validacion =False


    else:
        validacion = True


    return validacion

    
while(validacionDatosPreflop == False):
    preFlop1 = input("1º CARTA: ")
    preFlop1 = preFlop1.strip().upper()


    preFlop2 = input("2ª CARTA: ")
    preFlop2 = preFlop2.strip().upper()



