decNum=int(input('enter your number'))
origNum=decNum
binNum=''

if decNum<0:
  isNeg= True
  decNum=abs(decNum)
else:
  isNeg= False

if decNum==0:
  binNum='0'

while decNum>0:
  binNum=str(decNum%2)+binNum
  decNum=decNum//2

if isNeg:
  binNum='-'+binNum

print('Binary representation of',origNum,'is',binNum)
