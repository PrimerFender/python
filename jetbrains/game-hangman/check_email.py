def check_email(string):

    if string.find(" ") > -1 \
            or string.find("@") < 1 \
            or string.find(".", string.find("@") + 2) == -1:
        return False

    return True

string = input()
check_email(string)