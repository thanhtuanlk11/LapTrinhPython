
test_dict = {"Gfg": 1, "is": 3, "Best": 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

a = list(test_dict.keys())
b = list(test_dict.values())
a.extend(b)
res = a

# printing result
print("The ordered keys and values : " + str(res))
