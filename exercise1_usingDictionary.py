courtsDict = {'Mumbai': ["CCI", "Bombay Gym"], 'Delhi' : ["Sarova", "Gurugram Green"], 'Kolkata' : ["Calcutta Club", "Park Street"]}
citylist = courtsDict.keys()
print(citylist)

entries = list(courtsDict.items())
count = 0
for e in entries:    
    city, courts = e
    print(str(count) + ' ' + str(city))  
    count= count + 1    
    
#citylist = 

user_input = input(f"Put the number for the city you would like to see the courts from \n")
chosen_city, courts = entries[int(user_input)]
print(courts)
user_input2 = input(f"Press Y if you would you like to add a court fo this city else press N /n Y/N ")
if user_input2 == "y":
    newCourt = input("Enter the name of the court")    
    courtsDict[chosen_city].append(newCourt)
print(courtsDict)
# print(entries[1])

#
#print (courts['Delhi'][1])


