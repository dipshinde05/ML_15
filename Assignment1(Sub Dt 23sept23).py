#!/usr/bin/env python
# coding: utf-8

#  ##                                                          Assignment 1

# ### Exercise 1: Print First 10 natural numbers using while loop\n

# ### 

# In[1]:


#here we use while loop for printing 10 natural numbers.
# so for getting 10 natural numbers we have give 11 as end range because while loop exclude end range.

i = 1
while i<11:
    print(i)
    i=i+1


# ### 

# ###
# ### Exercise 2: Print the following pattern:  
# #### 1111\n
# #### 111\n
# #### 11\n
# #### 1\n

# In[2]:


# for printing the pattern we have to use for loop 
# as a given condition we have to take 4 to 0 range in reverse order

for i in range(4, 0, -1):  # this for loop is for rows 
    for j in range(4, i, -1):  # Print spaces in between values 
        print(" ", end="")
    for k in range(i):  # Inner loop for numbers
        print("1", end="")
    print()  # Move to the next line after each row


# ### 

# ### Exercise 3: Calculate the sum of all numbers from 1 to a given number\n

# ### 

# In[3]:


# taking user input number to calculate sum 

num = int(input("Enter number: "))

# here we assign total named variable to calculate sum of user input number.
# by using sum and range function we calculate sum of numbers.

total= sum(range(1,num+1))

#below we print the sum of all number given by user from 1

print("Sum of given number ", num , "from 1 to end is", total)


# ### 

# ###  Exercise 4: Write a program to print multiplication table of a given number

# In[1]:


# Input the number by user which user want to print the multiplication table
number = int(input("Enter a number: "))

# Print the multiplication table and we use format function here "f " means format
print(f"Multiplication table for {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")


# ### 

# ### Exercise 5: Display numbers from a list using loop\n

# In[10]:


# To display numbers from list create a list with elements


lst = [5,8,9,7,3,6,1,2.5,3.5,6.01,'ghg']

#now create a for loop to execute every element of list from index 0 to length of list

for i in range(0, len(lst)):
    
    print(lst[i])


# ### 

# ### Exercise 6: Count the total number of digits in a number\n

# In[22]:


# here we take input from user as integer to calculate no of digit
num = int(input("Enter a number: "))

#to calculate no of digits of number we have to convert it in to string bcoz integer does not support len function.
num_str = str(num)

#now count digits of a number by using len() method
num_digits = len(num_str)

# using format we print digits of number
print("Total number of digits in {} are {}".format(num, num_digits))


# ### 

# ### Exercise 7: Print the following pattern : Diamond shape

# In[38]:


# Get the number of rows for the diamond mostly try it would be an odd number
n = int(input("Enter the number of rows for the diamond: "))

# let we have to ensure that the number of rows is odd if it is even then add 1 to n
if n % 2 == 0:
    n += 1

# Upper part of the diamond pattern 
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)

# Lower part of the diamond pattern
for i in range(n - 2, 0, -2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)


# ### Exercise 8: Print list in reverse order using a loop

# In[63]:


# we need to create a list

List = [1,2,3,4,5,6,7,8,9]

## we should use [::-1] also for reversing or reversed keyword instead of List slicing
## item is inbuilt keyword of python which is use to get all element or items in a list  
for item in List[-1:-10:-1]:  
    print(item)


# ### 

# ### Exercise 9: Display numbers from -10 to -1 using for loop

# In[2]:


# here we use simply range between -10 to 0 zero in which 0 is exclusive so we use for loop for this

for i in range(-10,0):
    print(i)


# ### 

# ### Exercise 10: Use else block to display a message “Done” after successful execution of for loop

# In[16]:


# as a question said we have to use for loop with else block and print(Done)

for i in range(0):
    pass
else:
    print("Done")


# ### 

# ### Exercise 11: Write a program to display all prime numbers within a range

# In[24]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num **0.5)+1):
        if num %i == 0:
            return False
    return True
start_range = int(input("enter the starting number: "))
end_range = int(input("enter the end range number: "))

print("Prime number in range",(start_range,end_range))

for num in range(start_range,end_range + 1):
    if is_prime(num):
        print(num)


# ### 

# ### Exercise 12: Display Fibonacci series up to 10 terms

# In[33]:


# so here we take two variables a & b with value 1 & 2 for create fibonacci series from 1.

a,b = 1,2

#here we assign the number upto the fibonacci should be display
fib_term = 10

# after that we have used for loop in which we give range of previous declared variable to iterate it 10 times 
for i in range(fib_term):
    print(a, end=" ")       # here this print function prints the value of first element of a and after that,
    a,b = b, a+b            #after iteration we change the value or update the value of a and b from previous,
                            #it means the value of 'a' will 'b' and value of 'b' will be 'a+b'


# ### 

# ### Exercise 13: Find the factorial of a given number

# In[39]:


num = int(input("enter the number: "))

facts = 1

for i in range(1,num+1):
    facts *= i
    
print(f"The factorial of {num} is {facts}")


# ### 

# ### Exercise 14: Reverse a given integer number

# In[9]:


num = int(input("enter the number: "))

reverse_num = int(str(num)[::-1])

print(f'the reversed of a given number {num} is {reverse_num}')


# ### 

# ### Exercise 15: Use a loop to display elements from a given list present at odd index positions

# In[18]:


is_list = (input("enter elements of a list:"))
user_list = is_list.split()
print()
print(f"the list is : {user_list}")

print()
print("The odd index position elements in list are: ")
for i in range(1, len(user_list),2):
    print(user_list[i])


# ### 

# ### Exercise 16: Calculate the cube of all numbers from 1 to a given number

# In[24]:


#we have to calculate cube of all number from 1 to given range inclusive.
num = int(input("enter a number: "))
#here we take input as end range from user and after that we have to use for loop for range(1,num)

for i in range(1,num+1):       #we use end range as +1 because we want end range is inclusive
    cube=i**3
    print(f"the cube of {i} is: {cube}")


# ### 

# ### Exercise 17: Find the sum of the series upto n terms

# In[30]:


n = int(input("Enter the n terms: "))

series = 0

for i in range(1,n+1):
    series += i
print(f'the sum of series from 1 to {n} terms is {series}')


# ### 

# ### Exercise 18: Print the following pattern:
#              1
#              1 2 
#              1 2 3 
#              1 2 3 4
#              1 2 3 4 5

# In[38]:


# take input the number of rows for the pattern
n = int(input("Enter the number of rows: "))

# for loop to print the pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ### 

# ## Complete assignment 1 
