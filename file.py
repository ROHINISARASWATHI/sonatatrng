def myfile():
    try:
        b = open('rohini.txt', 'r')
        print(b.read())
    except(FileNotFoundError):
        return ('file not exits')


p = myfile()
print(p)
