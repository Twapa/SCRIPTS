while true:
    try:
        x = int(input("Enter number: "))
        break
    except ValueError:
        print("Oops: You have entered a wrong value")