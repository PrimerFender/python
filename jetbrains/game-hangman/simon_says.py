def what_to_do(instructions):

    command = "Simon says"
    if instructions.startswith("Simon says"):
        return "I" + instructions.split(command)[1]
    if instructions.endswith("Simon says"):
        return "I " + instructions.split(command)[0]
    
    return "I won't do it!"

string = input()
print(what_to_do(string))