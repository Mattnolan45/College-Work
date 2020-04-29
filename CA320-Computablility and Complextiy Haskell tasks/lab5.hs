
delFirst :: Eq a => a -> [a] -> [a]

delFirst a [] = []
delFirst a (x:xs)
  | a == x = xs
  | otherwise = x : delFirst a xs

delAll :: Eq a => a-> [a] ->[a]

delAll a [] = []
delAll a (x:xs)
  | a == x = delAll a xs
  | otherwise = x : delAll a xs

num :: Eq a => a -> [a] -> Int

num a [] = 0
num a (x:xs)
  | a == x = 1+(num a xs)
  | otherwise = num a xs

numSorted :: Ord a => a -> [a] -> Int

numSorted a [] = 0
numSorted a (x:xs) 
  | a < x = 0
  | a == x = 1 + (numSorted a xs)
  | otherwise = numSorted a xsc

repFirst :: Eq a => a -> a-> [a] -> [a]

repFirst a b []  = []
repFirst a b (x:xs)
  | a == x = b:xs
  | otherwise = x:repFirst a b xs

repAll :: Eq  a => a -> a -> [a] -> [a]

repAll a b [] = []
repAll a b (x:xs)
  | a == x = repAll a b (b:xs)
  | otherwise = x : repAll a b xs

elemSorted :: Ord a => a -> [a] -> Bool

elemSorted a [] = False
elemSorted a (x:xs)
  | a < x = False
  | a == x = True
  | otherwise = elemSorted a xs

nubSorted :: Ord a => [a] -> [a] 

nubSorted [] = []
nubSorted (x:xs) 
  | (numSorted x xs) < 1 = x : nubSorted xs 
  | otherwise = nubSorted xs


dupSorted :: Ord a => [a] -> Bool

dupSorted [] = False
dupSorted (x:xs) = (numbool x xs) 

numbool :: Ord a => a -> [a] -> Bool

numbool x [] = False
numbool x (y:ys) 
  | x > y = False
  | x == y = True
  | otherwise = numbool y ys

dup :: Eq a => [a] -> Bool

dup [] = False
dup [a] = False
dup (x:xs)
  | elem x xs == True = True
  | otherwise = dup xs 



