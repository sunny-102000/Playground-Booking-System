import xlrd
import xlwt
from tkinter import *
from xlutils.copy import copy
import smtplib


def new_booking(name,mobno,on,emailid):
    rb=xlrd.open_workbook("OBS.xls")
    wb=copy(rb)
    data=wb.get_sheet('Booking')
    first_sheet=rb.sheet_by_name('Booking')

    print("The Grounds That We Have Are")
    tg=int(input("1)Cricket\n2)Football\n3)Hockey\n4)Basketball\n5)Badminton"))
    if(tg==1 or tg==2 or tg==3 or tg==4 or tg==5):
        month=int(input("Enter 10)October   11)November   12)December"))
        if(month==10 or month==11 or month==12):
            print()

        else:
             new_booking(name,mobno,on)
    else:
        new_booking(name,mobno,on)
    if(tg==1):
        ground='Cricket'
    elif(tg==2):
        ground='Football'
    elif(tg==3):
        ground='Hockey'
    elif(tg==4):
        ground='Basketball'
    else:
        ground='Badminton'




    while(1):
        print("Enter The Date on which you want {} ground".format(ground))
        reqdate=input()
        date=str(month)+'/'+str(reqdate)+'2019'
        rowv=int(reqdate)
        if(month==10):
            rowv=rowv+1
        elif(month==11):
            rowv=rowv+32
        elif(month==12):
            rowv=rowv+62
        x=first_sheet.cell(rowv,tg).value
        if(x=='Vacant'):
            print("The Date you choose is available for booking....")
            yn=int(input("1)Yes    2)No"))
            if(yn==1):
                z=mobno+name
                print(z)
                data.write(rowv,tg,z)
                print("Booking successful")
                sender="Asdfgh@gmail.com"//Our Email ID
                password="Xyz@12365489"//Our Password
                obj=smtplib.SMTP("smtp.gmail.com",587)
                obj.starttls()
                obj.login(sender,password)
                obj.sendmail(sender,emailid,"Dear "+name+", Booking Succesful for "+ground+" ground for date "+reqdate+"/"+str(month)+"/2019")
                obj.quit()
                wb.save("OBS.xls")
                break
            else:
                return
        else:
            print("Sorry The Date You Have Chosen Was Not Available.....")
def cancel_booking(name,mobno,emailid):
    print("Cancel Booking")
    rb=xlrd.open_workbook("OBS.xls")
    wb=copy(rb)
    data=wb.get_sheet('Booking')
    first_sheet=rb.sheet_by_name('Booking')
    
    print("The Grounds That We Have Are")
    tg=int(input("1)Cricket\n2)Football\n3)Hockey\n4)Basketball\n5)Badminton"))
    if(tg==1 or tg==2 or tg==3 or tg==4 or tg==5):
        month=int(input("Enter 10)October   11)November   12)December"))
        if(month==10 or month==11 or month==12):
            print()

        else:
             cancel_booking(name,mobno)
    else:
        cancel_booking(name,mobno)
    if(tg==1):
        ground='Cricket'
    elif(tg==2):
        ground='Football'
    elif(tg==3):
        ground='Hockey'
    elif(tg==4):
        ground='Basketball'
    else:
        ground='Badminton'

    while(1):
        print("Enter The Date on which you want {} ground".format(ground))
        reqdate=input()
        date=str(month)+'/'+str(reqdate)+'2019'
        rowv=int(reqdate)
        if(month==10):
            rowv=rowv+1
        elif(month==11):
            rowv=rowv+32
        elif(month==12):
            rowv=rowv+62
        x=first_sheet.cell(rowv,tg).value
        y=x[0:10:]
        print(y)
        if(y==mobno):
            print("Do you Want To Proceed With Canceltion ....?")
            yn=int(input("1)Yes    2)No"))
            if(yn==1):
                data.write(rowv,tg,'Vacant')
                print("Cancelation successful")
                sender="Asdfgh@gmail.com"//Our Email ID
                password="Xyz@12365489"//Our Password
                obj=smtplib.SMTP("smtp.gmail.com",587)
                obj.starttls()
                obj.login(sender,password)
                obj.sendmail(sender,emailid,"Dear "+name+", Cancelation Succesful for "+ground+" ground for date "+reqdate+"/"+str(month)+"/2019")
                obj.quit()
                wb.save("OBS.xls")
                break
            else:
                return
        else:
            print("Sorry The Date You Have Given Wrong Info For Cancelation.....Please Start The Process From The Beginning......")
            break


            
while(1):
    import tkinter.messagebox
    tkinter.messagebox.showinfo("Welcome"," * * * * * Welcome To Online Play Ground Booking System * * * * *")

    ans=tkinter.messagebox.askquestion("New To Portal?")
    if(ans=='yes'):
        on=1
        
    else:
        on=2

    
    ans1=tkinter.messagebox.askquestion("New Booking?")
    if(ans1=='yes'):
            bc=1
    else:
            bc=2
    name=input("Please Enter Your Name::")
    mobno=input("Please Enter Your Mobile Number::")
    emailid=input("Please Enter Your Email ID::")
    
    if(bc==1):
        new_booking(name,mobno,on,emailid)
    elif(bc==2):
        cancel_booking(name,mobno,emailid)
    
    
