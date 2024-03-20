
p1 = "Juan"
p2 = "Sol"
p3 = "Jose"
p4 = "Luz"
p5 = "Mica"
test1 = [(p1, p1), (p2, p3), (p3, p4), (p1, p3)]
test2 = [(p2, p4), (p1, p3), (p4, p2), (p1, p4)]
test3 = [(p1, p2), (p1, p3), (p4, p2), (p3, p4)]
test4 = [(p1, p2), (p1, p3), (p4, p2), (p3, p4), (p5, p1), (p3, p5)]

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas (x:xs) = fst x /= snd x && not (pertenece x xs) && not (pertenece (tuplaInversa x) xs) && relacionesValidas xs

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = e == x || pertenece e xs

tuplaInversa :: (t1, t2) -> (t2, t1)
tuplaInversa (a, b) = (b, a)

personas :: [(String, String)] -> [String]
personas xs = quitarRepetidos (listarPersonas xs)

listarPersonas :: [(String, String)] -> [String]
listarPersonas [] = []
listarPersonas ((p1,p2):xs) = p1 : p2 : listarPersonas xs

eliminar :: (Eq t) => t -> [t] -> [t]
eliminar _ [] = []
eliminar e (x:xs)
    | e == x = eliminar e xs
    | otherwise = x : eliminar e xs

quitarRepetidos :: (Eq t) => [t] -> [t]
quitarRepetidos [] = []
quitarRepetidos (x:xs)
    | pertenece x xs = x : quitarRepetidos (eliminar x xs)
    | otherwise = x : quitarRepetidos xs

amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe e (x:xs)
    | estaEnTupla e x = devolverAmigue e x : amigosDe e xs
    | otherwise = amigosDe e xs

estaEnTupla :: (Eq t) => t -> (t, t) -> Bool
estaEnTupla e (a,b) = e == a || e == b

devolverAmigue :: (Eq t) => t -> (t, t) -> t
devolverAmigue e (a, b)
    | e == a = b
    | e == b = a

personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos xs = compararApariciones (personas xs) (listarPersonas xs)

compararApariciones :: (Eq t) => [t] -> [t] -> t
compararApariciones [x] _ = x
compararApariciones (x:y:xs) rs
    | contarApariciones x rs >= contarApariciones y rs = compararApariciones (x:xs) rs
    | contarApariciones x rs < contarApariciones y rs = compararApariciones (y:xs) rs

contarApariciones :: (Eq t) => t -> [t] -> Integer
contarApariciones _ [] = 0
contarApariciones e (x:xs)
    | e == x = 1 + contarApariciones e xs
    | otherwise = contarApariciones e xs