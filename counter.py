

print("Ingrese un numero: ")
user_guest = int(input())
x = False
while user_guest:
    if user_guest == 3:
        print('numero correcto')
        x = True
    elif user_guest > 10 and user_guest < 0:
        print('Error')

    else:
        print('incorrecto, intentelo de nuevo')