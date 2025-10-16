class invalidAge(Exception):
    pass
def check_age(age):
    if(age<=0):
        raise invalidAge('Age should not be negative')
    elif(age<18):
        raise invalidAge('Age should be greater than 18')
    elif(age>=80):
        raise invalidAge('Too old for enployment')
    else:
        print(f'Age {age} is valid age for employment')

try:
    userage=int(input('Enter your age: '))
    check_age(userage)
except invalidAge as e:
    print('Invalid age',e)
except Exception as ex:
    print('Error occured!!',ex)