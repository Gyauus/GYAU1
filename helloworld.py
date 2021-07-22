print("Hello world")
x=4
y="Sally"
print(x)
x = 5
y = "John"
print(type(x))
print(type(y))

x = "awesome"
print("Python is " + x)
x="awesome" 
def myfunc():
    print("Python is " + x)
myfunc()    
#x="awesome"
#def myfunc():
    #global x
    #x="fantastic"
    #print("Python is " + x)

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

    #myfunc()
    #print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

import random
print(random.randrange(1,10))


# a = '''Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.'''
#print(a)

#a="     Hello World"
#print(a.strip())

#a="    Hello World"
#print(a)

#a="Hello World"
#print(a.replace("H", "J"))

#a="Hello, World"
#print(a.split(","))

#a="Hello"
#c= a + " " +b
#print(c)

age= 36
txt = "My name is John, and I am {}"
print(txt.format(age))

def tri_recursion(k):
  if(k>0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

  print("\n\nRecursion Example Results")
  tri_recursion(6)    
HOME
