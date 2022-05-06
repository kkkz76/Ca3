from tabulate import tabulate
import datetime
#main dictionary





swimmers = {'Mgmg': {'Name': ['Mgmg'], 'Age': ['18'], 'Gender': ['male'] ,'Status' : ['active'],'Event':['Freestyle'],'Time':['1:11:11'],"Meet":['Apple2020']}, 'Zaw': {'Name': ['Zaw'], 'Age': ['18'], 'Gender': ['male'] ,'Status' : ['inactive'],'Event':['Backstroke'],'Time':['1:10:10'],"Meet":['Apple2021']}}

#register_status
reg_status_true = ["active"]
reg_status_false = ["inactive"]


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
        return ['Male']
    elif check_reg_gender == '2':
        return ['Female']
    elif check_reg_gender == '3':
        return ['Others']
    else:
        return False


main_program = True
while main_program == True:

   


    user_choice = input("\n\n\nFor register press 1\nFor record swimmer time press 2\nFor search individual press 3\nTo display unposted press 4\nTo execute program press 5\nEnter Your option:")
    if user_choice == '5':
        main_program = False
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



            if reg_name in swimmers and reg_status_false == swimmers[reg_name]['Status']:
                swimmers[reg_name]['Status'] = reg_status_true
                print("This username is now active")
                input_loop = True

            elif reg_name in swimmers and reg_status_true == swimmers[reg_name]['Status']:
                print("This user is already active")
                input_loop = True
            else:
                input_loop = False
                swimmers[reg_name]={}
                swimmers[reg_name]['Name']=[reg_name]

                reg_dob= input("Enter data of birth in format yy/mm/dd:")

                #check input_validation_for dateTime  
                check_date(reg_dob)
                while check_date(reg_dob) == False:
                    print("Input date is not valid..")
                    reg_dob= input("Enter data of birth in format yy/mm/dd:")
                    check_date(reg_dob)
                swimmers[reg_name]['Age']=[reg_dob] 


                reg_gen= input("Enter 1 for Male\nEnter 2 for Female\nEnter 3 for Others\nEnter your gender number:")
                check_gender(reg_gen)
                while check_gender(reg_gen) == False:
                    reg_gen= input("Enter 1 for Male\nEnter 2 for Female\nEnter 3 for Others\nEnter your gender number:")
                    check_gender(reg_gen)
                    
                swimmers[reg_name]['Gender']=check_gender(reg_gen)

            
                swimmers[reg_name]['Status']=reg_status_true
                swimmers[reg_name]['Event']=[]
                swimmers[reg_name]['Time']=[]
                swimmers[reg_name]['Meet']=[]


                print("Register Successful and now active")
                print(swimmers)
                main_program = True

    # .....................................record.......................................
    elif user_choice == '2':
        record_name = input('Enter player name to record(must be registered):')

        if record_name in swimmers:

            record_event_type =input("Choose the event type\nPress 1 for Freestyle\nPress 2 for Backstroke\nPress 3 for Breaststroke\nPress 4 for Butterfly\nPress 5 for individual Medley\nEnter your type:")

            if record_event_type == '1':
                record_event_type_detail = "Freestyle"
                record_event_meter= input('Choose between meter 50,100,200,400,800,1500:')
            elif record_event_type == '2':
                record_event_type_detail = "Backstroke"
                record_event_meter= input('Choose between meter 50,100,200:')
            elif record_event_type == '3':
                record_event_type_detail = "Breaststroke"
                record_event_meter= input('Choose between meter 50,100,200:')
            elif record_event_type == '4':
                record_event_type_detail = "Butterfly"
                record_event_meter= input('Choose between meter 50,100,200:')
            elif record_event_type == '5':
                record_event_type_detail = "individual Medley"
                record_event_meter= input('Choose between meter 100,200,400:')
            else:
                print("invaild input")
                main_program = True

            record_time=input("Enter time to record(eg.01:11:00):")
            record_meet=input("Enter the name of competition:")


            if record_event_type in swimmers[record_name]['Event'] and record_time in swimmers[record_name]['Time'] and record_meet in swimmers[record_name]['Meet']:
                    print("You can not add same record twice")
                    main_program = True

            else:

                
                if swimmers[record_name]['Event'] != [] and swimmers[record_name]['Time'] != [] and swimmers[record_name]['Meet'] != []:
                    swimmers[record_name]['Name'].append(swimmers[record_name]['Name'][0])
                    swimmers[record_name]['Age'].append(swimmers[record_name]['Age'][0])
                    swimmers[record_name]['Gender'].append(swimmers[record_name]['Gender'][0])
                    swimmers[record_name]['Status'].append(swimmers[record_name]['Status'][0])
                    swimmers[record_name]['Event'].append(record_event_type_detail)
                    swimmers[record_name]['Time'].append(record_time)
                    swimmers[record_name]['Meet'].append(record_meet)
                

                if swimmers[record_name]['Event'] == [] and swimmers[record_name]['Time'] == [] and swimmers[record_name]['Meet'] == []:
                    swimmers[record_name]['Event'].append(record_event_type_detail)
                    swimmers[record_name]['Time'].append(record_time)
                    swimmers[record_name]['Meet'].append(record_meet)

                total_swimmer = {'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[]}

                for x in swimmers.values():

                    for a in x['Name']:
                        total_swimmer['Name'].append(a)

                    for a in x['Age']:
                        total_swimmer['Age'].append(a)

                    for a in x['Gender']:
                        total_swimmer['Gender'].append(a)

                    for a in x['Status']:
                        total_swimmer['Status'].append(a)

                    for a in x['Event']:
                        total_swimmer['Event'].append(a)
                    
                    for a in x['Time']:
                        total_swimmer['Time'].append(a)
                    
                    for a in x['Meet']:
                        total_swimmer['Meet'].append(a)
                

                print(tabulate(total_swimmer, headers='keys'))            
                main_program = True
                

        else:
            print("no user found")
            main_program = True

# .....................................tableform..............



