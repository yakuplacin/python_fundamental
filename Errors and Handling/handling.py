# error handling

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)

# except ZeroDivisionError:
#     print("You cannot give 0 to y")
# except ValueError:
#     print("You should give numeric values to both x and y")

# except (ZeroDivisionError, ValueError) as e:
#     print("What you gave was wrong!")
#     print(e)

    except Exception as ex:
        print("You gave wrond values ", ex)
    else:
        # print("Everything is fine!")
        break
    finally:
        print("try-except has done!")
