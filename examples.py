def fizz_buzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# # Example usage:
fizz_buzz(100)
# Kaggle Notebook
# https://www.kaggle.com/code/jameslko/fizz-buzz-rnn
def hello_world(name):
    print("Hello, World!", name)
    text ="checking the code"
    if "code" in text:
        print("Code is in the text")
        print(text)
hello_world('James')
