
nubSorted :: Ord a => [a] -> [a]
nubSorted [] = []
nubSorted (x:xs)
  | x:xs == reverse (x:xs) = x:xs
  | elem x xs == True = nubSorted (xs)
  | otherwise = x:nubSorted (xs) 