import string
def bs(l1):
    slide=[]
    for i in range(len(l1)):
        if(l1[i].islower()):
            k=alpha.index(l1[i])
            j=k-l
            slide.append(alpha[j])
        else:
            slide.append(l1[i])
    s=''.join(map(str,slide))
    print (s)
print ("Enter number of skipping sequences you wanna generate")             
t=int(input())
l1=[]
s=''
alpha=[]
for letter in string.ascii_lowercase:
    alpha.append(letter)

for i in range(t):
    print ("the input alphabets in string "+str(i+1))
    s=input()
    l1=list(s)
    l=len(l1)
    bs(l1)
