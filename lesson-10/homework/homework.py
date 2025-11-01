from datetime import datetime

# Homework 1: ToDo List Application

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} | {self.status} | Due: {self.due_date} | {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                break

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if task.status == "Incomplete":
                print(task)


def run_todo_app():
    todo = ToDoList()
    while True:
        print("\nToDo List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Task Title: ")
            desc = input("Description: ")
            due = input("Due Date (YYYY-MM-DD): ")
            todo.add_task(title, desc, due)
        elif choice == "2":
            title = input("Enter task title to mark complete: ")
            todo.mark_task_complete(title)
        elif choice == "3":
            todo.list_all_tasks()
        elif choice == "4":
            todo.list_incomplete_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


# Homework 2: Simple Blog System

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date = datetime.now()

    def __str__(self):
        return f"{self.title} by {self.author} on {self.date.strftime('%Y-%m-%d %H:%M')}\n{self.content}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)

    def list_posts(self):
        for post in self.posts:
            print(post, "\n")

    def posts_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author == author:
                print(post, "\n")
                found = True
        if not found:
            print("No posts found for this author.")

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                break

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                break

    def latest_posts(self):
        latest = sorted(self.posts, key=lambda p: p.date, reverse=True)
        for post in latest[:5]:
            print(post, "\n")


def run_blog_app():
    blog = Blog()
    while True:
        print("\nBlog Menu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Post Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(title, content, author)
        elif choice == "2":
            blog.list_posts()
        elif choice == "3":
            author = input("Enter author name: ")
            blog.posts_by_author(author)
        elif choice == "4":
            title = input("Enter title to delete: ")
            blog.delete_post(title)
        elif choice == "5":
            title = input("Enter title to edit: ")
            content = input("New content: ")
            blog.edit_post(title, content)
        elif choice == "6":
            blog.latest_posts()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


# Homework 3: Simple Banking System

class Account:
    def __init__(self, acc_number, name, balance=0):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def transfer(self, target_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            target_account.deposit(amount)
        else:
            print("Insufficient funds for transfer.")

    def __str__(self):
        return f"Account: {self.acc_number}, Holder: {self.name}, Balance: ${self.balance}"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc_number, name, balance=0):
        account = Account(acc_number, name, balance)
        self.accounts.append(account)

    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    def deposit(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, from_acc, to_acc, amount):
        src = self.find_account(from_acc)
        dest = self.find_account(to_acc)
        if src and dest:
            src.transfer(dest, amount)
        else:
            print("One or both accounts not found.")

    def display_account(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            print(acc)
        else:
            print("Account not found.")


def run_bank_app():
    bank = Bank()
    while True:
        print("\nBank Menu:")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            num = input("Account Number: ")
            name = input("Holder Name: ")
            balance = float(input("Initial Balance: "))
            bank.add_account(num, name, balance)
        elif choice == "2":
            num = input("Account Number: ")
            bank.display_account(num)
        elif choice == "3":
            num = input("Account Number: ")
            amount = float(input("Amount: "))
            bank.deposit(num, amount)
        elif choice == "4":
            num = input("Account Number: ")
            amount = float(input("Amount: "))
            bank.withdraw(num, amount)
        elif choice == "5":
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            amount = float(input("Amount: "))
            bank.transfer(from_acc, to_acc, amount)
        elif choice == "6":
            num = input("Account Number: ")
            bank.display_account(num)
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


# Main Program Launcher

if __name__ == "__main__":
    print("Choose Homework Project to Run:")
    print("1. ToDo List Application")
    print("2. Simple Blog System")
    print("3. Simple Banking System")

    option = input("Enter option: ")
    if option == "1":
        run_todo_app()
    elif option == "2":
        run_blog_app()
    elif option == "3":
        run_bank_app()
    else:
        print("Invalid selection.")
