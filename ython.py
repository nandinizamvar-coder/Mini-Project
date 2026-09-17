#import calendar as cd

# these are terms that will be used later
task_list_relation = {
    1: "strength",
    2: "discipline",
    3: "intellect"
}

array_of_tasks_made_by_user = []
array_of_tasks_made_by_user_bool = []


#creating tasks
def create_tasks():

    # Clear previous tasks
    array_of_tasks_made_by_user.clear()

    # CONSTRAIN NUMBER OF TASKS
    while True:
        try:
            n = int(input("How many tasks do you want? "))

            if n > 0:
                break
            else:
                print("Invalid input. Enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Enter a whole number.")

    i = 0

    while i < n:

        value_1 = str(input(f"Enter task {i + 1}: "))

        # CONSTRAIN TASK TYPE
        while True:
            try:
                task_type = int(input(
                    "Enter task type 1,2,3 = strength,discipline,intellect: "
                ))

                if 1 <= task_type <= 3:
                    break
                else:
                    print("Invalid task type. Please enter 1, 2, or 3.")

            except ValueError:
                print("Invalid input. Please enter 1, 2, or 3.")

        value_2 = task_list_relation[task_type]

        array_of_tasks_made_by_user.append([value_1, value_2])

        i += 1

    print("\nTasks created successfully!")


#task completion
def enter_completion():

    if len(array_of_tasks_made_by_user) == 0:
        print("Please create tasks first.")
        return

    array_of_tasks_made_by_user_bool.clear()

    n = len(array_of_tasks_made_by_user)

    i_bool = 0

    while i_bool < n:

        # CONSTRAIN TASK COMPLETION
        while True:
            try:
                completion = int(input(
                    f"Enter task completion (1 = True, 0 = False) "
                    f"for task {i_bool + 1}: "
                ))

                if completion == 1:
                    value = True
                    break

                elif completion == 0:
                    value = False
                    break

                else:
                    print("Invalid input. Please enter 0 or 1.")

            except ValueError:
                print("Invalid input. Please enter 0 or 1.")

        array_of_tasks_made_by_user_bool.append(value)

        i_bool += 1

    print("\nTask completion saved!")


#calculating score
def calculate_score():

    if len(array_of_tasks_made_by_user) == 0:
        print("Please create tasks first.")
        return

    if len(array_of_tasks_made_by_user_bool) != len(array_of_tasks_made_by_user):
        print("Please enter completion status for all tasks first.")
        return

    result = [
        a + [b]
        for a, b in zip(
            array_of_tasks_made_by_user,
            array_of_tasks_made_by_user_bool
        )
    ]

    strength_score = sum(
        1 for entry in result
        if entry[1] == "strength" and entry[2]
    )

    discipline_score = sum(
        1 for entry in result
        if entry[1] == "discipline" and entry[2]
    )

    intellect_score = sum(
        1 for entry in result
        if entry[1] == "intellect" and entry[2]
    )

    final_score = (
        strength_score,
        discipline_score,
        intellect_score
    )

    print(
        "\nYour score for strength, discipline and intellect respectively are:",
        final_score
    )


#main menu
def main_menu():

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Create Tasks")
        print("2. Enter Task Completion")
        print("3. Calculate Score")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                create_tasks()

            elif choice == 2:
                enter_completion()

            elif choice == 3:
                calculate_score()

            elif choice == 4:
                print("Thank you for using the program!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3 or 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


main_menu()

