import Data.Char
octtodec :: String -> Int

octtodec n = octtodec2 n 0

octtodec2 :: String -> Int -> Int

octtodec2 "" r = r
octtodec2 (x:xs) r  
  |length xs /=1 = octtodec2 xs (r+digitToInt x)*8
  | otherwise =  octtodec2 xs (r+digitToInt x)
