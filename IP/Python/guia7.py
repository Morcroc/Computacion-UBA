import array
import math
import random
# EJERCICIO 1
#######################
print("\nEJERCICIO 1")
# 1)
def pertenece_while(lista:list, e:int) -> bool:
    i = 0
    aparece:bool = False
    while (i < len(lista) and not aparece):
        aparece = e == lista[i]
        i += 1

    return aparece

print(pertenece_while([1,2,3,4,5,6,7,8,9,10], 11))
print(pertenece_while([1,2,3,4,5,6,7,8,9,10], 5))

def pertenece_for(lista:"list[int]", e:int) -> bool:
    aparece:bool = False
    for i in range(len(lista)):
        if(e == lista[i]):
            aparece = True

    return aparece

a = array.array('i', [1,2,3,4,5,6,7,8,9,10,0])
print(pertenece_for(a, 6))
print(pertenece_for(a, 12))

def pertenece_simple(lista:[int], e:int) -> bool:
    return e in lista

print("pertenece simple? " + str(pertenece_simple(a, 6)))
print("pertenece simple? " + str(pertenece_simple(a, 12)))

def pertenece(lista, e) -> bool:
    for i in lista:
        if(i == e):
            return True
    return False

print(pertenece("hola, mi nombre es manola", 'a'))
print(pertenece("hola, mi nombre es manola", 'z'))
print(pertenece([1,2,3,4,5,6,7,8,9,10], 5))

# 2)
def divide_todos(lista:"list[int]", e:int) -> bool:
    divide:bool = True
    i = 0
    while (i < len(lista) and divide):
        divide = lista[i] % e == 0
        i += 1

    return divide

b = array.array('i', [2,4,6,8,10,12,14,16])
print("1 divide a todos? " + str(divide_todos(a, 1)))
print("2 divide a todos? " + str(divide_todos(b, 2)))
print("3 divide a todos? " + str(divide_todos(a, 3)))

# 3)
def suma_total(lista:list) -> int:
    suma:int = 0
    for i in lista:
        suma += i
    return suma

print(suma_total(b))
print(suma_total(a))

# 4)
def ordenados(lista:[int]) -> bool:
    ordenada:bool = True
    i = 0
    while (i < len(lista) - 1 and ordenada):
        ordenada = lista[i] < lista[i+1]
        i += 1
    return ordenada

print("La lista " + str(a) + " esta ordenada? " + str(ordenados(a)))
print("La lista " + str(b) + " esta ordenada? " + str(ordenados(b)))

# 5)
def tiene_palabra_larga(lista:list) -> bool:
    res:bool = False
    # tengo que hacer que sea true si una de las palabras que aparecen en la frase tiene >7 letras
    # esto se puede hacer separando primero las palabras y despues contando su longitud
    i:int = 0
    palabra:list = []
    while (i < len(lista) and not res):
        if(lista[i] != ' '):
            palabra.append(lista[i])
        else:
            res = len(palabra) > 7
            palabra.clear()
        i += 1
    return res

print("Tiene palabra larga? " + str(tiene_palabra_larga("hola mi nombre es josefa catas milena")))
print("Tiene palabra larga? " + str(tiene_palabra_larga("hola mi nombre es josefa catastrofica milena")))

# 6)
def palindromo(palabra:list) -> bool:
    res = True
    i:int = 0
    while (i < len(palabra)/2 and res):
        res = palabra[i] == palabra[-i -1]
        i += 1

    return res

print("Es palindromo 'Tu vieja'? " + str(palindromo("Tu vieja")))
print("Es palindromo 'hanah'? " + str(palindromo("hanah")))
print("Es palindromo 'peppep'? " + str(palindromo("peppep")))

# 7)
def password(contra:str) -> str:
    def tiene_minuscula(c:str) -> bool:
        minuscula:bool = False
        i:int = 0
        while (i < len(c) and not minuscula):
            minuscula = c[i] >= 'a' and c[i] <= 'z'
            i += 1
        return minuscula
    def tiene_mayuscula(c:str) -> bool:
        mayuscula:bool = False
        i:int = 0
        while (i < len(c) and not mayuscula):
            mayuscula = c[i] >= 'A' and c[i] <= 'Z'
            i += 1
        return mayuscula
    def tiene_digito(c:str) -> bool:
        digito:bool = False
        i:int = 0
        while (i < len(c) and not digito):
            digito = c[i] >= '0' and c[i] <= '9'
            i += 1
        return digito
    
    res:str
    if(len(contra) > 9 and tiene_minuscula(contra) and tiene_mayuscula(contra) and tiene_digito(contra)):
        res = "VERDE"
    elif(len(contra) < 5):
        res = "ROJA"
    else:
        res = "AMARILLA"

    return res

print("Contraseña 'Jesucr1sto': " + password("Jesucr1sto"))
print("Contraseña 'lol': " + password("lol"))
print("Contraseña 'Gorila': " + password("Gorila"))
print("Contraseña 'Moñ1t0': " + password("Moñ1t0"))

# 8)
def banco(movimientos:"list[(str, int)]") -> int:
    saldo:int = 0
    for (mov, monto) in movimientos:
        if(mov == 'I'):
            saldo += monto
        elif(mov == 'R'):
            saldo -= monto

    return saldo

print(banco([("I",2000), ("R", 20),("R", 1000),("I", 300)]))

# 9)
def vocales_distintas(palabra:str) -> bool:
    vocales:list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vocales_presentes:list = []
    i:int = 0
    while (i < len(palabra) and len(vocales_presentes) < 6):
        if(palabra[i] in vocales and not palabra[i] in vocales_presentes):
            vocales_presentes.append(palabra[i].upper())
            vocales_presentes.append(palabra[i].lower())
        i += 1
    return len(vocales_presentes) >= 6

print("Tiene 'perro' tres vocales distintas? " + str(vocales_distintas("perro")))
print("Tiene 'unicornio' tres vocales distintas? " + str(vocales_distintas("unicornio")))
print("Tiene 'perrEro' tres vocales distintas? " + str(vocales_distintas("perrEro")))
print("Tiene 'guerrero' tres vocales distintas? " + str(vocales_distintas("guerrero")))


# EJERCICIO 2
#####################
print("\nEJERCICIO 2")

# 1)
def borra_lugares_pares(lista:[int]):
    for i in range(len(lista)):
        if(i % 2 == 0):
            lista[i] = 0
def borra_lugares_pares_bis(lista:[int]):
    for i in range(0, len(lista), 2):
        lista[i] = 0

test1 = [1,2,3,4,5,6,7,8,9,10]
test2 = [0,2,4,6,8,10,12,14,16]
print(test1)
borra_lugares_pares(test1)
print(test1)
print(test2)
borra_lugares_pares_bis(test2)
print(test2)

# 2)
def borra_lugares_pares_2(lista:"list[int]") -> [int]:
    nueva_lista:list[int] = []
    nueva_lista += lista
    borra_lugares_pares(nueva_lista)
    return nueva_lista

# 3)
def borrar_vocales(palabras:str) -> str:
    res:str = ""
    vocales:list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for c in palabras:
        if(not c in vocales):
            res += c
    return res

print(borrar_vocales("hola, mi nombre es catalina B)"))

# 4)
def reemplaza_vocales(palabras:str) -> str:
    res:str = ""
    vocales:list = ['a', 'e', 'i', 'o', 'u']
    for c in palabras:
        if(c in vocales):
            res += '_'
        else:
            res += c
    return res

print(reemplaza_vocales("Hola, soy Akatosh, conquistador de mundos"))

# 5)
def daVueltaStr(s:str) -> str:
    res:str = ""
    for i in range(len(s)):
        res += s[len(s)-1-i]
    return res

print(daVueltaStr("Hola mundo!"))

# 6)
def eliminarRepetidos(s:str) -> str:
    res:str = ""
    for c in s:
        if(not c in res):
            res += c
    return res

frase1 = "Voy a ver que queda de comer hoy, porque mañana hay estofado!"
print("Quitar repetidos de: " + frase1 + "\nEs igual a: " + eliminarRepetidos(frase1))


# EJERCICIO 3
################
print("\nEJERCICIO 3")

def mayores_iguales_que(s:[int], m:int) -> bool:
    res = True
    i = 0
    while(i < len(s) and res):
        res = s[i] >= m
        i += 1
    return res

def aprobado(notas:[int]) -> int:
    promedio: int = suma_total(notas) / len(notas)
    todos_aprobados:bool = mayores_iguales_que(notas, 4)
    if (not todos_aprobados or promedio <= 4):
        return 3
    elif (todos_aprobados and promedio >= 4 and promedio < 7):
        return 2
    elif (todos_aprobados and promedio >= 7):
        return 1
    else:
        return 0
    
notas1 = [4, 5,7, 7]
notas2 = [3, 4, 5, 6]
notas3 = [10, 10, 4, 4]
print("Condicion de notas: " + str(notas1) + " es igual a: " + str(aprobado(notas1)))
print("Condicion de notas: " + str(notas2) + " es igual a: " + str(aprobado(notas2)))
print("Condicion de notas: " + str(notas3) + " es igual a: " + str(aprobado(notas3)))


# EJERCICIO 4
#################
print("\nEJERCICIO 4")
# 1)
def listado_estudiantes() -> [str]:
    ciclo:bool = True
    lista:[str] = []
    while (ciclo):
        nombre = input("Ingrese nombre de estudiante: ")
        if(nombre == "listo"):
            ciclo = False
        else:
            lista.append(nombre)
    return lista

#print(listado_estudiantes())

# 2)
#devuelve una LISTA de DUPLAS
def sistema_sube() -> [(str, float)]:
    ciclo:bool = True
    historial:[(str, float)] = []
    saldo:float = 0
    while(ciclo):
        operacion:str = input("Ingrese una operación válida:\n'C' = Cargar crédito\n'D' = Descontar créditos\n'X' = Terminar programa\n")
        if(operacion == 'C' or operacion == 'c'):
            monto:float = float(input("Ingrese monto a cargar: "))
            saldo += monto
            historial.append((operacion.upper(), saldo))
        elif(operacion == 'D' or operacion == 'd'):
            monto:float = float(input("Ingrese monto a descontar: "))
            saldo -= monto
            historial.append((operacion.upper(), saldo - monto))
        elif(operacion != 'X' and operacion != 'x'):
            print(operacion + " no es una operación válida.")
        else:
            ciclo = False
    return historial

#print(sistema_sube())

# 3)
def siete_y_medio() -> list[int]:
    baraja:list[int] = [1,2,3,4,5,6,7,10,11,12]
    baraja *= 4
    suma:float = 0
    cartas:list[int] = []
    ciclo:bool = True
    input("Presiona ENTER para iniciar el 7 y medio...")
    while (ciclo):
        nueva_carta:int = random.choice(baraja)
        cartas.append(nueva_carta)
        baraja.remove(nueva_carta)
        if(nueva_carta >= 10 and nueva_carta <= 12):
            suma += 0.5
        else:
            suma += nueva_carta
        print("Sacaste un " + str(nueva_carta) + "\nSumás " + str(suma))
        if(suma == 7.5):
            print("Ganaste!")
            ciclo = False
        elif(suma > 7.5):
            print("Perdiste! Que lástima...")
            ciclo = False
        else:
            ciclo = yes_no_decision("Querés sacar otra carta?")            

    return cartas

def yes_no_decision(promt:str) -> bool:
    flag:bool = True
    res:bool = False
    while(flag):
        response = input(promt + " (Y/N) : ")
        if(response == 'Y' or response == 'y'):
            res = True
            flag = False
        elif(response == 'N' or response == 'n'):
            res = False
            flag = False
        else:
            print("Please, input a valid operation (Y)es/(N)o")
    return res


#print(siete_y_medio())