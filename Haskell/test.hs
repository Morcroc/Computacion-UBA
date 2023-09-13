absoluto :: Integer -> Integer
absoluto n
    | n >= 0 = n
    | n < 0 = - n

maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y
    | absoluto x >= absoluto y = x
    | absoluto x < absoluto y = y

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z
    | x >= y && x >= z = x
    | y >= x && y >= z = y
    | z >= x && z >= y = z