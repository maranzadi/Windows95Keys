import random




print("-----------------------------------------")
print("------- Windows 95 key generator --------")
print("-----------------------------------------\n\n")

print("INSTRUCICIONES\n")
print("Ingresas la cantidad de claves de Windows 95 que quieres generar")
cuantos = input("Cantidad de claves: ")

cuantos = int(cuantos)

cantidad = 0

for i in range(cuantos):
    numbers = 0
    V_O = False
    code = 0
    ultimo = 0
    cantidad = int(cantidad)
    dia = 0
    ano = 0 
    while True:
     if V_O == True:

        break
     else:
        V_O = False
        def generate_number(numbers):

            n = random.randint(0,0)
            u = random.randint(0,0)
            m = random.randint(0,9)
            b = random.randint(0,9)
            e = random.randint(0,9)
            r = random.randint(0,9)
            s = random.randint(0,9)

            numeros = [n,u,m,b,e,r,s]

            complete = ''.join(str(num) for num in numeros)
            number = n+u+m+b+e+r+s
            number = number / 7        

            return number, complete

        numbers, code = generate_number(numbers)
        #saca los decimales de todos los numeros
        #print (numbers)
        #comprobar si es un numero entero
        def is_integer_num(numbers):
        #Nos comprueba si es numero entero
            if numbers.is_integer():
                #print ("salio verdadero")
                return True
            else:
                #print ("salio falso")
                return False


        V_O = is_integer_num(numbers)
        #Imprime todo los numeros que calcula
        #print("False: " + code)
        cantidad = cantidad + 1

    
        if V_O == True:
            #El primer digito del codigo, nos da igual que numero es
            #primero = random.randint(0,9)
            #Realmente es de 0-99999, los posibles numeros, pero los numeros menores a 1000, no tiene 0 por delante, y puede traer fallos. Igualmente estos ultimos 5 digitos no hacen nada.
            ultimo = random.randint(10000,99999)
            #Por la misma razon que el de arriba, para quitar problemas
            dia = random.randint(100,364)
            #Del 95 al 97 se que se vendian las licencias, y como no afecta en nada a la licencia, lo he puesto de esta manera.
            ano = random.randint(95,97)
            cantidad = ''.join(str(cantidad))
            #primero = ''.join(str(primero))
            code = ''.join(str(code))
            ultimo = ''.join(str(ultimo))
            dia = ''.join(str(dia))
            ano = ''.join(str(ano))
            print("La clave es: " + dia + ano + "-OEM-" + code + "-" + ultimo)

            
            break

print("Calculados " + cantidad + " posibles contraseñas")





#                      .:.....:...      :Y7         :::::::..         
#       :PPPPPPPPPGBY  ~GGPGGGGG&#:     G@#PP5PG7  ^GPPPPPP#&J        
#        :...:::.!@&~    :^.   ?@P    :B@7:^^^#@!         ~@&:        
#         :J~   ~&#^     7BBJ:~&#:   ?&B^    7@P         :#&~         
#         :Y&G~7@G:        ~5&@@^    !7     ?@G.        7&@B.         
#           :P@@5          ~G&5B#?.       ~G@Y        !G@Y!#&?        
#             !&&7     ^75BBJ: .J&J   :!YB#5^     .!5##Y:  .P@G:      
#              :57    .Y5?^      .    ?GJ~.       .JY~       ?J: 