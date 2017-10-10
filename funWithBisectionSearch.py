high=100
low=0
guess=int((high+low)/2)

print('Please think of a number between 0 and 100!')

while True:
  print('Is your secret number',guess,'?')
  response=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
  
  if response=='c':
    break
  elif response=='l':
    low=guess
  elif response=='h':
    high=guess
  else:
    print('Sorry, I did not understand your input')
    
  guess=int((high+low)/2)

print('Game over. Your secret number was:',guess)
