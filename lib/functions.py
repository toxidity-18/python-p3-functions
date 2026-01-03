# converting js function into python function .
def greet_Programmer():
  print('Hello , Programmer!')
greet_Programmer()

def  greet(name):
  print(f'Hello , {name}!   ')
greet('Blushbae')   

def greet_with_default(name='Programmer'):
  print(f'Hello , {name}!')
  return 'Hello , programmer!'
greet_with_default()

def add (num1,num2) :
  return num1 + num2
result = add(3,5)
print(result)

def halves(num3):
  return num3/2
halves(10)