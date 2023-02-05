from datetime import date
firtdate = date(2022, 6, 1)
lastdate = date(2022, 8, 15)
deadline = lastdate - firtdate
print(deadline.days)