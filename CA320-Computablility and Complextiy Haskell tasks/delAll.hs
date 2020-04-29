delAll :: Eq a => a -> [a] -> [a]

delAll x [] = []
delAll a (x:xc)  
	| a == x = delAll a xc
	| otherwise = x : delAll a xc