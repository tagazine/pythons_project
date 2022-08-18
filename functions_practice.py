def hello():
    print("Hello, kind user!")


def pack(arg1, arg2, arg3):
    list = [arg1, arg2, arg3]
    return list


def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else: 
        for item in list:
            if item == list[0]:
                print("First, I eat " + item + ".")
            else:
                print("Next, I eat " + item + ".")


hello()
print(pack('shrimp', 'scallops', 'Shrek 3'))

list = ['Chicken Fried Rice', 'Ice Cream', 'Something Healthy']
eat_lunch(list)
