 
import os 
import random 
import hashlib 
 
class BankAccount: 
    def __init__(self, account_number, customer_name, balance): 
        self.account_number = account_number 
        self.customer_name = customer_name 
        self.balance = balance 
 
    def deposit(self, amount): 
        if amount > 0: 
            self.balance += amount 
            return True 
        else: 
            return False 
 
    def withdraw(self, amount): 
        if amount > 0 and amount <= self.balance: 
            self.balance -= amount 
            return True 
        else: 
            return False 
 
    def get_balance(self): 
        return self.balance 
 
class Customer: 
    def __init__(self, username, password): 
        self.username = username 
        self.password = hashlib.sha256(password.encode()).hexdigest() 
 
def load_accounts(): 
    accounts = [] 
    if os.path.exists("accounts.txt"): 
 
        with open("accounts.txt", "r") as file: 
            lines = file.readlines() 
            for line in lines: 
                account_info = line.strip().split(',') 
                account_number, customer_name, balance = account_info 
                accounts.append(BankAccount(account_number, customer_name, float(balance))) 
    return accounts 
 
def save_accounts(accounts): 
    with open("accounts.txt", "w") as file: 
        for account in accounts: 
            file.write(f"{account.account_number},{account.customer_name},{account.balance}\n") 
 
def authenticate(username, password, customers): 
    for customer in customers: 
        if username == customer.username and hashlib.sha256(password.encode()).hexdigest() ==customer.password: 
            return True 
    return False 
 
def main(): 
    accounts = load_accounts() 
    customers = [Customer("Sanvi", "sanvi@123"), Customer("Shambhu",     
"sham@123"),Customer("Ishita","ishita@123")] 
 
    while True: 
        print("\nWelcome to the Bank of Python") 
        print("1. Login") 
        print("2. Exit") 
        choice = input("Enter your choice: ") 
 
        if choice == "1": 
            username = input("Enter username: ") 
            password = input("Enter password: ") 
            if authenticate(username, password, customers): 
                while True: 
                    print("\nWelcome, " + username) 
                    print("1. Create Account") 
                    print("2. Deposit") 
                    print("3. Withdraw") 
                    print("4. Check Balance") 
                    print("5. Logout") 
                    option = input("Enter your option: ") 
                    if option == "1": 
                        account_number = str(random.randint(10000, 99999)) 
                        customer_name = input("Enter account holder's name: ") 
                        initial_balance = float(input("Enter initial balance: ")) 
                        accounts.append(BankAccount(account_number, customer_name, initial_balance)) 
                        save_accounts(accounts) 
                        print(f"Account created successfully. Your account number is: {account_number}")
 
                    elif option == "2": 
                        account_number = input("Enter account number: ") 
                        amount = float(input("Enter deposit amount: ")) 
                        for account in accounts: 
                            if account.account_number == account_number: 
                                if account.deposit(amount): 
                                    save_accounts(accounts) 
                                    print("Deposit successful.") 
                                else: 
                                    print("Invalid amount.") 
                                break 
                        else: 
                            print("Account not found.") 
                    elif option == "3": 
                        account_number = input("Enter account number: ") 
                        amount = float(input("Enter withdrawal amount: ")) 
                        for account in accounts: 
                            if account.account_number == account_number: 
                                if account.withdraw(amount): 
                                    save_accounts(accounts) 
                                    print("Withdrawal successful.") 
                                else: 
                                    print("Insufficient balance or invalid amount.") 
                                break 
                        else: 
                            print("Account not found.") 
                    elif option == "4": 
                        account_number = input("Enter account number: ") 
                        for account in accounts: 
                            if account.account_number == account_number: 
                                print(f"Account balance: {account.get_balance()}") 
                                break 
                        else: 
                            print("Account not found.") 
                    elif option == "5": 
                        break 
                    else: 
                        print("Invalid option.") 
            else: 
                print("Authentication failed. Please check your username and password.") 
        elif choice == "2": 
            break 
        else: 
            print("Invalid choice. Please try again.") 
 
if __name__ == "__main__": 
    main() 