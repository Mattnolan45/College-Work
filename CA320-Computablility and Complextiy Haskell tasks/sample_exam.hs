import Data.Char(toUpper)

string2upper :: String -> String

string2upper "" = ""
string2upper (x:s)  = [(toUpper x)] ++ (string2upper s)

delFirst :: Eq a => a -> [a] -> [a]

delFirst a [] = []
delFirst a (x:xs) 
  | a == x = xs
  | otherwise = x : delFirst a xs

numSorted :: Ord a => a -> [a] -> Int

numSorted a [] = 0
numSorted a (x:xs)
  | a == x = 1+(numSorted a xs)
  | otherwise = numSorted a xs

repAll :: Eq a => a -> a -> [a] -> [a]

repAll a b [] = []
repAll a b (x:xs)
  | a == x = b : repAll a b xs
  | otherwise = x : repAll a b xs