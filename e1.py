# open the file in read mode
fille_read = open('Codingal.txt','r')
print("File in Read Mode -")
print(fille_read.read())
fille_read.close()


# open the file in write mode
fille_write = open('Codingal.txt','w')
# Write in the file
fille_write.write(" File in write mode ....")
fille_write.write("Hi! I am Penguin. I am 1 yr. old ")
fille_write.close()


#open the file in append mode
file_append = open('Codingal.txt', 'a')
# append in the file
file_append.write("\n File in append mode ....")
file_append.write("Hey guys see append mode")
file_append.close()