i = 0
balance = 1000
while i < 1:
    code = input("Enter your Ussd code: ")
    if code == "*124#":
        first_sel = input("1.Check balance\n2.Send money\n3.Buy airtime\n4.Select a number to proceed:")
        if first_sel == "1":
            print(f'Your currentbalance is {balance}GHS')
        elif first_sel == "2":
            recepient = int(input("Enter recepient number: "))
            amount_to_send = float(input("Enter amount to send: "))
            if amount_to_send > balance:
                print("Your balance insuffient for this transaction!")
            else:
                print(f"Transaction Succesful and your current balance is {balance - amount_to_send}GHS")
        
        elif first_sel == "3":
            airtime_amount = float(input("Enter amount of airtime you want to purchase: "))
            airtime_bought = airtime_amount * 0.5
            print(f"You have purchased airtime worth {airtime_amount}, your curent balance is {balance- airtime_bought}GHS")