my_file = open('data.txt', 'r') #this is an object ( a pointer to the file )
file_content = my_file.read()

#there is a limit for the number of files that we can have oppened

my_file.close()
print(file_content)


user_name = input('Enter your name: ')
my_file_write = open('data.txt', 'w')
my_file_write.write(user_name)

my_file_write.close()