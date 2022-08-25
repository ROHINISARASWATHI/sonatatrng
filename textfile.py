try:
    with open("address.py")as s:
        print("rohini")
except FileNotFoundError:
    print('File does not exist')
