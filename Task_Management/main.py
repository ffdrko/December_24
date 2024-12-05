todo_list = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            task = input("Enter a todo: ")
            todo_list.append(task)
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
