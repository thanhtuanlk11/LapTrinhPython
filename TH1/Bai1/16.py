def match(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(match(25))
print(match(6))