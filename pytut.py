# Basic python programmes syntaxes

print "Hello world"
phrase= "ulooi uio"

print(phrase[2]) #2ND ELEMENT IN THE STRING
print(phrase.index("i")) #index of the given letter
print(phrase.replace("uio","umamam"))#replacing

num =122
print(num)
print(str(num) + "is a good number")
print(str(num))#converting into string
value = -33
print(abs(value))#the absolute
print(pow(122,2))#power of the number
print(pow(5,3))#power of 3 thimes 5

# Inputting your name
# name = raw_input("What is your name: ")#in python 2.0 we use raw_input and in python 3 we use just input
# print("My name is" + name + "!")
  
# newname = raw_input("The new name is :")
# print("The newest name is "+newname)

        #lists

friends =['Haley','kendall','jacob','kim','luis','Avdol','paul']
print(friends)
print(friends[2])
print(friends[1:4])
friends.append("SAleem")
friends.insert(1,'tully');
print(friends)
friends.remove("kim")
print(friends)
friends.index('Haley')
friends.pop()#remove the last element
print(friends)



lucky_nums =[2,4,6,7,9,44,56,78,89,33,67,14,41]
print(lucky_nums)
lucky_nums.sort()
print(lucky_nums)
lucky_nums.reverse()
print(lucky_nums)

# same_nums = lucky_nums.copy()
# print(lucky_nums)

#tuples

some_tuples =[(1,2),(3,5),(11,23),(45,54),(55,78),(00,21)]
print(some_tuples)
print(some_tuples[2])

some_tuples[1]= 33
print(some_tuples)

