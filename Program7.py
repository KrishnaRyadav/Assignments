
#input number of months and print number of days in that month with name of month

month = int(input("Enter a Number Of Month :"))

if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    if(month==1):
        print("January has 31 days")
    elif(month==3):
        print("March has 31 days")
    elif(month==5):
        print("May has 31 days")
    elif(month==7):
        print("July has 31 days")
    elif(month==8):
        print("August has 31 days")
    elif(month==10):
        print("October has 31 days")
    else:
        print("December has 31 days")
elif(month==4 or month==6 or month==9 or month==11):
    if(month==4):
        print("April has 30 days")
    elif(month==6):
        print("June has 30 days")
    elif(month==9):
        print("September has 30 days")
    else:
        print("November has 30 days")
elif(month==2):
    print("February has 28 days")
else:
    print("You Enterd invalid Month...!!")
