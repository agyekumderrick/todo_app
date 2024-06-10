tasks = []
# display menu
def display_menu():
    print("1.Add task")
    print("2.View task")
    print("3.Update task")
    print("4.Delete task")
    print("5.Exit")


# add tasks function
def add_task():
    user_task = input("Kindly enter a task:\n")
    tasks.append(user_task)
    print("Task added successfully")

# view task functon
# def view_task():
#     if len(tasks) > 0:
#         print(tasks)
#     else:
#         print("Nothing in your task yet")
# another way to view task
def view_task():
    if not tasks:
        print("Sorry, but you do not have any saved task yet. Choose option 1(add tak) from he previous dialog to add a new task")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}")

# users are allowed to update an already saved task
def update_task():
    view_task()
    task_number = int(input("Enter the task number you ant to update"))
    if 1 <= task_number <= len(tasks):
        updated_task = input("Enter update")
        tasks[task_number -1] = updated_task

# users are allowed to omit an already entered task from the todo_list 
def delete_task():
    view_task()
    delete_option = int(input("Would you like to delete\n"
                          "1. Delete a task\n"
                          "2. Delete all\n"
                          "Enter here ... "))
    if delete_option == 1:
        tobe_deleted = int(input("Input the task number to delete\n"))
        # if tobe_deleted >= len(tasks) or tobe_deleted <= len(tasks):
        if 1 <= tobe_deleted <= len(tasks):
            tasks.pop(tobe_deleted -1)
            print("Task deleted successfully")
    elif delete_option == 2:
        tasks.clear
    else:
        print("Kindly choose either 1 or 2 to delete")  
# exit function
def exit_program():
    exit(1)