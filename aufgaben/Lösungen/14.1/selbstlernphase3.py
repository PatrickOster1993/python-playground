for zahl in range(101):
    if zahl % 3 == 0 and zahl % 5 == 0:
        print(f"{zahl} **FizzBuzz**")

    elif zahl % 3 == 0:
        print(f"{zahl} **Fizz**")
    
    elif zahl % 5 == 0:
        print(f"{zahl} **Buzz**")

    else:
        print(f"{zahl}")