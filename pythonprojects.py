# print("my name is aastha\n"
#       "and i am learning python")
# # fuck off
# '''
# pardon me
# what seriously
# unbeliveable
# '''
# print("really?\"you bitch\" whatever\n"
#       "i don't give a fuck")
# print("hello my name is",6,7,sep="~",end="1012\n")
# print("aastha")
# print("haa thik h na yrr\n"
#       "pakka mat")
# # heloooooooooooooooooooo
# """


# """
# print("kanta\"gatuuuuuuuuuuuuuuuu\" sharma")
# print("heloo my name is kanta sharma",1982,14,7,sep="-",end="aalahhhhhhhhhhhhhhhhhh")
# print("ediit")
# a="1"
# b="2" 
# print(int(a)+int(b))
# string="10"
# number=12
# string_number=int(string)
# sum=number+string_number
# print("sum of both the number:", sum)

# price=20.9
# number=28
# decimal_number=float(number)
# sum=decimal_number+(price)
# print("total sum of number is:", sum)

# price=51.652
# number=125
# price_number=int(price)
# sum=price_number+number
# print("total sum of number is:", sum)

# try:
#     num1=float(input("enter first number: "))
#     num2=float(input("enter second number: "))
#     sum=num1+num2
#     print("sum of both the numbers is:", sum)
# except ValueError:
#     print("please enter a valid integer") 

    
# try:
#         text1=(input("enter first text: "))
#         text2=(input("enter second text: "))
#         result=text1+text2
#         print("concatenated text is:", result)
# except ValueError:
#         print("please enter a valid text")

# a=input("how many flowers:" )
# b=input("how many boquets can be made: ")
# c=int(a)//int(b)
# print("how many girls can get flowers:", c)

# a=input("name: ")
# print("number of characters in the name:", len(a))
# print("number of words in the name:", len(a.split()))
# for character in a:
#     print(character)
# for character in a:
#     print(character,end=" ")
# for character in a:
#       print(character,end="\n")
# for character in a:
#      print("number of charachters are:", character)

# st="""hello my name is aastha sharma and 
# i am learning python programming language"""

# # print(st)
# print("hello world")
# print("hello world")

# nm="harry"
# print(nm[-4:-1]) 
# # %%
# a="aastha"
# print(a[0:5:2])
# a="aastha"
# print(a.upper())

# # %%
# a="Aastha"
# print(a.lower())
# print(a.uppercase())



# # %%
# a="aastha"
# print(a.uppercase())

# # %%
# a="aastha"
# print(a.upper())

# # %%
# a="aastha"
# print(a.lower())
# # %%
# a="????aastha????"
# print(a.rstrip("????"))

# # %%
# a="aastha"
# print(a.replace("aastha","kanta"))
# # %%
# a="aastha sharma is learning python"
# print(a.split())

# # %%
# a="aastha"
# print(a.split("a"))
# # %%
# a="aastha sharma is learning python"
# print(a.capitalize())
# # %%
# a="aastha"
# print(a.center(20,"*"))
# # %%
# a="aastha"
# print(a.center(40,))
# # %%
# a="aastha"
# print(a.count("a"))
# # %%
# a="aasthaaa"
# print(a.count("a",0,8))

# # %%
# a="aasthaaa"
# print("a.rstrip('a'):", a.rstrip("a"))

# # %%
# a="aasthaaa"
# print("a.lstrip('a'):", a.lstrip("a"))
# # %%
# a="aasthaaa"
# print("a.strip('a'):", a.strip("a"))
# # %%
# a="aasthaaa"
# print("a.rstrip('a'):",a.rstrip("a",5,8))
# # %%
# a="aasthaaa"
# print(a[0:5:2])

# # %%
# a="aasthaaa"
# print(a[0:6])
# # %%
# a="aasthaaa"
# print(a.endswith("a"))
# # %%
# a="aasthaaa"
# print(a.endswith("sth",0,5))


# # %%
# a="aasthaaa"
# print(a.find("s"))

# # %%
# a="aasthaaa"
# print(a.find("s",0,5))
# # %%
# a="aasthaaa"
# print(a.find("a"))
# # %%
# a="aasthaaa"
# print(a.index("s"))
# # %%
# str="aasthaispreetty"
# print(str.isalnum())
# # %%
# str="aasthaispretty"
# print(str.isalpha())

# # %%
# str="aastha is preety"
# print(str.islower())
# # %%
# str="Aastha1012"
# print(str.isprintable())
# # %%
# str="\n             \t      "
# print(str.isspace())

# # %%
# a="ROSES AND TULIPS"
# converted_a=a.title()
# print(converted_a.istitle())
# # %%
# a="aastha"
# print(a.isupper())

# # %%
# a="hie aastha"
# print(a.startswith("hie"))
# # %%
# a="hie aastha"
# print(a.swapcase())
# # %%
# a=int(input("enter your age: "))
# print("your age is:", a)
# print(a==18)
# print(a!=18)
# if a>18:
#     print("you are eligible for voting")
# else:
#     print("you are not eligible for voting")
# ####


# a=int(input("enter your age: "))
# print("your age is:", a)
# print(a==18)
# print(a!=18)
# print(a>=18)
# print(a<=18)
# if a>18:
#     print("you are eligible for voting")
# else:
#     print("you are not eligible for voting")
# a=int(input("enter your number: "))
# if(a==0):
#     print("number is zero")
# elif(a>0):
#     print("number is positive")
# elif(a<0):
#     print("number is negative")
# else:
#     print("invalid input")


# a=int(input("enter the number of flowers:  "))
# if a>50:
#     bouquets=a//5
#     print("number of bouquets that can be made:", bouquets)
# elif a<50:
#      if(a<10 and a>0):
#         print("number of bouquets that can be made: 1")
#      elif(a>10 and a<50):
#         print("number of bouquets that can be made: 2")
#      else:
#         print("get more flowers")

# else:    print("invalid input")

# time=int(input("enter the time in 24 hour format: "))
# if time>=0 and time<12:
#     print("good morning")
# elif time>=12 and time<18:
#     print("good afternoon")
# else:
#     print("good evening")

# timestamp=(input("enter the time in 24 hour format: "))
# print(timestamp)
# if timestamp>=0 and timestamp<"12am":
#     print("good morning")
# elif timestamp>='12am' and timestamp<"6pm":
#     print("good afternoon")
# else:    print("good evening")

# hour=int(input("enter the hour(1-12): "))
# period=input("enter am or pm : ").strip().lower()

# if period=="am":
#     print("good morning")
# elif period=="pm" and hour<6:
#     print("good afternoon")
# else:
#     print("good evening")

# import time

# current_time=time.localtime()
# hour=current_time.tm_hour
# minute=current_time.tm_min
# print(f"current time: {hour}:{minute}")
# if hour>=0 and hour<12:
#     print("good morning")
# elif hour>=12 and hour<18:
#     print("good afternoon")
# else:
#     print("good evening")

# import time

# current_time=time.localtime()  

# twelve_hour_format=time.strftime("%I:%M:%S %p")
# print(f"current time: {twelve_hour_format}")
# if current_time.tm_hour>=0 and current_time.tm_hour<12:
#     print("good morning")
# elif current_time.tm_hour>=12 and current_time.tm_hour<18:
#     print("good afternoon")
# elif current_time.tm_hour>=18 and current_time.tm_hour<24:
#     print("good evening")    
# else:
#     print("good night")

# A=input("do you wanna go out?: ")
# match A.strip().lower():
#     case "yes":
#         print("lets go out")
#         if input("do you wanna go to a movie?: ").strip().lower() == "yes"|"sure"|"why not":
#             print("lets go to a movie")
#         else:
#             print("then lets go to a restaurant")
#     case "no"|"um no":
#         print("fuck you")
#         print("hehe")
#     case "maybe"|"idk":
#         print("that's why you are single")
#         if input("okay sorry but look at this beautiful weather come on :( :  ").strip().lower() == "okay cool"|"fine but you will decide":
#             print("love you")
#     case _:
#         print("invalid input")

# options_for_dinner = ["fried rice", "pasta", "pizza"]
# for food in options_for_dinner:
#      print(food,end="|")
#      if(food=="fried rice"):
#           print("good choice")

# options_for_dinner=("cupcake","icecream","pancake")
# food=",".join(options_for_dinner)
# print(food)

# colours=["red","mlue","aello"]
# for colour in colours:
#      print(colour)
#      for x in colour:
#           print(x)

# for number in range(12009,12559,2):
#      print(number)

# i=0
# while(i<3):
#     print(i)
#     i=i+1

# i=input("do you want to go out: ")
# while i.strip().lower() == "no":
#     i=input("do you want to go outtt ")
# if i.strip().lower() == "yes":
#     print("okay lets go")

# print("let's go to a movie")
# while True:
#     i = input("do you wanna go to a movie: ")
#     if i.strip().lower() in ("yes", "y", "no", "n"):
#         break

# while True:
#     i = input("do you wanna go to a movie: ")
#     if i.strip().lower() == "no":
#         print("ight no worries")
#         break
#     if i.strip().lower() == "yes":
#         print("ight lets go")
#         break

# ******calculator******
# num1 = float(input("enter first number: "))
# num2 = float(input("enter second number: "))
# operation = input("enter operation (+, -, *, /): ")

# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     result = num1 / num2
# else:
#     print("Invalid operation")

# print(f"Result: {result}")

# print("multiplication table")
# table=int(input("enter the number for which you want to print the multiplication table: "))
# print(f"multiplication table of {table}")
# for j in range(1, 11):
#     print(f"{table:2} x {j:2} = {table * j:3}")
# print()  # Print a newline after each table 

# secret_number = 7
# max_attempts = 0
# while True:
#     guess = int(input("guess the secret number between 1 and 10: "))
#     max_attempts += 1
#     if max_attempts >= 3 and guess != secret_number:
#         print("you have exceeded the maximum number of attempts. game over.")
#         break
#     if guess == secret_number:
#         print("congratulations! you guessed the secret number.")
#         break
#     elif guess < secret_number:
#         print("your guess is too low.")
#     elif guess > secret_number:
#         print("your guess is too high.")

# balance = 1000
# while True:
#     print(f"current balance:${balance}")
#     action=input("what would you like to choose?deposit,withdraw(d/w) or exit(e): ").strip().lower()
#     if action=="d":
#         amount=float(input("enter the amount to deposit: "))
#         balance+=amount
#         print(f"${amount}depositted succesfully,new balance:${balance}")
#     elif action=="w":
#         amount=float(input("enter the amount to withdraw: "))
#         if amount>balance:
#             print("insufficient balance")
#         else:
#             balance-=amount
#             print(f"${amount} withdrawn successfully,new balance:${balance}")
#     elif action=="e":
#         print("thank you for using our services")
        # break
# number=int(input("enter a number: "))
# for number in range(1,number+2):
#     if number%2!=0:
#         continue
#     else:
#      print(f"{number} is even")

# while True:
#  name=input("enter a name: ")
#  if name.lower()=="voldemort":
#     print(f"{name} access denied")
#     continue
#  else:
#     print(f"{name} access granted")

# choosen_floor=int(input("enter the floor number: "))
# for floor in range(1, choosen_floor + 1):
#     if floor == 13:
#         print("floor 13 is skipped")
#         continue
#     if floor != choosen_floor:
#         print(f"passing floor...{floor}")
#     else:
#         print(f"welcome to floor {floor}")

# def calculateGmean(a,b):
#     mean=(a*b)/(a+b)
#     print(f"mean: {mean}")
     
# a=8
# b=12
# if(a>b):
#     print("first number is greater than second number")
# else:
#     print("second number is greater than first number")

# c=52
# d=90
# calculateGmean(c,d)

# def isgreater(a,b):
#     if a>b:
#         print(f"{a}is greater than{b}")
#     else:
#       print(f"{b}is greater than{a}")

# isgreater(10,20)
# calculateGmean(c,d)

# def isless(a,b):
#     pass

# def name(f_name, m_name="", l_name=""):
#     if m_name == "" and l_name == "":
#         print(f"hello my name is {f_name}")
#     elif l_name == "":
#         print(f"hello my name is {f_name} {m_name}")
#     elif m_name == "":
#         print(f"hello my name is {f_name} {l_name}")
#     else:
#         print(f"hello my name is {f_name} {m_name} {l_name}")

# name("aastha", "sharma")

# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum+=i
#         print(f"your average is: {sum/len(numbers)}")


# average(10,20,30,40,50)        


# def student_info(**info):
#     print(type(info))
#     for key,value in info.items():
#         print(f"{key}:{value}")

# student_info(name="aastha", age=21, course="python programming")


# def max(*numbers):
#     print(type(numbers))     
#     maximum = numbers[0]
#     for i in numbers:
#         if i > maximum:
#                 maximum = i
#         return maximum
#     if len(numbers) == 0:
#         return None
        

# maximum_value = max(100, 20, 3.0, -40, 50)
# print(f"The maximum value is: {maximum_value}") 
#marks=[85, 92, 78, 90, 88]
# print("marks:", marks)
# print("highest marks:", max(marks))
# print("lowest marks:", min(marks))
# print("sum of marks:", sum(marks))
# print("average marks:", sum(marks)/len(marks))
# print("sorted marks:", sorted(marks))
# print("reversed marks:", list(reversed(marks)))
# print("length of marks:", len(marks))
# print("count of marks 90:", marks.count(90))
# print("index of marks 88:", marks.index(88))
# print("is 95 in marks:", 95 in marks)
# print(marks[0:3])
# print(marks[::2])
# print(marks[::-1])
# print(marks[0:3:2])
# print(marks[len(marks)-1:len(marks)-4:-1]) 
# lst=[i for i in range( 10)if i%2==0]
# print(lst)
# lst=[number for number in range(1, 21) if number % 3 == 0]
# print(lst)
# l=['haa jaa']
# l.append('or sun ice cream lete aana')
# print(l)
# def custom(text):
    # print(text,end="yes sir\n\n")


# l=[200,5,30,0.80,-9]
# l.sort()
# print(l)
# l=[200,5,30,0.80,-9]
# l.sort(reverse=True)
# print(l,end=" ")
# l=[200,500,67,30,0.80,-9]
# l.sort()
# print(l,end="---done boss\n\n")
# l=[-2,0.000067,-55,9,9000]
# l.reverse()
# custom(l)
# l=[67,67,6,7,67,67,67]
# print(l.count(67))
# print(l,end=' ')
# l=[200,5,30,0.80,-9]
# print(l)
# m = l.copy()
# m[0] = 0
# print(m)
# print(l)
# l=[200,5,30,0.80,-9]
# l.insert(3,67)
# print(l)
# l=[200,5,30,0.80,-9]
# m=[67,'vinti my vinti']
# k=l+m
# print(k)
# l.extend(m)
# print(l)
# l=[200,5,30,0.80,-9]
# l.append(67)
# print(l)

# print("AA exclusive club".upper())
# guest_list = {"karan aujla", "honey singh", "vedant", "nidhi"}
# vip_list = {"me", "ronaldo", "mia", "blush"}
# already_inside=set()

# while True:
#     print('Welcome to the party')

#     print('Help me with your name')
#     name = input(" ").strip().lower()
#     if not name:
#         print("No name entered. Exiting.")
#         import sys
#         sys.exit()

#     age=int(input("may i know your age: "))
#     if age<21:
#         print("sorry, your age must be 21 or above to enter")
#         continue
    
#     print("Let me check")
    
#     if name in already_inside:
#         print(f"w8,someone named {name.title()} is already inside")    
#         different_person=input("are you diff person with same name?(yes/no): ").strip().lower()
#         if different_person!="yes":
#             print("access denied! duplicate entry detected")
#             continue
#         else:
#             print("since you are diff person, you must buy a ticket")
#             buy_ticket = input("would you like to party ;)?(yes/no): ").strip().lower()
#             if buy_ticket == "yes":
#                 try:
#                     count = int(input("how many tickets you would like to buy: "))
#                 except ValueError:
#                     print("Invalid number of tickets.")
#                     continue
#                 grand_total = count * 100
#                 print(f"your total would be {grand_total}")
#                 print("welcome to the party!")
#                 already_inside.add(name)
#                 continue
#             else:
#                 print("okay, thank you")
#                 continue                                                                                 
#     elif name in vip_list:
#         print(f"Welcome {name.title()}")
#         print("Your entry will be from the golden gate")
#         print("enjoy your night :)")

#         already_inside.add(name)
#     elif name in guest_list:
#         print(f"Welcome {name.title()}")
#         print("your entry will be from this side")
#         already_inside.add(name)
     
#     else:
#         print("Sorry, I don't see your name on the list")
#         new_person = input("Do you want to buy a ticket? (yes/no): ").strip().lower()
#         if new_person == "yes":
#             try:
#                 count=int(input("how many tickets: "))
#             except ValueError:
#                 print("ivalid no. of tickets")
#                 continue
#             grand_total=count*100
#             print(f"your total is{grand_total}")
#             print(f"Welcome {name.title()} :)")
#             already_inside.add(name)
#         else:
#             print("Okay, thank you")
       
# scores=[50,48,99,110,112,156.88,253,259,120,310]
# print(f"raw score: {scores}")

# scores.sort(reverse=True)
# print(f"sorted score: {scores}")

# top3=scores[:3]
# print(f"top 3 scores: {top3}")

# check if any score reaches the 100-point milestone
# 1. Initialize the raw unsorted scores
# print  ()

# scores = [50,48,99,110,112,156.88,253,259,120,310]
# print(f"Raw Scores: {scores}")

# # 2. Sort from highest to lowest in-place
# scores.sort(reverse=True)
# print(f"Sorted Scores (Descending): {scores}")

# # 3. Slice the first 3 items for the podium
# top_3_podium = scores[:3]
# print(f"Top 3 Leaderboard Podium: {top_3_podium}")

# # 4. List comprehension to keep only scores 100 or higher
# milestone_scores = [score for score in scores if score >= 100]
# print(f"Milestone Scores (100+ points): {milestone_scores}")

# # Create an empty list first
# long_process_list = []

# for score in scores:
#     if score >= 100:
#         long_process_list.append(score)
#         # long_process_list.append(score) # Save it to our list

# # Move this print statement OUTSIDE the loop (remove the indentation)
# print(f"Milestone Scores (long process): {long_process_list}")


# print()

# def proccessing_leaderboard(scores):
    
#     sorted_score = sorted(scores, reverse=True)
#     print(f"sorted score(decending): {sorted_score}")
    
#     top_3_scores = sorted_score[:3]
#     print(f"top 3 scores: {top_3_scores}")

#     milestone=[score for score in scores if score >=100]
#     print(f"milestone(100+): {milestone}")

# def score_statics(score_list):
#     if not score_list:
#         return

#     highest_score = max(score_list)
#     average_score = sum(score_list) / len(score_list)
#     lowest_score = min(score_list)

#     print(f"highest score are: {highest_score}")
#     print(f"average score are: {average_score}")
#     print(f"lowest score are: {lowest_score}")
# print()
# team_a_score=[200, 219, 300, 298, 167, 315, 198]
# team_b_score=(199, 225, 154, 369, 149, 259, 121)
# print("-----proccessing team a score----".title())
# proccessing_leaderboard(team_a_score)
# score_statics(team_a_score)

# print()
# print("-----processing team b score-----".title())
# proccessing_leaderboard(team_b_score)
# score_statics(team_b_score)

# print()

# floor1=["apple", "mango", "plum", "coconut", "watermelon", "blueberries"]
# floor2=["onion", "garlic", "tomato", "green chilli", "capcicum", "cabbage"]
# print()

# print(f"fruits_and_vegetable_store: {floor1 + floor2}")

# print()
# floor1.insert(1, "blueberries")
# print(f"floor1: {floor1}")

# print()

# count = floor1.count("blueberries")
# print(f"count:{count}")
# if count > 1:
#     print("There are more than one blueberries in floor1.")

# print()

# fruits=("apple", "mango", "plum", "coconut", "watermelon","plum", "blueberries", "plum")

# items=list(fruits)
# items.pop(3)
# count=items.count("plum")
# items.append("coco")
# fruits = tuple(items)
# print(fruits)
# print(f"count:{count}")

# tuple1 = (0, 1, 2, 3, 4, 5, 3, 6 ,3 ,8, )
# # res =  tuple1.index(3,2,10)
# res = len(tuple1)
# print(f'count of 3 in tuple1 is: {res}'k )

# print("-----welcome to kbc-----".upper())
# player = input("your name: ").strip().lower()
# print(f"okay so {player} lets start the game!!!")

# question = [
#     {
#         "question": "What is the capital city of Rajasthan?",
#         "options": ["a) bhilwara", "b) chittorgarh", "c) jaipur", "d) jodhpur"],
#         "answer": "c",
#         "prize": 5000,
#         "50-50": "c) jaipur\nd) jodhpur",
#     },
#     {
#         "question": "Who was the first woman to go into the Mariana Trench?",
#         "options": ["a) Sally Ride", "b) Kathryn D. Sullivan", "c) Svetlana Savitskaya", "d) Valentina Tereshkova"],
#         "answer": "b",
#         "prize": 10000,
#         "50-50": "a) Sally Ride\nb) Kathryn D. Sullivan",
#     },
#     {
#         "question": "Where in Singapore did Netaji Subhash Chandra Bose make the first proclamation of an Azad Hind government?",
#         "options": ["A) HMS Minden", "B) HMS Cornwallis", "C) HMS Trincomalee", "D) HMS Meanee"],
#         "answer": "c",
#         "prize": 15000,
#         "50-50": "C) HMS Trincomalee\nA) HMS Minden",
#     },
#     {
#         "question": "Milinda-Panha is a dialogue between King Menander (Milinda) and which Buddhist monk?",
#         "options": ["A) Asanga", "B) Nagasena", "C) Mahadharmarakshita", "D) Dharmaraksita"],
#         "answer": "b",
#         "prize": 20000,
#         "50-50": "B) Nagasena\nA) Asanga",
#     },
# ]

# total_amount = 0
# safe_haven = 0
# lifeline = True

# for q in question:
#     print(f"for{q['prize']} : {q['question']}")
#     print(f"your options are: {q['options']}")
#     print()
#     print("choose from option: a, b, c, d | quit to walk away | 50-50 lifeline")

#     user_choice = input("your choice: ")
#     if user_choice == "quit":
#         print(f"you can leave, you won {total_amount}")
#         break
#     if user_choice == "lifeline":
#         if lifeline:
#             lifeline = False
#             print("2 wrong options are removed")
#             print("new options are: ")
#             print(f"{q['50-50']}")
#             user_choice = input("\nNow select your answer: ").strip().lower()
#         else:
#             print("You have already used your lifeline!")
#             user_choice = input("Select your answer: ").strip().lower()

#     if user_choice == q["answer"]:
#         total_amount = q["prize"]
#         print(f"you have won: {total_amount}")

#         if total_amount >= 15000:
#             safe_haven = 15000
#             print("safe haven reached! 15000 is guaranteed")
#     else:
#         print(f"\nWrong answer! Game Over.")
#         print(f"You drop down to your Safe Haven amount: ₹{safe_haven}")
#         break

# print(f"thanks for playing kbc {player}, your total earning is: {total_amount}")

# price = 7.696969
# print(f"the price of this is: {price: .2f}")
# print(type(f"yes it will be:{2*4}"))

# def square(n):
#     '''take in a number n and returns the square of n'''
#     return n**2
# result = square(5)
# print(result)
# print(square.__doc__)

# double_result = result * 2       # 25 * 2 = 50
# add_ten = result + 10            # 25 + 10 = 35

# print(double_result)

# print("----fibonacci sequance----")
# def fibonacii(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibonacii(n - 1) + fibonacii(n - 2) 

# print(f"f(5) = {fibonacii(5)}")
# result = fibonacii(5)
# print(result)

# for i in range(6):
#     print(fibonacii(i))
# print("_"*40)

# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)  

# result = factorial(5)
# print(result)

# print("----CLI TOOL----")
# def factorial(n):
#     '''takes in your number n and calculates the total number of ways you can arrange them in specific group of items'''
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# def fibonacci(n):
#     '''The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones'''
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#        return fibonacci(n - 1) + fibonacci(n - 2)   
    
# def square(n):
#     '''take in a number n and returns the square of n'''  
#     return n**2  

# def countdown(n):
#     '''Recursively counts down from n to 0 and prints a blast-off message'''
#     if n<= 0:
#         print("blast off!!")
#         return
#     else:
#         print(f"{n}")
#         countdown(n-1)    

# print("_" * 40)        
# print("_" * 40)
# print()

# print("           MATHS CLI TOOL")
# print("_" * 40)
# print("_" * 40)

# while True:
#     print("\n select your option")
#     print("1) factorial")
#     print("2) fibonacci")
#     print("3) square")
#     print("4) countdown")
#     print("5) exit")

#     choice = int(input("enter your option: "))

#     if choice == 1:
#         print(f"INFO: {factorial.__doc__}")
#         n = int(input("enter your choice of number: "))
#         print(f"result = {factorial(n)}")
    
#     elif choice == 2:
#         print(f"INFO: {fibonacci.__doc__}")
#         num = int(input("enter your choice of num: "))
#         print(f"result = {fibonacci(num)}")

#     elif choice == 3:
#         print(f"INFO: {square.__doc__}")
#         num = int(input("enter number: "))
#         result = (f"{square(num)}")

#     elif choice == 4:
#         print(f"INFO: {countdown.__doc__}")
#         num = int(input("enter number: "))
#         result = (f"{countdown(num)}")

#     elif choice == 5:
#         print("GOODBYE!")
#         exit
#     else:
#         print("ivalid! enter a int")    
       


# def fruit(f):
#     ''' fruits are of huge variety,they are great source of vitamins , iron , magnesium , and many diff things
#     they are also used in medicene , fruits are mostly seasonal'''
#     print(f"perfect choice {f}")

# fruit("mango")
# print(fruit.__doc__)

 
# import time

# current_time = time.localtime()

# if current_time.tm_hour >= 0 and current_time.tm_hour < 12:
#     print("Good morning")
# elif current_time.tm_hour >= 12 and current_time.tm_hour < 18:
#     print("Good afternoon")
# else:
#     print("Good evening")

# print("put all your items here")
# customer_name = input("your name: ")
# tax_rate = 0.08
# cart = [
#     {"name": "pen", "price": 10, "qty": 2},
#     {"name": "notebook", "price": 80, "qty": 3},
#     {"name": "book", "price": 150.05, "qty": 7},
# ]


# subtotal = 0
# print("here is you receipt")
# print("========================================")
# print(f"           {customer_name.upper()}         ")
# print("           OFFICIAL RECEIPT                 ")
# print("========================================")
# for item in cart:
#     item_total = item["price"] * item["qty"]
#     subtotal += item_total
#     print(f"{item['name']:<12} @{item['price']:.2f} x{item['qty']} = ₹{item_total:.2f}")

# print("----------------------------------------")
# tax_amount = subtotal * tax_rate
# grand_total = subtotal + tax_amount

# print(f"{'subtotal:':<25} ₹{subtotal:.2f}")
# print(f"{'tax_amount:':<25} ₹{tax_amount:.2f}")
# print(f"{'grand_total:':<25} ₹{grand_total:.0f}")

# print("----------------------------------------")
# print("thank you for shopping from us")
# s = {"aastha", 67, 10.12 }
# print(s)

# a = {" "}
# print(type(a))
# s = set()
# print(type(s))
# for value in s:
    # print(value, end=" ")
    # print(value) 
# set1 = {1, 2, 4, 5, 6}
# set2 = {3, 6, 7,}
# set3 = {8, 7, 9}
# set4 = set1.union(set3)
# set4 = set1.copy()
# print(set1.union(set2))
# set1.update(set2, set3)
# print(set1,set2)
# print(set1)
# set4.update(set2)
# print(set4)
# set4 = set1.intersection(set2)
# print(set4)
# set4 = set1.copy()
# set4.intersection_update(set2)
# print(set4)
# set4 = set1.symmetric_difference(set2)
# print(set4)
# set4 = set1.difference(set2)
# print(set4)
# set4 = set1.copy()
# set4.difference_update(set2)
# print(set4)

# print(set1.isdisjoint(set2))

# print(set1.issuperset(set2))
# set4 = set1.issuperset(set2)
# print(set4)

# print(set1.issubset(set2))

# set1.pop()
# print(set1)
# set1.add(18)
# print(set1)

# rr = set1.union(set2)
# print(rr)

# set4 = set1.isdisjoint(set2)
# print(set4)

# python_class = {"aastha", "ajay", "vedu", "sneha"}
# web_dev_class = {"kanta", "nidhi", "rachna", "aastha", "vedu"}

# both_class = python_class.intersection(web_dev_class)
# print(both_class)
# print()
# all_students = python_class.union(web_dev_class)
# print(all_students)
# print()
# loyal_python_students = python_class.difference(web_dev_class)
# print(loyal_python_students)
# print()
# one_course = python_class.symmetric_difference(web_dev_class)
# print(one_course)
# print()
# loyal_web = web_dev_class.difference(python_class)
# print(loyal_web)

# vip_guest = ["aastha", "ajay", "kanta", "vedu", "nidhi", "rachna" ]
# guest = ["karan aujla", "pen", "pencil", "roti","cherry"]

# vip_guest = set(vip_guest)
# print(vip_guest)
# common_list = set(guest)
# print(common_list)
# already_inside = set()

# print("good evening")
# print("welcome to the wedding")
# print()

# import sys

# while True:
#     name = input("help me with your name: ").strip().lower()
#     if not name:
#         print("invalid input")
#         sys.exit()

#     if name in already_inside:
#         print(f"w8 someone named {name.title()} is already inside")
#         continue

#     if name in vip_guest:
#         print("welcome, you are a VIP guest")
#         already_inside.add(name)
#         break
#     elif name in common_list:
#         print("welcome to the wedding")
#         already_inside.add(name)
#         break
#     else:
#         remove = input("do you want to remove your name from the list (yes/no): ").strip().lower()
#         if remove == "yes":
#             # attempt to remove from guest lists if present
#             removed = False
#             if name in vip_guest:
#                 vip_guest.discard(name)
#                 removed = True
#             if name in common_list:
#                 common_list.discard(name)
#                 removed = True
#             if removed:
#                 print(f"{name.title()} has been removed from the lists")
#             else:
#                 print(f"{name.title()} was not found on any list")
#         else:
#             print("Okay, no changes made")

# print("----amazon----".upper())
# phone_tags = {"5g", "camera", "electronics", "latest", "phone"}
# laptop_tags = {"electronics", "computer", "lenavo", "itel", "gaming", "work"}
# accessory_tags = {"wireless", "charger", "cover", "phone holder"}
# speaker_tags = {"speaker", "tv", "wireless"}
# buds_tags = {"bluetooth", "wireless", "waterproof"}


# user_search = input(" what are you looking for: ")

# products = set(user_search.lower().split())

# if products & phone_tags:
#     print("Phones found")
# if products & laptop_tags:
#     print("Laptops found")
# if products & accessory_tags:
#     print("Accessories found")
# if products & speaker_tags:
#     print("Speakers found")
# if products & buds_tags:
#     print("Buds found")
#     print("⚠️ Note: Buds are currently OUT OF STOCK!")
# if not products & (phone_tags | laptop_tags | accessory_tags | speaker_tags | buds_tags):
#     print("No matching products found")


# class8 = {"aastha" : 1, "ajay" :2, "akshita" : 3, 'dhruv': 4, 'dau' : 5, "gaurav": 6, "hina": 7 }
# from pprint import pprint
# pprint(class8)
# for items in class8:
    # print(items)
# for key, value in class8.items():
    # print(f"{key}: {value}")    

# print(class8["aastha"])    
# print(class8.get("aastha"))

# for key in class8.keys():
    # print(f"roll no. of {key} is {class8[key]}")

# print(class8.items())

# class8.update({"isha": 8})
# print(class8)

# class8.clear()
# print(class8)
# h = {}
# print(h)

# class8.pop("gaurav")
# print(class8) 
# class8.popitem()
# print(class8)

# del class8["aastha"]
# print(class8)
# import time 

# print("----welcome to the store----")

# current_time = time.localtime()

# if current_time.tm_hour >= 0 and current_time.tm_hour < 12:
#     print("jai shaiya ram")
# elif current_time.tm_hour >= 12 and current_time.tm_hour < 18:
#     print("jai shaiya ram")
# else :
#     print("jai shaiya ram")

# items = {
#     "milk": 60,
#     "bread": 40,
#     "eggs": 90,
#     "butter": 250,
#     "cheese": 180,
#     "rice": 80,
#     "flour": 45,
#     "sugar": 42,
#     "apples": 120,
#     "bananas": 50,
# }

# print("available items:")
# for product, price in items.items():
#     print(f"- {product}: ₹{price}")

# user_choice = input("haji bolo: ").strip().lower()
# selected_items = [item.strip() for item in user_choice.replace(",", " ").split()]

# valid_items = []
# for item in selected_items:
#     if item in items:
#         valid_items.append(item)
#     else:
#         print("kone")



# if not valid_items:
#     print("abanu his khtm huyo , sham tk ahjajiyo")
# else:
#     name = input("naam bolo: ")
#     print("recipt lelo")

#     print("========================================")
#     print(f"           {name.upper()}         ")
#     print("           OFFICIAL RECEIPT                 ")
#     print("========================================")

#     subtotal = 0
#     for item in valid_items:
#         try:
#             qty = int(input(f"khatri {item}: "))
#             if qty <= 0:
#                 raise ValueError
#             print("lo sa")
#         except ValueError:
#             print("invalid quantity, please enter a positive number")
#             continue

#         item_price = items[item]
#         item_total = item_price * qty
#         subtotal += item_total
#         print(f"{item:<12}: @{item_price} x {qty} = ₹{item_total:.2f}")

#     print("----------------------------------------")

#     tax_rate = 0.08
#     tax_amount = tax_rate * subtotal
#     grand_total = subtotal + tax_amount
#     print(f"subtotal = ₹{subtotal:.2f}")
#     print(f"tax_amount = ₹{tax_amount:.2f}")
#     print(f"grand_total = ₹{grand_total:.2f}")
#     print("----------------------------------------")
#     print("thank you for shopping")

# for i in range(6):
    # print(i)
    # if i == 4:
        # break

# else:
    # print('sorry no i')
# i = 0
# while i<8:
    # print(i)
    # i = i+1
# else:
    # print('sorry no i')    

# for x in range(8):
    # print(f"this is no {x+1}")
# else:
    # print("that's it")    
# try:
#     numm = int(input("enter a number: "))
#     a = [2,5]
#     print(a[numm])
# except ValueError:
#     print("Invalid integer input")
# except IndexError:
#     print("Index out of range")

# student_data = {
#     "Aastha": {
#         "Python": 99,
#         "Math": 98,
#         "Database": 95
#     },
#     "Rohan": {
#         "Python": 78,
#         "Math": 82,
#         "Database": 80
#     },
#     "Priya": {
#         "Python": 95,
#         "Math": 91,
#         "Database": 89
#     },
#     "Rahul": {
#         "Python": 65,
#         "Math": 70,
#         "Database": 72
#     },
#     "Neha": {
#         "Python": 90,
#         "Math": 91,
#         "Database": 80
#     }
# }

# top_student = ""
# highest_avg = 0

# for name , subject in student_data.items():
#         # print(f"{name} {subject}")
#         score = subject.values()
#         total_score = sum(score)
#         avg = total_score / len(score)

#         if avg >= 90:
#                 grade = 'A'
#         elif avg >=80:
#                 grade = 'B' 
#         elif avg >=70:
#                 grade = 'C'
#         else:
#                 grade = 'D'
#         print(f"{name:<12}- average: {avg:.2f}% | grade: {grade}")

#         if avg > highest_avg:
#                 highest_avg = avg
#                 top_student = name 

# print(f"Class Topper is {top_student} with {highest_avg:.2f}%!")        
# import time

# print("----grocery bill----")
# current_time = time.localtime()
# if current_time.tm_hour >= 0 and current_time.tm_hour < 12:
#     print("good morning")
# elif current_time.tm_hour >= 12 and current_time.tm_hour < 16:
#     print("good afternoon")
# else:
#     print("good eveing")       

# print("put all your items here")

# cart = [
#     {"item": "Milk", "price": 50, "quantity": 2},
#     {"item": "Bread", "price": 30, "quantity": 1},
#     {"item": "Eggs", "price": 6, "quantity": 12},
#     {"item": "Butter", "price": 100, "quantity": 1}
# ]

# subtotal = 0
# tax_rate = 0.08
# name = input("your name please: ")
# print("========================================")
# print(f"           {name.upper()}         ")
# print("           OFFICIAL RECEIPT                 ")
# print("========================================")

# for item in cart:
#     item_total = item["price"] * item["quantity"]
#     subtotal += item_total
#     print(f"{item['item']:<12} {item['quantity']} @{item['price']:.2f} = {item_total:.2f}")

# tax_amount = subtotal * tax_rate
# grand_total = tax_amount + subtotal
# print(f"tax_rate: {tax_rate}")
# print(f"subtotal: {subtotal:.2f}")
# print(f"grand total: {grand_total:.2f}.")
# def func1():
#     try:
#         l =[1, 3, 5, 6]
#         i = int(input('enter index: '))
#         print(l[i])
#         return 1
#     except:
#         print("error")
#         return 0

#     finally:
#         print("permanent")
# print("sameeeeeee")    

# x = func1()
# print(x)

# try:
    # l = [1, 3, 5, 7]
    # a = int(input("enter index: "))
    # print(l[a])
# except:
    # print("index in l only")
    # raise IndexError("value should be under l index range")


# class MinorError(Exception):
#     pass

# def voting_eligiblity(age):
#     if age<18:
#         raise MinorError("age must be greater than 18")
#     else:
#         print("eligible for voting")
       

# try:
#     age = int(input("enter your age: "))
#     voting_eligiblity(age)
# except MinorError as error:
#     print(f"error caught: {error}")
# except ValueError:      
#     print("enter valid age")     

# import random
# import string

# print("----secret language coding and decoding----")
# user_message = input("enter your message: ")
# user_choice = input("encode or decode?: ").strip().lower()

# words = user_message.split()
# new_words = []


# if user_choice == "encode":
#     for word in words:
#         if len(word) >= 3:
#             r1 = "".join(random.choices(string.ascii_lowercase, k=3))
#             r2 = "".join(random.choices(string.ascii_lowercase, k=3))
#             encoded_word = r1 + word[1:] + word[0] + r2
#             new_words.append(encoded_word)
#         else:
#             new_words.append(word[::-1])
#     result = " ".join(new_words)
#     print(f"encoded word : {result} ")

# elif user_choice == "decode":
#     for word in words:
#         if len(word) >= 6:
#             stripped_word = word[3:-3]
#             decoded_word = stripped_word[-1] + stripped_word[:-1]
#             new_words.append(decoded_word)
#         else:
#             new_words.append(word[::-1])
#     result = " ".join(new_words)
#     print(f"decoded word: {result}")

# a = 11
# b = 100
# print('A')if a>b else print('=') if a == b else print('B')

# C = 2009 if a < b else ''
# print(C)

# flag = True if 2 * 4 == 8 else False
# print(flag)
# result = True if 2 * 4 == 8 else False
# print(result)

# marks = [1, 60, 45, 98, 76, 67, 28]
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("INDEX IS 3")
#     index +=1

# marks = [1, 60, 45, 98, 76, 67, 28]
# for index,mark in enumerate(marks):
#     print(mark)
#     print(index,mark)

# fruits = ["apple", "mango"]
# for index , fruit in enumerate(fruits, start= 1):
#     print(index, fruit)

# words = ["python", "java", "c++", "ruby", "javascript"]
# for index, word in enumerate(words):
    # if index % 2 != 0:
        # print(index , word)

# scores = [45, 88, 72, 30, 95]
# for index,score in enumerate(scores):
#     status = "passed" if score >=50 else "failed"
#     print(f"#{index}: {status} {score}")
    # or
    # print()
    # print(f"{index}: {'passed' if score >=50 else 'failed'}")
# n = int(input("enter your number: "))
# for n in range(0, n+1 ):
#     print(n ** 2)
# def is_leap(year):
#     if year % 4 !=0:
#         print(False)
#     else:
#         (True)
#     # Write your logic here
# year = int(input())
# print(is_leap(year))
# is_leap(1990)

# import math
# from math import sqrt, pi 
# from math import *
# import math as m
# from math import sqrt as s
# from math import pi as p
# import math as math_builtin_python
# result = math_builtin_python.sqrt(9) * math_builtin_python.pi
# print(result)

# import math
# print(dir(math))
# print(math.nan, type(math.nan))
# print(type(math.sin))
# result = m.sqrt(7)

# def hie():
#     print("how are you")

# aastha = "is learning python"

# def hie():
    # print("how are you")


# aastha = "is learning python"

# from calculator import hie, aastha
# from calculator import *
# import calculator as cl
# print(cl.aastha)
# cl.hie()


# n = int(input())
# for i in range(1, n + 1):
#     print(i)

# n = int(input())
# arr = list(map(int, input().split()))
# arr = set(arr)
# dec = sorted(arr, reverse=True)
# # list(arr)
# winner = dec[0]
# runner_up = dec[1]
# print(runner_up)

# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     name_chars = [name, score]
#     aec = sorted(name_chars)
#     second_lowest_student = aec[1]

# students = []
# scores = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students.append([name, score])
#     scores.append(score)

# unique_scores = sorted(set(scores))
# second_lowest_score = unique_scores[1]

# students.sort()
# for student in students:
#     if student[1] == second_lowest_score:
#         print(student[0])


# import os
# if(not os.path.exists("data")):
#     os.mkdir("data")

# print(os.getcwd())

# for i in range(0, 10):
#     folder_path = f"data/day{i+1}"
#     if not os.path.exists(folder_path):
#         os.mkdir(folder_path)
#     # os.rename(folder_path, f"data/day_{i+1}")
#     folder =  os.listdir("data")
#     for folde in folder:
#         print(folde) 

# x = 10 #global variable

# def my_function():
#     global x
#     x = 15 #modifying the global variable
#     y = 20 #local variable
#     print(y)

# my_function()
# print(x)  # This will print 15, as x was modified within the function


# f = open("data/day1/sample.txt", "w")
# f.write("Hello, World!\n")

# f = open('work.py', 'w')
# f.write('Hie barbiee')
# f.close()

# f = open('work.py', 'r')
# content = f.read()
# print(content)
# f.close()

# f = open('work.py', 'a')
# f.write('hie ken')
# f.close()  

# with open('work.py', 'r') as a:
#     content = a.read()
#     print(content)

# f = open('work.py', 'r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     print(f"line {i}: {line.strip()}")
# f.close()

# f = open('work.py', 'w')
# f.write('"hie barbiee"')
# f.close()

# # f = open('work.py', 'r')
# # content = f.read()
# # print(content)
# # f.close()

# f = open('work.py', 'a')
# f.write('"hie ken"\n'
# '"wanna go for a ride"\n'
# '"sure ken"')
# f.close()

# with open('work.py', 'r')as f:
#     content = f.read()
#     print(content)

# with open ('work.py', 'r')as f:
#    i = 0
#    while True:
#        i = i+1
#        line = f.readline()
#        if not line:
#            break
#        print(f"line {i}: {line.strip()}")
# with open('work.py', 'r+') as f:
#      f.truncate(6)  # Truncate the file to 6 bytes
#      print(type(f))
#      f.seek(5)
#      print(f.tell())
#      data = f.read(10)
#      print(data)
    #  print(f"file truncated to 10 bytes. Current file size: {f.tell()} bytes")
    #  f.seek(0)  # Move the file pointer back to the beginning
    #  data = f.read()  # Read the remaining content after truncation
    #  f.truncate(5)
    #  f.seek(0)
    #  data = f.read()
    #  print(data)
       # print(data)  # This will read the remaining content after truncation

# double = lambda x: x*2
# cube = lambda x: x**3
# avg = lambda x,y : (x+y)/2
# print(avg(9,8))
# print(cube(3))
# print(double(4))

# def appl(fx, value):
#     return 6 + fx(value)

# print(appl(cube, 8))
# print(appl(double, 5))
# print(appl(lambda x: x**4, 2))
# print(appl(lambda x: x**3, 2))


# with open('work.py', 'w') as f:
#     f.write("'how are you?'\n967286 , 'i am fine'\n'what about you?'\n'good to hear that'\n'yes i am good too'")
#     print(f.tell())
    # f.seek(0)
    # data = f.readline()
    # print(data)

l = [1, 9, 6, 2, 5, 3, 8, 4, 7]
# newl = sorted(l)
# print(newl)
# newl = sorted(l, reverse=True)
# print(newl)
# newl = sorted(l, key=lambda x: x%3)
# print(newl)
# newl = list(map(lambda x: x**2, l))
# print(newl)
# newl = list(filter(lambda x: x%2==0, l))
# print(newl)
# newl = list(map(lambda x: x**2, filter(lambda x: x%2==0, l)))
# print(newl)
# newl = list(map(lambda x: x**2, filter(lambda x: x%2==0, sorted(l))))
# print(newl)l
# newl = list(map(lambda x: x**2, filter(lambda x: x%2==0, sorted(l, reverse=True))))
# print(newl)
# cube = lambda x: x**3
# newl = list(map(cube,l))
# print(newl)
# def filter_even(x):
#     return x%2==0
# newl = list(filter(filter_even, l))
# print(newl)

# from functools import reduce

# # result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
# # print(result)

# def mysum(x, y):
#     return x +y

# newl = reduce(mysum , l)
# print(newl)

# for i in range(1, 5):
     # print(str(i) * i)
#         print((str(i) + " ")* i)

# import random

# secret_number = random.randint(1, 100)
# print()
# print("----random number guessing game---- \n")
# print("I have selected a number between 1 and 100. Try to guess it!")
# print("You have 5 attempts to guess the correct number.\n")
# user_input = int(input("Attempt 1: Enter your guess: "))
# if user_input != secret_number:
#     for attempt in range(1, 5):
#         user_input = int(input(f"Attempt {attempt + 1}: Enter your guess: "))
#         if user_input == secret_number:
#             print("Congratulations! You guessed the correct number.")
#             break
#         elif user_input < secret_number:
#             print("Too low! Try guessing a higher number.")
#         else:
#             print("Too high! Try guessing a lower number.")
#     else:
#         print(f"Sorry, you've used all attempts. The correct number was {secret_number}.")    


# import random
# import string
# print()
# print("----random password generator----\n")
# length = int(input("Enter the desired length of the password: "))
# password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
# print(f"Generated password: {password}")


# import random

# print("----stones, paper, scissors game----")
# sps = random.choice(["stone", "paper", "scissors"])
# # print(f"Computer chose: {sps}")
# user_choice = input("Enter your choice (stone, paper, scissors): \n").strip().lower()
# if user_choice != sps:
#     if (user_choice == "stone" and sps == "scissors") or (user_choice == "paper" and sps == "stone") or (user_choice == "scissors" and sps == "paper"):
#         print(f"Computer chose: {sps}. You win!")
#     else:
#         print(f"Computer chose: {sps}. Computer wins!")

import random
print()
print("----random number guessing game----\n")
print("I have selected 5 random numbers between 1 and 20. Try to guess one of them!")
number = [random.randint(1, 20) for _ in range(5)]
for attempt in range(1, 11):
    user_input = int(input(f"Attempt {attempt}: Enter your guess (1-20): "))

    if user_input in number:
        number.remove(user_input)
        print(
            f"Congratulations! You guessed {user_input}. Remaining numbers to"
            f" guess: {len(number)}\n"
        )
        if len(number) == 0:
            print("You won! You found all 5 numbers!")
            break
    elif user_input < min(number):
        print("Too low! Try guessing a higher number.")
    elif user_input > max(number):
        print("Too high! Try guessing a lower number.")
    else:
        print("Incorrect guess! Try again.")    
else:
    print("you have run out of attempts. The correct numbers were: ", number)            
