while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            file = open("Files/todo_list.txt", "r")
            todo_list = file.readlines()
            file.close()

            task = input("Enter a todo: ") + "\n"
            todo_list.append(task)

            file = open("Files/todo_list.txt", "w")
            file.writelines(todo_list)
            file.close()

        case "show":
            for index, task in enumerate(todo_list):
                print(f"{index + 1}-{task}")
        case 'edit':
            todo_num = int(input("Enter your todo number: ")) - 1
            todo_list[todo_num] = input("Enter your new todo: ")
        case 'complete':
            todo_num = int(input("Enter your todo number: ")) - 1
            todo_list.pop(todo_num)
        case "exit":
            break

print("End of operation")
