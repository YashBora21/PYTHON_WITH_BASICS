def method():
    try:
        a = int(input("Hey, enter the number: "))
        print(a)
        return
    except ValueError as e:
        print("Error spotted:")
        print(e)
        return
    else:
        print("else code ran")
    finally:
        print("Finally block ran")

method()
