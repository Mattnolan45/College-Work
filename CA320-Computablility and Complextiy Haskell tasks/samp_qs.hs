import Data.Char

isPower :: Int -> Bool

isPower 0 = False
isPower 1 = True
isPower x
  | (power2 x 2) == True = True
  | otherwise = False

power2 :: Int-> Int -> Bool

power2 2 n = True
power2 x n
  | x == n = True
  | x > n = power2 x (n*2) 
  | otherwise = False

isPower2 :: Int -> Bool

isPower2 0 = False
isPower2 1 = True

isPower2 n 
  | n `mod`2 == 0 = isPower2(n`div`2)
  | otherwise = False

isFactorial :: Int -> Bool
isFactorial n = isFactorial' 1 n


isFactorial' x n
 | x==n = True
 | n `mod` x /= 0 = False
 | otherwise = isFactorial' (x+1) (n `div` x)





sort2 :: Ord a=> [a] -> [a] ->[a]
sort2 [] v = v
sort2 b v = sort3 b (v++[minimum b])

sort3 :: Ord a => [a] -> [a] -> [a]
sort3 [] v = v
sort3 (x:xs)
  | x /= tail v = x: sort3 xs v
  | x == tail v = sort3 xs v
  | otherwise = sort2 (x:xs) v


  