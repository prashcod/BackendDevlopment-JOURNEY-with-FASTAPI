#Variables and Data Types : 
# A variable is a name that stores a value in memory.

#Python let's muliple values storing or Multiple Assignment : 
# a , b = 100 , 120 
# print( a , b)

# age = 22   #int 
# Name = "Prashant" #str
# Grade = 'A' #char
# is_Student = True # bool 

# #Lists 
# marks = [45, 47, 48, 50]

# #Tuples 
# coordinates = (12.9 , 13.5)

# #dict 

# user = { 
#    "Name" : "PRASHANT", 
#    "age" : 21 , 
#    "sex" : "Male"
# }

# #sets 
# unique_id = {456, 221 ,342}

# print(age , Name , Grade , is_Student , marks)

# # ❓ Problem
# # Store student information:
# # Name
# # Age
# # Marks in 3 subjects
# # Whether the student passed (pass if avg ≥ 40)


# #solution : 
# Student = {
#    "Name" : "Prashant Gyawali" , 
#    "Age" : 21 ,
#    "Marks" : [45 , 48 ,50]
# }

# for key,value in Student.items():
#   print(f"{key} = {value}")

# for value in Student.values():
#   if Student["Marks"][0] >= 40: 
#     print("Student is passed")
  



# REAL BACKEND PROBLEM (Variables & Types)
# ❓ Problem
# You’re building a user registration API.
# Store:
# user id
# email
# roles (no duplicates)
# active status

#USER REGISTRATION API : 
# 🧪 YOUR TURN (Challenging Task)
# ❓ Task
# Modify the logic so that:
# User is eligible only if "admin" is in roles
# Age must be between 18 and 60
# If not eligible, return reason
# Try it yourself — then send your solution.
# I’ll review it like a backend code review 👨‍💻🔥

#incoming data from the user 
user_data  = { 
    "id" :101 , 
    "email" : "prashant@gmail.com" , 
    "age" : 65 , 
    "roles" :["user" , "editor" , "admin"],
    "isactive" : True 
}


#extracting variables with correct types : 

user_id = int(user_data["id"])
email = str(user_data["email"])
age = int(user_data["age"])
roles = set(user_data["roles"])
is_Active = bool(user_data["isactive"])


#evaluation of eligibility 
is_Eligible = (
age > 18 
and age < 60
and is_Active 
and "admin" in roles
)


#backend response object : 
response = { 
   "user_id" : user_id ,
   "email" : email , 
   "roles" : list(roles), 
   "eligibility" : is_Eligible
}

#check elgilibily : (BOOLEAN CHECK)
if not response["eligibility"]: 
  print("You are not ELigbile")

print(response)
# ---------------------------------------------------------------------------

#Type Casting a Variable

# s = "10"  
# n = int(s) 
# cnt = 5
# f = float(cnt)  
# age = 25
# s2 = str(age)  

# print(n)  
# print(f)  
# print(s2) 

# #Geting the type of variable 
# print(type(n))
# print(type(f))
# print(type(s2))


# ---------------------------------------------------------------------------
# Delete a Variable Using del Keyword (del)

# x = 100
# print(x)
# del(x)
# print(x) #Raises an error (NameError) as we have already deleted x . 


# ---------------------------------------------------------------------------

# Practical Examples
# 1. Swapping Two Variables

#my method : brute force or using temporary space 
# x , y = 100 , 101 
# a , b = 201 , 202 
# #before swapping 
# print( x , y )
# print( a , b )
# temp1 , temp2 = x , y
# x , y = a , b 
# a , b = temp1 , temp2 
# #after swapping
# print( x , y )
# print( a , b )

#effective way : to use muliple assignment 

# x , y , a , b = 100 , 101 , 201 , 202 
# print (x , y , a ,b )
# x , y , a , b = a  , b , x , y 
# print (x , y , a ,b )

# ---------------------------------------------------------------------------

# 2. Counting Characters in a String

# word = "Prashant"
# length = len(word)
# print(length)

# ---------------------------------------------------------------------------
# Python Operators
#Operators :  

#Arithmetic operators : 
# Variables
# a = 15
# b = 4
# # Addition
# print("Addition:", a + b)  
# # Subtraction
# print("Subtraction:", a - b) 
# # Multiplication
# print("Multiplication:", a * b)  
# # Division
# print("Division:", a / b) 
# # Floor Division -> gives only quotient 
# print("Floor Division:", a // b)  
# # Modulus -> gives remainder 
# print("Modulus:", a % b) 
# # Exponentiation --> power of 
# print("Exponentiation:", a ** b)

# Comparison Operators / Relational Operators 
# --> Always returns boolean result in Turue or False 

# a = 13
# b = 33
# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)


# ---------------------------------------------------------------------------

# import keyword
# print(keyword.kwlist)


# ---------------------------------------------------------------------------

