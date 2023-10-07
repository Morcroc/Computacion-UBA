digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10

digitoDecenas :: Integer -> Integer
digitoDecenas n = div (mod n 100) 10

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
    | otherwise = n*2 - 1 + sumaImpares (n-1)


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
sumatoria :: (Integer -> Integer) -> Integer -> Integer -> Integer
sumatoria f n i 
    | n < i = 0
    | otherwise = f n + sumatoria f (n-1) i

f1 :: Integer -> Integer
f1 n = sumatoria (2 ^)  n 0

f2 :: Integer -> Integer -> Integer
f2 n q = sumatoria (q ^) n 1

f3 :: Integer -> Integer -> Integer
f3 n q = sumatoria (q ^) (2*n) 1

f4 :: Integer -> Integer -> Integer
f4 n q = sumatoria (q ^) (2*n) n


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
raizDe2Aprox n = raizDe2AproxAux n -1

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


-- ACTIVIDAD 16
------------------------------
-- a)
-- Quiero el numero mas chiquito posible que divida a n
menorDivisor :: Integer -> Integer
menorDivisor n = buscarDivisor n 2

buscarDivisor :: Integer -> Integer -> Integer
buscarDivisor n i
    | mod n i == 0 = i
    | otherwise = buscarDivisor n (i+1)

-- b)
esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

-- c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = mcd n m == 1

mcd :: Integer -> Integer -> Integer
mcd n m = algoDeEuclides n m

algoDeEuclides:: Integer -> Integer -> Integer
algoDeEuclides a b 
    | b == 0 = a
    | otherwise = algoDeEuclides b (mod a b)

-- d)
--nEsimoPrimo :: Integer -> Integer


