from tabulate import tabulate
free_list=[]

total_swimmers = {'Mgmg#1': {'Name': 'aungaung', 'Age': '18', 'Gender': 'male','event':'free'}, 'aungaung#2': {'Name': 'Mgmg', 'Age': '18', 'Gender': 'male','event':'butterfly'}, 'Mgmg#3': {'Name': 'Mgmg', 'Age': '19', 'Gender': 'female','event':'breast'}}
name = input("enter name: ")
for x in total_swimmers.items():
    
    y = list(x)
    # print(y)
    
    for z in range(len(y)):
        # print(z)
      
         if 'Mgmg' in y[z]:
            
            free_list.append(list(y[1].values()))
            # print(name)

print(free_list)



# print(tabulate(free_list, headers=['Name', 'Age','Gender','Event']))















        


        # def loop_dic(dic):
        #     for index in dic:
        #         for keys, values in dic[index].items():
        #             print("{0:22}".format(values), end="")
        #         print("")