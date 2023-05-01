# def keywordagrdemo(no, name='Abdul', city='Hyderabad'):
#     print("no is ",no)
#     print("name is ",name)
#     print("lives in ", city)

# keywordagrdemo(123)
# keywordagrdemo(123,name="Salman")
# keywordagrdemo(245)
# keywordagrdemo(12)
# keywordagrdemo(name="Raja", city="Vijayawada",no=23455)

# function without parameters
# def Empdata():
#     name= input("Enter your name")
#     id= input("What is your ID")
#     salary = float(input("Enter salary"))
#     print("Employee name is",name)
#     print("ID is ",id)
#     print("Salary is",salary)


#Empdata()

# function with arguments / parmeters
# def add2numbers(no1, no2):
#     sum=no1+no2
#     #print(f"Sum of 2 numbers ={no1+no2}")
#     print(f"Sum of 2 numbers ={sum}")

# add2numbers(100,200)

# function with return value
# def difference2nos(no1,no2):
#     diffrence= no1-no2
#     return  diffrence

# dif=difference2nos(200,140)
# print("Difference of 2 Numbers =",dif)

# Define function GetNetSalary(basicSalary) , should return
#your net salary
# str="hello! How are you?"
# print(len(str))
# names=["Raju","Ameer", "Munna","Lilly"]
# print(len(names))

#merging & sorting list of lists and return it
# def sorted_merged_list(lists):
#     #global lists
#     #lists = [[2, 1, 5], [3, 2, 8, 6], [9, 6, 8, 3]]
#     mergelist = []
#     for i in lists:
#         for j in i:
#             mergelist.append(j)
#     #print("merged list=", mergelist)
#     mergelist.sort()
#     #print("sorted list is ", mergelist)
#     return  mergelist



# merging n lists and sorting all elements in ascending order
# mylists=[[2,1,5],[4,2,8,7],[3,8,4,6],[1,8,3,2]]
# print(sorted_merged_list(mylists))
# mylists=[[]]
# print(sorted_merged_list(mylists))


# import re
# def splitEmail(email):
#     firstsplit=re.findall(r"(\w+)",email)
#     secondsplit= re.findall(r"(\@\w*)",email)
#     thirdsplit = re.findall(r"\.\w*",email)
#     splitwords= [firstsplit[0],secondsplit,thirdsplit]
#     return  splitwords

# splitmailwords= splitEmail("ramees1234@gmail.com")
# print(splitmailwords)

# splitmailwords= splitEmail("radridgs9010@hotmail.uk")
# print(splitmailwords)

# Generate  n peranthesis
# def generatePeranthesis(n:int)-> list[str]:
#     if n <1 or n > 8 :
#         return "n must be between 1 and 8"
#     else:
#         p="("
#         q=")"
#         plist =[]

# word_list = ["Abdul", "Yesdani", "Shaik"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print("True")
#     else:
#         print("False")

#Encoding & Decoding a text
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# def encrypt(plain_text, shift_amount):
#    cipher_text = ""
#    for letter in plain_text:
#      position = alphabet.index(letter)
#      new_position = position + shift_amount
#      cipher_text += alphabet[new_position]
#    print(f"The encoded text is {cipher_text}")
# encrypt("hello",2)
# def decrypt(cipher_text, shift_amount):
#       plain_text = ""
#       for letter in cipher_text:
#           position = alphabet.index(letter)
#           new_position = position - shift_amount
#           plain_text += alphabet[new_position]
#       print(f"The decoded text is {plain_text}")

# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#  decrypt(cipher_text=text, shift_amount=shift)

# age finding
# import datetime
# def yourage(year,month,date):
#     age= datetime.date.today()-datetime.date(year,month,date)
#     years=age.days//365
#     print(years,"years")

# yourage(2000,11,21)
# distinct set from 2 lists
# list1=[12,2,3,4,5,6,7,8]
# list2=[4,5,61,1,2,2,3,12]
# distinct= set(list1+list2)
# print(list(distinct))

#years of services for a group of employees
# import datetime
# joiningyears=[2000,2010,2008,2020,2019,2012,2017]
# currentyear= datetime.date.today().year
# serviceyears=[currentyear- year for year in joiningyears]
# print(serviceyears)

# x=[2,3,4]
# y=[10,20,30]
# products= [a*b for a in x for b in y]
# products=[a*b for a in x for b in x]
# print(products)
# printing odd lenth words from a string
# str1="Hello Iam doing fine"
# words= str1.split(" ")
# for word in words:
#     if len(word)%2!=0:
#         print(word)

# function to find the longest length in the list
# def longWordfromString(sentence):
#     words=sentence.split(" ")
#     finalList = []
#     for word in words:
#         finalList.append((len(word), word))
#     finalList.sort()
#     print("longest word is:",
#           finalList[-1][1]," Count: ", len(finalList[-1][1]))

# words ="Micro management is unproductive"
# longWordfromString(words)

# print words from right side to left
# def rightToleft(longstr):
#     words=longstr.split(" ")
#     flipped= list(reversed(words))
#     print(flipped)
# rightToleft("Abdul! lets make it")
# def dictionaryDemo():
#     longstr = "Welcome to Abduls' Python sessions."
#     mylist = ["Welcome", "Abdul"]
#     dictionary = {}
#     for i in mylist:
#         occur = 0
#         lis1 = []
#         while (True):
#             x = longstr.find(i, occur)
#             if x != -1:
#                 lis1.append([x, x + len(i) - 1])
#                 occur = x + len(i)
#             else:
#                 break
#         dictionary.update({i: lis1})
#     print(dictionary)


# nos=[12,14,16]
# cubes= [n**3  for n in  nos]
# print(cubes)
# dictionaryDemo()

# x='Bike'
# y=x*(2**3)
# print(y)
# import logging
# import threading
# import time

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#
#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     #x.join()
#     logging.info("Main    : all done")

# from multiprocessing import Process
# import os
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# def abdulFnc(name):
#     info('abdulFnc')
#     print('hello', name)

# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=abdulFnc, args=('Abdul',))
#     p.start()
#     p.join()

# from collections import Counter
# import re
#  text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit
# corporation that holds the intellectual property rights behind
# the Python programming language. We manage the open source licensing
# for Python version 2.1 and later and own and protect the trademarks
# associated with Python. We also run the North American PyCon conference
# annually, support other Python conferences around the world, and
# fund Python related development with our grants program and by funding
# special projects."""
# words = re.findall('\w+',text)
# print(Counter(words).most_common(10))

# from collections import Counter, OrderedDict
# class OrderedCounter(Counter,OrderedDict):
#    pass
# word_array = []
# n = int(input("Input number of words: "))
# print("Input the words: ")
# for i in range(n):
#    word_array.append(input().strip())
# word_ctr = OrderedCounter(word_array)
# print(len(word_ctr))
# for word in word_ctr:
#    print(word_ctr[word],end=' ')

# def frequency_char(str1):
#    dict = {}
#    for n in str1:
#       keys = dict.keys()
#       if n in keys:
#          dict[n] += 1
#       else:
#          dict[n] = 1
#    return dict
#print(frequency_char('wanedomagerudgeo'))
