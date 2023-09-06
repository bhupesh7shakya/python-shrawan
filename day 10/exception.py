while True:
    try:
        first_number=int(input("number"))
        if first_number== 10:
            raise Exception("Number cannot greater then 10")
        second_number=int(input("second number"))

        print(first_number/second_number)

    except ValueError:
        print("invalid input")
    
    except ZeroDivisionError:
        print("number cannot be divided by zero")
        
    except:
        print("something went wrong server error")