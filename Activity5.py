print('*******************************')
print('TEMPERATUREE CONVERSION PROGRAM')
print('*******************************')
print('                               ')
print('Enter 1. For Celsius to Fahrenheit')
print('Enter 2. For Fahrenheit to Celsius')
opt=input('Enter 3 to Quit:')
temp=int(input('Enter Fahrenheit Temperature:'))
if opt=="2":
    print(temp,' Fahrenheit is equivalent to',round(temp/1.58898,2), 'Celsius')
elif opt=="1":
    print(temp,' Celsius is equivalent to',round(temp*1.58898,2), 'Fahrenheit')
else:
     print('Exit')





    
    

    
    


