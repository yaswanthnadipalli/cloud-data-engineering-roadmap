
#even odd counter
numlist=list(map(int,input().split()))
ec=0
oc=0
for i in range(len(numlist)):
    if numlist[i]%2==0:
        ec+=1
    else:
        oc+=1
print("Total Even numbers on the list:",ec)
print("Total Odd numbers on the list:",oc)
#prime number in the range of n
def is_prime(n)->bool:
    if n<2:
        return False
    for j in range(2,n):
        if n%j==0:
            return False
    return True
num=int(input())

for i in range(num):
    if is_prime(i):
        print(i)


# removing duplicates using sets 
num2list=list(map(int,input().split()))
unique_list=set(num2list)
print(unique_list)

# finding most frequnt number using dictionary
num3list=list(map(int,input().split()))
dict={}
for i in range(len(num3list)):
    if num3list[i] in dict:
        dict[num3list[i]]+=1
    else:
        dict[num3list[i]]=1
maxfreq=0
maxfreqval=None

for val in dict:
    if dict[val]>maxfreq:
        maxfreq=dict[val]
        maxfreqval=val
print("Mpst Frequent Value :",maxfreqval)




#fibonacci series
n=int(input())
fib=[0]*n
fib[0]
fib[1]=1
for i in range(2,n):
    fib[i]=fib[i-1]+fib[i-2]
print(fib)

# reverse the words in the sentence

sentence=input()
s=""
wordlist=sentence.split()

for word in wordlist:
    s=word+" "+s
print(s)
