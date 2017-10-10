def isIn(string1,string2):
  return bool(string1 in string2 or string2 in string1)

x = input('enter string1:')
y = input('enter string2:')

print(isIn(x,y))
