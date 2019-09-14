
# calling functions

def hello(name):
    print("Hello there "+ name)

hello("Salman")
hello("Steven")

def inform(name,age):
    print("His name is "+str(name)+" and he is "+str(age)+" old.")

inform("tony",34)
inform("Bruce",32)

#having return functions
def cube(num):
    return num*num*num

print(cube(5))
result = cube(8)
print(result)

#boolean operations or true/False

is_male =True
is_fmale =True

if is_male or is_fmale:
    print("He's alright")
else:
    print("Not cool aliens")

#if we are using 'and' then we have to make sure that either noth of them are true or booth are false

if is_fmale and is_male:
     print("It's a human")
else:
    print("It's a freaking alien")
#---------------------------------------#
is_male =False
is_fmale =True

if is_fmale and is_male:
     print("It's a human")
else:
    print("It's a freaking alien")

#------------------------------------#
if is_fmale and is_male:
     print("It's a human")
elif is_male and not(is_fmale):
    print("Is it possible")
else:
    print("It's a freaking alien")

#-----------------------------------#
if is_fmale and is_male:
     print("It's a human")
elif not(is_male) and is_fmale:
    print("This could be true")
else:
    print("It's a freaking alien")

#-------------------------------------#

#we can also write the two above fynctions as

if is_fmale and is_male:
     print("It's a human")
elif is_male and not(is_fmale):
    print("is it even possible")
elif not(is_male) and is_fmale:
    print("This could be true")
else:
    print("It's a freaking alien")

#-----------------------------------------#

def bignum(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print(str(n1)+ " is the greatest number")
    elif n2 > n1 and n2 > n3:
        print(str(n2)+" is the greatest number")
    else:
        print(str(n3)+"is the greatest number")

bignum(5,17,8)

#--------------------------------------------#
#return type,

def bignum(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return str(n1)+ " is the greatest number"
    elif n2 > n1 and n2 > n3:
        return str(n2)+" is the greatest number"
    else:
        return str(n3)+"is the greatest number"

print(bignum(34,56,674))

newnum = bignum(100,99,98)
print(newnum)

#---------------------------------------------#
#Using Dictionaries  
#using the most basic examples

months ={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

print(months["Feb"])

month8 = months["Aug"]
print(month8)

print(months.get("Sep"))
print(months.get("Luv","This is not a valid month"))#if we iput a wrong paramter for dictionary
#---------------------------------------------------------------------------------------------------
#Using for and while loops

i =0
while i<=20:
    print(i)
    i=i+1

#------------------------------------------------------------------------------

# guess = ""
# guess_word ="Halo"
# i =0

# while guess != guess_word:
#     # guess =str(raw_input("Enter your guess:"))
    # if guess == guess_word:
#           print("The guess is right.")          
#     elif guess != guess_word:
#         print("You wrong")
#     else:
#         print("There was no input")
  
#-----------------------------------------------------------------------

#multiple lists.

mul_nums =[
    [1,2,3],
    [11,22,33],
    [34,45,56],
    [44,14,52],
    [45,65],
    [45]
]

print(mul_nums)
#using for loop to print them.

for row in mul_nums:
    for cols in row:
        print(cols)

    

