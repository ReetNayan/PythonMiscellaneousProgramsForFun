# Program which adds logs with timestamp.

import time

time = time.asctime()

file = open('Daily_Log.txt' , 'a+')

timestamp = "---Log Start--- \n"+time+"\n- - - - - - - - - \n"

file.write(timestamp)

print("Write your notes and log here.")
print("A timestamp will be added before your new log entry")
print("After writing a sentence hit return to add new lines.")
print("- Want to exit and save?")
print("- Hit return for a new line, type 'end' and hit")
print("  return again to save and exit.")

x = input('Hit return and start writing.')
while True:
    data = input()
    if data == "end":
        break
    file.write("# "+data+"\n")

file.write("---Log End---\n")
file.close()
