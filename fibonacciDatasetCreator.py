fileWrite = open("fibonacciDataset.csv", 'w+')

num = int(input("Enter the number of data: "))

print("Writing new data in the file...")

done = 0
a = 0
b = 1
string = ""
pair = 0
while True:
    if pair < 2:
        if pair == 1:
            string = string + ',' + str(a)
        else:
            string = string + str(a)
        pair += 1
    if pair == 2:
        fileWrite.write(string + "\n")
        done += 1
        string = ""
        pair = 0
    c = a
    a = b
    b = c+b
    if done == num:
        break

print("Data written successfully!")
fileWrite.close()
print("File closed.")
