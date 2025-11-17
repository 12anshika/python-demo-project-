print("hello")

a = 10 
b = 20
print(a // b)

i = 1
while i<=5:
    if(i == 3):
        break
    else:
        print(i)
    i+=1;    


i=1
while i<=7:
    if(i == 5):
        continue
    else:
        print(i)
    i+=1;    


a = 10
b = 20

temp = a
a = b
b = temp

print(a,b)


a=[1,2,3,4,5]
i=0
while i<len(a):
    print(a[i])
    i+=1
else:
    print("end")



a=10
b=20
c=a+b
print(c)

for char in "loop":
    if char == 'o':
        continue
    print(char,end=" ")


total =  0
for i in [10,20,30,40,50]:
    if total > 30:
        break
    total += i
print(total)     


#list 1 dim

list = [1,3,'anshika','manya']
print(list)

# 2 dim
l1=[[1,2],['red','green']]
print(l1)


# list conversion 

a="this is a list"
l = list(a)
print(l)




 # Reverse of a number 

num = int(input("Enter a number: "))
temp = num     
rev = 0

while temp > 0:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp = temp // 10

print("Original number is:", num)
print("Reversed number is:", rev)


# Check if a number is palindrome 

num = int(input("Enter a number: "))
temp = num     
rev = 0

while temp > 0:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp = temp // 10

print("Original number is:", num)
print("Reversed number is:", rev)

if num == rev:
    print("It is palindorm")
else:
    print("its not")


# Find factorial of a number

num = int(input("Enter a number: "))
fact = 1   #why we are given fact 1 bcs fact = 0 is 1 so we can't give the fact to 0 its start ftom 1
temp = num

while temp > 0:
    fact = fact * temp
    temp = temp - 1

print("Factorial of", num, "is:",fact)



