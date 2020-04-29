import Data.Char

hextodec :: String -> Int
hextodec h = hextodec2 h 0



hextodec2 :: String -> Int -> Int
hextodec2 "" v = v
hextodec2 (d:ds) v = hextodec2 ds (16*v+digittodec d)

digittodec d
  | elem d['A'..'F'] = ord d - ord 'A' +10
  | elem d['0'..'9'] = ord d - ord '0'
