tasks = []

def creat_default_tasks():
    tasks.append({
        'title': 'Have a rest',
        'status': 'pending',
        'id': 0
    })
    tasks.append({
        'title': 'Go to sleep',
        'status': 'done',
        'id': 1
    })

def show_all_tasks():
    print("-----All tasks: -----")
    for task in tasks:
        print(f"{task['id']}. {task['title']} - {task['status']}")
    print("----- ----- -----")

def add_new_task():
    newId = len(tasks)
    title = input("Task title: ")
    tasks.append({
        'title': title,
        'status': 'pending',
        'id': newId
    })
    print(f"new task with id: {newId} was added!")

def mark_as_done():
    taskId = int(input("Which task ID mark as done: "))
    taskToUpdate = None
    
    for task in tasks:
        if task['id'] == taskId:
            taskToUpdate = task
            break
        
    if not taskToUpdate:
        print("You have provided wrong ID!")
    else:
        taskToUpdate['status'] = 'done'
        print(f"Task with ID {taskId} marked as done.")
                     
def delete_task():
    taskId = int(input("Which task ID should be deleted: "))
    taskToDelete = None
    
    for task in tasks:
        if task.get('id') == taskId:
            taskToDelete = task
            break
        
    if not taskToDelete:
        print("You have provided wrong ID!")
    else:
        tasks.remove(taskToDelete)
        print(f"Task with ID {taskId} was deleted.")
      
def show_all_done_tasks():
    doneTasks = [ task for task in tasks if task['status'] == 'done']
    if(len(doneTasks) == 0 ):
        print('No cmpleted tasks!')
    else:
        for item in doneTasks:
            print(f"{item['id']}. --> {item['title']}")        

def main():
    creat_default_tasks()
    while True:
        print("""
              1. Add a task
              2. View all tasks
              3. Mark a task as complete
              4. Delete a task
              5. View all done tasks
              6. Exit
              """)
        choice = input("Enter a task number: ")
        if choice == "1":
            add_new_task()
        elif choice == "2":
            show_all_tasks()
        elif choice == "3":
            mark_as_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            show_all_done_tasks()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
