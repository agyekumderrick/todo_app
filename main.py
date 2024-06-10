# import our program module
from program import *
print("************ Welometo my to-do application ************")
# get user choice
while True:
    display_menu()
    # accept user option
    user_option = int(input("kindly choose from either of the following options:\n"
                            "Enter here => "))
    if user_option == 1:
        add_task()
    elif user_option == 2:
        view_task()
    elif user_option == 3:
        update_task()
    elif user_option == 4:
        delete_task()
    elif user_option == 5:
        exit()
    else:
        print("Invalid option, Kindly choose between 1 - 5")