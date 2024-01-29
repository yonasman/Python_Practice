a = {}
while True:
   name = input("What is your name? ")
   score = int(input("Enter score from 0-10: "))
   if name == "":
      break
   # if score > 10 and score < 0:
   #    break
   if score not in range(0,11):
      break
   if name in a.keys():
      a[name] += (score,)
   else:
      a[name] = (score,)
for name in a.keys():
      adding = 0
      counter = 0
      for score in a[name]:
         adding += score
         counter += 1
      print(f"{name}, your average is {adding/counter}")

