import math

def algo ():
    print("Holiwis")
# EJERCICIO 1
#######################
print("\nEJERCICIO 1")
# 1)
def imprimir_hola_mundo():
    print("Aaaa te bañaste.")
# 2)
def imprimir_un_verso():
    print("No soy nada.\nNunca seré nada.\nNo puedo querer ser nada.\nMás allá de eso, tengo en mi todos los sueños del mundo.")
# 3)
def raiz_de_2() -> float:
    return round(math.sqrt(2), 4)
# 4)
def factorial_de_dos() -> int:
    return 2
# 5)
def perimetro() -> float:
    return 2 * math.pi

# EJERCICIO 2
#########################
print("\nEJERCICIO 2")
# 1)
def imprimir_saludo(nombre:str) -> str:
    print("Hola " + nombre)
# 2)
def raiz_cuadrada_de(numero:float) -> float:
    return math.sqrt(numero)
# 3)
def fahrenheit_a_celcius(t:float) -> float:
    return ((t - 32) * 5) / 9
# 4)
def imprimir_dos_veces(e:str) -> str:
    print(e * 2)

# 5)
def es_multiplo_de(n:int, m:int) -> bool:
    return math.remainder(n, m) == 0

print(es_multiplo_de(-9369, 3))
# 6)
def es_par(n:int) -> bool:
    return es_multiplo_de(n, 2)

print(es_par(419823231))
# 7)
def cantidad_de_pizzas(comensales:int, min_cantidad:int) -> int:
    return math.ceil((comensales * min_cantidad) / 8)

gente = 50
porciones = 5
print("La cantidad de pizza necesaria para " + str(gente) + " comensales que comen " + str(porciones) + " porciones es: " + str(cantidad_de_pizzas(gente, porciones)))

# EJERCICIO 3
#######################
print("\nEJERCICIO 3")
# 1)
def alguno_es_0(n1:float, n2:float) -> bool:
    return n1 == 0 or n2 == 0
# 2)
def ambos_son_0(n1:float, n2:float) -> bool:
    return n1 == 0 and n2 == 0
# 3)
def es_nombre_largo(nombre:str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

print(es_nombre_largo("A"))
print(es_nombre_largo("Abc"))
print(es_nombre_largo("Jose"))
print(es_nombre_largo("Jose Arcadio"))
print(es_nombre_largo("Catalina\n"))

# 4)
def es_bisiesto(a:int) -> bool:
    return es_multiplo_de(a, 400) or (es_multiplo_de(a, 4) and not es_multiplo_de(a, 100))

print(es_bisiesto(400))

# EJERCICIO 4
#######################
print("\nEJERCICIO 4")
# 3)
def sirve_pino(altura:float) -> bool:
    # 1)
    def peso_pino(altura:float) -> float:
        peso:float
        if(altura > 3):
            peso = (altura - 3) * 100 * 2 + 3 * 100 * 3
        else:
            peso = altura * 100 * 3
        return peso
    # 2)
    def es_peso_util(peso:float) -> bool:
        return peso >= 400 and peso <= 1000
    
    return es_peso_util(peso_pino(altura))
print(sirve_pino(3))

# EJERCICIO 5
####################
print("\nEJERCICIO 5")
# 1)
def devolver_el_doble_si_es_par(n:int) -> int:
    res:int
    if(es_par(n)):
        res = 2 * n
    else:
        res = n
    return res

# 2)
def devolver_valor_si_es_par_sino_el_que_sigue(n:int) -> int:
    res:int
    if(es_par(n)):
        res = n
    else:
        res = n + 1
    return res

# 3)
def doble_si_multiplo3_triple_si_multiplo9(n:int) -> int:
    res:int
    if(es_multiplo_de(n, 9)):
        res = 3 * n
    elif(es_multiplo_de(n, 3)):
        res = 2 * n
    else:
        res = n
    return res

# 4)
def lindo_nombre(nombre:str) -> str:
    res:str
    if(len(nombre) >= 5):
        res = "Tu nombre tiene muchas letras!"
    else:
        res = "Tu nombre tiene menos de 5 letras."
    return res

# 5)
def elRango(n:float):
    if(n > 20):
        print("Mayor a 20")
    elif(n > 10):
        print("Entre 10 y 20")
    if(n < 5):
        print("Menor a 5")

# 6)
def vacaciones3000(e:int, g:chr):
    if(e < 18 or ((g == 'f' or g == 'F') and e >= 60) or ((g == 'm' or g == 'M') and e >= 65)):
        print("Andá de vacaciones B)")
    else:
        print("Te toca trabajar >:)")

print(devolver_el_doble_si_es_par(1))
print(devolver_el_doble_si_es_par(2))
print(devolver_el_doble_si_es_par(3))
print(devolver_el_doble_si_es_par(4))
print(devolver_valor_si_es_par_sino_el_que_sigue(1))
print(devolver_valor_si_es_par_sino_el_que_sigue(2))
print(devolver_valor_si_es_par_sino_el_que_sigue(3))
print(devolver_valor_si_es_par_sino_el_que_sigue(4))
print(doble_si_multiplo3_triple_si_multiplo9(1))
print(doble_si_multiplo3_triple_si_multiplo9(2))
print(doble_si_multiplo3_triple_si_multiplo9(3))
print(doble_si_multiplo3_triple_si_multiplo9(9))
print(lindo_nombre("Gesisvaldo"))
print(lindo_nombre("Gorg"))
elRango(2)
elRango(6)
elRango(14)
elRango(40)
vacaciones3000(34, 'F')
vacaciones3000(98, 'M')
vacaciones3000(13, 'F')
vacaciones3000(61, 'F')
vacaciones3000(18, 'm')
vacaciones3000(62, 'm')

# EJERCICIO 6
#################
print("\nEJERCICIO 6")
# 1)
def f1():
    i = 1
    while(i <= 10):
        print(i)
        i += 1
# 2
def f2():
    i = 10
    while(i <= 40):
        if(es_par(i)):
            print(i)
        i += 1
# 3)
def eco():
    i = 0
    while(i < 10):
        print("eco")
        i += 1
# 4)
def cuenta_regresiva(t:int):
    while(t > 0):
        print(t)
        t -= 1
    print("DESPEGUE!!!! FIUUUM")
# 5)
def viaje_al_pasado(inicio:int, fin:int):
    i = 0
    i += inicio
    while(i > fin):
        i -= 1
        print("Viajó un año al pasado, estamos en el año: " + str(i))
    print("Estamos en el destino.")
# 6)
def conocer_aristoteteles(inicio:int):
    i = inicio
    while(abs(-384 - i) >= 20):
        i -= 20
        print("Viajó un año al pasado, estamos en el año: " + str(i))
    print("Estamos en el destino.")

# EJERCICIO 7
###################
print("\nEJERCICIO 7")
# 1)
def g1():
    for i in range(1, 11):
        print(i)
# 2)
def g2():
    for i in range(10, 41, 2):
        print(i)
# 3)
def g3():
    for i in range(0, 10):
        print("eco")
# 4)
def g4(i:int):
    for j in range(i, 0, -1):
        print(j)
    print("DESPEGUE!!!!")
# 5)
def g5(inicio:int, fin:int):
    for i in range(inicio, fin, -1):
        print("Viajó un año al pasado, estamos en el año: " + str(i))
    print("Llegamos")
def g6(inicio:int):
    for i in range(inicio, -384, -20):
        print("Viajó un año al pasado, estamos en el año: " + str(i))
    print("Conociste a Aristóteles.")
g1()
g2()
g3()
g4(5)
g5(2030, 1990)
g6(2400)



