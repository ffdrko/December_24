while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            with open('Files/todo_list.txt') as file:
                todo_list = file.readlines()

            task = input("Enter a todo: ") + "\n"
            todo_list.append(task)

            with open('Files/todo_list.txt', 'w') as file:
                file.writelines(todo_list)

        case "show":
            with open('Files/todo_list.txt') as file:
                todo_list = file.readlines()

            for index, task in enumerate(todo_list):
                print(f"{index + 1}-{task.strip('\n')}")
        case 'edit':
            with open('Files/todo_list.txt') as file:
                todo_list = file.readlines()

            todo_num = int(input("Enter your todo number: ")) - 1
            todo_list[todo_num] = input("Enter your new todo: ") + '\n'

            with open('Files/todo_list.txt', 'w') as file:
                file.writelines(todo_list)

        case 'complete':
            with open('Files/todo_list.txt') as file:
                todo_list = file.readlines()

            todo_num = int(input("Enter your todo number: ")) - 1
            todo_list.pop(todo_num)

            with open('Files/todo_list.txt', 'w') as file:
                file.writelines(todo_list)
        case "exit":
            break

print("End of operation")
