message=input("enter the message :")
words=message.split(" ")
coding=False
if(coding):
    nword=[]
    for word in words:
        if (len(words)>=3):
            a = "pqr"
            b = "xyz"
            value = a + (word[1:]) + (word[0]) + b
            nword.append(value)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))
else:
    nword=[]
    for word in words:
        if (len(words)>=3):
            value = (word[-1]) + (word[:-1])
            nword.append(value)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))