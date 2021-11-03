# Udemy lectures
## lists and strings
print('hello')
num = 12
name = 'Sam'
print('My number is {one} and my name is {two}'.format(one=num,two=name))
my_list = ['a','b','c']
my_list.append('d')
print(my_list)
sss = 'hello'
print(sss[0])
nest = [1,2,[3,4]]
print(nest)
print(nest[2][1])
nest = [1,2,3,[4,5,['target']]]
print(nest[3][2][0])

## Dictionary
d = {'key1':'value','key2':'123'}
print(d['key1'])
print(d['key2'])

d = {'k1':[1,2,3]}
my_list = d['k1']
print(my_list[0])
print(my_list[1])
print(my_list[2])

d = {'k2':{'innerkey':[1,2,3]}}
print(d['k2'])
print(d['k2']['innerkey'])

print({1,2,3})
print('even with multiple values')
print({1,1,1,1,1,1,2,2,2,2,3,3})

## Tuples
my_list = [1,2,3]
print(my_list)
t = (1,2,3)
print(t[0])
my_list[0]='NEW'
print(my_list)
#t[0]='NEW' #tuple boject does not support item assignment.

## comparison -> boolean
print( 1 > 2 )
print( 1 <= 1 )
print( 1 == 2 )
print( 1 != 2 )
print( 'hi' == 'bye' )
print( 'hi' != 'bye' )
print( (1 < 2) and (2 < 3) )
print( (1 > 2) and (2 < 3) )
print( (1 > 2) or (2 < 3) )
print( True and True )
print( True and False )
print( True or False )

### this will return yep
#i = 2
### this will return yup
#i = 3
### this will return nope
i = 4
## if and elif statements
if i==2:
    print('yep!')
elif i==3:
    print('yup!')
else:
    print('nope!')

### Let's make that into a function and test all three cases!
def udemy_function(iValue=4):
    i = iValue
    if i==2:
        print('yep!')
    elif i==3:
        print('yup!')
    else:
        print('nope!')

udemy_function(2) # yep!
udemy_function(3) # yup!
udemy_function() # nope! because default is 4

## Function that returns instead of prints.
def square(num):
    """
    This is a doc string that gets displayed
    On jupyer notebook where you type the name of function without ()
    and shift+tab to see the details.
    """
    return num ** 2

output = square(2)
print( "2 squared is..." + str(output) )

## for loops
seq = [1,2,3,4,5]
for jellyBellyNum in seq:
    print(jellyBellyNum)
    print('hello')

## while loop
i = 1
while i < 5:
    print( 'i is: {}'.format(i) )
    i += 1

## range example
for x in range(0,5):
    print(x)

x = list(range(10))
out = []
for num in x:
    out.append(num**2)
print(out)

## List comprehansion (shorter version of the for loop in some cases)
out = [num ** 2 for num in x]
print(out)

## map() in memory
### with defined function
seq = [1,2,3,4,5,6]
print( list( map(square,seq) ) )
### with lambda expression
print( list (map( lambda num: num*3, seq)) ) 

## filter() even numbers from the seq
print( list ( filter( lambda num: num%2 == 0, seq)) ) 

## methods
s = 'hello my name is Sam'
print( s.lower() )
print( s.upper() )
print( s.split() )
tweet = 'Go Sports! #Sports'
print(tweet.split('#'))
print(tweet.split('#')[1])

## filter string from list
def countDog(st):
    count = 0
    for word in  st.lower().split():
        if word == 'dog':
            count += 1
    return count
print(countDog('This dog runs faster than the other dog dude!'))

## filter with lambda
seq = ['soup','dog','salad','cat','bob']
print(list(filter(lambda word: word[0] == 's', seq)))

## final problem
def caught_speeding(speed, is_birthday):
    """
    You are driving a little too fast, and a police officer stops you.
    Write a function to return one of 3 possible results:"No ticket", "Small ticket", or "Big Ticket".
    If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive,
    the result is "Small Ticket". If speed is 81 or more "Big Ticket". Unless it is your birthday (encoded as boolean)
    -- on your birthday, your speed can be **5 higher** in all cases
    """
    if is_birthday == True:
        speeding = speed - 5
    else:
        speeding = speed
    if speeding >= 81:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

print( caught_speeding(81, False) )
print( caught_speeding(83, True) )
print( caught_speeding(65, False) )
print( caught_speeding(65, True) )
print( caught_speeding(55, False) )