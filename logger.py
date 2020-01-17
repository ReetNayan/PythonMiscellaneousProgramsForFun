# Program which adds logs with timestamp.
# e.g.
# ---Log Start---
# Current Time & Date
# - - - - - - - -
# #Your log
# #...
# ---Log End---

import time

time = time.asctime()

file = open('Daily_Log.txt' , 'a+') # Create a new file if not exists and open to append data

timestamp = "\n---Log Start--- \n"+time+"\n- - - - - - - - - \n" # Add the Date and time

file.write(timestamp) # Write the timestamp to file

# Instructions for user...
print("Write your notes and log here.")
print("A timestamp will be added before your new log entry")
print("After writing a sentence hit return to add new lines.")
print()
print("- Want to exit and save?")
print("- Hit return for a new line, type 'end' and hit")
print("  return again to save and exit.")

x = input('Hit return and start writing.')

# A loop which keeps asking for Log data to write and will stop only when 'end' is entered.
while True:
    data = input()
    if data == "end":
        break
    file.write("# "+data+"\n")

file.write("---Log End---\n")
file.close()
