def vowelCount(s):
 count=0
 for x in range(0,len(s)):
  if s[x]=='a' or s[x] == 'e' or s[x] == 'i' or s[x] == 'o' or s[x] == 'u':
   count=count+1
 print(count)