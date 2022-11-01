class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def print(self):
        temp = self.head
        while (temp):
            print("\nMovie Name:",temp.data[0],"  \nMovie ID:",temp.data[1],"  \nTheatre Name:",temp.data[2],"  \nTotal Seats:",temp.data[3])
            temp = temp.next
    def delete(self,x):
        temp=self.head
        if temp is not None:
            if temp.data[1]==x:
                self.head=temp.next
                temp=None
                return
            while temp is not None:
                if temp.data[1]==x:
                    break
                prev=temp
                temp=temp.next
            if temp==None:
                return
            prev.next=temp.next
            temp=None 

    def insert(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node
                
a=[]
w,h=10,10
q1=[[0 for x in range(w)] for y in range(h)]
q2=[[0 for x in range(w)] for y in range(h)]
q3=[[0 for x in range(w)] for y in range(h)]
cancel1=0
cancel2=0
cancel3=0
s1=1
s2=1
s3=1
i1=0
i2=0
i3=0
z1=0
z2=0
z3=0
LL=LinkedList()
j=1
x=input("Enter movie name:")
a.append(x)
x=int(input("Enter movie id:"))
a.append(x)
x=input("Enter theatre name:")
a.append(x)
x=int(input("Enter no.of seats:"))
a.append(x)
LL.insert(a)
a=[]
x=input("Enter movie name:")
a.append(x)
x=int(input("Enter movie id:"))
a.append(x)
x=input("Enter theatre name:")
a.append(x)
x=int(input("Enter no.of seats:"))
a.append(x)
LL.insert(a)
a=[]
x=input("Enter movie name:")
a.append(x)
x=int(input("Enter movie id:"))
a.append(x)
x=input("Enter theatre name:")
a.append(x)
x=int(input("Enter no.of seats:"))
a.append(x)
LL.insert(a)
a=[]
while(True):
    print("1 -----> DISPLAY ALL MOVIES\n2 -----> BOOK TICKET\n3 -----> CANCEL A TICKET\n4 -----> DELETE AND UPDATE TICKET\n5 -----> ENTERING INTO THE MOVIE\n6 -----> DISPLAY A PARTICULAR TICKET\n7 -----> EXIT\n");
    ch=int(input("Enter your choice: "))
    if(ch==1):
        if LL.head==None:
            print("No Movies Available!!!")
        else:
            LL.print()
    elif(ch==2):
        count=1
        if LL.head==None:
            print("\n No Movies available!!!")
        else:
            LL.present=LL.head
            i=0
            while(LL.present):
                print("\nMovie Name:",LL.present.data[0],"\nMovie ID:",LL.present.data[1])
                i+=1
                LL.present=LL.present.next
            x=int(input("\nEnter the movie id:"))
            y=int(input("\nEnter the no.of tickets:"))
            LL.present=LL.head
            if(x==1):
             j=0
             if(cancel1==1 and y==1):
                 q1[i1][j]=z1
                 print("\nBooked ticket successfully!!!")
                 print("\n Your ticket no is:",i1)
                 print("\nSeat no is ",q1[i1][j])
                 LL.present.data[3]-=y
                 cancel1=0
             elif(LL.present.data[3]>0):
                LL.present.data[3]-=y
                while(j<y):
                    q1[i1][j]=s1
                    s1+=1
                    j+=1
                print("\nBooked ticket successfully!!!")
                print("\n Your ticket no is:",i1)
        
                print("\nSeat no is ")
                k=0
                while(k<y):
                    print(q1[i1][k])
                    k+=1
                i1+=1
            elif(x==2):
             LL.present=LL.head
             while(count!=2):
                    LL.present=LL.present.next
                    count+=1
             j=0
             if(cancel2==1 and y==1):
                 q2[i2][j]=z2
                 print("\nBooked ticket successfully!!!")
                 print("\n Your ticket no is:",i2)
                 print("\nSeat no is ",q2[i2][j])
                 LL.present.data[3]-=y
                 cancel2=0
             elif(LL.present.data[3]>0):
                LL.present.data[3]-=y
                
                while(j<y):
                    q2[i2][j]=s2
                    s2+=1
                    j+=1
                print("\nBooked ticket successfully!!!")
                print("\n Your ticket no is:",i2)
                print("\nSeat no is ")
                k=0
                while(k<y):
                    print(q2[i2][k])
                    k+=1
                i2+=1
            elif(x==3):
             LL.present=LL.head
             while(count!=3):
                    LL.present=LL.present.next
                    count+=1
             j=0
             if(cancel3==1 and y==1):
                 q3[i3][j]=z3
                 print("\nBooked ticket successfully!!!")
                 print("\n Your ticket no is:",i3)
                 print("\nSeat no is ",q3[i3][j])
                 LL.present.data[3]-=y
                 cancel3=0
             elif(LL.present.data[3]>0):
                LL.present.data[3]-=y
                
                while(j<y):
                    q3[i3][j]=s3
                    s3+=1
                    j+=1
                print("\nBooked ticket successfully!!!")
                print("\n Your ticket no is:",i3)
                print("\nSeat no is ")
                k=0
                while(k<y):
                    print(q3[i3][k])
                    k+=1
                i3+=1
    elif(ch==3):
                x=int(input("\nEnter your movie ID:"))
                y=int(input("\nEnter your ticket no:"))
                z=int(input("\nEnter the seat no:"))
                if(x==1):
                    j=0
                    c=1
                    while(c):
                        if(q1[y][j]==z):
                            if(j!=0):
                                while(j>=1):
                                    s=q1[y][j-1]
                                    q1[y][j-1]=q1[y][j]
                                    q1[y][j]=s
                                    j-=1
                                z1=z
                                q1[y].pop(0)
                                print("\nTicket cancelled successfully!!!")
                                cancel1=1
                                c=0
                            else:
                                q1[y].pop(0)
                                print("\nTicket cancelled successfully!!!")
                                cancel1=1
                                c=0
                        j+=1
                elif(x==2):
                    j=0
                    c=1
                    while(c):
                        if(q2[y][j]==z):
                            if(j!=0):
                                while(j>=1):
                                    s=q2[y][j-1]
                                    q2[y][j-1]=q2[y][j]
                                    q2[y][j]=s
                                    j-=1
                                z2=z
                                q2[y].pop(0)
                                print("\nTicket cancelled successfully!!!")
                                cancel2=1
                                c=0
                            else:
                                q2[y].pop(0)
                                print("\nTicket cancelled successfully!!!")
                                cancel2=1
                                c=0
                        j+=1
                elif(x==3):
                    j=0
                    c=1
                    while(c):
                        if(q3[y][j]==z):
                            if(j!=0):
                                while(j>=1):
                                    s=q3[y][j-1]
                                    q3[y][j-1]=q3[y][j]
                                    q3[y][j]=s
                                    j-=1
                                z3=z
                                q3[y].pop(0)
                                print("\nTicket cancelled successfully!!!")
                                cancel3=1
                                c=0
                            else:
                                q3[y].pop(0)
                                print("\nTicket cancelled successfully!!!")
                                cancel3=1
                                c=0
                        j+=1
    
    elif(ch==4):
        x5=0
        x=int(input("Enter the movie id to delete:"))
        x5=x
        if LL.head==None:
            print("No movies are available")
        else:
            
            LL.delete(x)
            x=input("Enter the movie name:")
            a.append(x)
            x=x5
            a.append(x)
            x=input("Enter the theatre name:")
            a.append(x)
            x=100
            a.append(x)
            LL.insert(a)
            a=[]
            print("\nUpdated successfully")
    elif(ch==5):
        x=int(input("Enter the movie id:"))
        y=int(input("Enter your ticket number:"))
        
        if(x==1):
            while(y>=1):
                s=q1[y-1]
                q1[y-1]=q1[y]
                q1[y]=s
                y-=1
            while(q1[y]):
                q1[y].pop(0)
            del(q1[y])
            print("Have a good time")
        elif(x==2):
            while(y>=1):
                s=q2[y-1]
                q2[y-1]=q2[y]
                q2[y]=s
                y-=1
            while(q2[y]):
                q2[y].pop(0)
            del(q2[y])
            print("Have a good time")
        elif(x==3):
            while(y>=1):
                s=q3[y-1]
                q3[y-1]=q3[y]
                q3[y]=s
                y-=1
            while(q3[y]):
                q3[y].pop(0)
            del(q3[y])
            print("Have a good time")
    elif(ch==6):
        x=int(input("Enter ticket no:"))
        y=int(input("Enter movie id:"))
        if(y==1):
            print("\n\n\t\t\t**TICKET**")
            print("\n\nYour seat no:",q1[x])
        elif(y==2):
            print("\n\n\t\t\t**TICKET**")
            print("\n\nYour seat no:",q2[x])
        elif(y==3):
            print("\n\n\t\t\t**TICKET**")
            print("\n\nYour seat no:",q3[x])
    else:
        break
            
        
        
    
        
    
        
              
