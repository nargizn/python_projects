#Scrum to do list - для управления своими ежедневными делами и для повышения продуктивности дел. 
import time

todo = ["Wake up at 7 a.m.", "Have a breakfast", "Go to the university"]
inprocess = []
done = []

while True:
    print("\n1. Start task")
    print("2. Add task")
    print("3. Skip task")
    print("4. Edit task")
    print("5. Search task")
    print("6. Show tasks to do")
    print("7. Show tasks in process")
    print("8. Show finished tasks")
    print("9. Finish task")
    print("10. Exit\n")

    option = int(input("Choose: \n"))

    if option == 1:
        if len(todo) == 0:
            print("Nothing in todo list!")
        else:
            n = int(input("Enter task # you want to start:"))
            if(0<=n<len(todo)):
                inprocess.append(todo[n])
                del todo[n]
            else:
                print("No such task in todo list!")
        
    elif option == 2:
        task = input("Enter the task: ")
        todo.append(task)
        
      
    elif option == 3: 
        task = input("Enter the task to skip: ")
        a = 0
        for i in range(0, len(todo)): 
            if todo[i] == task:
                a = 1
                del todo[i]
                break
        if a==0:
            print("\nNo such task")


    elif option == 4: 
        task = int(input("Enter # of the task to edit: "))
        newtask = input("Enter new task: ")
        if task<len(todo):
            todo[task] = newtask
            
        else:
            print("No such task!")


    elif option == 5: 
        task = input("Enter the task to search: ")
        if task in todo: 
                print("It is in todo list!")
                
        elif task in inprocess:
                print("It is in process list!")
                
        elif task in done:
                print("It is in done list!")
                
        else:
            print("No such task!") 


    elif option == 6:
        for i in range(0, len(todo)):
            print(i, todo[i])

    elif option == 7:
        for i in range(0, len(inprocess)):
            print(i, inprocess[i])

    elif option == 8:
        for i in range(0, len(done)):
            print(i, done[i])

    elif option == 9:
        if len(inprocess) == 0:
            print("Nothing in inprocess list!")
        else:
            n = int(input("Enter task # you want to finish:"))
            if(0<=n<len(inprocess)):
                done.append(inprocess[n])
                del inprocess[n]
            else:
                print("No such task in inprocess list!")

    elif option == 10:
        print("Bye!")
        break

    else:
        print("No such option!")
    
    time.sleep(2)

