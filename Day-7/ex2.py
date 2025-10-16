# import random

# print('Random number from 1 to 1000')
# print(random.randint(1,1000))

import random
def findwinner():
    name=input('Enter your Name ')
    LuckyNumber=random.randint(1,10)
    print(f'Welcome Mr\\Ms {name} Cuppon Number : {LuckyNumber}')
    if(LuckyNumber==1):
        print('You have won Proton XL-65 !!')
    elif(LuckyNumber==3):
        print('You have won an Ipad!!')
    elif(LuckyNumber==9):
        print('You have won an Iphone!!')
    else:
        print('Better luck next time')
