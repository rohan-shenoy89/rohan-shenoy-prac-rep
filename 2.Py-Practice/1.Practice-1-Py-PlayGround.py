#################################
#SUBJECT - Python Learnig
#CORE SUBJECT - Loop Learing
#DEVELOPER - Rohan Shenoy
################################

#Function to Calculate Factorial:

def factorial(n):
    result = 1 # Define initial value in result argument

    for i in range(1, n+1): #For loop to iterate over the given range
        result += i         # Add each number to the result from above given range
    return result           # Return the result


print(f"The value for given Factorial - {factorial(11)}")        # Call the function to get the result
print("\n*****************\n")

#Function to Check for Palindrome

def palindrome(word):
    word = word.lower()     # Make sure the all the letters are in lower case

    for s in range(len(word)//2): # Take the length of the word and round it up with base
       if word[s] != word[-s -1]: # Check if 1st letter is not eq to last letter
           return False           # if yes, return False
    return True                   # Else return True


palindrome('Radar')               # Take the value in the function:
if True:                          # Check the functions returned value and print your statement
    print(f"The given word is a Palindrome")
else:
    print(f"The given word is not a Palindrome")
print("\n*****************\n")

import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        # Task Entry
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task Button
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # To-Do List
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Remove Task Button
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=2, column=0, padx=10, pady=10)

        # Mark as Completed Button
        complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        complete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def mark_completed(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.itemconfig(index, {'bg': 'light green'})
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
