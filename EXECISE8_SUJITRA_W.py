#!/usr/bin/env python
# coding: utf-8

# In[3]:


# SUJITRA WAKARIN 362515241016 EE36241N
usernameinput = input("username : ")
passwordinput = input("password : ")
if usernameinput == "1234" and passwordinput == "1111":
    print("-----------------------------------------------------------")
    print("--------WELCOME TO PANGFOON BRAND----------")
    print("WHICH CLOTHES DO YOU WANT TO BUY?")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("ALL THE CLOTHES OF THIS PANGFOON BRAND")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1.DRESSES         350 THB")
    print("2.T-SHIRT          200 THB")
    print("3.JEANS SKIRT   280 THB")
    print("4.JEANS             320 THB")
    print("5.SHORTS          220 THB")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    CL=int(input("DO YOU WANT TO BUY?"))

    if CL==1:
        price1=350 
        print("YOUR ORDER:",CL,"PRICE=",price1,"THB")
    elif CL==2:
        price1=200
        print("YOUR ORDER:",CL,"PRICE=",price1,"THB")
    elif CL==3:
        price1=280
        print("YOUR ORDER:",CL,"PRICE=",price1,"THB")
    elif CL==4:
        price1=320
        print("YOUR ORDER:",CL,"PRICE=",price1,"THB")
    elif CL==5:
        price1=220
        print("YOUR ORDER:",CL,"PRICE=",price1,"THB")
    else:
        print("YOU NOT ORDER: ")
        print("THNK YOU >-< ")
    amount1 =int(input("HOW MANY PIECES DO YOU WANT TO BUY?"))

    if CL==1:
        price1=350
        print("TOTAL:",CL,"PRICE = ",price1*amount1,"THB")
    elif CL==2:
        price1=200
        print("TOTAL:",CL,"PRICE = ",price1*amount1,"THB")
    elif CL==3:
        price1=280
        print("TOTAL:",CL,"PRICE = ",price1*amount1,"THB")
    elif CL==4:
        price1=320
        print("TOTAL:",CL,"PRICE = ",price1*amount1,"THB")
    elif CL==5:
        price1=220
        print("TOTAL:",CL,"PRICE = ",price1*amount1,"THB")
    CL=int(input("DO YOU WANT TO BUY?"))

    if CL==1:
        price2=350 
        print("YOUR ORDER:",CL,"PRICE=",price2,"THB")
    elif CL==2:
        price2=200
        print("YOUR ORDER:",CL,"PRICE=",price2,"THB")
    elif CL==3:
        price2=280
        print("YOUR ORDER:",CL,"PRICE=",price2,"THB")
    elif CL==4:
        price2=320
        print("YOUR ORDER:",CL,"PRICE=",price2,"THB")
    elif CL==5:
        price2=220
        print("YOUR ORDER:",CL,"PRICE=",price2,"THB")
    else:
        print("YOU NOT ORDER: ")
        print("THNK YOU >-< ")

    amount2 =int(input("HOW MANY PIECES DO YOU WANT TO BUY?"))

    if CL==1:
        price2=350
        print("TOTAL:",CL,"PRICE = ",price2*amount2,"THB")
    elif CL==2:
        price2=200
        print("TOTAL:",CL,"PRICE = ",price2*amount2,"THB")
    elif CL==3:
        price2=280
        print("TOTAL:",CL,"PRICE = ",price2*amount2,"THB")
    elif CL==4:
        price2=320
        print("TOTAL:",CL,"PRICE = ",price2*amount2,"THB")
    elif CL==5:
        price2=220
        print("TOTAL:",CL,"PRICE = ",price2*amount2,"THB")
    CL=int(input("DO YOU WANT TO BUY?"))
 
    if CL==1:
        price3=350 
        print("YOUR ORDER:",CL,"PRICE=",price3,"THB")
    elif CL==2:
        price3=200
        print("YOUR ORDER:",CL,"PRICE=",price3,"THB")
    elif CL==3:
        price3=280
        print("YOUR ORDER:",CL,"PRICE=",price3,"THB")
    elif CL==4:
        price3=320
        print("YOUR ORDER:",CL,"PRICE=",price3,"THB")
    elif CL==5:
        price3=220
        print("YOUR ORDER:",CL,"PRICE=",price3,"THB")
    else:
        print("YOU NOT ORDER: ")
        print("THNK YOU >-< ")
    amount3 =int(input("HOW MANY PIECES DO YOU WANT TO BUY?"))

    if CL==1:
        price3=350
        print("TOTAL:",CL,"PRICE = ",price3*amount3,"THB")
    elif CL==2:
        price3=200
        print("TOTAL:",CL,"PRICE = ",price3*amount3,"THB")
    elif CL==3:
        price3=280
        print("TOTAL:",CL,"PRICE = ",price3*amount3,"THB")
    elif CL==4:
        price3=320
        print("TOTAL:",CL,"PRICE = ",price3*amount3,"THB")
    elif CL==5:
        price3=220
        print("TOTAL:",CL,"PRICE = ",price3*amount3,"THB")
    print("ALL TOTAL=",price1*amount1+price2*amount2+price3*amount3,"THB")   
    print("THANK YOU FOR PURCHASING CLOTHES PANGFOON BRAND 😊")


else :
    print("PROGRAM ERROR")


# In[ ]:




