#Getting to know the persone
first_name = input ('What is your first name? ')
last_name = input ('What is your last name? ')
msg = f'{first_name} {last_name} is a boy?'
print (msg)
input()

#Identifying friend
friend = f'{first_name} are you my friend?'
print(friend)
input()

#Chat and magic tricks
Yes = True
no = False
if Yes and not no:
    print('You are so nice!!!!!!')
    input ('Wanna see a magic trick ')
    birth_year =  input ('Tell me your birth year ')
    age = 2023 - int(birth_year)
    print ('Your age is_____')
    print(age)   
    print ("Let's do another magic trick.") 
    weight_lbs = input ('Tell me your weight in  lbs ')
    weight_kg = int(weight_lbs) * 0.45
    weight = f'{first_name} your weight is {weight_kg} in kg'
    print (weight)
    input ('Tell me more about yourself. ')
    input ('What is your favourite color? ')
    input ('What is your favourite food? ')
    input ('Tell me about your hobies. ')
    print ('We have so much in common.')
    print ('Thank you for talking to me goodbye')
else:
    print("I don't like you!!!")
    print('Goodbye')