type Configuration = (Int, String, String)
type Transitiion = ((Int, String, String), (Int, String))
type PDA = (Int, [Int], [Transitiion])

data Result = Accept | Reject deriving Show

getNewConfigs :: Configuration -> [Transitiion] -> [Configuration] -> [Configuration]
getNewConfigs c [] cs = cs
getNewConfigs (a, "", c) tr cs = cs
getNewConfigs (a, b, c) (t:tr) cs = getNewConfigs (a,b,c) tr (cs ++ (step(a,b,c)t))


step :: Configuration -> Transitiion -> [Configuration]

step (a,b,"") ((d,"",""),(g,""))
  | a == d = [(g,b,"")]
  | otherwise = []


step (a, b, "") ((d, "", ""),(g, [h]))
  | a == d = [(g, b, [h])]
  | otherwise = []


step (a, (b:bs), "") ((d, [e], ""), (g, ""))
  | a == d && b == e = [(g, bs, "")]
  | otherwise = []



step (a,(b:bs),"") ((d,[e],""),(g,[h]))
  | a == d && b == e = [(g, bs, [h])]
  | otherwise = []



step (a,b,c) ((d,"",""),(g,""))
  | a == d = [(g, b, c)]
  | otherwise = []


step (a,b,c) ((d,"",""),(g,[h]))
  | a == d = [(g, b, (h:c))]
  | otherwise = []


step (a,b,(c:cs)) ((d,"",[f]),(g,""))
  | a == d && c == f = [(g, b, cs)]
  | otherwise = []


step (a,b,(c:cs)) ((d,"",[f]),(g,[h]))
  | a == d && c == f = [(g, b, (h:cs))]
  | otherwise = []



step (a,(b:bs),c) ((d,[e],""),(g,""))
  | a == d && b == e = [(g, bs, c)]
  | otherwise = []



step (a,(b:bs),c) ((d,[e],""),(g,[h]))
  | a == d && b == e = [(g, bs, h:c)]
  | otherwise = []


step (a,(b:bs),(c:cs)) ((d,[e],[f]),(g,""))
    | a == d && b == e && c == f = [(g, bs, cs)]
    | otherwise = []



step (a,(b:bs),(c:cs)) ((d,[e], [f]), (g, [h]))
    | a == d && b == e && c == f = [(g, bs, (h:cs))]
    | otherwise = []


step (a,b,"") ((d,[e],[f]),(g,"")) = []
step (a,b,"") ((d,"",[f]),(g,"")) = []
step (a,b,"") ((d,[e],[f]),(g,[h])) = []
step (a,b,"") ((d,"",[f]),(g,[h])) = []


endState :: Configuration -> [Int] -> Bool
endState (a,b,c) [] = False
endState (a,b,c) (x:xs)
  | a == x && b == "" && c == "" = True
  | otherwise = endState (a,b,c) xs


runPrime :: PDA -> [Configuration] -> Result
runPrime (start, end, transition) [] = Reject
runPrime (start, end, transition) (head:tail)
  | endState head end == True = Accept
  | otherwise = runPrime(start, end, transition) (tail ++ (getNewConfigs head transition []))


run :: PDA -> String -> Result
run (start, end, transition) "" = Accept
run (start, end, transition) str  = runPrime (start, end, transition) [(start, str, "")]