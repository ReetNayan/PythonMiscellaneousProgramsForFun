fileWrite = open("polarDataset.csv", 'w+')

num = int(input("Enter the number of data: "))

print("Writing new data in the file...")

i = 1
dataDone = 0
check = True
print("Generating prime from 1 and writing to file as polar co-ord...")
while check:
    prime = 0
    for x in range(1, i + 1):
        if i % x == 0:
            prime += 1
    if prime == 2:
        # the number is prime and can be filled as data
        string = str(i) + "," + str(i)
        fileWrite.write(string + "\n")
        dataDone += 1
    i += 1
    if dataDone == num:
        check = False

print("Data written successfully!")
fileWrite.close()
print("File closed.")
