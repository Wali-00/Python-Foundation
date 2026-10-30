try:
    number = int(input())
    a =10/number
    x=number

except ZeroDivisionError:
    print("You cannot divide a number by zero")
except ValueError:
    print("please enter a valid number")
except Exception as E:
    print(E)
else:
    print(f"The result is {a/number}")
finally:
    print("code execution finished")