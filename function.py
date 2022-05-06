def check_name(x):
    
    if x.isalpha():
        return True
    else:
        return False



reg_name = input("Enter name:")
check_name(reg_name)

if check_name(reg_name) == True:
    print("it is ok")
elif check_name(reg_name) == False:
    print("it is not ok")

reg_input = input("Enter input:")
check_name(reg_input)

if check_name(reg_input) == True:
    print("it is ok")
elif check_name(reg_input) == False:
    print("it is not ok")




