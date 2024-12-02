prompt = "Enter a todo: "
todo_list = []

while True:
    user_todo = input(prompt)
    todo_list.append(user_todo)
    print(user_todo)
    print(todo_list)