# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# Datu tipi, mekle float - https://www.w3schools.com/python/python_datatypes.asp
# Pārbaudēm izmanto if...else - https://www.w3schools.com/python/python_conditions.asp
# Cipari https://www.w3schools.com/python/python_numbers.asp
# 

balance = 0

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':

        deposit = int(input("How much u want to deposit, type amount: "))
    
        balance = balance + deposit

        pass
    elif choice == '2':
         
        withdraw = int(input("How much u want to withdraw, type amount: "))
        
        if withdraw > balance :
            print("You dont have that much money.")
        else:
            balance = balance - withdraw

        pass
    elif choice == '3':
        
        print("Your balance " + str(balance))

        pass
    elif choice == '4':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
