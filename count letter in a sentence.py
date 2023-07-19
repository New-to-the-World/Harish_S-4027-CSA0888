s=str(input("Enter the sentence: "))
n=len(s)
i=0
count=0
for i in range(0,n,1):
    if s[i]=='A':
        count+=1
print("Count: ",count)
    
