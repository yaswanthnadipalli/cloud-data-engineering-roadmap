'''
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
    '''
import csv
from collections import defaultdict

# Step 1: Create the CSV file
with open("people.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Country"])
    writer.writerow(["Alice", 30, "USA"])
    writer.writerow(["Bob", 25, "Canada"])
    writer.writerow(["Charlie", 35, "UK"])
    writer.writerow(["Diana", 28, "India"])

# Step 2: Read and display contents
print("CSV Contents:")
with open("people.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Step 3: Print names of people older than 28
print("\nPeople older than 28:")
with open("people.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Age"]) > 28:
            print(row["Name"])

# Step 4: Count people from each country
country_count = defaultdict(int)
with open("people.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        country = row["Country"]
        country_count[country] += 1

print("\nPeople per country:")
for country, count in country_count.items():
    print(f"{country}: {count}")
