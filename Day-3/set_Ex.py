# print("Sets in Python")
# set_one={"laptop","airphone","ipad","mobile","headphone","laptop","ipad"}
# print("Number of items in set_one are :", len(set_one))
# for item in set_one:
#     print(item,end=(" "))

#Clear(): remove all the item from set
# set_one.clear()
# print("\nNumber of items in set_one are :", len(set_one))
# for item in set_one:
#     print(item,end=(" "))

#remove(8): Updates the set s and removes 8 from s
# set_one={"laptop","airphone","ipad","mobile","headphone","laptop","ipad"}
# print("Number of items in set_one are :", len(set_one))
# for item in set_one:
#     print(item,end=(" "))

# set_one.remove("ipad")
# print("\nNumber after removing  item in set_one:",len(set_one))
# for item in set_one:
#     print(item,end=(" "))

#union,intersection,difference
# set_one={100,200,300,400,700,900,150}
# set_two={200,800,600,300,200,500,250}
# set_three={780,670,400,300,200,170}

# #union(s2): Returns a new set with all items from both sets s1 s2.# it will not conside duplicate
# print(f"set_one contains : ",{len(set_one)})
# print(set_one)
# print(f"set_two contain : ",{len(set_two)})
# print(set_two)
# print(f"set_three contain : ",{len(set_three)})
# print(set_three)
# unionset=set_one.union(set_two,set_three)
# print(f"Union of set_one ,set_two and set_three contain : {len(unionset)} following items")
# print(unionset)

# #s1.intersection(s2): Return a set which contains only item in both sets s1,s2....
# set_one={100,200,300,400,700,900,150}
# set_two={200,800,600,300,200,500,250}

# print(f"set_one contains : ",{len(set_one)})
# print(set_one)
# print(f"set_two contain : ",{len(set_two)})
# print(set_two)
# newset=set_one.intersection(set_two)
# print(f"intersection of set_one and set_two contain : {len(newset)} following items")
# print(newset)


#Different(s2):Return set which contains only item those are in s1 but not in s2
set_one={100,200,300,400,700,900,150}
set_two={200,800,600,300,200,500,250}

print(f"set_one contains : ",{len(set_one)})
print(set_one)
print(f"set_two contain : ",{len(set_two)})
print(set_two)
newset=set_one.difference(set_two)
print(f"Different of set_one and set_two contain : {len(newset)} following items")
print(newset)
