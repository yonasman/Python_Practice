# Working with files
# ****************************
#Exercise 1:
# Write a program that reads words.txt and prints only the words with more than 20
# characters (not counting whitespace).
# *******************
# Answer
# with open("words.txt",'r') as file:
#     for word in file:
#         data = word.strip()
#         if(len(data) > 20):
            # print(data)
# Exercise 2
# Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
# it.: 
# ***********
# answer
# def has_no_e(word):
#     if 'e' in word:
#         return False
#     else:
#         return True
# print(has_no_e("hello"))
# Exercise 3:
# Write a program that reads words.txt and prints only the words that have no “e”. Compute the
# percentage of words in the list that have no “e”.
# def has_no_e(file):
#     count = 0
#     total_words = 0
#     with open(file,'r') as f:  
#         for word in f:
#             total_words += 1
#             data = word.strip()
#             if 'e' not in data:
#                 print(data)
#                 count += 1
#         return f"The percentage of words that don't have letter 'e' is {(count/total_words) * 100}%"
# print(has_no_e("words.txt"))
# Exercise 4
# Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters.
# *****************
# answer
# def avoids(word,str):
#     for e in str:
#         if e in word:
#             return False
#     return True
# print(avoids("hello",'dfe'))
# Exercise 5
# Write a program that prompts the user to enter a string of forbidden letters and then prints the
# number of words that don’t contain any of them.
# **********************
# answer
# def no_avoids(word):
#     str = input("Please enter your forbidden letter: ")
#     count = 0
#     for e in word:
#         if e not in str:
#             count += 1
#     return f"The number of letter that aren't forbidden is {count}"
# print(no_avoids("hello"))

# Exercise 6
# Write a function named uses_only that takes a word and a string of letters, and
# that returns True if the word contains only letters in the list. 
# def uses_only(word,str):
#     if (len(word) != len(str)):
#         return False
#     for e in word:
#         if e not in str:
#             return False
#     return True
# print(uses_only("hello","hello"))
#Exercise 7
# Write a function named uses_all that takes a word and a string of required letters,
# and that returns True if the word uses all the required letters at least once. How many words are
# there that use all the vowels aeiou? How about aeiouy?
# def uses_all(word,str):
#     count = 0
#     with open(word,'r') as file:
#         f = file.read()
#         for words in f:
#             flag = True
#             for let in str:
#                 if let not in words:
#                     flag = False
#                     break
#             if(flag):
#                 count += 1        
#     return count
# print(uses_all("words.txt","aeoui"))
    # count = 0
    # for e in word:
    #     if e not in str:
    #         return False
    # return True
# Exercise 8
# Write a function called is_abecedarian that returns True if the letters in a word
# appear in alphabetical order (double letters are ok). How many abecedarian words are there?
# ************************
# answer
# def is_abecedarian(file):
#     with open(file,'r') as f:
#         count = 0
#         data = f.read()
#         fl = data.split()
#         for line in fl:
#             flag = True
#             line = line.lower()
#             for i in range(len(line) - 1):
#                 if line[i] > line[i + 1]:
#                     flag = False
#                     break
#             if(flag):
#                 count += 1
#     return count
# print(is_abecedarian("words.txt"))
# **********************
# try:
#     with open("/hello.txt", 'r') as f:
#         for line in f:
#             line = line.strip()
#             print(line)
# except FileNotFoundError:
#     print("File not found")
# except:
#     print("Some error occurred")
# else:
#     print("You printed the file successfully")
# finally:
#     print("File closed")
def dict_convertor_writer(f):
    # converting the file into dictionary
    try:
        with open(f, 'r') as file:
            lines = file.readlines()
            dictionary = {}
            inverted_dict = {}
            for line in lines:
                parts = line.strip().split(':')
                # print(parts)
                if len(parts) == 2:
                    key = parts[0].strip()
                    values = [value.strip() for value in parts[1].split(',')]
                    dictionary[key] = values
            # print(dictionary)
            # dictionary invertor
            for key,value in dictionary.items():
                for e in value:
                    if e in inverted_dict:
                        inverted_dict[e].append(key)
                    else:
                        inverted_dict[e] = [key]
            # print(inverted_dict)
            # writing to a file
            with open("inverted.txt",'w') as f:
                try:
                    f.write('{\n')
                    for keys,values in inverted_dict.items():
                        f.write(f"{keys}:{", ".join(values)}\n")
                    f.write('}')
                except Exception as e:
                    print("Error",e)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print('Error',e)
dict_convertor_writer("sample.txt")
