import random
charlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def createRandomString():
    code=""    
    for j in range(10):
        code = code+random.choice(charlist)
    f=open('discountcodes.csv', 'a')
    f.write(code + '\n')
    f.close()
    print(code)            

i = 0

while i<50:
    i=i+1
    createRandomString()

