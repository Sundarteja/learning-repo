import datetime 
#print(datetime.date.today().day)
check = datetime.date.today().day
if(check > 1):
    print("Its due past date that is First")
elif(check == 1):
    print("Exact Match is true")
else:
    print("not satified condition") 
