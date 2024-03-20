# exercise 1
# Write a function called nested_sum that takes a list of lists of integers and adds up
# the elements from all of the nested lists. For example:
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21
# answer
# *************
t = [[1, 2], [3], [4, 5, 6],[5]]

def nested_sum(t):
    sum = 0
    for e in t:
        for i in e:
            sum += i
    return sum
# print(nested_sum(t))
# exercise 2
# Write a function called cumsum that takes a list of numbers and returns the cumu-
# lative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
# original list. For example:
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]
# answer
# **********
t = [1, 2, 3]

def custom(par):
    new = []
    for e in par:
        sum = 0
        for i in range(par.index(e) + 1):
            sum += par[i]
        new.append(sum)
    return new
# print(custom(t))

# exercise 3
# Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements. For example:
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]
# answer
# *******************
t = [1, 2, 3, 4]
def middle(par):
    new_array = []
    for i in range(len(par)):
        if(i == 0 or (i == len(par) - 1)):
            continue
        else:
            new_array.append(par[i])
    return new_array
# print(middle(t))
# exercise 4
# Exercise 10.4. Write a function called chop that takes a list, modifies it by removing the first and
# last elements, and returns None. For example:
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t
# [2, 3]
# answer
# *************
t = [1, 2, 3, 4]

def chop(par):
    for i in range(len(par)):
        if(i == 0 or (i == len(par) - 1)):
            par.pop(i)
# print(chop(t))
# print(t)

# exercise 5
# Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. For example:
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b', 'a'])
# False
# answer
# **************
def is_sorted(par):
    for i in range(len(par) - 1):
        if(par[i] > par[i + 1]):
            return False
        
    return True
# print(is_sorted(['b','a']))
# exercise 6
# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.

# answer
# *****************
def is_anagram(word1,word2):
    if(len(word1) == len(word2)):
        for e in word1:
            if(e in word2):
                return True
    else:
        return False
# print(is_anagram('cat','taccat'))    
# Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there
# is any element that appears more than once. It should not modify the original list.
t = [1,2,3,4,5,6,7,6]
def has_duplicates(par):
    count = 0
    for i in range(len(par)):
        for j in range(i + 1,len(par)):
            if(par[i] == par[j]):
                count += 1
    if(count >= 1):
        return True
    else:
        return False
# print(has_duplicates(t))

# exercise 8
t = "parrot"
def histogram(par):
    dup = {}
    for e in par:
        if(e not in dup):
            dup[e] = 1
        else:
            dup[e] += 1
    return dup
# print(histogram(t))
# exercise
# Write a function called most_frequent that takes a string and prints the let-
# ters in decreasing order of frequency.
# answer
# *************
def most_frequent(arg):
    d = {}
    for e in arg:
        d[e] = d.get(e,0) + 1
    for key in sorted(d .items(),key=lambda x:x[1],reverse=True):
        print(key)
# most_frequent("parrot")
# exercise
# reading file and writing to a file
# answer
# # ******************
# with open("./hello.txt","w") as file:
#     data = file.write("I wrote in it.")
with open("./hello.txt",'r') as file:
    data = file.read()
    a = data.split()
    # print(a)
# ********************
tpl1 = (1,2,3)
tpl2 = ('a','b','c')
zipped1 = zip(tpl1,tpl2)
result = (zipped1)
# for number,letter in result:
#     print(f"{number} ---> {letter}")
# result.append((1,2))
# print(result)
list1 = [1,2,3]
list2 = ['a','b','c']
zipped2 = zip(list1,list2)
result2 = list(zipped2)
# result2.append((1,2))
# print(result2)
dict1 = {1:'a',2:"b"}
dict2 = {3:'c',4:'d'}
zipped3 = zip(dict1.items(),dict2.items())
# r3 = dict(zipped3)
# r3.update({5:'e'})
# print(r3)
import time
ls1 = [1,2,3,4]
tp1 = (1,2,3,4)
dict = {1:'a',2:'3'}

dict1 = {1:'a',2:'b',3:'c'}
# print(dict1.items())
# for key,value in dict1.items():
    # print(f"{key} ---> {value}")
ls = ['a','b','c']
# for index,value in enumerate(ls,start = 1):
    # print(f"{index} ---> {value}")
#Output:
test2 = { 
    'Stud1': ['CS1101', 'CS2402', 'CS2001'], 
    'Stud2': ['CS2402','CS2001','CS1102'] 
    } 
# test2 = {
#     "Stud1": ["Math", "Physics"],
#     "Stud2": ["Chemistry", "Physics"]
# }
# def invert_dict(arg):
#     new_dict = {}
#     print("The given dictionary")
#     print("-----------------------")
#     print(arg)
#     for value in arg.values():
#         for item in value:
#             if(item in arg["Stud1"] and item in arg["Stud2"]):
#                 new_dict[item] = ["Stud1","Stud2"]
#             elif (item in arg["Stud1"]):
#                 new_dict[item] = ["Stud1"]
#             else:
#                 new_dict[item] = ["Stud2"]
#     print("The inverted dictionary")
#     print("-----------------------")
#     print(new_dict)
# invert_dict(test2)
# Inverted Output: 
def inverted_dict(arg):
    print("The original dict")
    print("-----------------")
    print(arg)
    inverted_dict = {}
    for keys,values in arg.items():
        for value in values:
            inverted_dict.setdefault(value,[]).append(keys)
    print("The inverted dict")
    print("----------------")
    print(inverted_dict)
inverted_dict(test2)
{ 

'CS1101': ['Stud1'], 

'CS2402':['Stud1','Stud2'], 

'CS2001': ['Stud1','Stud2'] ,

'CS 1102':['Stud2'] 

}
{'CS11011': ['Stud1'], 'CS2402': ['Stud1', 'Stud2'], 'CS2001': ['Stud1', 'Stud2'], 'CS1102': ['Stud2']}