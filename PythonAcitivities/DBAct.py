import tkinter as tk
from tkinter import ttk, messagebox

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("650x500")

        # Make the window resizable
        self.root.resizable(True, True)

        # Initialize variables
        self.employee_number_var = tk.StringVar()
        self.employee_name_var = tk.StringVar()
        self.employment_status_var = tk.StringVar(value="Permanent")
        self.position_var = tk.StringVar()
        self.salary_var = tk.StringVar()

        # Create the main frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10, bg="#f0f0f0")
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Configure grid weights for resizing
        self.main_frame.grid_rowconfigure(10, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=1)

        # Create title
        title_label = tk.Label(self.main_frame, text="EXERCISE : by Group", font=("Arial", 14, "bold"), bg="#f0f0f0")
        title_label.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=(0,20))

        # Create form inputs
        # Employee Number
        tk.Label(self.main_frame, text="Employee Number:", anchor="w", bg="#f0f0f0").grid(row=1, column=0, sticky=tk.W)
        employee_number_entry = tk.Entry(self.main_frame, textvariable=self.employee_number_var, width=20)
        employee_number_entry.grid(row=1, column=1, sticky=tk.W, padx=(0,10))

        # Search button
        search_button = tk.Button(self.main_frame, text="SEARCH", width=8)
        search_button.grid(row=1, column=2, sticky=tk.W)

        # Employee Name  
        tk.Label(self.main_frame, text="Employee Name:", anchor="w", bg="#f0f0f0").grid(row=2, column=0, sticky=tk.W)
        employee_name_entry = tk.Entry(self.main_frame, textvariable=self.employee_name_var, width=20)
        employee_name_entry.grid(row=2, column=1, sticky=tk.W)

        # Employment Status
        tk.Label(self.main_frame, text="Employment Status:", anchor="w", bg="#f0f0f0").grid(row=3, column=0, sticky=tk.W)
        status_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        status_frame.grid(row=3, column=1, sticky=tk.W)

        status_options = [("Permanent", "Permanent"), ("Probationary", "Probationary"),
                       ("Casual", "Casual"), ("Contractual", "Contractual")]

        for i, (text, value) in enumerate(status_options):
            tk.Radiobutton(status_frame, text=text, variable=self.employment_status_var, value=value,
                        bg="#f0f0f0").grid(row=i, column=0, sticky=tk.W)

        # Position
        tk.Label(self.main_frame, text="Position:", anchor="w", bg="#f0f0f0").grid(row=7, column=0, sticky=tk.W)
        self.position_combo = ttk.Combobox(self.main_frame, textvariable=self.position_var,
                                       values=["Clerk", "Accountant", "Sales Manager", "Production Staff",
                                             "Project Manager"], width=18)
        self.position_combo.grid(row=7, column=1, sticky=tk.W)

        # Salary 
        tk.Label(self.main_frame, text="Salary:", anchor="w", bg="#f0f0f0").grid(row=8, column=0, sticky=tk.W)
        salary_entry = tk.Entry(self.main_frame, textvariable=self.salary_var, width=20, state='disabled')
        salary_entry.grid(row=8, column=1, sticky=tk.W)

        # Display position and salary reference
        position_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        position_frame.grid(row=1, column=3, rowspan=5, padx=20, sticky=tk.N+tk.S)

        positions = ["Clerk", "Accountant", "Sales Manager", "Production Staff", "Project Manager"]
        salaries = ["20,000.00", "25,000.00", "40,000.00", "22,000.00", "50,000.00"]

        tk.Label(position_frame, text="Position:", bg="#f0f0f0").grid(row=0, column=0, sticky=tk.W)
        tk.Label(position_frame, text="Salary", bg="#f0f0f0").grid(row=0, column=1, sticky=tk.W, padx=(20,0))

        for i, (pos, sal) in enumerate(zip(positions, salaries)):
            tk.Label(position_frame, text=pos, bg="#f0f0f0").grid(row=i+1, column=0, sticky=tk.W)
            tk.Label(position_frame, text=sal, bg="#f0f0f0").grid(row=i+1, column=1, sticky=tk.W, padx=(20,0))

        # Create button frame
        button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        button_frame.grid(row=9, column=0, columnspan=3, pady=10, sticky=tk.W+tk.E)

        # Buttons
        add_button = tk.Button(button_frame, text="ADD", width=10)
        add_button.grid(row=0, column=0, padx=5)

        update_button = tk.Button(button_frame, text="UPDATE", width=10)
