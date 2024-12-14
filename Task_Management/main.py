while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if 'add' in user_action:
        with open('Files/todo_list.txt') as file:
            todo_list = file.readlines()

        task = input("Enter a todo: ") + "\n"
        todo_list.append(task)

        with open('Files/todo_list.txt', 'w') as file:
            file.writelines(todo_list)

    elif 'show' in user_action:
        with open('Files/todo_list.txt') as file:
            todo_list = file.readlines()

        for index, task in enumerate(todo_list):
            print(f"{index + 1}-{task.strip('\n')}")

    elif 'edit' in user_action:
        with open('Files/todo_list.txt') as file:
            todo_list = file.readlines()

        todo_num = int(input("Enter your todo number: ")) - 1
        todo_list[todo_num] = input("Enter your new todo: ") + '\n'

        with open('Files/todo_list.txt', 'w') as file:
            file.writelines(todo_list)

    elif 'complete' in user_action:
        with open('Files/todo_list.txt') as file:
            todo_list = file.readlines()

        todo_num = int(input("Enter your todo number: ")) - 1
        todo_list.pop(todo_num)

        with open('Files/todo_list.txt', 'w') as file:
            file.writelines(todo_list)

    elif 'exit' in user_action:
        break

    else:
        print("Wrong operation!!!")


print("End of operation")
