-- ACTIVIDAD 2
----------------------

absoluto :: (Num t, Ord t) => t -> t
absoluto i 
    | i >= 0 = i
    | i < 0 = -i


maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto i j 
    | absoluto i >= absoluto j = i
    | absoluto i < absoluto j = j


maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 i j k 
    | i >= j && i >= k = i
    | j >= i && j >= k = j
    | k >= i && k >= j = k
    | otherwise = -1


algunoEs0 :: Double -> Double -> Bool
algunoEs0 x y = (x == 0) || (y == 0)
{-algunoEs0 _ 0 = True
algunoEs0 0 _ = True
algunoEs0 _ _ = False-}


ambosSon0 :: Double -> Double -> Bool
ambosSon0 x y = x == 0 && y == 0
--ambosSon0 0 0 = True
--ambosSon0 _ _ = False


mismoIntervalo :: Double -> Double -> Bool
mismoIntervalo x y = 
    (x <= 3 && y <= 3) ||
    (x <= 7 && x > 3 && y <= 7 && y > 3) ||
    (x > 7 && y > 7)


sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos i j k 
    | i /= j && j /= k && i /= k = i + j + k
    | i == j && i /= k && j /= k = i + k
    | i /= j && i == k && j /= k = i + j
    | i /= j && i /= k && j == k = i + j
    | i == j && j == k && i == k = i

--esMultiploDe
esMultiplo :: (Integral t, Eq t) => t -> t -> Bool
esMultiplo x y = mod x y == 0


digitoUnidades :: Integer -> Integer
digitoUnidades n = mod (absoluto n) 10


digitoDecenas :: Integer -> Integer
digitoDecenas n 
    | n < 10 && n > (-10) = 0
    |otherwise = div (mod (absoluto n) 100) 10


-- ACTIVIDAD 3)
-------------------------

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y 
    | ecuacion == 0 = False
    | otherwise = (x * x) + (x * y * ecuacion) == 0
    where ecuacion = div (-x * x) (x * y)


-- ACTIVIDAD 4)
-------------------------

prodInt :: (Double, Double) -> (Double, Double) -> Double
prodInt t1 t2 = fst t1 * fst t2 + snd t1 * snd t2


todoMenor :: (Double, Double) -> (Double, Double) -> Bool
todoMenor (x,y) (v, w) = x < v && y < w


distanciaPuntos :: (Double, Double) -> (Double, Double) -> Double
distanciaPuntos p1 p2 = sqrt((fst p2 - fst p1)^2 + (snd p2 - snd p1^2))


sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (x, y, z) = x+y+z


sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x,y,z) n 
    | esMultiplo x n && esMultiplo y n && esMultiplo z n = x+y+z
    | esMultiplo x n && esMultiplo y n = x+y
    | esMultiplo x n && esMultiplo z n = x+z
    | esMultiplo y n && esMultiplo z n = y+z
    | esMultiplo x n = x
    | esMultiplo y n = y
    | esMultiplo z n = z
    | otherwise = 0


esPar ::(Integral t, Eq t) => t -> Bool
esPar x = mod x 2 == 0

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x, y, z) 
    | esPar x = 1
    | esPar y = 2
    | esPar z = 3
    | otherwise = 4


crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)


invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)


-- ACTIVIDAD 5
-------------------------------

f :: Integer -> Integer
f n 
    | n <= 7 = n * n
    | otherwise = 2*n - 1

g :: Integer -> Integer
g n
    | esPar n = div n 2
    | otherwise = 3*n + 1

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (x, y, z) = f x > g x && f y > g y && f z > g z 


-- ACTIVIDAD 6
------------------------------

bisiesto :: Integer -> Bool
bisiesto n = esMultiplo n 4 || esMultiplo n 100 && not (esMultiplo n 400)


-- ACTIVIDAD 7
------------------------------

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x,y,z) (a,b,c) = absoluto (x-a) + absoluto (y-b) + absoluto (z-c)


-- ACTIVIDAD 8
-----------------------------

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = digitoUnidades x + digitoDecenas x

comparar :: Integer -> Integer -> Integer
comparar x y 
    | sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
    | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
    | sumaUltimosDosDigitos x == sumaUltimosDosDigitos y = 0

---------  GUIA 4  ---------------

-- ACTIVIDAD 1
------------------

fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci x = fibonacci(x-1) + fibonacci(x-2)


-- ACTIVIDAD 2
--------------------

parteEntera :: Double -> Int
parteEntera x
    | x < 0 && x >= -1 = -1
    | x >= 0 && x < 1 = 0
    | x > 1 = parteEntera (x-1) + 1
    | x < -1 = parteEntera (x+1) - 1


-- ACTIVIDAD 3
----------------------

esDivisible :: Int -> Int -> Bool
esDivisible x y 
    | x == y = True
    | x < y = False
    | otherwise = esDivisible (x-y) y


-- ACTIVIDAD 4
----------------------

sumaImpares :: Int -> Int
sumaImpares n
    | n == 1 = 1
    | otherwise = n*2 - 1 + (sumaImpares (n-1))


-- ACTIVIDAD 5
-----------------------

medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = medioFact (n-2) * n


-- ACTIVIDAD 6
-------------------------

sacarUltimo :: Integer -> Integer
sacarUltimo n = div n 10

sumaDigitos :: Integer -> Integer
sumaDigitos n 
    | n < 10 = n
    | n >= 10 = digitoUnidades n + sumaDigitos (sacarUltimo n)


-- ACTIVIDAD 7
---------------------------

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n
    | n < 10 = True
    | n >= 10 = todosDigitosIguales (sacarUltimo n) && digitoUnidades n == digitoDecenas n


sacarPrimero :: Integer -> Integer
sacarPrimero x = mod x (10 ^ (cantDigitos x -1))

-- ACTIVIDAD 8
---------------------------

cantDigitos :: Integer -> Integer
cantDigitos n
    | n == 0 = 0
    | otherwise = 1 + cantDigitos(sacarUltimo n)

iesimoDigitoDer :: Integer -> Integer -> Integer
iesimoDigitoDer n i
    | i == 1 = digitoUnidades n
    | i > 1 = iesimoDigitoDer (sacarUltimo n) (i-1)

iesimoDigitoIzq :: Integer -> Integer -> Integer
iesimoDigitoIzq n i = mod (div n (10^(cantDigitos n -i))) 10


-- ACTIVIDAD 9
------------------------------

capicua :: Integer -> Bool
capicua x = compararIesimos x 1

compararIesimos :: Integer -> Integer -> Bool
compararIesimos x i 
    | i == (cantDigitos x - i) + 1 = True
    | i == cantDigitos x - i = iesimoDigitoIzq x i == iesimoDigitoDer x i
    | otherwise = iesimoDigitoIzq x i == iesimoDigitoDer x i && compararIesimos x (i+1)

-- ACTIVIDAD 10
--------------------------------

-- a)
--f1 :: Integer -> Integer


-- ACTIVIDAD 11
--------------------------------

factorial :: Integer -> Integer
factorial 0 = 1
factorial 1 = 1
factorial n = n * factorial (n-1)

eAprox :: Integer -> Double
eAprox 0 = 1
eAprox n = 1.0 / fromIntegral (factorial n) + eAprox (n-1)

e :: Double
e = 2.7182818011463845


-- ACTIVIDAD 12
-----------------------------

raizDe2Aprox :: Integer -> Double
raizDe2Aprox n = (raizDe2AproxAux n) -1

raizDe2AproxAux :: Integer -> Double
raizDe2AproxAux 1 = 2.0
raizDe2AproxAux n = 2.0 + (1.0 / raizDe2AproxAux (n-1))


-- ACTIVIDAD 13
-----------------------------

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 0 _ = 0
sumatoriaDoble n m = sumatoriaSimple n m + sumatoriaDoble (n-1) m

sumatoriaSimple :: Integer -> Integer -> Integer
sumatoriaSimple _ 0 = 0
sumatoriaSimple i m = i ^ m + sumatoriaSimple i (m-1)


-- ACTIVIDAD 14
--------------------------------

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias _ 0 _ = 0
sumaPotencias q n m = sumatoriaPotencias q n m + sumaPotencias q (n-1) m

sumatoriaPotencias :: Integer -> Integer -> Integer -> Integer
sumatoriaPotencias _ _ 0 = 0
sumatoriaPotencias q n m = q ^ (n + m) + sumatoriaPotencias q n (m-1)


-- ACTIVIDAD 15
-----------------------------

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 0 _ = 0
sumaRacionales n m = sumatoriaRacionales n m + sumaRacionales (n-1) m

sumatoriaRacionales :: Integer -> Integer -> Float
sumatoriaRacionales _ 0 = 0
sumatoriaRacionales n m = (fromIntegral n / fromIntegral m) + sumatoriaRacionales n (m-1)


----------------- GUIA 5 ------------------------
-- ACTIVIDAD 1
------------------------------
-- 1)
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs
-- 2)
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs
-- 3)
principio :: [t] -> [t]
principio (x:[]) = []
principio (x:xs) = x : principio xs
-- 4)
reverso :: [t] -> [t]
reverso [] = []
reverso xs = ultimo xs : reverso (principio xs)


-- ACTIVIDAD 2
------------------------------

-- 1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) = x == y || pertenece x ys
-- 2)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:[]) = True
todosIguales (x:y:[]) = x == y
todosIguales (x:y:xs) = x == y && todosIguales (y:xs)
-- 3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:[]) = True
todosDistintos (x:xs) = not (pertenece x xs) && todosDistintos xs
-- 4)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs
-- 5)
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (y:ys)
    | x == y = ys
    | otherwise = y : quitar x ys
-- 6)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys) 
    | x == y = quitar x ys
    | otherwise = y : quitar x ys
-- 7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos x xs)
-- 8)
listaContenidaEn :: (Eq t) => [t] -> [t] -> Bool
listaContenidaEn [] _ = True
listaContenidaEn (x:xs) ys = pertenece x ys && listaContenidaEn xs ys

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos xs ys = listaContenidaEn xs ys && listaContenidaEn ys xs
-- 9)
listaCapicua :: (Eq t) => [t] -> Bool
listaCapicua xs = xs == reverso xs

-- ACTIVIDAD 3
--------------------------

-- 1)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs
-- 2)
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs
-- 3)
mayor :: Integer -> Integer -> Integer
mayor x y 
    | x >= y = x
    | otherwise = y

maximo :: [Integer] -> Integer
maximo (x:[]) = x
maximo (x:xs) = mayor x (maximo xs)
-- 4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (n+x) : sumarN n xs
-- 5)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)
-- 6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (xs) = sumarN (ultimo xs) xs
-- 7)
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs)
    | esPar x = x : pares xs
    | otherwise = pares xs
-- 8)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs)
    | esMultiplo x n = x : multiplosDeN n xs
    | otherwise = multiplosDeN n xs
-- 9)
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar xs = ordenar(quitar (maximo xs) xs) ++ [maximo xs]


-- ACTIVIDAD 4
------------------------

-- 1)
sacarEspaciosRepetidos :: [Char] -> [Char]
sacarEspaciosRepetidos [] = []
sacarEspaciosRepetidos (x:[]) = [x]
sacarEspaciosRepetidos (x:y:xs) 
    | x == ' ' && x == y = sacarEspaciosRepetidos (x:xs)
    | otherwise = x : sacarEspaciosRepetidos (y:xs)
-- 2)
sacarEspaciosInFin :: [Char] -> [Char]
sacarEspaciosInFin [] = []
sacarEspaciosInFin (x:xs)
    | x == ' ' = sacarEspacioFin xs
    | otherwise = sacarEspacioFin (x:xs)

sacarEspacioFin :: [Char] -> [Char]
sacarEspacioFin [] = []
sacarEspacioFin (x:[])
    | x == ' ' = []
    | otherwise = [x]
sacarEspacioFin (x:xs) = x: sacarEspacioFin xs

contarPalabras :: [Char] -> Integer
contarPalabras xs = 1 + contarEspacios (sacarEspaciosInFin (sacarEspaciosRepetidos xs))

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs)
    | x == ' ' = 1 + contarEspacios xs
    | otherwise = contarEspacios xs
-- 3)
palabras :: [Char] -> [[Char]]
palabras xs = palabrasAux (sacarEspaciosInFin (sacarEspaciosRepetidos xs))

palabrasAux :: [Char] -> [[Char]]
palabrasAux [] = []
palabrasAux xs = primerPalabra xs : palabrasAux(sacarPrimerPalabra xs)

primerPalabra :: [Char] -> [Char]
primerPalabra [] = []
primerPalabra (x:xs)
    | x == ' ' = []
    | otherwise = x : primerPalabra xs

sacarPrimerPalabra :: [Char] -> [Char]
sacarPrimerPalabra [] = []
sacarPrimerPalabra (x:xs)
    | x == ' ' = xs
    | otherwise = sacarPrimerPalabra xs
-- 4)
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = palabraMasLargaAux (sacarEspaciosInFin (sacarEspaciosRepetidos xs))

palabraMasLargaAux :: [Char] -> [Char]
palabraMasLargaAux [] = []
--palabraMasLargaAux xs = 


-- ACTIVIDAD 5
----------------------------

-- 2)
{-esPrimo :: Integer -> Bool
esPrimo 1 = False
esPrimo n = menorDivisor x == x

-- vos imaginate que anda
menorDivisor :: Integer -> Integer
menorDivisor n = buscaDivisor n 2

buscaDivisor :: Integer ->

descEnPrimos :: Integer -> [Integer]
descEnPrimos n = primosDivisores 2 n

primosDivisores :: Integer -> Integer -> [Integer]
primosDivisores d n 
    | esPrimo n = [n]
    | esPrimo d && mod n d == 0 = d : primosDivisores d (div n d)
    | otherwise = primosDivisores (d+1) n

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = [[]]
descomponerEnPrimos (x:xs) = descEnPrimos x : descomponerEnPrimos xs-}

