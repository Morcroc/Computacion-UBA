module Solucion where

-- 1)
golesDeNoGoleadores :: [(String, String)] -> [Int] -> Int  -> Int
golesDeNoGoleadores [] [] t = t
golesDeNoGoleadores (j:js) (g:gs) t = golesDeNoGoleadores js gs (t-g)


-- 2)
equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = True
equiposValidos (j:js) = equiposValidosAux j js && equiposValidos js

equiposValidosAux :: (String, String) -> [(String, String)] -> Bool
equiposValidosAux _ [] = True 
equiposValidosAux (c1,j1) ((c2,j2):js) = c1 /= j1 && c1 /= c2 && j1 /= j2 && j1 /= c2 && c1 /= j2 && equiposValidosAux (c1, j1) js



-- 3)
porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles j js gs = division (golesDelJugador j js gs) (totalGoles gs)

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

golesDelJugador :: String -> [(String,String)] -> [Int] -> Int
golesDelJugador j ((a,b):js) (g:gs) 
    | j == b = g
    | otherwise = golesDelJugador j js gs

totalGoles :: [Int] -> Int
totalGoles [] = 0
totalGoles (x:xs) = x + totalGoles xs

-- 4)
botinDeOro :: [(String, String)] -> [Int] -> String
botinDeOro [] [] = ""
botinDeOro ((a,b):[]) _ = b
botinDeOro (j:k:js) (g:h:gs)
    | g >= h = botinDeOro (j:js) (g:gs)
    | otherwise = botinDeOro (k:js) (h:gs)

