print("*=*=*=*=*=*===== TO DO LIST =====*=*=*=*=*=*")
lis=[]
while True:
    inp=input(" Do you want to create a List ? (Yes/No):")
    if inp.lower()=='yes':
        print("*=*=*=*=*=List is Created=*=*=*=*=*=* \n Proceed for nexr Process")
        while True:
            choice=input(" MENU :\n 1. Enter the Task\n 2. View the Tasks \n 3. Change the Task conditon\n 4. Delete the Task\n 5. Exit the List\n Enter the any option (from 1 to 5):")
            if choice=='1':
                i=int(input("Enter the how many Tasks are to be entered Now :"))
                for n in range(i):
                    task=input("Enter the Task:")
                    lis.append({'Task':task,'done':'Not Done'})
                    print("*=*=*=*=*=Task was Added in to the List*=*=*=*=*=")
                print("*****The Entering Tasks to List  is completed*****")
            elif choice=='2':
                for ind,tem in enumerate(lis):
                    print(f" Task {ind+1}: {tem['Task']} *=*=*=*=*=Condition :{tem['done']}")
            elif choice=='3':
                k=int(input("Enter the Order of the Task :"))
                while 0<=k<=len(lis):
                    Con=input("Enter the Condition to be changed:")
                    print("*=*=*=*=*=Condition Changed*=*=*=*=*=")
                    lis[k-1]['done']=Con
                    print(f"Task {k} :{lis[k-1]['Task']} \n The  Condition of Task changed to: {lis[k-1]['done']}")
                    break
            elif choice=='4':
                dl=int(input("enter the Task Order to Delete: "))
                del lis[dl-1]
                print("*=*=*=*=*=Task was Deleted from the List*=*=*=*=*=")
                print("The Tasks after the Deletion of the above Specific Task in List: ")
                for ix,tem in enumerate(lis):
                    print(f"Task {ix+1}: {tem['Task']} -----{tem['done']}")
            elif choice=='5':
                print("Exiting the List")
                print("*****Thank You*****")
                print("*=*=*=*=*= Welcome *=*=*=*=*=")
                break
            else:
                print("Invalid Choice")
        break
    elif inp.lower()=='no':
        print("*=*=*=*=*=Thank You For Visiting*=*=*=*=*=")
        break
    else:
        print("Invalid Input \n Please Try Again")
