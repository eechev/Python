nameList = ["Bob", "Ralph", "Sally"]
print(nameList)

nameTupple = ("Bob", "Ralph", "Sally") # tuples are immutable
print(nameTupple)

nameSet = {"Bob", "Ralph", "Sally"}    # sets are unordered and no duplicates
print(nameSet)


print(nameList[0])
print(nameTupple[1])

nameList.append("Richard")
print(nameList)

nameSet.add("Richard")
print(nameSet)

nameList.remove("Ralph")
print(nameList)