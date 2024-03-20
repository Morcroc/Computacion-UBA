from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

# Guía 8 - Archivos, Pilas, Colas y Diccionarios


#archivo1 = "Archivos/palabras"#r"C:\Users\velas\Desktop\Cosas\UBA\Proyectos-UBA\IP\Python\Archivos\palabras"
# ----ARCHIVOS----
# EJERCICIO 1
print("\nEJERCICIO 1")
# 1)
def contar_lineas(dir_archivo:str) -> int:
    archivo = open(dir_archivo, 'r', encoding="UTF-8")
    res = len(archivo.readlines())
    archivo.close()
    return res

def contar_lineas_bis(dir_archivo:str) -> int:
    with open(dir_archivo, 'r', encoding="UTF-8") as archivo:
        return len(archivo.readlines())
    
# 2)

def tiene_palabra(palabra:str, texto:str) -> bool:
    coincidencia:str = ""
    for c in texto:
        if(coincidencia == palabra):
            return True
        elif(c == palabra[len(coincidencia)]):
            coincidencia += c
        else:
            coincidencia = ""
    return False

def existe_palabra(palabra:str, dir_archivo:str) -> bool:
    with open(dir_archivo, 'r', encoding="UTF-8") as archivo:
        for linea in archivo.readlines():
            if(tiene_palabra(palabra, linea)):
                return True
    return False

texto1 =  "marisa iba caminando por la calle con su perro cuando vieron un caballero ingles"
#print(tiene_palabra("perro", "marisa iba caminando por la calle con su perro cuando vieron un caballero ingles"))
#print(tiene_palabra("estupido", "marisa iba caminando por la calle con su perro cuando vieron un caballero ingles"))
#print(existe_palabra("jojo", archivo1))
#print(existe_palabra("dios", archivo1))

# 3)
def contar_apariciones(palabra:str, texto:str) -> int:
    coincidencia:str = ""
    contador:int = 0
    for c in texto:
        if(coincidencia == palabra):
            contador += 1
            coincidencia = ""
        elif(c == palabra[len(coincidencia)]):
            coincidencia += c
        else:
            coincidencia = ""
    return contador

texto2 = "marisa iba caminando por la calle con su perro cuando vieron otro perro ladrando"
#print(f"perro aparece {contar_apariciones('perro', texto1)} veces")
#print(f"perro aparece {contar_apariciones('perro', texto2)} veces")

def cantidad_apariciones(palabra:str, dir_archivo:str) -> int:
    contador:int = 0
    with open(dir_archivo, 'r', encoding="UTF-8") as archivo:
        for linea in archivo.readlines():
            contador += contar_apariciones(palabra, linea)

    return contador

p1 = "cayo"
p2 = "a"
#print(f"la palabra {p1} aparece en {archivo1}: {cantidad_apariciones(p1, archivo1)} veces")
#print(f"la palabra {p2} aparece en {archivo1}: {cantidad_apariciones(p2, archivo1)} veces")


# EJERCICIO 2
print("\nEJERCICIO 2")

def clonar_sin_comentarios(dir_archivo:str):
    lineas_sin_comentario:"list[str]" = []
    with open(dir_archivo, 'r', encoding="UTF-8") as lectura:
        lineas:"list[str]" = lectura.readlines()
        for linea in lineas:
            if (not linea.lstrip().startswith('#')):
                lineas_sin_comentario.append(linea)
    with open(dir_archivo + "sin_comentarios.txt", 'w', encoding="UTF-8") as escritura:
        escritura.writelines(lineas_sin_comentario)
        


#print(contar_lineas(archivo1))
#clonar_sin_comentarios(r"nomo/nomo")

# EJERCICIO 3
print("\nEJERCICIO 3")

def reverso(dir_archivo:str):
    lineas:"list[str]" = []
    with open(dir_archivo, 'r', encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
    
    with open(dir_archivo + "_reverso.txt", 'w', encoding="UTF-8") as archivo:
        lineas = lineas[::-1]
        archivo.writelines(lineas)
    
#reverso(archivo1)

# EJERCICIO 4
print("\nEJERCICIO 4")

def agregar_al_final(frase:str, dir_archivo:str):
    with open(dir_archivo, 'a', encoding="UTF-8") as archivo:
        archivo.write(frase)

#agregar_al_final("pim pam pum, el mundo se convirtio en atun",archivo1)
#print(f"Se modifico el {archivo1}")

# EJERCICIO 5
print("\nEJERCICIO 5")

def agregar_al_principio(frase:str, dir_archivo:str):
    with open(dir_archivo, 'r+', encoding="UTF-8") as archivo:
        archivo.write(frase)

#agregar_al_principio("habia una vez un pais de gente de tres orejas", archivo1)
#print(f"Se modifico el {archivo1}")

# EJERCICIO 6
print("\nEJERCICIO 6")

def palabras_legibles(dir_archivo:str) -> "list[str]":
    def es_legible(c:chr) -> bool:
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9') or c == ' ' or c == '_'
    palabras:"list[str]" = []
    with open(dir_archivo, 'rb') as archivo:
        palabra:str = ""
        for linea in archivo.readlines():
            for c in str(linea):
                if (es_legible(c)):
                    palabra += c
                elif (len(palabra) >= 5):
                    palabras.append(palabra)
                    palabra = ""
                else:
                    palabra = ""
    
    return palabras

archivo2 = "Archivos/Código.zip"
#print(palabras_legibles(archivo2))
archivo3 = "Archivos/DISCO.png"
#print(palabras_legibles(archivo3)) #Dura mucho

# EJERCICIO 7
print("\nEJERCICIO 7")
def convertir_csv(linea:str) -> "list[str]":
        res:list[str] = []
        valor:str = ""
        for c in linea:
            if(c != ','):
                valor += c
            else:
                res.append(valor)
                valor = ""
        res.append(valor)
        return res

def promedio_estudiante(lu:str) -> float:
    promedio:float = 0
    notas: int = 0
    lineas:"list[list[str]]" = []
    with open("IP/Python/Archivos/Lista.csv", 'r') as archivo:
        for linea in archivo.readlines():
            lineas.append(convertir_csv(linea.strip()))
    for linea in lineas:
        if(linea[0] == lu):
            promedio += int(linea[-1])
            notas += 1
    return promedio / notas

print(promedio_estudiante("3716/21"))
print(promedio_estudiante("1413/23"))

# ---- PILAS ----
# EJERCICIO 8
print("\nEJERCICIO 8")

def generar_nros_al_azar(n:int, desde:int, hasta:int) -> Pila:
    res:"Pila[int]" = Pila()
    for i in range(0, n):
        res.put(random.randint(desde, hasta))
    return res
lista = []
pila1 = generar_nros_al_azar(10, -1000, 1000)
#while(not pila1.empty()):
#    lista.append(pila1.get())
#print(lista)

# EJERCICIO 9
print("\nEJERCICIO 9")

def cantidad_elementos(p:Pila) -> int:
    pila_aux:Pila = Pila()
    contador:int = 0
    while not p.empty():
        elemento = p.get()
        pila_aux.put(elemento)
        contador += 1
    while not pila_aux.empty():
        p.put(pila_aux.get())

    return contador

print(cantidad_elementos(pila1))
print(pila1.qsize())

# EJERCICIO 10
print("\nEJERCICIO 10")

def buscar_maximo(p:Pila) -> int:
    maximo = float('-inf')
    pila_aux:Pila = Pila()

    while not p.empty():
        elemento = p.get()
        pila_aux.put(elemento)
        maximo = max(maximo, elemento)
    while not pila_aux.empty():
        p.put(pila_aux.get())
    return maximo

print(buscar_maximo(pila1))

# EJERCICIO 11
print("\nEJERCICIO 11")

def esta_bien_balanceada(s:str) -> bool:
    # quiero recorrer el string e ir almacenando los caracteres que 
    pass






# ---- COLAS ----
# EJERCICIO 13
print("\nEJERCICIO 13")

def cola_generada_al_azar(n:int, desde:int, hasta:int) -> Cola:
    res = Cola()
    pila = generar_nros_al_azar(n, desde, hasta)
    while(not pila.empty()):
        res.put(pila.get())
    return res

def listar_cola(cola:Cola) -> list:
    res:list = []
    cola_aux = Cola()
    while(not cola.empty()):
        elemento = cola.get()
        res.append(elemento)
        cola_aux.put(elemento)
    while(not cola_aux.empty()):
        cola.put(cola_aux.get())
    return res

def colar_lista(lista:list) -> Cola:
    res:Cola = Cola()
    for e in lista:
        res.put(e)
    return res

print(listar_cola(cola_generada_al_azar(10, -1000, 1000)))
print(listar_cola(cola_generada_al_azar(5, -9999, 9999)))

# EJERCICIO 14
print("\nEJERCICIO 14")

def cantidad_elementos(cola:Cola) -> int:
    cola_aux = Cola()
    contador:int = 0
    while(not cola.empty()):
        cola_aux.put(cola.get())
        contador += 1
    while(not cola_aux.empty()):
        cola.put(cola_aux.get())
    return contador

cola1 = cola_generada_al_azar(10, 5, 20)
cola2 = cola_generada_al_azar(80, -1, 1)
print(listar_cola(cola1))
print(cantidad_elementos(cola1))
print(listar_cola(cola1))
print(listar_cola(cola2))
print(cantidad_elementos(cola2))
print(listar_cola(cola2))

# EJERCICIO 15
print("\nEJERCICIO 15")

def buscar_el_maximo(c:"Cola[int]") -> int:
    cola_aux = Cola()
    res = float('-inf')
    while(not c.empty()):
        elemento = c.get()
        res = max(res, elemento)
        cola_aux.put(elemento)
    while(not cola_aux.empty()):
        c.put(cola_aux.get())
    return res

print(buscar_el_maximo(cola1))
print(buscar_el_maximo(cola2))

# EJERCICIO 16
print("\nEJERCICIO 16")

def armar_secuencia_de_bingo() -> "Cola[int]":
    res:"Cola[int]" = Cola(100)
    numeros:"list[int]" = list(range(0,100))
    random.shuffle(numeros)
    for n in numeros:
        res.put(n)
    return res


def jugar_carton_bingo(carton:"list[int]", bolillero:"Cola[int]") -> int:
    num_marcados:"list[int]" = []
    res: int = 0
    cola_aux:"Cola[int]" = Cola()
    while len(num_marcados) < len(carton) and not bolillero.empty():
        n = bolillero.get()
        cola_aux.put(n)
        if(n in carton):
            num_marcados.append(n)
        res += 1
    while not bolillero.empty():
        cola_aux.put(bolillero.get())
    while not cola_aux.empty():
        bolillero.put(cola_aux.get())
    return res

bolillero = armar_secuencia_de_bingo()
carton = [12,54,9,84,65,32,44,78,96,58,36,11]
print(f"tomaron {jugar_carton_bingo(carton, bolillero)} intentos llenar el carton {carton}")

# EJERCICIO 17
print("\nEJERCICIO 17")

def n_pacientes_urgentes(c:"Cola[(int,str,str)]") -> int:
    cola_aux:"Cola[(int,str,str)]" = Cola()
    res:int = 0
    while not c.empty():
        e = c.get()
        cola_aux.put(e)
        if(e[0] >= 1 and e[0] <= 3):
            res += 1
    while not cola_aux.empty():
        c.put(cola_aux.get())
    return res

pacientes = [(7,"",""),(2,"",""),(8,"",""),(1,"",""),(4,"",""),(3,"",""),(2,"","")]
colastica = Cola()
for i in pacientes:
    colastica.put(i)

print(n_pacientes_urgentes(colastica))

# EJERCICIO 18
print("\nEJERCICIO 18")


''' primero personas con cuenta preferencial y prioridad, despues personas con prioridad, despues personas con cuenta preferencial, 
despues el resto, y todos esos segmentos en el orden en que aparecen en la lista
problema atencion_clientes_banco (s: seq<(String, Z, Bool, Bool)>) : seq<(String, Z, Bool, Bool)>{
    requiere: {True}
    asegura: {res contiene exactamente los mismos elementos de s, y su misma longitud}
    asegura: {los primeros n elementos de res corresponden a los n elementos de s que tienen la forma (_,_,True,True) en el orden de aparicion}
    asegura: {el segundo segmento de res corresponde a los m elementos de s que tienen la forma (_,_,False,True) en el orden de aparicion}
    asegura: {el tercer segmento de res corresponde a los k elementos de s que tienen la forma (_,_,True,False) en orden de aparicion}
    asegura: {el ultimo segmento de res corresponde a los j elementos de s que tienen la forma (_,_,False,False) en orden de aparicion}
}'''

def a_clientes(c:"Cola[(str,int,bool,bool)]") -> "Cola[(str,int,bool,bool)]":
    cola_aux:"Cola[(str,int,bool,bool)]" = Cola()
    res = Cola()
    prioridad = Cola()
    cuenta = Cola()
    # tengo que recorrer la lista, pasando los resultados de a poco en la cola de resultados y en la auxiliar
    while not c.empty():
        e = c.get()
        if(e[2] and e[3]):
            res.put(e)
        elif(not e[2] and e[3]):
            prioridad.put(e)
        elif(e[2] and not e[3]):
            cuenta.put(e)
        cola_aux.put(e)

    while not prioridad.empty():
        res.put(prioridad.get())

    while not cuenta.empty():
        res.put(cuenta.get())

    while not cola_aux.empty():
        e = cola_aux.get()
        if(not e[2] and not e[3]):
            res.put(e)
        c.put(e)
    return res

clientes = [("Juan Martín Marino",55555555, False, True), ("Sabino Sabbatini",55555555, False, False), ("Godfredo Fernandez",55555555, True, False), ("Gervasio Piazza",55555555, True, True),
            ("Clarissa Gallo",55555555, False, False), ("Clementina Borroni",55555555, False, True), ("Emesta Varela",55555555, True, False), ("Natividad Molina",55555555, False, False),
            ("Agustín Figueroa",55555555, True, True), ("Chayo Fernández",55555555, False, True), ("Casimiro Luna",55555555, True, False), ("Iván Milani",55555555, False, False),
            ("Lucrecia Pinto",55555555, False, False), ("Sabana Ramirez",55555555, False, True), ("Melosia Prieto",55555555, True, False), ("Elisa Schmidt",55555555, False, False),
            ("Roderigo Cohen",55555555, False, True), ("Richie Ferreyra",55555555, True, False), ("Melita Bianchi",55555555, True, True), ("Marilu Munoz",55555555, True, True)]

print(listar_cola(a_clientes(colar_lista(clientes))))


# ---- DICCIONARIOS ----
# EJERCICIO 19
print("\nEJERCICIO 19")
def separar_en_palabras(s:str) -> "list[str]":
    res:"list[str]" = []
    palabra:str = ""
    for c in s:
        if(c != ' '):
            palabra += c
        else:
            res.append(palabra)
            palabra = ""
    if len(palabra) > 0:
        res.append(palabra)
    return res
def agrupar_por_longitud(path:str) -> dict:
    res:dict = {}
    with open(path, 'r', encoding="UTF-8") as archivo:
        for line in archivo.readlines():
            for palabra in separar_en_palabras(line):
                if len(palabra) in res.keys():
                    res[len(palabra)] = res[len(palabra)] + 1
                else:
                    res[len(palabra)] = 1
                    
    return res

archivito = "IP\Python\Archivos\palabrerio.txt"
with open(archivito) as archivo:
    for linea in archivo.readlines():
        print(separar_en_palabras(linea))


print(agrupar_por_longitud(archivito))

# EJERCICIO 20
print("\nEJERCICIO 20")

def promedio_notas() -> dict:
    res:dict = {}
    listado:list = []
    libretas:list = []
    with open("IP\Python\Archivos\Lista.csv", 'r', encoding="UTF-8") as archivo:
        for linea in archivo.readlines():
            if(linea != ",,,\n"):
                listado.append(convertir_csv(linea))
    
    for e in range(1, len(listado)):
        if(not listado[e][0] in libretas):
            libretas.append(listado[e][0])
    for libreta in libretas:
        promedio:float = 0
        notas:int = 0
        for e in listado:
            if(e[0] == libreta):
                promedio += float(e[3])
                notas += 1
        res[libreta] = promedio/notas
    return res

print(promedio_notas())

# EJERCICIO 21
print("\nEJERCICIO 21")

def palabra_mas_frecuente(path:str) -> str:
    res:str = ""
    diccionario:dict = {}
    max = 0
    with open(path, 'r', encoding="UTF-8") as archivo:
        for linea in archivo.readlines():
            for palabra in separar_en_palabras(linea.strip()):
                if(palabra in diccionario.keys()):
                    diccionario[palabra] += 1
                else:
                    diccionario[palabra] = 1
                if diccionario[palabra] > max:
                    res = palabra
                    max = diccionario[palabra]
    #print(diccionario)

    return res

print(palabra_mas_frecuente("IP\Python\Archivos\descripcion_01"))
print(palabra_mas_frecuente("IP\Python\Archivos\descripcion_02"))

# EJERCICIO 22
print("\nEJERCICIO 22")

historiales:"dict[str,tuple[Pila,Pila]]" = {}
def visitar_sitio(historiales:"dict[str,tuple[Pila,Pila]]",usuario:str, sitio:str):
    if(usuario in historiales.keys()):
        historiales[usuario][0].put(sitio)
    else:
        historiales[usuario] = (Pila(), Pila())
        historiales[usuario][0].put(sitio)
    
def navegar_atras(historiales:"dict[str,tuple[Pila,Pila]]", usuario:str):
    if(usuario in historiales.keys()):
        historiales[usuario][1].put(historiales[usuario][0].get())
    else:
        print("No hay un historial para el usuario ingresado")
    
def navegar_adelante(historiales:"dict[str,tuple[Pila,Pila]]", usuario:str):
    if(usuario in historiales.keys()):
        historiales[usuario][0].put(historiales[usuario][1].get())
    else:
        print("No hay un historial para el usuario ingresado")

visitar_sitio(historiales, "usuario-01", "youtube")
visitar_sitio(historiales, "usuario-01", "itch.io")
visitar_sitio(historiales, "usuario-02", "instagram")
navegar_atras(historiales, "usuario-01")
visitar_sitio(historiales, "usuario-01", "twitter")
visitar_sitio(historiales, "usuario-02", "youtube")
navegar_adelante(historiales, "usuario-03")


print(f"En usuario-01 hay historiales de {historiales["usuario-01"][0].queue} y {historiales["usuario-01"][1].queue}")
print(f"En usuario-02 hay historiales de {historiales["usuario-02"][0].queue} y {historiales["usuario-02"][1].queue}")


# EJERCICIO 23
print("\nEJERCICIO 23")

inventario:"dict[str,tuple[float, int]]" = {}
def agregar_producto(inventario, nombre, precio, cantidad):
    
    pass