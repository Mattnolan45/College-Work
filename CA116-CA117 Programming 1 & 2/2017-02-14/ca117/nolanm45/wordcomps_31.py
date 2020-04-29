import sys
lines=sys.stdin.readlines()

print("Words containing 17 letters:",[w.strip() for w in lines if len(w)==18])
print("Words containing 18+ letters:",[w.strip() for w in lines if len(w)>18])
print("Shortest word containing all vowels:",min([w.strip() for w in lines if set("aeiou").issubset(w.lower())],key=len))
print("Words with 4 a's:",[w.strip() for w in lines if w.lower().count("a")==4])
print("Words with 2+ q's:",[w.strip() for w in lines if w.lower().count("q")>=2])
print("Words containing cie:",[w.strip() for w in lines if "cie" in w])
print("Anagrams of angle:",[w.strip() for w in lines if str(w.lower()).sort()=="angle".sort()])
print("Words ending in iary:",len([w.strip() for w in lines if "iary" in w]))
print("Words with q but no u:",[w.strip() for w in lines if ("q" in w.lower() and "u" not in w.lower())])
#print("Words with most e's:",[w.strip()


