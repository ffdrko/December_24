todo_list = []

while True:
    user_action = input("Type add, show or exit: ").strip()

    match user_action:
        case "add":
            task = input("Enter a todo: ")
            todo_list.append(task)
        case "show":
            for task in todo_list:
                print(task)
        case "exit":
            break

print("End of operation")