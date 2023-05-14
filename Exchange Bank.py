# name of company
# notic:>>> I suppose we have three branches in this assaiment 
print("Exchange company") 
c = 1 # c mean counter
while c < 4: # this loop for move betweeen the branches
    branches = input("Enter the name of branche AKB or SB or AB: ")
    date = input("Enter the date: ")
    if branches == "AKB":  # AKB mean Al Khor Branch
        count = 0 # counter for loop
        num_of_costd = 0 # to keep value of deposit
        num_of_costw = 0 # to keep value of withdrawal
        num_of_costx = 0 # to keep value of exchange 
        total1 = 0
        oper1 = int(input("Enter the Number of operatios allowed per day: ")) # oper mean operation
        while count < oper1 :
            operation = input("Enter the operation: ") # type of operation
            if operation == "deposit":
                named = input("Enter depositor's name: ") # depositor's name
                num_of_Account = int(input("Enter Account Number: ")) # Account Number
                num_of_mony = float(input("Enter the cost: ")) # value of mony
                d = print(f"name: {named}\n Account Number: {num_of_Account}\n balance: {num_of_mony}\n operation: {operation}\n date: {date} ")
                num_of_costd = num_of_costd + num_of_mony
            elif operation == "withdrawal": # withdrawal operation
                namew = input("Enter Customer Name: ") # Customer Name
                num_of_Account = int(input("Enter Account Number: ")) # Account Number
                num_of_mony = float(input("Enter the cost: ")) # value of mony
                w = print(f"name: {namew}\n Account Number: {num_of_Account}\n balance: {num_of_mony}\n operation: {operation}\n date: {date} ")
                num_of_costw = num_of_costw + num_of_mony
            elif operation == "Exchange": # Exchange operation
                namex = input("Enter Name: ") # Name for the owner of the exchange
                num_of_mony = float(input("Enter the cost: ")) # value of mony
                x = print(f"name: {namex}\n balance: {num_of_mony}\n operation: {operation}\n date: {date} ")
                num_of_costx = num_of_costx + num_of_mony
            total = num_of_costd  + num_of_costw + num_of_costx
            total1 = total1 + total
            new1 = input("Add anther operation prss new or you want report press report or to stop press stop: ")
            if new1 == "new": # to enter anther item
                count = count + 1
            elif new1 == "stop": # to out of system
                print(f"your finshed for today")
                break
            elif new1 == "report": # to print the report for today
                print(f" Balance from operation deposit for today is: {num_of_costd } \n"
                    f" Balance from operation withdrawal for today is: {num_of_costw} \n"
                    f" Balance from operation Exchange for today is: {num_of_costx} \n")
            else:
                print(f"input wrong, please try again")
                break
    elif branches == "SB":  # SB mean Sana'a branch
        count = 0
        num_of_costddd = 0 # to keep value of deposit
        num_of_costwww = 0 # to keep value of withdrawal
        num_of_costxxx = 0 # to keep value of Exchange
        total2 = 0
        oper2 = int(input("Enter the Number of operatios allowed per day: ")) # oper mean operation
        while count < oper2:
            operation = input("Enter the operation: ") # type of operation
            if operation == "deposit":
                namedd = input("Enter depositor's name: ") # depositor's name
                num_of_Account = int(input("Enter Account Number: ")) # Account Number
                num_of_mony = float(input("Enter the cost: ")) # value of mony
                d = print(f"name: {namedd}\n Account Number: {num_of_Account}\n balance: {num_of_mony}\n operation: {operation}\n date: {date} ")
                num_of_costddd = num_of_costddd + num_of_mony
            elif operation == "withdrawal": # withdrawal operation
                nameww = input("Enter Customer Name: ") # Customer Name
                num_of_Account = int(input("Enter Account Number: ")) # Account Number
                num_of_mony = float(input("Enter the cost: ")) # value of mony
                w = print(f"name: {nameww}\n Account Number: {num_of_Account}\n balance: {num_of_mony}\n operation: {operation}\n date: {date} ")
                num_of_costwww = num_of_costwww + num_of_mony
            elif operation == "Exchange": # Exchange operation
                namexx = input("Enter Name: ") # Name for the owner of the exchange
                num_of_mony = float(input("Enter the cost: ")) # value of mony
                x = print(f"name: {namexx}\n balance: {num_of_mony}\n operation: {operation}\n date: {date} ")
                num_of_costxxx = num_of_costxxx + num_of_mony
            totall = num_of_costxxx + num_of_costxxx + num_of_costddd
            total2 = total2 + totall
            new1 = input("Add anther operation or you want report: ")
            if new1 == "new": # to enter anther item
                count = count + 1
            elif new1 == "stop": # to out of system
                print(f"your finshed for today")
            elif new1 == "report": # to print the report for today
                print(f" Balance from operation deposit for today is: {num_of_costddd} \n"
                    f" Balance from operation withdrawal for today is: {num_of_costxxx} \n"
                    f" Balance from operation Exchange for today is: {num_of_costxxx} \n")
            else:
                print(f"input wrong, please try again")
                break
    elif branches == "AB":  # AB mean Aden Branch
        count = 0
        num_of_costdddd = 0 # to keep value of deposit
        num_of_costwwww = 0 # to keep value of withdrawal
        num_of_costxxxx = 0 # to keep value of Exchange
        total3 = 0
        oper3 = int(input("Enter the Number of operatios allowed per day: ")) # oper mean operation
        while count < oper3:
            operation = input("Enter the operation: ") # type of operation
            if operation == "deposit":
                nameddd = input("Enter depositor's name: ") # depositor's name
                num_of_Account = int(input("Enter Account Number: ")) # Account Number
                num_of_mony = float(input("Enter the cost: ")) # value of mony
                d = print(f"name: {nameddd}\n Account Number: {num_of_Account}\n balance: {num_of_mony}\n operation: {operation}\n date: {date} ")
                num_of_costdddd = num_of_costdddd + num_of_mony
            elif operation == "withdrawal": # withdrawal operation
                namewww = input("Enter Customer Name: ") # Customer Name
                num_of_Account = int(input("Enter Account Number: ")) # Account Number
                num_of_mony = float(input("Enter the cost: ")) # value of mony
                w = print(f"name: {namewww}\n Account Number: {num_of_Account}\n balance: {num_of_mony}\n operation: {operation}\n date: {date} ")
                num_of_costwwww = num_of_costwwww + num_of_mony
            elif operation == "Exchange": # Exchange operation
                namexxx = input("Enter Name: ") # Name for the owner of the exchange
                num_of_mony = float(input("Enter the cost: ")) # value of mony
                x = print(f"name: {namexxx}\n balance: {num_of_mony}\n operation: {operation}\n date: {date} ")
                num_of_costxxxx = num_of_costxxxx + num_of_mony
            totalll = num_of_costdddd + num_of_costwwww + num_of_costxxxx
            total3 = total3 + totalll
            new1 = input("Add anther operation or you want report press r: ")
            if new1 == "new": # to enter anther item
                count = count + 1
            elif new1 == "stop": # to out of system
                print(f"your finshed for today")
                break
            elif new1 == "r": # to print the report
                print(f"Balance from operation deposit for today is: {num_of_costdddd} \n"
                    f" Balance from operation withdrawal for today is: {num_of_costwwww} \n"
                    f" Balance from operation Exchange for today is: {num_of_costxxxx} \n")
                break
            else:
                print(f"input wrong, please try again")
                break   
    else:
        print(f"sorry sir,but not find Branch by this name \n please try to enter anther once ")
    c = c + 1

# >>>> under this commant is code for the print report for the maneger about all branches 
# >>>> 

reportAll = input("Do you want to print reoprt? yes or no: ")
if reportAll == "yes":
    print(f"the total balance for Al Khor Branch {total1} \n"
        f"the total balance for Sana'a branch: {total2} \n "
        f"the total balance for Aden branch: {total3} ")
else:
    print(f"see you soon")
                


    
        




