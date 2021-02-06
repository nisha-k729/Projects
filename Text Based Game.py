name=str(input('Enter your name:'))
print(f'{name} you are stuck at solving a puzzle')
print('you are solving a puzzle and suddenly you saw a new puzzle,Now you have two options')
print('1. Solve new puzzle first.  2.First solve the old puzzle and then solve the new one')
user=int(input('Chose 1 or 2:'))
if user==1:
    print('You are not that smart')
elif user==2:
    print('You are smart')
else:
    print('Check your input')

