names= ["Jane","Dan", "Alvin", "Ben", "Edwin", "Simon", "Brian", "Glen", "Alice"]

#Create a new list with names of 4 or less characters with n as last character

new_names = [name.upper() for name in names if len(name) <= 4 and name[-1] == 'n']

print(new_names)