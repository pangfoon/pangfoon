# SUJITRA WAKARIN 362515241016 EE36241N
usernameinput = input("username : ")
passwordinput = input("password : ")

if usernameinput == "1234" and passwordinput == "1111":
    print("-------------------------------------")
    print("------WELCOME TO PANGFOON BRAND------")
    print("WHICH CLOTHES DO YOU WANT TO BUY?")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("ALL THE CLOTHES OF THIS PANGFOON BRAND")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1.DRESSES       350 THB")
    print("2.T-SHIRT       200 THB")
    print("3.JEANS SKIRT   280 THB")
    print("4.JEANS         320 THB")
    print("5.SHORTS        220 THB")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
CL=int(input("DO YOU WANT TO BUY?"))
    
if CL==1:
    price=350 
    print("YOUR ORDER:",CL,"PRICE=",price,"THB")
elif CL==2:
    price=200
    print("YOUR ORDER:",CL,"PRICE=",price,"THB")
elif CL==3:
    price=280
    print("YOUR ORDER:",CL,"PRICE=",price,"THB")
elif CL==4:
    price=320
    print("YOUR ORDER:",CL,"PRICE=",price,"THB")
elif CL==5:
    price=220
    print("YOUR ORDER:",CL,"PRICE=",price,"THB")
else:
    print("YOU NOT ORDER: ")

amount =int(input("HOW MANY PIECES DO YOU WANT TO BUY?"))

if CL==1:
    price=350
    print("TOTAL:",CL,"PRICE = ",price*amount,"THB")
elif CL==2:
    prce=200
    print("TOTAL:",CL,"PRICE = ",price*amount,"THB")
elif CL==3:
    prce=280
    print("TOTAL:",CL,"PRICE = ",price*amount,"THB")
elif CL==4:
    prce=320
elif CL==5:
    prce=220
    print("TOTAL:",CL,"PRICE = ",price*amount,"THB")
else :
    print("NO THIS PRODUCT")
    print("THNK YOU >-< ")
