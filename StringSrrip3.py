# Python code to illustrate the working of strip() 
string = ': an outbreak or product of sudden rapid spread, growth hjjweweavnk aan epidemic of bankruptcies '

# Leading spaces are removed 
print(string.strip()) 

# Geeks is removed 
print(string.strip(' of bankruptcies')) 

# Not removed since the spaces do not match 
print(string.strip('Geeks')) 


# Python code to illustrate the working of strip() 
string = '@@@@Geeks for Geeks@@@@@'

# Strip all '@' from beginning and ending 
print(string.strip('@')) 

string = 'www.Geeksforgeeks.org'

# '.grow' removes 'www' and 'org' and '.' 
print(string.strip('.grow')) 
