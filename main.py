import os

menuChoice = input("=============\n= Main menu =\n=============\n[1]Enable Super Admin Account\n[2]Disable Super Admin Account\n[3]Add New User Account\n[4]List All Users\n[5]Delete a user account\n")
if menuChoice == "1":
    os.system("Net user administrator /active:yes")
if menuChoice == "2":
    os.system("Net user administrator /active:no")
if menuChoice == "3":
    os.system("Net user")
if menuChoice =="4":
    nun = input("Enter new user name: ")
    nup = input("Enter the password for your new user: ")
    os.system("Net user "+ nun + " " + nup + " /add")
if menuChoice == "5":
    utd = input("Enter name of user account to delete: ")
    os.system("Net user "+ utd +" /delete")