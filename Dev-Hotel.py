import csv
import os
import random
      
def custdetails():   #need update
      name=input("Enter your Name:")
      city=input("Enter your city:")
      age=input("Enter your Age:")
      nationality=input("Enter your Nationality:")
      phone=input("Enter Phone Number:")
      verification=input("Enter Verification:")
      noofperson=input("How many persons you want to accomodate?:")
      l=[name,city,age,nationality,phone,verification,noofperson]
      roomrent(l,name,phone)

def roomrent(l,name,phone):
      print()
      print('\t\t\t Rooms\t\t\t')
      print('Rooms\t\tPrice')
      print("_____________________________________________\t\t")
      print("1) ROYAL\t\t₹10000")
      print("2) LUXURY\t₹7500")
      print("3) ELITE\t\t₹5000")
      print("4) BUDGET\t₹2500")
      print("_____________________________________________\t\t")
      print("Enter Your Room Choice (1-4):")
      roomchoice=choice(1,4)
      print("Enter Floor Number (0-6):")
      floor=choice(0,6)
      noofdays=int(input("Enter Number of Days:"))
      checkin=input('Enter Check-in Date:')
      checkout=input('Enter Check-out Date:')
      with open("DEV_HOTEL/roomrec.csv","r") as f:
            with open('DEV_HOTEL/temp.csv','w',newline='') as f1:
                  w=csv.writer(f1)
                  flag=0
                  r=csv.reader(f)
                  for i in r:
                        if flag==0:
                              if int(i[2])==floor and int(i[3])==roomchoice and i[4]=='available': #check i[5]
                                    wing=int(i[1])
                                    if wing==1:
                                          wing='North'
                                    elif wing==2:
                                          wing='East'
                                    elif wing==3:
                                          wing='South'
                                    elif wing==4:
                                          wing='West'
                                    roomno=int(i[0])
                                    if roomchoice==1:
                                        cost=noofdays*10000
                                    elif roomchoice==2:
                                        cost=noofdays*7500
                                    elif roomchoice==3:
                                        cost=noofdays*5000
                                    elif roomchoice==4:
                                        cost=noofdays*2500
                                    i[4]='booked'
                                    flag=1
                        w.writerow(i) 
                  code=random.randint(1000,9999)
                  if flag==1:
                        print()
                        print('ROOM DETAILS:-')
                        print('Your Room No is:',roomno)
                        print('Room is at \''+wing+'\' wing')
                        print('Your Room CODE is:',code)
                        print('REMEMBER IT!')
                        print()
      os.remove('DEV_HOTEL/roomrec.csv')
      os.rename('DEV_HOTEL/temp.csv','DEV_HOTEL/roomrec.csv')
      if flag==0:
          print('Room Not Available')
          print('1. Book again')
          print('2. Menu')
          print('Enter ')
          c=choice(1,2)
          if c==1:
              roomrent(l)
          else:
              menu()
      else:
            print('Room Rent for',noofdays,'days is:','₹',cost)
            print()
            print('Room Booked!')
            with open('DEV_HOTEL/activerec.csv','a',newline='') as f4:
                  w=csv.writer(f4)
                  w.writerow([roomno,name,phone,checkin,checkout,cost,code,0])
            with open("DEV_HOTEL/customerrec.csv","a",newline='') as f2:
                  l2=[roomno,noofdays,checkin]
                  l.extend(l2)
                  c=csv.writer(f2,delimiter=',')
                  c.writerow(l)
    
def arcaderent():
    print('Enter your Room No.')
    roomno=choice(1,1000)
    password=input('Enter room Code')
    print("\t\t\tArcade\t\t\t")
    print("Game Name\t\tPrice")
    print("_____________________________________________\t\t")
    print(" 1. SNOOKER\t\t₹200")
    print("2.TABLE TENNIS\t\t₹150")
    print("3. XBOX/PS4\t\t₹100")
    print("4. PINBALL\t\t₹300")
    print("5. VR WORLD\t\t₹400")
    print("6. GOLF\t\t\t₹700")
    print("_____________________________________________\t\t")
    print("Enter Game Choice")
    gamechoice=choice(1,6)
    check=passwordcheck(roomno,password)
    if check == True:
        print("How many hours you want to play? (1-10)")
        hours=choice(1,10)
        if gamechoice==1:
            print("You chose to play SNOOKER")
            bill=200*hours
        elif gamechoice==2:
            print("You chose to play TABLE TENNIS")
            bill=150*hours
        elif gamechoice==3:
            print("You chose to play Console Games(XBOX/PS4)")
            bill=100*hours
        elif gamechoice==4:
            print("You chose to play PINBALL")
            bill=300*hours
        elif gamechoice==5:
            print("You chose to play VR GAMES")
            bill=400*hours
        elif gamechoice==6:
            print("You chose to play GOLF")
            bill=700*hours
        while True:
            print('Confirm Your Sport?')
            print('Enter Y for yes')
            ans=input('Enter N for no')
            if ans in 'Yy':
                print('Order Confirmed!')
                print('Enjoy!')
                with open('DEV_HOTEL/activerec.csv','r') as f:
                    r=csv.reader(f)
                    for i in r:
                          if int(i[0])==roomno:
                                originalcost=int(i[5])+bill
                print('Your Total Cost cost is: ₹'+str(bill)) 
                upgrate_cost(roomno,originalcost)
                break
            elif ans in 'Nn':
                print('order Canceled')
                break
            else:
                print('Invalid input')
    else:
        print('Invalid Code')
        
def food_menu(m):   #m=1 for breakfast, m=2 for lunch and m=3 for dinner
      with open('DEV_HOTEL/menu.csv','r') as f:   #displaying menu screen
            r=csv.reader(f)
            print('    S.no \t','food \t\t\t','price')
            print()
            flag=0
            flag2=0
            for i in r:
                  try:
                        if int(i[1])==1 or int(i[1])==2 or int(i[1])==3:
                              flag=0
                        if int(i[1])==m:
                              flag=1
                  except:
                        pass
                  if flag==1:
                        if flag2==1:
                              if len(i[0])<16 and len(i[0])>8:
                                    print('   ',i[0],'\t',i[1],'\t\t',i[2])
                              elif len(i[0])<8:
                                    print('   ',i[0],'\t',i[1],'\t\t\t',i[2])
                              else:
                                    print('   ',i[0],'\t',i[1],'\t',i[2])
                        else:
                              flag2=1
                        
def order_food():
      print()
      confirmorder=0
      with open ('DEV_HOTEL/activerec.csv','r') as f:
            r=csv.reader(f)
            room_no=input('Enter Room No')
            password=input('Enter Room Code')
            flag=0
            for i in r:
                  if i[0]==room_no:
                        flag=1
                        if i[6]==password:
                              originalcost=int(i[5])
                              with open('DEV_HOTEL/menu.csv','r') as f:
                                    with open('DEV_HOTEL/orders.csv','a',newline='') as f1:
                                          print()
                                          print('Select your time')
                                          print('1. Breakfast')
                                          print('2. Lunch')
                                          print('3. Dinner')
                                          time=choice(1,3)
                                          food_menu(time)
                                          w=csv.writer(f1,delimiter=',')
                                          r=csv.reader(f)
                                          print()
                                          print('Enter your order')
                                          print('Enter S.no of food seprated by space')
                                          print('(Enter twice to get double)')
                                          print()
                                          a=input()
                                          order=a.split()
                                          print('Your Orders:  ',end='')
                                          cost=0
                                          orderlist=[room_no]
                                          for i in order:  #getting order
                                                fflag=0
                                                f.seek(0,0)
                                                for j in r:
                                                      if j[1] in ['1','2','3']:
                                                            fflag=0
                                                      if j[1]==str(time):
                                                            fflag=1
                                                      if fflag==1:
                                                            if j[0]==i:
                                                                  print(j[1],end=', ')
                                                                  orderlist.append(j[1])
                                                                  cost=cost+int(j[2])
                                          orderlist.append(cost)
                                          print()
                                          print('Your total Cost: ₹'+str(cost))
                                          orderlist.append(time)
                                          while True:
                                                confirm=input('Confirm your order?  (yes/no)  ')
                                                if confirm.lower() == 'yes':
                                                      print('Order Confirmed')
                                                      print('Enjoy Your Meal !')
                                                      w.writerow(orderlist)
                                                      originalcost+=cost
                                                      confirmorder=1
                                                      break
                                                elif confirm.lower()=='no':
                                                      print('Your order has been canceled')
                                                      break
                                                else:
                                                      print('Invalid Input')
                        else:
                              print('Room Code is Incorrect')
            if flag==0:
                  print('Invalid Room No')
      if confirmorder==1:
            upgrate_cost(room_no,originalcost)
            
def upgrate_cost(room_no,originalcost):
    with open ('DEV_HOTEL/activerec.csv','r') as f:
          with open('DEV_HOTEL/temp.csv','w',newline='') as f1:
                r=csv.reader(f)
                w=csv.writer(f1,delimiter=',')
                for i in r:
                      if i[0]==str(room_no):
                            i[5]=originalcost
                      w.writerow(i)
                      
    os.remove('DEV_HOTEL/activerec.csv')
    os.rename('DEV_HOTEL/temp.csv','DEV_HOTEL/activerec.csv')
            
def passwordcheck(roomno,password):
      with open('DEV_HOTEL/activerec.csv','r') as f8:
            r=csv.reader(f8)
            for i in r:
                  if int(i[0])==roomno:
                        if i[6]==password:
                              return True
                        else:
                              return False

def massage():
      print('Enter your Room No.')
      roomno=choice(1,1000)
      password=input('Enter Room Code')
      check=passwordcheck(roomno,password)
      if check == True:
            quit1=0
            print("\t\t\tMassage")
            print("\tMassage Type\t\tPrice")
            print("________________________________________________\t\t")
            print('1. Swedish Massage (90 min) \t\t ₹500')
            print('2. Hot Stone Massage (90 min) \t\t ₹750')
            print('3. Thai Massage (60 min) \t\t ₹1000')
            print('4. Aromatherapy (60 min) \t\t ₹560')
            print('5. Deep Tissue Massage (60 min) \t ₹800')
            print('6. Sports Massage (50 min) \t\t ₹450')
            print('7. Trigger Point Massage (90 min) \t ₹1500')
            print('8. Quit this Screen')
            print()
            print('Enter your choice(1-8):')
            c=choice(1,8)
            if c==1:
                  cost=500
            elif c==2:
                  cost=750
            elif c==3:
                  cost=1000
            elif c==4:
                  cost=560
            elif c==5:
                  cost=800
            elif c==6:
                  cost=450
            elif c==7:
                  cost=1500
            elif c==8:
                  quit1=1
            if quit1==0:
                  print('Your Total Bill is: ₹'+str(cost))
                  with open('DEV_HOTEL/activerec.csv','r') as f:
                        with open ('DEV_HOTEL/temp.csv','w',newline='') as f1:
                              r=csv.reader(f)
                              w=csv.writer(f1)
                              for i in r:
                                    if int(i[0])==roomno:
                                          i[5]=int(i[5])
                                          i[5]=i[5]+cost
                                    w.writerow(i)
                  updateactiverec()        
            else:
                  print('Canceled')
      else:
            print('Wrong Code')
            
def updateactiverec():
      os.remove('DEV_HOTEL/activerec.csv')
      os.rename('DEV_HOTEL/temp.csv','DEV_HOTEL/activerec.csv')

def vehiclerent():
      print('Enter Room no')
      roomno=choice(1,1000)
      password=input('Enter Room Code')
      check=passwordcheck(roomno,password)
      if check==1:
            quit1=0
            print("\t\tRent a Car\t\t")
            print("Car\t\tPrice(per hour)")
            print("________________________________________________\t\t")
            print("1. Mini\t\t₹600")
            print("2. Sedan\t\t₹1000")
            print("3. Hatchback\t₹700")
            print("4. SUV\t\t₹2000")
            print("5. Sports\t\t₹6500")
            print('6. Quit This Screen')
            print("________________________________________________\t\t")
            print("Enter your Choice")
            c=choice(1,6)
            if c!=6:
                  hours=int(input("How many hours?"))
                  if c==1:
                        print("You chose a Mini")
                        bill=600*hours
                  elif c==2:
                        print("You chose a Sedan")
                        bill=1000*hours
                  elif c==3:
                        print("You chose a Hatchback")
                        bill=700*hours
                  elif c==4:
                        print("You chose a SUV")
                        bill=2000*hours
                  elif c==5:
                        print("You chose a Sports car, drive it safely!")
                        bill=6500*hours
                  print('Your Cost for',hours,'hours is',"₹",bill)
                  with open('DEV_HOTEL/activerec.csv','r') as f:
                              r=csv.reader(f)
                              for i in r:
                                    if int(i[0])==roomno:
                                          originalcost=int(i[5])+bill
                  upgrate_cost(roomno,originalcost)
            else:
                  print('Order Canceled')

def complaint():
      print('Enter Room No.')
      roomno=choice(1,1000)
      password=input('Enter Room Code')
      check=passwordcheck(roomno,password)
      if check==1:
            print("\t\tChoose your Cateogry\t\t")
            print("1. Room Cleanliness")
            print("2. Behaviour of the Staff")
            print("3. Restaurant")
            print("4. Hygiene")
            print("5. Others")
            c=choice(1,5)
            if c>=1 and c<=5:
                  with open("DEV_HOTEL/complaint.csv","a",newline='') as f:
                        cw=csv.writer(f,delimiter=',')
                        while True:
                              roomn=roomno
                              complaint=input("Enter your Complaint:")
                              l=[roomn,complaint]
                              cw.writerow(l)
                              print("Complaint registered for Room No.",roomn,". Issue will be resolved as soon as possible")
                              print("Sorry for your Inconvinience")
                              print("Enter N to stop and Y to continue")
                              a=input()
                              if a in 'Nn':
                                    break
            else:
                  print("Invalid Input")
                  complaint()


def customerhelpline():
      print('1. Toll-free')
      print('2. Reception Desk')
      print('3. Account Desk')
      print('4. Cleaning')
      print('5. Restaurant Desk')
      print('6. Car Rental')
      print('7. Exit')
      print('Enter Choice(1-6)')
      c=choice(1,6)
      if c==1:
            print("Toll-Free Numbers")
            print("1. Hotel- 1800 313 1212")
            print("2. Restaurant- 1800 124 6755")
      elif c==2:
            print("Reception Desk")
            print("Meet- +919785264256")
            print("Alok- +917488527914")
            print("Ramya- +916288121345")
            print("Shlok- +917888246653")
      elif c==3:
            print("Account Desk")
            print("Shubhrojeet- +919778392543")
            print("Shubham- +918210568662")
            print("Sujeet- +918907654661")
      elif c==4:
            print("Cleaning Desk")
            print("Bhavya- +917778821445")
            print("Abhishek- +918992568875")
      elif c==5:
            print("Restaurant Desk")
            print("Shilpa- +919976343244")
            print("Ananya- +918340651524")
      elif c==6:
            print("Car Rental Company Desk")
            print("Amandeep- +916264600542")
      elif c==7:
            pass

def choice(i,f):  
      try:
            c=int(input())
            if c>=i and c<=f: 
                  return c
            else:
                  print('Invalid Number')
                  c=choice(i,f)
                  return c
      except:
            print('Invalid Number')
            c=choice(i,f)
            return c
      
      
      
def cmenu():
      while True:
            print("\t\t\t\t  DEV PALACE\t\t\t\t")
            print("\n\t\t****************************************************\t\t")
            print()
            print('\t\t\t\tMain Menu')
            print('1. Book a Room')
            print('2. Order Food')
            print('3. Play an arcade')
            print('4. Massage')
            print('5. Rent a Vehicle')
            print('6. File a complaint')
            print('7. Customer Helpline')
            print('8. Quit')
            print('Enter (1-8)')
            c=choice(1,8)
            if c==1:
                custdetails()
            elif c==2:
                order_food()
            elif c==3:
                arcaderent()
            elif c==4:
                massage()
            elif c==5:
                  vehiclerent()
            elif c==6:
                  complaint()
            elif c==7:
                  customerhelpline()
            elif c==8:
                  break
######################


def updateRoomRec():
    os.remove("DEV_HOTEL/roomrec.csv")
    os.rename("DEV_HOTEL/temp.csv","DEV_HOTEL/roomrec.csv")
    
def disableRoom():
    with open("DEV_HOTEL/roomrec.csv","r") as f:
        with open("DEV_HOTEL/temp.csv","w",newline='') as f1:
            print("Enter Room No. to Disable")
            check=choice(1,1000)
            csvr=csv.reader(f)
            csvw=csv.writer(f1,delimiter=',')
            flag=0
            for i in csvr:
                if int(i[0])==check:
                    if i[4].lower()!='disable':
                        i[4]='disable'
                        flag=1
                csvw.writerow(i)
    if flag==1:
        print("Room Disabled")
    else:
        print("Room Already Disabled")
    updateRoomRec()

def showdisabledrooms():
    with open("DEV_HOTEL/roomrec.csv","r") as f:
        print('1. North Wing')
        print('2. East Wing')
        print('3. South Wing')
        print('4. West Wing')
        print('5. Hotel') 
        print("Enter (1-5)")
        wing=choice(1,5)
        csvr=csv.reader(f)
        if wing!=5:
            print('Room \tFloor')
            print("_____________________________________________\t\t")
            for i in csvr:
                if int(i[1])==wing:
                    if i[4]=='disable':
                        print(i[0],'\t',i[2])
        else:
            print('Room \t wing \t Floor')
            for i in csvr:
                if i[4]=='disable':
                    print(i[0],'\t',i[1],'\t',i[2])
                    
def showbookedrooms():
    with open("DEV_HOTEL/roomrec.csv","r") as f:
        print('1. North Wing')
        print('2. East Wing')
        print('3. South Wing')
        print('4. West Wing')
        print('5. Hotel') 
        print("Enter (1-5)")
        wing=choice(1,5)
        csvr=csv.reader(f)
        if wing!=5:
            print('Room \tFloor')
            print("_____________________________________________\t\t")
            for i in csvr:
                if int(i[1])==wing:
                    if i[4]=='booked':
                        print(i[0],'\t',i[2])
        else:
            print('Room \t wing \t Floor')
            for i in csvr:
                if i[4]=='booked':
                    print(i[0],'\t',i[1],'\t',i[2])

def readorder():
    print()
    rol=[] #carries room no that should removed
    with open('DEV_HOTEL/orders.csv','r') as f:
        r=csv.reader(f)
        for i in r:
            print('Room No:',i[0])
            if i[-1]=='1':
                print('Time: BreakFast')
            elif i[-1]=='2':
                print('Time: Lunch')
            elif i[-1]=='3':
                print('Time: Dinner')
            print('Orders:-')
            ol=i[1:-2]
            for j in ol:
                print(j)
            print()
            print('Type N for Next Order')
            print('or Type Y to Complete Order')
            while True:
                c=input()
                if c in 'Nn':
                    break
                elif c in 'Yy':
                    print('Order Confirmed')
                    print()
                    rol.append(i[0])
                    break
        print()
        print('No More Orders')
    if any(rol) == True:
        removeorder(rol)
def removeorder(l):
    with open('DEV_HOTEL/orders.csv','r') as f:
        with open('DEV_HOTEL/temp.csv','w',newline='') as f1:
            r=csv.reader(f)
            w=csv.writer(f1)
            for i in r:
                if i[0] not in l:
                    w.writerow(i)
    update_orders()
    
def update_orders():
    os.remove('DEV_HOTEL/orders.csv')
    os.rename('DEV_HOTEL/temp.csv','orders.csv')

def getcostinfo(w=0): #w=1 for costumer
      print('Enter Room no:')
      roomno=choice(1,1000)
      check=True
      if w==1:
            check=False
            password=input('Enter Room Code')
            check=checkpassword(roomno,password)
      if check==True:
            with open('DEV_HOTEL/activerec.csv','r') as f:
                  r=csv.reader(f)
                  flag=0
                  for i in r:
                        if int(i[0])==roomno:
                              flag=1
                              print('Total Cost: ',int(i[7])+int(i[5]))
                              print('Cost Paid: ',i[7])
                              print('Left: ',i[5])
                  if flag==0:
                        print("Room isn't booked")
      else:
            print('Wrong Code')
def billing():
      print('Enter Customer Room no')
      roomno=choice(1,1000)
      print('Enter amount Costumer deposited')
      with open('DEV_HOTEL/activerec.csv','r') as f:
            with open('DEV_HOTEL/temp.csv','w',newline='') as f1:
                  r=csv.reader(f)
                  w=csv.writer(f1)
                  flag=0
                  for i in r:
                        if int(i[0])==roomno:
                              amount=choice(1,int(i[5]))
                              flag=1
                              i[5]=int(i[5])-amount
                              i[7]=int(i[7])+amount
                        w.writerow(i)
      if flag==0:
            print('Room isnt booked')
      updateactiverec()
                  
def readcustomerrec():
      with open('DEV_HOTEL/customerrec.csv','r') as f:
            r=csv.reader(f)
            name=input('Enter name to search').lower()
            flag=1
            for i in r:
                  if i[0].lower()==name:
                        flag=1
                        print()
                        print('Name: ',i[0])
                        print('City: ',i[1])
                        print('Phone No.:',i[4])
                        print('Verification:',i[5])
                        print('Room No.',i[7])
                        print('Check-in Date',i[9])
##                        print(i[10])  #checkout date
                  print('type n for next page')
                  enter=input('Type Q to quit')
                  if enter in 'Nn':
                        pass
                  elif enter in 'Qq':
                        flag=2
                        break
            if flag==0:
                  print('No records found with that name')
            elif flag==1:
                  print('No more records with same name')

                  
def complaintview():
      print("View Complaints")
      print("Room No.\t Complaint")
      print("_____________________________________________\t\t")
      with open("DEV_HOTEL/complaint.csv","r") as f:
            r=csv.reader(f)
            for i in r:
                  print(i[0],'\t',i[1])


def feedbackview():
      print("View feedbacks by Customers")
      print("_____________________________________________\t\t")
      with open("DEV_HOTEL/feedback.csv","r") as f:
            r=csv.reader(f)
            c=0
            q1,q2,q3,q4,q5,q6=0,0,0,0,0,0
            for i in r:
                  q1=q1+int(i[0])
                  q2=q2+int(i[1])
                  q3=q3+int(i[2])
                  q4=q4+int(i[3])
                  q5=q5+int(i[4])
                  q6=q6+int(i[5])
                  c=c+1
                  print('1. How do you like our Hospitality?',int(q1//c),'⭐')
                  print('2. How do you like our Food?',int(q2//c),'⭐')
                  print('3. How is our arcade facility for kids?',int(q3//c),'⭐')
                  print('4. How is our taxi rental company?',int(q4//c),'⭐')
                  print('5. How is the massage?',int(q5//c),'⭐')
                  print('6. In the end, how would you rate this hotel?',int(q6//c),'⭐')
                  
def feedback():
      print('Enter Room No.')
      roomno=choice(1,1000)
      print("\t\tHow would you like us to Rate?\t\t")
      print('chose (1-5) ⭐')
      print('1. How do you like our Hospitality?')
      print('chose (1-5) ⭐')
      c1=choice(1,5)
      print('2. How do you like our Food?')
      print('chose (1-5) ⭐')
      c2=choice(1,5)
      print('3. How is our arcade facility for kids?')
      print('chose (1-5) ⭐')
      c3=choice(1,5)
      print('4. How is our taxi rental company?')
      print('chose (1-5) ⭐')
      c4=choice(1,5)
      print('5. How is the massage?')
      print('chose (1-5) ⭐')
      c5=choice(1,5)
      print('6. In the end, how would you rate this hotel?')
      print('chose (1-5) ⭐')
      c6=choice(1,5)
      with open("DEV_HOTEL/feedback.csv","a",newline='') as f:
            cw=csv.writer(f,delimiter=',')
            cw.writerow([c1,c2,c3,c4,c5,c6])
            print("Thank You for your valuable feedback!")

def update_rooms():
      print()
      print('\t\t\t\tRoom Update')
      print('1. Disable Room')
      print('2. Enable Room')
      print('3. Back')
      c=choice(1,3)
      if c==1:
            disableRoom()
      if c==2:
            enableRoom()
            
def show_rooms():
      print()
      print('\t\t\t\tRoom Update')
      print('1. Show Disabled Room')
      print('2. Show Booked Room')
      print('3. Back')
      c=choice(1,3)
      if c==1:
            showdisabledrooms()
      if c==2:
            showbookedrooms()

            
def costumer():
      print()
      print('\t\t\t\tRoom Update')
      print('1. read customer record')
      print('2. check avg feedback')
      print('3. check complain ')
      print('4. Back')
      c=choice(1,4)
      if c==1:
            readcustomerrec()
      if c==2:
            feedbackview()
      if c==3:
            complaintview()
            
def smenu():
      while True:
            print("\t\t\t\t  DEV PALACE\t\t\t\t")
            print("\n\t\t****************************************************\t\t")
            print()
            print('\t\t\t\tMain Menu')
            print('1. Update rooms')
            print('2. show rooms')
            print('3. check orders')
            print('4. show cost info')
            print('5. payments')
            print('6. Customer')
            print('7. Quit')
            print('Enter (1-8)')
            c=choice(1,8)
            if c==1:
                update_rooms()
            elif c==2:
                show_rooms()
            elif c==3:
                readorder()
            elif c==4:
                  getcostinfo()
            elif c==5:
                  billing()
            elif c==6:
                  costumer()
            elif c==7:
                  break      
def menu():
    password='dev123'
    while True:
        print()
        print("\t\t\t\t  DEV PALACE\t\t\t\t")
        print('1) for customer')
        print('2) for staff')
        print('enter (1,2)')
        c=choice(1,2)
        if c==1:
            cmenu()
        if c==2:
            a=input('Enter password')
            if password==a:
                smenu()
            else:
                print('Wrong Password')
menu()
