s=raw_input()
is_palindrome = "true"
i=0


while i<len(s):
   is_palindrome = is_palindrome and s[i] == s[len(s)-1-i]
   i=i+1
 
if is_palindrome:
   print s


