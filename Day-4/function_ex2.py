#default parameter in function
# def info(id,name,city="kl"):
#     print(f"Details as follow \n ID: {id}, Name: {name}, City: {city}")

# info(1,"sam","New Delhi")
# info(109,"xiuxiu")  # if did not give any info on city then it will take the default value = kl
# info(108, "mamu")  # if did not give any info on city then it will take the default value = kl

#To create a single method that able to add 2/3/4/5 numbers and return correct total
# def add(n1,n2=0,n3=0,n4=0,n5=0):
#     return n1+n2+n3+n4+n5
# print("Result: \t",add(1,2))
# print("Result: \t",add(1,24,5,8))
# print("Result: \t",add(1,26,6,7,9))

#if want infinite number can be added(sum)
# def add(*args):
#     return sum(args)

# print("sum of 1,10,11 is :", add(1,10,11))
# print("sum of 1,3is :", add(1,3))
# print("sum of 1,10,11,45,89,90,78 is :", add(1,10,11,45,89,90,78))


# def findMax(*nums):
#     return max(nums)
# print("maximum of 1,10,11 is :", max(1,10,11))
# print("maximum of 1,3 is :", max(1,3))
# print("maximum of 1,10,11,45,89,90,78 is :", max(1,10,11,45,89,90,78))

# print("Maximum Example")
# print("maximum of 1,10,11 is :", max(1,10,11))
# print("maximum of 1,3 is :", max(1,3))
# print("maximum of 1,10,11,45,89,90,78 is :", max(1,10,11,45,89,90,78))

# print("Minimum Example")
# print("Minimum of 1,10,11 is :", min(1,10,11))
# print("Minimum of 1,3 is :", min(1,3))
# print("Minimum of 1,10,11,45,89,90,78 is :", min(1,10,11,45,89,90,78))

