# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
# s = [-1,4,0,4,100,0,100,0,-1,-1]
# e = 0
# se debería devolver res=7

def ultima_aparicion(s: list, e: int) -> int:
    res:int = 0
    for i in range(len(s)):
        if(s[i] == e):
            res = i
    return res

##########################################################################
##########################################################################

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def pertenece(l:list, e) -> bool:
    res = False
    i = 0
    while(not res and i < len(l)):
        res = e == l[i]
        i += 1
    return res


def elementos_exclusivos(s: "list[int]", t: "list[int]") -> "list[int]":
    # tengo que recorrer cada lista, viendo que los elementos que este viendo no pertenezcan a la otra 
    # lista ni a la lista de resultados, y ahi agregarlo a la lista de resultados
    res:"list[int]" = []
    for i in s:
        if(not i in t and not i in res):
            res.append(i)
    for j in t:
        if(not j in s and not j in res):
            res.append(j)
    return res


##########################################################################
##########################################################################

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#  aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#  inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    res:int = 0
    for clave, valor in ingles.items():
        if(clave in aleman.keys()):
            if(valor == aleman[clave]):
                res += 1
    return res

##########################################################################
##########################################################################

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

def convertir_a_diccionario(lista: list) -> dict:
    res:dict[int,int] = {}
    lista_aux:list = []
    lista_aux += lista
    for i in lista:
        if(i not in res.keys()):
            res[i] = lista_aux.count(i)
            while i in lista_aux:
                lista_aux.remove(i)
    return res