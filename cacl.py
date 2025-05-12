#program to read a file line by line
try:

    file= open('sample.txt','r')
    result  = file.readline(3)
    print("reading file content ")
    print(result)
    file.close()
except FileNotFoundError:
    print("ERROR no file....")
