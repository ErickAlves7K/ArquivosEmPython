#file = open("amazingFile.txt", "w")

#file.write("It's too difficult to create a file in Python, omg!!!!")

#file.close()

with open("amazingFile.txt", "a") as file:
    file.write("\nCan you see it?")
