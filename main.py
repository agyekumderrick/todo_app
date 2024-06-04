tasks = []
# display menu
def display_menu():
    print("1.Add task")
    print("2.View task")
    print("3.Update task")
    print("4.Delete task")
    print("5.Exit")


# add tasks function
def Add_task():
    user_task = input("Kindly enter a task:\n")
    tasks.append(user_task)
    print("Kindly enter a task")


# exit function
def exit_program():
    exit(1)