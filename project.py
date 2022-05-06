import datetime
#main dictionary





swimmers = {'Mgmg#1': {'Name': 'Mgmg', 'Age': '18', 'Gender': 'male' ,'Status' : 'active' }, 'Zaw#2': {'Name': 'Zaw', 'Age': '18', 'Gender': 'male' ,'Status' : 'active' }}

#register_status
reg_status_true = "active"
reg_status_false = "inactive"



#input_validation_function
def check_name(check_reg_name):
    
    if check_reg_name.isalpha():
        return True
    else:
        return False

#check date function
def check_date(check_reg_date):

    year,month,day = check_reg_date.split('/')
    #check input_validation_for age
    
    try:
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        return False

#check gender
def check_gender(check_reg_gender):

    if check_reg_gender == '1':
        return 'Male'
    elif check_reg_gender == '2':
        return 'Female'
    elif check_reg_gender == '3':
        return 'Others'
    else:
        return False




user_choice = input("For register press 1\nFor record swimmer time press 2\nFor search individual press 3\nTo display unposted press 4\nEnter Your option:")

if user_choice == '1':

    input_loop = True
   
    while input_loop == True:

        reg_name  = input("Enter name:")

        #check input_validation_for name  
        check_name(reg_name)                                 
        while check_name(reg_name) == False:
              print("Only allow alphabets for name")
              reg_name  = input("Enter name:")
              check_name(reg_name)

        for swimmer in swimmers.items():
            

            

                    if reg_name == swimmer[1]['Name'] and 'inactive' == swimmer[1]['Status']:
                        swimmers[reg_name]['Status'] = reg_status_true
                        print("This username is now active")
                        input_loop = True
                        

                    elif reg_name == swimmer[1]['Name'] and 'active' == swimmer[1]['Status']:
                        print("This user is already active")
                        input_loop = True
                        
                    else:
                        break
                        
        input_loop = False

        reg_id_name = reg_name+"#"+str(len(swimmers)+1)
        swimmers[reg_id_name]={}
        swimmers[reg_id_name]['Name']=[reg_name]

        reg_dob= input("Enter data of birth in format yy/mm/dd:")

        #check input_validation_for dateTime  
        check_date(reg_dob)
        while check_date(reg_dob) == False:
            print("Input date is not valid..")
            reg_dob= input("Enter data of birth in format yy/mm/dd:")
            check_date(reg_dob)
            swimmers[reg_id_name]['Age']=[reg_dob] 


        reg_gen= input("Enter 1 for Male\nEnter 2 for Female\nEnter 3 for Others\nEnter your gender number:")
        check_gender(reg_gen)
        while check_gender(reg_gen) == False:
            reg_gen= input("Enter 1 for Male\nEnter 2 for Female\nEnter 3 for Others\nEnter your gender number:")
            check_gender(reg_gen)
                            
            swimmers[reg_id_name]['Gender']=check_gender(reg_gen)

                    
            swimmers[reg_id_name]['Status']=reg_status_true
            print("Register Successful and now active")

            print(swimmers)