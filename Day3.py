def eliminateVowles(word:str)->str:
  vowels=['A','E','I','O','U','a','e','i','o','u']
  res=[]
  for i in range(0,len(word)):
    if word[i] not in vowels:
      res.append(word[i])
  final=''.join(res)
  return final

#ex
word="Lets-Upgrade"
a=eliminateVowles(word)
print(a)
#Lts=pgrd
