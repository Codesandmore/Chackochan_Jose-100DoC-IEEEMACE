alphabets=list('abcdefghijklmnopqrstuvwxyz')
word=input("Enter the string:")
letter=''
for i in word:
    k=i.lower()
    if k in alphabets:
        h=str(alphabets.index(k)+1)
        letter=letter+h+''
    else:
        continue
print(letter)        
        