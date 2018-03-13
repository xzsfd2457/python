str=input("Enter the strnigL:")
try:
  i=float(str)
except(ValueError,TypeError):
    print("not numeric")
else:    
    print("Yes")
