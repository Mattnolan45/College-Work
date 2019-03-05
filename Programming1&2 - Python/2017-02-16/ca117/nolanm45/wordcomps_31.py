import sys
lines=[line.strip() for line in sys.stdin.read().split()]

print("Words containing 17 letters:",[w.strip() for w in lines if len(w)==17])
print("Words containing 18+ letters:",[w.strip() for w in lines if len(w)>=18])
print("Shortest word containing all vowels:",min([w.strip() for w in lines if set("aeiou").issubset(w.lower())],key=len))
print("Words with 4 a's:",[w.strip() for w in lines if w.lower().count("a")==4])
print("Words with 2+ q's:",[w.strip() for w in lines if w.lower().count("q")>=2])
print("Words containing cie:",[w.strip() for w in lines if "cie" in w])
print("Anagrams of angle:",[w.strip() for w in lines if sorted("angle")==sorted(w.strip().lower()) and w.strip()!="angle"])
print("Words ending in iary:",len([w.strip() for w in lines if w.endswith("iary")]))
print("Words with q but no u:",[w.strip() for w in lines if w.lower().count("q")>0 and w.lower().count("qu")==0])

e_max=[word for word in sorted(lines, key=lambda word: word.count("e"), reverse=True)][0].count("e")

print("Words with most e's:",[w.strip() for w in lines if w.lower().count("e")==e_max])


