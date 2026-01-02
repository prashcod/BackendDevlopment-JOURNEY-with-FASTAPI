#!Variables and Data Types : 
#?A variable is a name that stores a value in memory.

#?Python let's muliple values storing or Multiple Assignment : 
# a , b = 100 , 120 
# print( a , b)

# age = 22   #?int 
# Name = "Prashant" #?str
# Grade = 'A' #?char
# is_Student = True #? bool 

# ?#Lists 
# marks = [45, 47, 48, 50]

#? #Tuples 
# coordinates = (12.9 , 13.5)

#? #dict 

# user = { 
#    "Name" : "PRASHANT", 
#    "age" : 21 , 
#    "sex" : "Male"
# }

#? #sets 
# unique_id = {456, 221 ,342}

# print(age , Name , Grade , is_Student , marks)

# ?# ❓ Problem
#? # Store student information:
#? # Name
#? # Age
#? # Marks in 3 subjects
#? # Whether the student passed (pass if avg ≥ 40)


#? #solution : 
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
  



#!REAL BACKEND PROBLEM (Variables & Types)
#? ❓ Problem
# ?You’re building a user registration API.
#? Store:
#? user id
#? email
#? roles (no duplicates)
# ?active status

#?USER REGISTRATION API : 
# ?🧪 YOUR TURN (Challenging Task)
# ?❓ Task
#? Modify the logic so that:
#? User is eligible only if "admin" is in roles
#? Age must be between 18 and 60
#? If not eligible, return reason
#? Try it yourself — then send your solution.
#? I’ll review it like a backend code review 👨‍💻🔥

#?incoming data from the user 
# user_data  = { 
#     "id" :101 , 
#     "email" : "prashant@gmail.com" , 
#     "age" : 65 , 
#     "roles" :["user" , "editor" , "admin"],
#     "isactive" : True 
# }


#? #extracting variables with correct types : 

# user_id = int(user_data["id"])
# email = str(user_data["email"])
# age = int(user_data["age"])
# roles = set(user_data["roles"])
# is_Active = bool(user_data["isactive"])


#? #evaluation of eligibility 
# is_Eligible = (
# age > 18 
# and age < 60
# and is_Active 
# and "admin" in roles
# )


#? #backend response object : 
# response = { 
#    "user_id" : user_id ,
#    "email" : email , 
#    "roles" : list(roles), 
#    "eligibility" : is_Eligible
# }

# ?#check elgilibily : (BOOLEAN CHECK)
# if not response["eligibility"]: 
#   print("You are not ELigbile")

# print(response)
# ---------------------------------------------------------------------------

#!Type Casting a Variable

# s = "10"  
# n = int(s) 
# cnt = 5
# f = float(cnt)  
# age = 25
# s2 = str(age)  

# print(n)  
# print(f)  
# print(s2) 

#? #Geting the type of variable 
# print(type(n))
# print(type(f))
# print(type(s2))


# ---------------------------------------------------------------------------
# ?Delete a Variable Using del Keyword (del)

# x = 100
# print(x)
# del(x)
# print(x) #Raises an error (NameError) as we have already deleted x . 


# ---------------------------------------------------------------------------

#? Practical Examples
#? 1. Swapping Two Variables

#?my method : brute force or using temporary space 
# x , y = 100 , 101 
# a , b = 201 , 202 
#? #before swapping 
# print( x , y )
# print( a , b )
# temp1 , temp2 = x , y
# x , y = a , b 
# a , b = temp1 , temp2 
#? #after swapping
# print( x , y )
# print( a , b )

#?effective way : to use muliple assignment 

# x , y , a , b = 100 , 101 , 201 , 202 
# print (x , y , a ,b )
# x , y , a , b = a  , b , x , y 
# print (x , y , a ,b )

# ---------------------------------------------------------------------------

#? 2. Counting Characters in a String

# word = "Prashant"
# length = len(word)
# print(length)

# ---------------------------------------------------------------------------
#!Python Operators
#!Operators :  

#?Arithmetic operators : 
# ?Variables
# a = 15
# b = 4
# ?# Addition
# print("Addition:", a + b)  
#? # Subtraction
# print("Subtraction:", a - b) 
#? # Multiplication
# print("Multiplication:", a * b)  
#? # Division
# print("Division:", a / b) 
#? # Floor Division -> gives only quotient 
# print("Floor Division:", a // b)  
#? # Modulus -> gives remainder 
# print("Modulus:", a % b) 
#? # Exponentiation --> power of 
# print("Exponentiation:", a ** b)

#? Comparison Operators / Relational Operators 
#? --> Always returns boolean result in Turue or False 

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

# !CONTROL STATEMENTS : IF , FOR , RANGE 

#?IF STATEMENS :  a decision gate in a system in backend system it is widely used for  every request which goes through muliple decision gates . 

#? EXAMPLE : Real Backend Use Case 2: Rule-Based Logic (ML + Backend)
#? In your recommendation system:
#? “Only recommend content if similarity score ≥ threshold”

# similarity_score = 4.5 
# threshold = 3.5 

# if similarity_score >= threshold: 
#   print("You can recommend the system to me")

# ---------------------------------------------------------------------------

#! FOR STATEMENTS : 
#? Real Backend Use Case 2: Ranking Content
#? Problem
#? You have similarity scores for multiple contents.

# scores = [
#     {"id": 1, "score": 0.8},
#     {"id": 2, "score": 0.6},
#     {"id": 3, "score": 0.9}
# ]

# for item in scores: 
#   if item["score"] >= 0.7: 
#     print("Recommend:" , item["id"])

#!ANOTHER EXAMPLE : 
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# for key ,item in users.items(): 
#   print(f"{key} = {item}")

# for user , status in users.copy().items(): 
#   if status == "inactive": 
#     del users[user]

# active_users= {}
# for user , status in users.items(): 
#   if status == "active": 
#     active_users[user] = status

# print(active_users)


# ---------------------------------------------------------------------------

# !RANGE() FUNCITON : 
#? SYTAX : range(start , stop , step)
#?Real Backend Use Case 1: Vector Indexing
#? Your vectors are lists.
# vector = [1, 0 ,1 ,0]
#?#to access each dimension we uses : 
# for i in range(len(vector)): 
#   print(vector[i])
# ---------------------------------------------------------------------------
#!BREAK AND CONTINUE STATEMENTS : 

#! BREAK : 
#? Backend Use Case 1: Early Exit (Performance)
#? Problem (your project)
#? You want the first best recommendation, not all of them .
# scores = [
#     {"id": 1, "score": 0.6},
#     {"id": 2, "score": 0.9},
#     {"id": 3, "score": 0.8},
# ]
# best = None
# for item in scores: 
#   if item["score"] >= 0.9: 
#       best = item
#       break 

# print(best)

#! CONTINUE : 
#? Backend Use Case 2: Skipping Invalid Data
#? Problem
#? Some content is inactive — skip it.


# contents = [
#     {"id": 1, "active": True},
#     {"id": 2, "active": False},
#     {"id": 3, "active": True},
# ]

# for item in contents: 
#   if not item["active"]: 
#      continue
#   else : 
#      print(item)

# ---------------------------------------------------------------------------
#! ELSE CLAUSE ON LOOPS : 
#? 🔥 Backend Use Case: Search & Validation
#? Problem (very real)
#? Check if an admin user exists.

# users = [
#     {"name": "A", "role": "user"},
#     {"name": "B", "role": "editor"},
# ]
# for item in users: 
#       if item["role"] == "admin": 
#           print("admin found")
#           break
# else : 
#     print("admin not found")

# ---------------------------------------------------------------------------

#! Pass Statements -> are the used to define an empty function or class in python 
#? Syntax : 
#? while True : 
#?    pass 

# ---------------------------------------------------------------------------

#! match statement : 

#? Used IN HTTP Method Routing 

# method = "POST"

# match method : 
#   case "GET" : 
#     print("Fetch Data")
#   case "POST": 
#     print("Create Data")
#   case "PUT" : 
#     print("Update Data")
#   case "DELETE": 
#     print("Delete Data")
#   case _: 
#     print("Invalid Data")


# ---------------------------------------------------------------------------
#! Terinary Conditional statement : 

#? Interaction with return (IMPORTANT)
#? You can use ternary inside return safely.

# def get_message(is_active):
#     return "OK" if is_active else "BLOCKED"

#? Use case in : Score Categorization (Your Project)

# score = 0.83 
# category = "High" if score > 0.75 else "Low"
# print(category)


#^ Problem associated with Terninary COnditonal Statement : 
#? Problem (Project-Aligned)
#? You have:
#? score = 0.65
# ?threshold = 0.7
#? Task
#? Create:
#? decision: "RECOMMEND" or "SKIP"
#? message: "Shown to user" or "Hidden due to low score"
#? Using ternary expressions only.

# score = 0.65 
# threshold = 0.7 
# user_id = 749

# response = {
#    "user_id"  : user_id ,
#    "decision" : "RECOMMEND" if score > 0.5 else "SKIP" ,
#    "message" : "Shown to user" if threshold >= 0.65 else "Hidden due to low score"
# }

# print(response)


# ---------------------------------------------------------------------------
#! NOTE : 
#^ Looping through function which returns : 
# def addition(): 
#   return [1,2,3,4]

# for i in addition(): 
#   print(i)
  
#! FOR LOOPS : 

# ? Project-aligned example: Vector dot product (CORE)
# a = [1, 0, 1, 0]
# b = [0, 1, 1, 0]

# dot = 0 
# for i in range (len(a)): 
#   dot += a[i] * b[i]

# print(dot)

# ? Backend example: Filtering content

# contents = [
#     {"id": 1, "active": True},
#     {"id": 2, "active": False},
#     {"id": 3, "active": True},
# ]

# active_contents = []

# for content in contents: 
#   if content["active"] : 
#     active_contents.append(content)

# print(active_contents)


#^ Problem 1 (FOR loop — project aligned)
#^Given vectors, compute L2 norm.
#^ v = [3, 4]
#^ Expected output:
#^ 5.0
#^ Rules:
#^ use for
#^ no math libraries
#^ return value

# v = [3 ,4]
# value = 0 
# for i in range(len(v)) : 
#   value += v[i]*v[i]

# final = value ** 0.5 
# print(final)


# ---------------------------------------------------------------------------
#! While LOOP — CONDITION-DRIVEN EXECUTION
#? While loop in tuples use case : 

# tuple = (2,3,4)
# i =0 

# while i < len(tuple) : 
#   print(tuple[i])
#   i += 1 


# ? Backend example: Retry mechanism

# attempts = 0
# MAX_RETRIES = 3

# while attempts < MAX_RETRIES: 
#   sucess = False  # pretend API CALL 

#   if sucess : 
#     break 

#   attempts += 1 

# print(sucess)

#? Project-aligned example: Score threshold search

# scores = [0.3, 0.5, 0.6, 0.9]
# i = 0

# while i < len(scores): 
#   if scores[i] >= 0.8 : 
#     print("High score found" , scores[i])
#     break 
  
#   i += 1 

#^ Problem 3 (WHILE loop — retry logic)
#^ Simulate retry logic with max 3 attempts.

# attempts = 3 
# i =1

# while i <= attempts: 
#   print("Attempts" , i)

#   i +=1 


# ---------------------------------------------------------------------------
#! Mistakes in loops : 

# babies = [1,2,3,4,5]
# for x in babies[:]: #! Iterating over shallow copy to avoid python logical error in loops 
#   if x % 2 == 0 : 
#     babies.remove(x)

# print(babies)

# ---------------------------------------------------------------------------

#! Python Functions : 
#* Functions are reusuable execution templates which creates an isolated runtime enviornment or stack frames everytime it is called . 

#? PURE AND IMPURE FUNCTIONS : 
#^ Problem Statement : “Lists are mutable… but I want my function to be pure.
#^ So how do I work with them without breaking purity?”

#? Impure Functions : 
# def add_one(nums): 
#   nums.append(1)

# nums = [1,2,3]
# add_one(nums) # Here it changes/mutates the nums and  caller's data is changed so it's impure 
# print(nums)

#? Pure Functions : 
# def add_oneP(nums): 
#   return nums + [1]

# nums = [1,2,3]
# new_nums =add_oneP(nums) #as python immediately throws after stack frame is destroyed 
# print(new_nums)



#? FUNTIONS ARGUMENTS AND IT'S TYPES : 
#? 1. Default Arguments : 
# def recommend(score , threshold=0.7): 
#   return score>= threshold

# recommend_val = recommend(0.9)
# print(recommend_val) #true 


#? Keyword Arguments : 
# def create_user (email , is_active , is_admin): 
#   return email , is_active , is_admin

# create_user_val = create_user(email = "prash.@gmail.com" , is_active=True , is_admin=False)
# print(create_user_val)

#? it's actually algins with my project 
#? when calling
# def get_recommendation(user_vector , content_vectors , top_k , threshold): 
#   pass 

# get_recommendation(user_vector ="user_vec" , content_vectors="contents" , top_k=5 , threshold=0.7)



#? Positional Arguments : 
# def dot_product(a,b): 
#   return sum(x*y for x,y in zip(a,b))

# a = [1,2,3]
# b= [2,3,4]   
# dot_val = dot_product(a,b)
# print(dot_val)


#? Arbitary Arguments : (*args , **kwargs)
#? *args
# def f (*args): 
#   print(args)

# f(1,2,3,4,5)

#? Real Backend Example: Score Aggregation (Your Project)
#?In your recommendation engine, you may combine multiple scoring signals later:

# def aggreate_scores(*scores): 
#   result = 0 
#   for score in scores: 
#     result += score
#     return result/len(scores)

# avg = aggreate_scores(0.7,0.8,0.9)
# print(avg)

#? **kwargs 
#? Real Backend Example: Logging / Metadata

# def log_request(**metadata): 
#   for key , value in metadata.items(): 
#     print(f"{key} = {value}")

# log_request(
#    user_id=101 , 
#    endpoint="/recommend",
#    score=0.82
# )

#^ REAL PROJECT-ALIGNED PROBLEM (DO THIS)
#^ Problem: Flexible Recommendation Logger Requirements
#^ Create a function that:
#^ accepts user_id
#^ accepts any number of similarity scores
#^ accepts optional metadata
#^ returns average score and metadata

# def recommendation_logger(user_id,*scores , **metadata): 
#   if not scores: 
#     avg = 0.0 
#   else : 
#     result = 0 
#     for score in scores: 
#       result += score
#     avg = result/len(scores)
    
#   return { 
#          "user_id" : user_id , 
#          "avg_score": avg ,
#          "metadata": metadata
#            }



# logger = recommendation_logger(101,0.7,0.8,0.9 , algorithm="cosine",model_version= "v1")
# print(logger)

#? FUNCTIONS WITHIN FUNCTIONS (inner function or nested function )

#? Simple Example : 
# def outer(): 
#   x = 10 
#   print("This is Outer function")
#   def inner(): 
#     print("This is inner Function")
#     print(x)      #HERE inner() is Closure function which remebers x variable even after it has been executed .  
#   return inner

# obj =outer()
# obj()

#^ Making real REQUEST SCOPED BACKEND FUNCTION : 

#* It is teaching you how backend servers safely handle user requests.
#? MOCKED DATA( USUALLY COMES FROM DATABASES )
# USERS = { 
#           1: [1,2,3,4], 
#           2: [2,1,0,3]
#         }
# CONTENT = [
#     [4, 5, 6, 7],
#     [1, 0, 1, 0],
#     [3, 3, 3, 3]
#            ]

#? Missing funcitons 
# def get_user_vector(user_id): 
#   return USERS[user_id]

# def get_all_content_vector(): 
#   return CONTENT

# def dotproduct(user_vector , content_vector): 
#   return sum(x*y for x,y in zip(user_vector,content_vector))
  

# def recommend(user_id): 
#   user_vector = get_user_vector(user_id)
  
#   def score(content_vector): 
#     return dotproduct(user_vector , content_vector)
  
#   results = []
#   for c in get_all_content_vector(): 
#     results.append(score(c))
  
#   return results 
  

# print(recommend(1))
# print(recommend(2))



# ---------------------------------------------------------------------------
#! Anonymous Functions : 


# s = "PrashforPrashant"
# ss = lambda s:s.upper()
# print(ss(s))

#? USE COMMNALY IN BACKEND CODE  WHICH HELPS TO SORT : 
# contents = [
# {"id" : 1 , "score" : 0.6},
# {"id" : 2 , "score" : 0.9},
# {"id" : 3 , "score" : 0.7}
# ]
# func = contents.sort(key= lambda x : x["score"] , reverse=True)

# print(contents) #sorted according to score and in decresasing order 






# ---------------------------------------------------------------------------













# ---------------------------------------------------------------------------













# ---------------------------------------------------------------------------
















# ---------------------------------------------------------------------------
















# ---------------------------------------------------------------------------
















# ---------------------------------------------------------------------------















# ---------------------------------------------------------------------------













# ---------------------------------------------------------------------------













# ---------------------------------------------------------------------------

   












