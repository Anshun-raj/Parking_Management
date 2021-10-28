class Parking:
    total_amt=0
    lim=int(input("Enter the maximum limit of vehicles that can be park in the parking zone:"))
    c=0
    def entry(self):
        if Parking.c<Parking.lim:
            r = 0
            name = input("Enter the name of vehicle user:")
            typ = input("Enter the type of vehicle park by the vehicle user:")
            num = int(input("Enter the vehicle number which is parked:"))
            Parking.c+=1
            if typ == 'car':
                r = 30
                Parking.total_amt += r
            elif typ == 'bike':
                r = 20
                Parking.total_amt += r
            else:
                pass
        else:
            raise Exception("There is no space in the parking zone")

    def eliminate(self):
        rem = int(input("Enter the vehicle no. to be eliminated:"))
        Parking.c-=1
        print("total no. of vehicles in the parking zone is:",Parking.c)


    def total_col(self):
        print("Total amount collected from the  parking zone is:",Parking.total_amt)

obj=Parking()
while True:
    print("press 1. for Entering of the vehicle")
    print("press 2. for elimination of the vehicle")
    print("press 3. for finding the total amount collected")
    print("press 4. for exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        obj.entry()
    elif choice==2:
        obj.eliminate()
    elif choice==3:
        obj.total_col()
    else:
        break

