from tabulate import tabulate
d = [ ["apple"],["banana"],["orange"],[["12"],["12"],["12"]]]

print(tabulate(d, headers=["Name", "Age", "Percent"]))