#write a function to find out the table of given number
def gen_table(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{(num*i)}')

number=int(input('Enter Number to findout table '))
gen_table(number)

