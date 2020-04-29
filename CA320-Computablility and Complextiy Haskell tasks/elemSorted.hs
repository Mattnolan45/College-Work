elemSorted :: Int -> [Int] -> Bool

elemSorted a [] = False
elemSorted a (x:xs)
 | a < x = False
 | a == x = True
 | otherwise = elemSorted a xs