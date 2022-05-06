append_swimmer_list = []



swimmers = {'Mgmg#1': {'Name': 'Mgmg', 'Age': '18', 'Gender': 'male' ,'Status' : 'inactive' }, 'Zaw#2': {'Name': 'Zaw', 'Age': '18', 'Gender': 'male' ,'Status' : 'inactive' },'Mgmg#2': {'Name': 'Mgmg', 'Age': '18', 'Gender': 'male' ,'Status' : 'inactive' }}
reg_status_false = 'inactive'
reg_status_true='active'
reg_name  = input("Enter name:")

for x in swimmers.items():
    
    y = list(x)
    # print(y)
    
    for z in range(len(y)):
        # print(z)
      
        if reg_name in y[z]:

           print(list(y[1].values())) 
            
           append_swimmer_list.append(list(y[1].values()))
            

# print(append_swimmer_list)

# if reg_status_false in append_swimmer_list[0]:


















# for list_swimmers_value in swimmers.values():
#         append_swimmer_list.append(list_swimmers_value['Name'])

# print(append_swimmer_list)
# if reg_name in append_swimmer_list:
#     print('yes')
# else:
#     print('no')

# if reg_name in append_swimmer_list and reg_status_false == swimmers[swimmer_keys]['Status']:
#     swimmers[swimmer_keys]['Status'] = reg_status_true
#     print("This username is now active")
# else:
#     print('dog phit p')
# print(swimmers)