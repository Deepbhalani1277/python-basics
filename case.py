x = int(input("enter you number:"))

match x:
    case 0:
        print(x, "is in case 0.")
    case 4 if x % 2 == 0:
        print(x, "is in case 2")
    case _:
        print("nothing")
