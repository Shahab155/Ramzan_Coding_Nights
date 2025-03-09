import click  # Import click library to create CLI
import json  # Import json to save and load tasks from a file
import os  # Import os to check if the file exists

TODO_FILE = "todo.json"  # Define the filename where tasks are stored

# Function to load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TODO_FILE):  # Check if file does not exist
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)  # Load and return the JSON data as a Python list

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)  

# Function to create the CLI group
@click.group()  
def cli():
    """Simple To-Do List Manager"""  
    pass  # No action, acts as a container for commands

@click.command()  
@click.argument("task")  
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()  
    tasks.append({"task": task, "done": False})  
    save_tasks(tasks)  
    click.echo(f"Task added: {task}")  

@click.command()  
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:  
        click.echo("No tasks found!")  
        return  
    for index, task in enumerate(tasks, 1):  
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {task['task']} [{status}]")

@click.command()  
@click.argument("task_number", type=int)  
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()  
    if 0 < task_number <= len(tasks):  
        tasks[task_number - 1]["done"] = True  
        save_tasks(tasks)  
        click.echo(f"Task {task_number} marked as completed!")
    else:  
        click.echo("Invalid task number.")  

@click.command()  
@click.argument("task_number", type=int)  
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()  
    if 0 < task_number <= len(tasks):  
        removed_task = tasks.pop(task_number - 1)  
        save_tasks(tasks)
        click.echo(f"Removed task: {removed_task['task']}")  

# Add commands to the CLI group
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

# If the script is run directly, start the CLI
if __name__ == "__main__":
    cli()
