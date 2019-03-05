import sys
lines=sys.stdin.readlines()

print("Words containing 17 letters:",[w.strip() for w in lines if len(w)==18])
print("Words containing 18+ letters:",[w.strip() for w in lines if len(w)>18])
print("Shortest word containing all vowels:",min([w.strip() for w in lines if set("aeiou").issubset(w.lower())],key=len))
print("Words with 4 a's:",[w.strip() for w in lines if w.lower().count("a")==4])
print("Words with 2+ q's:",[w.strip() for w in lines if w.lower().count("q")>=2])
print("Words containing cie:",[w.strip() for w in lines if "cie" in w])
print("Anagrams of angle:",[w.strip() for w in lines if sorted("angle")==sorted(w.strip().lower()) and w.strip()!="angle"])
print("Words ending in iary:",len([w.strip() for w in lines if "iary" in w]))
print("Words with q but no u:",[w.strip() for w in lines if ("q" in w.lower() and "u" not in w.lower())])

highest=0
for s in lines: 
     s=s.count("e")
     if s>highest:
           highest=s

print("Words with most e's:",[w.strip() for w in lines if w.count("e")== highest])	
