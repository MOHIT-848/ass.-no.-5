#program to write in a file
file = open("sample.txt",'a')
a = input("enter date to file:")
data= file.write(a)
print('data is add in file ,THANKYOU')
file.close()

file4= open("sample.txt",'r')
read= file4.readlines()
print("data is:")
print(read)
file4.close()
