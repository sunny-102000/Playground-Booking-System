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
