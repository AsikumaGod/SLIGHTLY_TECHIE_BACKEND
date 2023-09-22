i = 0
balance = 1000
while i < 1:
    code = input("Welcome to Stephen's E-wallet\nEnter your Ussd code: ")
    if code == "*124#":
        first_sel = input("Select a number to proceed\n1.Check balance\n2.Send money\n3.Buy airtime\n4.Quit\n:")
        if first_sel == "1":
            print(f'Your currentbalance is {balance}GHS')

            #Executed if a user select option 2
        elif first_sel == "2":
            recepient = int(input("Enter recepient number: "))
            try:
                amount_to_send = float(input("Enter amount to send: "))
                if amount_to_send > balance:
                    print("Your balance insuffient for this transaction!")
                else:
                    print(f"Transaction Succesful and your current balance is {balance - amount_to_send}GHS")
            except ValueError:
                print("Enter a number as amount")
            #Executed if a user select option 3
        elif first_sel == "3":
            airtime_amount = float(input("Enter amount of airtime you want to purchase: "))
            airtime_bought = airtime_amount * 0.5
            print(f"You have purchased airtime worth {airtime_amount}, your curent balance is {balance- airtime_bought}GHS")
            
            #Executed if a user select option 5
        elif first_sel == "4":
            break
            SystemExit()