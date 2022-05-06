from tabulate import tabulate
free_list=[]

total_swimmers = {'Mgmg#1': {'Name': 'Mgmg', 'Age': '18', 'Gender': 'male','event':'free'}, 'aungaung#2': {'Name': 'aungaung', 'Age': '18', 'Gender': 'male','event':'butterfly'}, 'Mgmg#3': {'Name': 'Mgmg', 'Age': '19', 'Gender': 'female','event':'free'}}

for x in total_swimmers.items():
    
    y = list(x)
    # print(y)
    
    for z in range(len(y)):
      
        if 'Mgmg' in y[z]:

            # print(y[1])
            if "free" in y[1].values():
                
                free_list.append(list(y[1].values()))

print(free_list)
print(tabulate(free_list, headers=['Name', 'Age','Gender','Event']))