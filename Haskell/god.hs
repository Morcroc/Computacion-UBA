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
-- :: Integer -> Integer
