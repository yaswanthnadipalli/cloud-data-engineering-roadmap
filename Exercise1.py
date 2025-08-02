
#reversing a string
s=input()
print(s[::-1])

#counting vowels in a string 

str=input()
str=str.lower()
c=0
for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c+=1
print(c)


#sum of the elements in the list

numlist=[]
numlist=list(map(int,input().split()))
print(numlist)
sum=0
for j in range(0,len(numlist)):
    sum+=numlist[j]
print(sum)


#mi and ma of the list
numlist=[]
numlist=list(map(int,input().split()))

mi=numlist[0]
ma=numlist[0]

for i in range(len(numlist)): # range(len(numlist)) is equivalent to range(0, len(numlist))
    if numlist[i] < mi:  # If current element is smaller than current minimum
        mi = numlist[i]
    if numlist[i] > ma:  # If current element is larger than current maximum
         ma = numlist[i]
print(mi,ma)
    

#Frequency of elements using a dictionary
items=[]
items=input().split()
freq={}
print(items)
for item in items:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
print(freq)

# a function that returns factorial of a number using recursion
def fact(n):
    if n==0:
        return 1
    elif n>0:
        return n*fact(n-1)
n=int(input())
result=fact(n)
print(result)
