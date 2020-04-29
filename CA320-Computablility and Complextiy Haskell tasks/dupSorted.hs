dupSorted :: Ord a => [a] -> Bool

dupSorted [] = False
dupSorted (x:xs) = (numSorted x xs) 

numSorted :: Ord a => a -> [a] -> Bool

numSorted x [] = False
numSorted x (y:ys) 
  | x > y = False
  | x == y = True
  | otherwise = numSorted y ys
