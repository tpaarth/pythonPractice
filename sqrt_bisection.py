x=25.0
epsilon=0.01
numGuesses=0
low=0.0
high=x

ans=(low+high)/2.0

while abs(ans**2-x)>=epsilon:
  print('low: ',low,'high: ',high)
  numGuesses += 1
  
  if ans**2 < x:
    low=ans
  else:
    high=ans
  
  ans=(low+high)/2.0
  
print('number of guesses:',numGuesses)
print(str(ans),'is close to root of',str(x))
  
