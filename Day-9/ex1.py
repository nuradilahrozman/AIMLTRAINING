#Write a function to check the number is odd or even
def check_odd_even(number):
    if(number%2==0):
        print(f'{number} is Even Number')
    else:
        print(f'{number} is Odd Number')
given_number=int(input('Enter Number : '))
check_odd_even(given_number)