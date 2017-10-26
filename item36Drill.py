#Assign an integer to a variable
number = 4


#Assign a string to a variable
string = 'This is a string'


#Assign a float to a variable
x = float (25.0/6.0 )


#Use the print function and .format() notation to print out the variable you assigned
print 'The variables are {0}, {1}, {2}'.format(number, string, x)

#Use each of these operators +, - , * , / , +=, = , %
print 4+2, 3-2, 5*5, 36/6, 9%2
y = 3
y += 2
print y

#Use of logical operators: and, or, not
if 3 < 4 and 5 > 4:
    print('condition met')
    
if 10 < 11 or 15 < 223:
    print('condition met')

#Use of conditional statements: if, elif, else
x = 10
if x == 10:
    print'x = 10'
elif x == 9:
    print'x = 9'
else:
    print 'x does not equal 9 or 10'

#Use of a while loop
counter = 0
while counter < 5:
    print counter
    counter += 1

#Use of a for loop
for counter in range(0,5):
    print counter

#Create a list and iterate through that list using a for loop to print each item out on a new line
favorite_games_list = ['Overwatch',
                     'PUBG',
                     'Hearthstone',
                     'Destiny']
for game in favorite_games_list:
    print game

#11. Create a tuple and iterate through it using a for loop to print each item out on a new line
candy = ('apple', 'orange', 'banana', 'chocolate')
print ('\n Flavors of candy that we have', candy)
print ('Your items: ')
for item in candy:
    print (item)

#12. Define a function that returns a string variable
    #Function that determines if a girl is too young for you or not
def allowed_dating_age(my_age):
    girls_age = my_age/2 +7
    return girls_age

dans_limit = allowed_dating_age(24)
carls_limit = allowed_dating_age(27)
glens_limit = allowed_dating_age(40)
print('Dan can date girls', dans_limit, 'or older')
print('Carl can date girls', carls_limit, 'or older')
print('Glen can date girls', glens_limit, 'or older')
