username = "chan"
password = "no39"

a = input("username : ")
b = input("password : ")
if a == username and b == password :
    print("Welcome !")
    print("Choose your product")
    print("rice                 : 120 bth")
    print("agg                  : 10  bth")
    print("milk                 : 40  bth")
    select = input("your pro duct : ")
    if select  == "rice":
        num1 = int(input("How many do you want :"))
        print(num1 * 120)
    elif select  == "agg":
        num1 = int(input("How many do you want :"))
        print(num1 * 10)
    elif select  == "milk":
        num1 = int(input("How many do you want :"))
        print(num1 * 40)
    elif select  == "rice and agg":
        num1 = int(input("How many rice do you want :"))
        num2 = int(input("How many agg do you want :"))
        print(num1 * 120 + num2 * 10)
    elif select  == "rice and milk":
        num1 = int(input("How many rice do you want :"))
        num2 = int(input("How many milk do you want :"))
        print(num1 * 120 + num2 * 40)
    elif select  == "agg and milk":
        num1 = int(input("How many agg do you want :"))
        num2 = int(input("How many milk do you want :"))
        print(num1 * 10 + num2 * 40)