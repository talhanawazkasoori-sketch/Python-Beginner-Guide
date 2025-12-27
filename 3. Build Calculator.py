str_a = input('Enter 1st Number: ')
str_b = input('Enter 2nd Number: ')

# print(type(str_a))
# print(type(str_b))

# str_a = int(str_a)
# str_b = int(str_b)
# As it doesnt work for numbers with decimal points

#Now for Decimal numbers
str_a = float(str_a)
str_b = float(str_b)

total = str_a + str_b
print(total)

#Default Data-Type Functions i need to know about
# str()
# float()
# int()
# bool()

# list()
# tuple()
# set()
# dict()

# Convert Data-Types
# Numbers
x          = 10
str_x      = str(x)   #Convert intiger to string: 10
float_x    = float(x) #Convert intiger to float: 10.0
bool_x     = bool(x)  #Convert intiger to boolean: True(Non zero is True)
bool_neg_x = bool(0)  #Convert 0 to boolean: False
# and other Data-Types conversion