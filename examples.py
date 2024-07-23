# def fizz_buzz(n):
#     for i in range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# # # Example usage:
# fizz_buzz(100)
# Kaggle Notebook
# https://www.kaggle.com/code/jameslko/fizz-buzz-rnn
# def hello_world(name):
#     print("Hello, World!", name)
#     text ="checking the code"
#     if "code" in text:
#         print("Code is in the text")
#         print(text)
# hello_world('James')
#Bank Account and Transactions
def bank_account():
    print("Hello, How much would you like to deposit?")
    balance = int(input())
    def get_balance():
        return balance
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    def withdraw():
        print("How much would you like to withdraw?")
        nonlocal balance
        balance -= int(input())
        return balance
    return get_balance, deposit, withdraw

get_balance, deposit, withdraw = bank_account()
balance = get_balance()
withdraw()
print(balance)