bintodec :: String -> Int

bintodec b = bintodec2 b 0

bintodec2 :: String -> Int -> Int

bintodec2 [] v = v
bintodec2 ('1':bs) v = bintodec2 bs(2*v+1)
bintodec2 ('0':bs) v = bintodec2 bs(2*v)