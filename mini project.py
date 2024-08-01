#mini project
accounts={}
def create_account():
    username = input("Enter the username: ")
    pin = int(input("Enter the 4 digit number: "))
    initial_deposit=float(input('Enter initial deposit number: '))
    accounts[username] ={'pin': pin, 'balance':initial_deposit}
    print('account successfully created')
def deposit(amount,username):
    accounts[username]["balance"] += amount
    print(f"deposited {amount}")
def withdraw(amount,username):
    if amount <= accounts[username]["balance"]:
        accounts[username]["balance"] -= amount
        print(f"withdrawn {amount}")
    else:
        print("Insufficient balance")
def check_balance(username):
    print(f"your account balance:{accounts[username]["balance"]}")
while True:
    print("1.open a new account")
    print("2.withdraw money")
    print("3.deposit name")
    print("4.check balance")
    print("5.exit and quit")
    ch=input("enter the option: ")
    if ch =="1":
        create_account()
    elif ch in ["2", "3", "4"]:
        username=input("enter the username: ")
        if username in accounts:
             pin=int(input("enter your 4 digit pin: "))
             if ch == "2":
                 amount =float(input("enter the amount to deposit: "))
                 withdraw(amount,username)
             if ch =="2":
                amount=float(input("enter the amount to deposit:"))
                deposit(amount,username)
             elif ch =="3":
                amount=float(input("enter the amount to withdraw:"))
                withdraw(amount,username)
             elif ch=="4":
                check_balance(username)
             else:
                print("wrong password")
    elif ch =="5":
        break
    else:
        print("invalid option")
                                

    
    
