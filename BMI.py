bmi=float(input("Enter the bmi: "))
if bmi<=18.5:
    print("underwgt")

elif 18.5<=bmi<=24.9:
    print("normal wgt")

elif 25<=bmi<=29.9:
    print("over wgt")
    
else: print("obese")