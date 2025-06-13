import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os
from PIL import Image, ImageTk  # Import PIL for image handling

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("650x500")

        # Make the window resizable
        self.root.resizable(True, True)

        # Create or connect to SQLite database
        self.conn = sqlite3.connect('employee.db')
        self.cursor = self.conn.cursor()

        # Create table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee_tbl (
                empNo INTEGER PRIMARY KEY,
                empName TEXT NOT NULL,
                empStat TEXT NOT NULL,
                empPos TEXT NOT NULL,
                empSal REAL NOT NULL
            )
        ''')
        self.conn.commit()

        # Initialize variables
        self.employee_number_var = tk.StringVar()
        self.employee_name_var = tk.StringVar()
        self.employment_status_var = tk.StringVar(value="Permanent")
        self.position_var = tk.StringVar()
        self.salary_var = tk.StringVar()

        # Load the GIF image using PIL
        self.gif_path = "your_gif_file.gif"  # Replace with your GIF file path
        try:
            self.gif_image = Image.open(self.gif_path)
            self.frames = []
            try:
                while True:
                    self.frames.append(ImageTk.PhotoImage(self.gif_image.copy()))
                    self.gif_image.seek(self.gif_image.tell() + 1)
            except EOFError:
                pass  # End of frames

            self.current_frame_index = 0
        except Exception as e:
            print(f"Error loading GIF: {e}.  Using a default background.")
            self.gif_image = None
            self.frames = []

        # Create a label to display the GIF frames
        self.background_label = tk.Label(self.root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Make it fill the entire window
        if self.frames:
            self.update_background_gif()  # Start updating the GIF frames

        # Create the main frame (on top of the background)
        self.main_frame = tk.Frame(self.root, padx=10, pady=10, bg="#f0f0f0")  # Use a background color
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Configure grid weights for resizing
        self.main_frame.grid_rowconfigure(10, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=1)

        # Create title with underline
        title_label = tk.Label(self.main_frame, text="EXERCISE : by Group", font=("Arial", 14, "bold"), bg="#f0f0f0")
        title_label.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=(0, 20))

        # Create form inputs
        # Employee Number
        tk.Label(self.main_frame, text="Employee Number:", anchor="w", bg="#f0f0f0").grid(row=1, column=0, sticky=tk.W)
        employee_number_entry = tk.Entry(self.main_frame, textvariable=self.employee_number_var, width=20)
        employee_number_entry.grid(row=1, column=1, sticky=tk.W, padx=(0,5))

        # Search button
        search_button = tk.Button(self.main_frame, text="SEARCH", command=self.search_employee, width=8)
        search_button.grid(row=1, column=2, sticky=tk.W)

        # Employee Name
        tk.Label(self.main_frame, text="Employee Name:", anchor="w", bg="#f0f0f0").grid(row=2, column=0, sticky=tk.W)
        employee_name_entry = tk.Entry(self.main_frame, textvariable=self.employee_name_var, width=20)
        employee_name_entry.grid(row=2, column=1, sticky=tk.W)

        # Employment Status
        tk.Label(self.main_frame, text="Employment Status:", anchor="w", bg="#f0f0f0").grid(row=3, column=0,
                                                                                            sticky=tk.W)
        status_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        status_frame.grid(row=3, column=1, sticky=tk.W)

        status_options = [("Permanent", "Permanent"), ("Probationary", "Probationary"),
                          ("Casual", "Casual"), ("Contractual", "Contractual")]

        for i, (text, value) in enumerate(status_options):
            tk.Radiobutton(status_frame, text=text, variable=self.employment_status_var, value=value,
                           bg="#f0f0f0").grid(row=i, column=0, sticky=tk.W)

        # Position
        tk.Label(self.main_frame, text="Position:", anchor="w", bg="#f0f0f0").grid(row=7, column=0, sticky=tk.W)
        # Use Combobox instead of Entry
        self.position_combo = ttk.Combobox(self.main_frame, textvariable=self.position_var,
                                          values=["Clerk", "Accountant", "Sales Manager", "Production Staff",
                                                  "Project Manager"], width=18)
        self.position_combo.grid(row=7, column=1, sticky=tk.W)

        # Create button frame
        button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        button_frame.grid(row=9, column=0, columnspan=3, pady=10,
                            sticky=tk.W + tk.E)  # Make button frame sticky to West and East

        # Buttons
        add_button = tk.Button(button_frame, text="ADD", width=10, command=self.add_employee)
        add_button.grid(row=0, column=0, padx=5)

        update_button = tk.Button(button_frame, text="UPDATE", width=10, command=self.update_employee)
        update_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(button_frame, text="DELETE", width=10, command=self.delete_employee)
        delete_button.grid(row=0, column=2, padx=5)

        view_button = tk.Button(button_frame, text="VIEW", width=10, command=self.view_all_records)
        view_button.grid(row=1, column=3, padx=5, pady=5)

        exit_button = tk.Button(button_frame, text="EXIT", width=10, command=root.destroy)
        exit_button.grid(row=1, column=4, padx=5, pady=5)

        # Text area for displaying results
        text_area_frame = tk.LabelFrame(self.main_frame, text="Text Area (unedited)", padx=5, pady=5, bg="#f0f0f0")
        text_area_frame.grid(row=10, column=0, columnspan=4, pady=10,
                            sticky=tk.W + tk.E + tk.N + tk.S)  # Make text area frame sticky

        self.text_area = tk.Text(text_area_frame, width=60, height=8)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Set the position entry to populate the salary when it matches a known position
        self.position_combo.bind("<<ComboboxSelected>>", self.update_salary_based_on_position)

    def update_salary_based_on_position(self, event=None):
        position = self.position_var.get()
        if position == "Clerk":
            self.salary_var.set("20000.00")
        elif position == "Accountant":
            self.salary_var.set("25000.00")
        elif position == "Sales Manager":
            self.salary_var.set("40000.00")
        elif position == "Production Staff":
            self.salary_var.set("22000.00")
        elif position == "Project Manager":
            self.salary_var.set("50000.00")

    def clear_fields(self):
        self.employee_number_var.set("")
        self.employee_name_var.set("")
        self.employment_status_var.set("Permanent")
        self.position_var.set("")
        self.salary_var.set("")
        self.text_area.delete(1.0, tk.END)

    def display_in_text_area(self, message):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, message)

    def search_employee(self):
        employee_number = self.employee_number_var.get()
        if not employee_number:
            messagebox.showerror("Error", "Please enter an Employee Number to search")
            return

        try:
            # Fixed query to use correct table name and column names
            self.cursor.execute("SELECT * FROM employee_tbl WHERE empNo = ?", (employee_number,))
            record = self.cursor.fetchone()

            if record:
                # Populate fields with the found record
                self.employee_number_var.set(record[0])  # empNo
                self.employee_name_var.set(record[1])  # empName
                self.employment_status_var.set(record[2])  # empStat
                self.position_var.set(record[3])  # empPos
                self.salary_var.set(record[4])  # empSal

                # Display the record in the text area
                display_text = f"Employee Number: {record[0]}\n"
                display_text += f"Employee Name: {record[1]}\n"
                display_text += f"Employment Status: {record[2]}\n"
                display_text += f"Position: {record[3]}\n"
                display_text += f"Salary: {record[4]}"

                self.display_in_text_area(display_text)
            else:
                # Display error message if no record found
                self.display_in_text_area("Error: No employee found with the given Employee Number")
                self.clear_fields()
                self.employee_number_var.set(employee_number)  # Keep the searched employee number
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def add_employee(self):
        # Get values from form
        employee_number = self.employee_number_var.get()
        employee_name = self.employee_name_var.get()
        employment_status = self.employment_status_var.get()
        position = self.position_var.get()

        # Update salary based on position before proceeding
        self.update_salary_based_on_position()
        salary = self.salary_var.get()

        # Validate inputs
        if not employee_number or not employee_name or not position:
            messagebox.showerror("Error", "Please fill all required fields")
            return

        try:
            # Check if employee number already exists
            self.cursor.execute("SELECT COUNT(*) FROM employee_tbl WHERE empNo = ?", (employee_number,))
            if self.cursor.fetchone()[0] > 0:
                messagebox.showerror("Error", "Employee Number already exists")
                return

            # Insert new employee with correct table and column names
            self.cursor.execute("""
                INSERT INTO employee_tbl (empNo, empName, empStat, empPos, empSal)
                VALUES (?, ?, ?, ?, ?)
            """, (employee_number, employee_name, employment_status, position, salary))

            self.conn.commit()
            messagebox.showinfo("Success", "Employee added successfully")

            # Update text area to show the added record
            display_text = f"Added Employee:\n"
            display_text += f"Employee Number: {employee_number}\n"
            display_text += f"Employee Name: {employee_name}\n"
            display_text += f"Employment Status: {employment_status}\n"
            display_text += f"Position: {position}\n"
            display_text += f"Salary: {salary}"

            self.display_in_text_area(display_text)
            self.clear_fields()

        except sqlite3.Error as e:
            self.conn.rollback()
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def update_employee(self):
        # Get values from form
        employee_number = self.employee_number_var.get()
        employee_name = self.employee_name_var.get()
        employment_status = self.employment_status_var.get()
        position = self.position_var.get()

        # Update salary based on position before proceeding
        self.update_salary_based_on_position()
        salary = self.salary_var.get()

        # Validate inputs
        if not employee_number:
            messagebox.showerror("Error", "Please enter Employee Number to update")
            return

        try:
            # Check if employee exists with correct table name
            self.cursor.execute("SELECT COUNT(*) FROM employee_tbl WHERE empNo = ?", (employee_number,))
            if self.cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "Employee Number does not exist")
                return

            # Update employee with correct table and column names
            self.cursor.execute("""
                UPDATE employee_tbl 
                SET empName = ?, empStat = ?, empPos = ?, empSal = ?
                WHERE empNo = ?
            """, (employee_name, employment_status, position, salary, employee_number))

            self.conn.commit()
            messagebox.showinfo("Success", "Employee updated successfully")

            # Update text area to show the updated record
            display_text = f"Updated Employee:\n"
            display_text += f"Employee Number: {employee_number}\n"
            display_text += f"Employee Name: {employee_name}\n"
            display_text += f"Employment Status: {employment_status}\n"
            display_text += f"Position: {position}\n"
            display_text += f"Salary: {salary}"

            self.display_in_text_area(display_text)

        except sqlite3.Error as e:
            self.conn.rollback()
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def delete_employee(self):
        employee_number = self.employee_number_var.get()

        if not employee_number:
            messagebox.showerror("Error", "Please enter Employee Number to delete")
            return

        try:
            # Check if employee exists with correct table name
            self.cursor.execute("SELECT COUNT(*) FROM employee_tbl WHERE empNo = ?", (employee_number,))
            if self.cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "Employee Number does not exist")
                return

            # Confirm deletion
            confirm = messagebox.askyesno("Confirm Delete",
                                          f"Are you sure you want to delete employee #{employee_number}?")
            if not confirm:
                return

            # Delete employee with correct table name
            self.cursor.execute("DELETE FROM employee_tbl WHERE empNo = ?", (employee_number,))
            self.conn.commit()

            messagebox.showinfo("Success", "Employee deleted successfully")
            self.display_in_text_area(f"Employee #{employee_number} has been deleted from the database.")
            self.clear_fields()

        except sqlite3.Error as e:
            self.conn.rollback()
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def view_all_records(self):
        try:
            # Use correct table name in query
            self.cursor.execute("SELECT * FROM employee_tbl ORDER BY empNo")
            records = self.cursor.fetchall()

            if records:
                display_text = "All Employee Records:\n\n"

                for record in records:
                    display_text += f"Employee Number: {record[0]}\n"
                    display_text += f"Employee Name: {record[1]}\n"
                    display_text += f"Employment Status: {record[2]}\n"
                    display_text += f"Position: {record[3]}\n"
                    display_text += f"Salary: {record[4]}\n"
                    display_text += "-" * 40 + "\n"

                self.display_in_text_area(display_text)
            else:
                self.display_in_text_area("No employee records found in the database.")

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def update_background_gif(self):
        """Update the background label with the next frame of the GIF."""
        if self.frames:
            self.background_label.config(image=self.frames[self.current_frame_index])
            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
            self.root.after(50, self.update_background_gif)  # Adjust the delay (50ms) as needed for your GIF

    def __del__(self):
        # Close database connection when object is destroyed
        if hasattr(self, 'conn'):
            self.conn.close()

# Main application
root = tk.Tk()
app = EmployeeManagementSystem(root)
root.mainloop()