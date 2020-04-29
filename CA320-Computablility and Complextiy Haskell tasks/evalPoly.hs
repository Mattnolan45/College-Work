evalPoly :: Int -> [Int] -> Int
evalPoly x [] = 0
evalPoly x (h:t) = h + x * (evalPoly x t)