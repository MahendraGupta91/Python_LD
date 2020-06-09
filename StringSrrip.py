# Python code to illustrate the working of strip() 
string = ': an outbreak or product of sudden rapid spread, growth an epidemic of bankruptcies '

# Leading spaces are removed 
print(string.strip()) 

# Geeks is removed 
print(string.strip(' an epidemic of bankruptcies')) 

# Not removed since the spaces do not match 
print(string.strip('Geeks')) 
