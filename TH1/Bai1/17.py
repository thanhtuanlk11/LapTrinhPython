def sad(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(sad(1000))
print(sad(900))
print(sad(800))   
print(sad(2200))