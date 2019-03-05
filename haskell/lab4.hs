import Data.Char(toUpper)

myProduct :: [Int] -> Int

myProduct [] = 1
myProduct [x] = x
myProduct (x:xs) = x*myProduct(xs)

stringToUpper :: String -> String

stringToUpper "" = ""
stringToUpper (x:xs) = toUpper x : stringToUpper xs

shortest :: [[a]] -> [a]

shortest [] = []
shortest [x] = x
shortest (x:xs)
  | length x < length(shortest xs) = x
  | otherwise = shortest xs

isPalindrome :: Eq a => [a] -> Bool

isPalindrome x = if x == reverse x
  then True
  else False 

sumPoly :: [Int] -> [Int] -> [Int]

sumPoly [] [] = []
sumPoly x [] = x
sumPoly (x:xs) (y:ys) = (x+y) : sumPoly xs ys

evalPoly :: Int -> [Int] -> Int

evalPoly n [] = 0
evalPoly n (x:xs) = x + n * evalPoly n xs