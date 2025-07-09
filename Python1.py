#1. Write a Python program to print "Hello, World!".
print("\"Hello World!\"")
#2. Create a program that takes input from the user and prints it in reverse.
word=input("Enter Name you want to reverse: ")
print("The Reverse of the word ", word ,"is : ",word[::-1])
#3. Write a function that returns the factorial of a number.
num1=int((input("Enter number you want to find factorial of : ")))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print("The Factorial of",num1," is: ",factorial(num1))
#4. Write a script to swap two variables without using a third variable.
num2=int((input("Enter first number : ")))
num3=int((input("Enter second number : ")))
def swap(num2,num3):
    num2=num2+num3
    num3=num2-num3
    num2=num2-num3
    return num2,num3
print("The Given number sequence is ",num2,num3," and the swapped value is ",swap(num2,num3))
#Create a list of even numbers from 1 to 100.
even_numbers=[]
for i in range (1,101):
    if i % 2 == 0:
        even_numbers.append(i)
print("Even numbers from 1 to 100 is : ",even_numbers)
#6. Write a program that counts the number of vowels in a string.
word=input("Enter a word: ")
vowels="aeiouAEIOU"
count=0
for i in range(len(word)):
    if word[i] in vowels:
        count=count+1
print("The count of vowels is: ",count)
#7. Write a script to check if a string is a palindrome.
word=input("Enter a word: ")
reversed_word=word[::-1]
if word==reversed_word:
    print("The word is Palindrome : ",reversed_word)
else:
    print("The word is not Palindrome : ",reversed_word)
#8. Write a program to calculate the sum of all numbers in a list.
list=list(input("Enter a list of numbers : "))
sum=0
for i in list:
    sum=sum+i
print("The sum of the numbers in list is : ",sum)
#9. Write a function that returns the maximum of three numbers.
num4=int((input("Enter first number : ")))
num5=int((input("Enter second number : ")))
num6=int((input("Enter third number : ")))
print("The highest number is : ",max(num4,num5,num6))
#10. Create a calculator that performs +, -, *, / using functions.
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
num7=int((input("Enter first number : ")))
num8=int((input("Enter second number : ")))
print("The addition is : ",add(num7,num8),"The subtraction is : ",subtract(num7,num8))
print("The multiplication is : ",multiply(num7,num8),"The division is : ",divide(num7,num8))
#11. Create a dictionary of student names and their marks. Print names with marks above 80.
names=[]
student={
    "Roshan":89,"Samir":99,"Bijay":60,"Bibhu":98
}
for name,marks in student:
    if marks>80:
        names.append(name)
print("The students who has marks greater than 80 are : ",names)
#12. Write a class `Rectangle` with methods to calculate area and perimeter.
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return self.width+self.height
width=int(print("Enter width of Rectangle : "))
height=int(print("Enter height of Rectangle : "))
Rectangle1=Rectangle(width,height)
Print("The area of the Rectangle is: ",Rectangle1.area())
Print("The perimeter of the Rectangle is: ",Rectangle1.perimeter())




