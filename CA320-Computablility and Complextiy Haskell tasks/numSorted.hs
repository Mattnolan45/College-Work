numSorted :: Ord a => a -> [a] -> Int

numSorted x [] = 0
numSorted x (y:ys) 
 | x < y = 0
 | x==y = 1+(numSorted x ys)
 | otherwise = numSorted x ys
