#Take user marks from user with in 0 - 50
#if user enter outside(0-50) raise Error invalid marks using custom exception
#Give chance to the user till, he/she entered validmarks

# class InvalidMarks(Exception):
#     pass
# def checkMarks(Mark):
#     if(Mark<0):
#         raise InvalidMarks("Marks can not be negative")
#     elif(Mark>50):
#         raise InvalidMarks('Invalid Marks')
#     else:
#         print(f' Mark {Mark} is valid marks')

# while True:
#     try:
#         MarksEnter=int(input('Enter you marks :'))
#         checkMarks(MarksEnter)
#     except ValueError as v:
#         print('Error in value',v)
#     except Exception as e:
#             print('Errorr!!')
#     else:
#         print('Recorded')
#     choice=input('Please re-enter marks? If yes enter y : ').lower()
#     if(choice!='y'):
#         print("Thank youu")
#         break
        
# take the function from package

from ourpack import Mark
while True:
    try:
        MarksEnter=int(input('Enter you marks :'))
        Mark.checkMarks(MarksEnter)
    except ValueError as v:
        print('Error in value',v)
    except Exception as e:
            print('Errorr!!')
    else:
        print('Recorded')
    choice=input('Please re-enter marks? If yes enter y : ').lower()
    if(choice!='y'):
        print("Thank youu")
        break