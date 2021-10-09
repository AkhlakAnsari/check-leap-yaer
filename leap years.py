#CHECK LEAP YEAR
year = int(input("ENTER YEAR TO CHECK LEAP YEAR ="))
# CENTURY YEARS DIVISIBLE BY 400
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year,"= IS LEAP YEAR")

else:
   print(year," IS NOT LEAP YEAR")
#THANKS akhlakansari94@gmail.com