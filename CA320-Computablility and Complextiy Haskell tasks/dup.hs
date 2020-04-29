dup :: Eq a => [a] -> Bool

dup [] = False
dup [a] = False
dup (x:xs)
  | elem x xs == True = True
  | otherwise = dup xs 



