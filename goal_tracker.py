from tkinter import Frame, Entry, Button, Tk, Canvas, Label
from tkinter import Listbox


class GoalTracker(Tk):
    def __init__(self):
        super().__init__()
        self.title("Goal Tracker")
        self.geometry("500x500")

        # Goals panel
        goals_panel = Frame(self)
        goals_label = Label(goals_panel, text="Goal: ")
        self.goals_entry = Entry(goals_panel, width=20)
        add_goal_button = Button(
            goals_panel, text="Add Goal", command=self.add_goal)
        self.goals_listbox = Listbox(goals_panel)
        goal_progress = Canvas(goals_panel, width=200, height=25)

        # Pack Goals panel components
        goals_label.pack(side="left")
        self.goals_entry.pack(side="left")
        add_goal_button.pack(side="left")
        self.goals_listbox.pack(side="left")
        goal_progress.pack(side="left")
        goals_panel.pack(side="top")

        # Tasks panel
        tasks_panel = Frame(self)
        tasks_label = Label(tasks_panel, text="Task: ")
        add_task_button = Button(
            tasks_panel, text="Add Task", command=self.add_task)
        self.tasks_listbox = Listbox(tasks_panel)
        task_progress = Canvas(tasks_panel, width=200, height=25)

        # Pack Tasks panel components
        tasks_label.pack(side="left")
        add_task_button.pack(side="left")
        self.tasks_listbox.pack(side="left")
        task_progress.pack(side="left")
        tasks_panel.pack(side="bottom")

    def add_goal(self):
        goal = self.goals_entry.get()
        self.goals_listbox.insert("end", goal)

    def add_task(self):
        goal = self.goals_listbox.get(self.goals_listbox.curselection())
        self.tasks_listbox.insert("end", f"{goal} task")


if __name__ == "__main__":
    app = GoalTracker()
