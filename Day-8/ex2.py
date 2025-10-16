#this one we take formula from the pack without the try(exception)
# from ourpack import calc

# fnum=float(input('Enter first number: '))
# snum=float(input('Enter second number: '))
# op=input("Choose operation +,-,*,/: ")
# if(op=='+'):
#     print('Result : ',calc.add(fnum,snum))
# elif(op=='-'):
#     print('Result : ',calc.sub(fnum,snum))
# elif(op=='*'):
#     print('Result : ',calc.mult(fnum,snum))
# elif(op=='/'):
#     print('Result : ',calc.div(fnum,snum))
# else:
#     print('Wrong operation')


#this one we take formula from the pack with the try(exception)
# try:
#     from ourpack import calc

#     fnum=float(input('Enter first number: '))
#     snum=float(input('Enter second number: '))
#     op=input("Choose operation +,-,*,/: ")
#     if(op=='+'):
#         print('Result : ',calc.add(fnum,snum))
#     elif(op=='-'):
#         print('Result : ',calc.sub(fnum,snum))
#     elif(op=='*'):
#         print('Result : ',calc.mult(fnum,snum))
#     elif(op=='/'):
#         print('Result : ',calc.div(fnum,snum))
#     else:
#         print('Wrong operation')
# except Exception as e:
#     print('Error',e)
# finally:
#     print('End program')

# #this one we take formula from the pack with the try(exception) on every error
# try:
#     from ourpack import calc

#     fnum=float(input('Enter first number: '))
#     snum=float(input('Enter second number: '))
#     op=input("Choose operation +,-,*,/: ")
#     if(op=='+'):
#         print('Result : ',calc.add(fnum,snum))
#     elif(op=='-'):
#         print('Result : ',calc.sub(fnum,snum))
#     elif(op=='*'):
#         print('Result : ',calc.mult(fnum,snum))
#     elif(op=='/'):
#         print('Result : ',calc.div(fnum,snum))
#     else:
#         print('Wrong operation')
# except ZeroDivisionError as ze:
#     print('Division by 0 not allowed',ze)
# except ValueError as v:
#     print('Error in value',v)
# except Exception as v:
#     print('Error',v)
# finally:
#     print('End program')   

 #this one we take formula from the pack with the try(exception) on every error but we dont want it to end evrytime

from ourpack import calc
while True:
    try:
        fnum=float(input('Enter first number: '))
        snum=float(input('Enter second number: '))
        op=input("Choose operation +,-,*,/: ")
        if(op=='+'):
            print('Result : ',calc.add(fnum,snum))
        elif(op=='-'):
            print('Result : ',calc.sub(fnum,snum))
        elif(op=='*'):
            print('Result : ',calc.mult(fnum,snum))
        elif(op=='/'):
            print('Result : ',calc.div(fnum,snum))
        else:
            raise ValueError
        
    except ZeroDivisionError as ze:
        print('Division by 0 not allowed',ze)
    except ValueError as v:
        print('Error in value',v)
    except Exception as v:
        print('Error',v)
    choice=input('Do you want to continue? If yes press y :').lower() #lower mean lower case
    if(choice!='y'):
        print('Byeeeeeee')
        break


    