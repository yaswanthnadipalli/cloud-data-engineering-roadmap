
#A function to check whether a string is a palindrome.

def is_palindrome(str):
    if str==str[::-1]:
        return True
    return False

str=input().lower()
if is_palindrome(str):
    print("The String is palindrme")
else:
    print("The String is not palindrme")

# A function to return the second largest number in a list.

def second_largest(numlist):
    numlist.sort()
    return numlist[-2]

numlist=list(map(int,input().split()))
print(second_largest(numlist))

# A function to calculate the GCD of two numbers.

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
a = 20
b = 28
print(gcd(a, b))

#Create a list of squares from 1 to 20.
sqlist=[]
for i in range(1,21):
    sqlist.append(i*i)
  
print(sqlist)

#Create a list of even numbers from a given list.
numlist=list(map(int,input().split()))
evenlist=[]
for i in range(len(numlist)):
    if numlist[i]%2==0:
        evenlist.append(numlist[i])
print(evenlist)


#Extract words longer than 4 characters from a sentence.

sentence=input()
wordlist=sentence.split()
maxlist=[]
for word in wordlist:
    if len(word)>4:
        maxlist.append(word)
print(maxlist)

# File I/O Basics
file=open("sample.txt","w")
for i in range(5):
    file.write(input())
    file.write("\n")
file.close()

file1=open("sample.txt","r+")
print(file1.read())

word_count = 0
with open("sample.txt", "r") as file:
    content = file.read()
    words = content.split()  # Splits the string by whitespace into a list of words
    word_count = len(words)
print(word_count)

# Write a program to flatten a 2D list

my2dlist=[[1,2,3],[4,5],[6]]
list=[]
for sublis in my2dlist:
    for num in sublis:
        list.append(num)
print(list)
    