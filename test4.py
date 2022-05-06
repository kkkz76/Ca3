from tabulate import tabulate
swimmers = {'Mgmg': {'Name': ['Mgmg','Mgmg'], 'Age': ['18','19'], 'Gender': ['male','male'] ,'Status' : ['active','active'] }, 'Zaw': {'Name': ['Zaw'], 'Age': ['18'], 'Gender': ['male'] ,'Status' : ['inactive'] }}



total_swimmer = {'Name':[],"Age":[],"Gender":[],"Status":[]}

for x in swimmers.values():

    for a in x['Name']:
        total_swimmer['Name'].append(a)

    for a in x['Age']:
        total_swimmer['Age'].append(a)

    for a in x['Gender']:
        total_swimmer['Gender'].append(a)

    for a in x['Status']:
        total_swimmer['Status'].append(a)
print(total_swimmer)

print(tabulate(total_swimmer, headers='keys'))
    




                





