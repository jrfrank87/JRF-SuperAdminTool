import os

menuChoice = input("=============\n= Main menu =\n=============\n[1]Enable Super Admin Account\n[2]Disable Super Admin Account\n[3]List All Users\n[4]Add New User Account\n[5]Delete a user account\n")
if menuChoice == "1":
    os.system("Net user administrator /active:yes")
    print("Super admin account enabled.")
if menuChoice == "2":
    os.system("Net user administrator /active:no")
    print("Super admin account disabled.")
if menuChoice == "3":
    os.system("Net user")
if menuChoice =="4":
    nun = input("Enter new user name: ")
    nup = input("Enter the password for your new user: ")
    os.system("Net user "+ nun + " " + nup + " /add")
if menuChoice == "5":
    utd = input("Enter name of user account to delete: ")
    os.system("Net user "+ utd +" /delete")