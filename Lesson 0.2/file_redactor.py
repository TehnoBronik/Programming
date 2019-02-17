with open("privet.sys","r") as our_file:
    fs = our_file.read()
with open("privet.sys","w") as our_file:
    our_file.write(input(fs))
