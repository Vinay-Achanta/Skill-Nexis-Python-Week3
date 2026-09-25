# Count total lines in a file

with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))