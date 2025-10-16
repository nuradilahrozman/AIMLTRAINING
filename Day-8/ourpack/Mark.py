class InvalidMarks(Exception):
    pass
def checkMarks(Mark):
    if(Mark<0):
        raise InvalidMarks("Marks can not be negative")
    elif(Mark>50):
        raise InvalidMarks('Invalid Marks')
    else:
        print(f' Mark {Mark} is valid marks')