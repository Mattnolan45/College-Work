delFirst :: Eq a => a -> [a] -> [a]

delFirst x [] = []
delFirst a (x:xc)  
	| a == x = xc
	| otherwise = x : delFirst a xc