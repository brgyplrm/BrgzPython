import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os


class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("650x500")

        self.root.resizable(True, True)

        self.conn = sqlite3.connect('employee.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS employee_tbl
                            (
                                empno INTEGER PRIMARY KEY, empname TEXT NOT NULL, position TEXT NOT NULL, 
                                empsal DECIMAL(10,2) NOT NULL
                            )
                            ''')
        self.conn.commit()

        self.employee_number_var = tk.StringVar()
        self.employee_name_var = tk.StringVar()
        self.employment_status_var = tk.StringVar(value="Permanent")
        self.position_var = tk.StringVar()
        self.salary_var = tk.StringVar()

        self.png_path = "your_png_file.png"
        try:
            self.png_image = Image.open(self.png_path)
            self.background_image = ImageTk.PhotoImage(self.png_image)
        except Exception as e:
            print(f"Error loading PNG: {e}. Using a default background.")
            self.background_image = None

        self.background_label = tk.Label(self.root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        if self.background_image:
            self.background_label.config(image=self.background_image)

        self.main_frame = tk.Frame(self.root, padx=10, pady=10, bg="#f0f0f0")
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.main_frame.grid_rowconfigure(10, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=1)

        self.main_frame.grid_rowconfigure(10, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=1)

        tk.Label(self.main_frame, text="Employee Number:", anchor="w", bg="#f0f0f0").grid(row=1, column=0, sticky=tk.W)
        employee_number_entry = tk.Entry(self.main_frame, textvariable=self.employee_number_var, width=20)
        employee_number_entry.grid(row=1, column=1, sticky=tk.W, padx=(0, 10))

        search_button = tk.Button(self.main_frame, text="SEARCH", command=self.search_employee, width=8)
        search_button.grid(row=1, column=2, sticky=tk.W)

        tk.Label(self.main_frame, text="Employee Name:", anchor="w", bg="#f0f0f0").grid(row=2, column=0, sticky=tk.W)
        employee_name_entry = tk.Entry(self.main_frame, textvariable=self.employee_name_var, width=20)
        employee_name_entry.grid(row=2, column=1, sticky=tk.W)

        tk.Label(self.main_frame, text="Employment Status:", anchor="w", bg="#f0f0f0").grid(row=3, column=0,
                                                                                            sticky=tk.W, padx=(5, 10))
        status_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        status_frame.grid(row=3, column=1, sticky=tk.W)

        status_options = [("Permanent", "Permanent"), ("Probationary", "Probationary"),
                          ("Casual", "Casual"), ("Contractual", "Contractual")]

        for i, (text, value) in enumerate(status_options):
            rb = tk.Radiobutton(status_frame, text=text, variable=self.employment_status_var, value=value,
                                bg="#f0f0f0")
            rb.grid(row=i, column=0, sticky=tk.W, pady=2)
            if i == 0:
                rb.config(padx=5)

        tk.Label(self.main_frame, text="Position:", anchor="w", bg="#f0f0f0").grid(row=7, column=0, sticky=tk.W)
        self.position_combo = ttk.Combobox(self.main_frame, textvariable=self.position_var,
                                           values=["Clerk", "Accountant", "Sales Manager", "Production Staff",
                                                   "Project Manager"], width=18)
        self.position_combo.grid(row=7, column=1, sticky=tk.W)

        tk.Label(self.main_frame, text="Salary:", anchor="w", bg="#f0f0f0").grid(row=8, column=0, sticky=tk.W)
        salary_entry = tk.Entry(self.main_frame, textvariable=self.salary_var, width=20, state='disabled')
        salary_entry.grid(row=8, column=1, sticky=tk.W)

        position_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        position_frame.grid(row=1, column=3, rowspan=5, padx=20, sticky=tk.N + tk.S)

        positions = [" ", " ", " ", " ", " "]
        salaries = [" ", " ", " ", " ", " "]

        button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        button_frame.grid(row=9, column=0, columnspan=3, pady=10, sticky=tk.W + tk.E)

        add_button = tk.Button(button_frame, text="ADD", width=10, command=self.add_employee)
        add_button.grid(row=0, column=0, padx=5, pady=5)

        update_button = tk.Button(button_frame, text="UPDATE", width=10, command=self.update_employee)
        update_button.grid(row=0, column=1, padx=5, pady=5)

        delete_button = tk.Button(button_frame, text="DELETE", width=10, command=self.delete_employee)
        delete_button.grid(row=0, column=2, padx=5, pady=5)

        view_button = tk.Button(button_frame, text="VIEW", width=10, command=self.view_all_records)
        view_button.grid(row=1, column=0, padx=5, pady=5)

        exit_button = tk.Button(button_frame, text="EXIT", width=10, command=root.destroy)
        exit_button.grid(row=1, column=2, padx=5, pady=5)

        text_area_frame = tk.LabelFrame(self.main_frame, text="DATABASE", padx=5, pady=5, bg="#f0f0f0")
        text_area_frame.grid(row=10, column=0, columnspan=4, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

        self.text_area = tk.Text(text_area_frame, width=60, height=8)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.position_combo.bind("<<ComboboxSelected>>", self.update_salary_based_on_position)

    def update_salary_based_on_position(self, event=None):
        position = self.position_var.get()
        if position == "Clerk":
            self.salary_var.set("20,000.00")
        elif position == "Accountant":
            self.salary_var.set("25,000.00")
        elif position == "Sales Manager":
            self.salary_var.set("40,000.00")
        elif position == "Production Staff":
            self.salary_var.set("22,000.00")
        elif position == "Project Manager":
            self.salary_var.set("50,000.00")

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

        self.cursor.execute("SELECT COUNT(*) FROM employee_tbl WHERE empNo = ?", (employee_number,))
        if self.cursor.fetchone()[0] == 0:
            messagebox.showerror("Error", "Employee Number does not exist in database")
            return

        try:
            self.cursor.execute("SELECT * FROM employee_tbl WHERE empNo = ?", (employee_number,))
            record = self.cursor.fetchone()

            if record:
                self.employee_number_var.set(record[0])
                self.employee_name_var.set(record[1])
                self.employment_status_var.set(record[2])
                self.position_var.set(record[3])
                self.salary_var.set(record[4])

                display_text = f"Employee Number: {record[0]}\n"
                display_text += f"Employee Name: {record[1]}\n"
                display_text += f"Employment Status: {record[2]}\n"
                display_text += f"Position: {record[3]}\n"
                display_text += f"Salary: {record[4]}"

                self.display_in_text_area(display_text)
            else:
                self.display_in_text_area("Error: No employee found with the given Employee Number")
                self.clear_fields()
                self.employee_number_var.set(employee_number)
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def add_employee(self):
        employee_number = self.employee_number_var.get()
        employee_name = self.employee_name_var.get()
        employment_status = self.employment_status_var.get()
        position = self.position_var.get()

        self.update_salary_based_on_position()
        salary = self.salary_var.get()

        if not employee_number or not employee_name or not position:
            messagebox.showerror("Error", "Please fill all required fields")
            return

        try:
            self.cursor.execute("SELECT COUNT(*) FROM employee_tbl WHERE empNo = ?", (employee_number,))
            if self.cursor.fetchone()[0] > 0:
                messagebox.showerror("Error", "Employee Number already exists")
                return

            self.cursor.execute("""
                                INSERT INTO employee_tbl (empNo, empName, empStat, empPos, empSal)
                                VALUES (?, ?, ?, ?, ?)
                                """, (employee_number, employee_name, employment_status, position, salary))

            self.conn.commit()
            messagebox.showinfo("Success", "Employee added successfully")

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
        employee_number = self.employee_number_var.get()
        employee_name = self.employee_name_var.get()
        employment_status = self.employment_status_var.get()
        position = self.position_var.get()

        self.update_salary_based_on_position()
        salary = self.salary_var.get()

        if not employee_number:
            messagebox.showerror("Error", "Please enter Employee Number to update")
            return

        try:
            self.cursor.execute("SELECT COUNT(*) FROM employee_tbl WHERE empNo = ?", (employee_number,))
            if self.cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "Employee Number does not exist")
                return

            self.cursor.execute("""
                                UPDATE employee_tbl
                                SET empName = ?,
                                    empStat = ?,
                                    empPos  = ?,
                                    empSal  = ?
                                WHERE empNo = ?
                                """, (employee_name, employment_status, position, salary, employee_number))

            self.conn.commit()
            messagebox.showinfo("Success", "Employee updated successfully")

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
            self.cursor.execute("SELECT COUNT(*) FROM employee_tbl WHERE empNo = ?", (employee_number,))
            if self.cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "Employee Number does not exist")
                return

            confirm = messagebox.askyesno("Confirm Delete",
                                          f"Are you sure you want to delete employee #{employee_number}?")
            if not confirm:
                return

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

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()


root = tk.Tk()
app = EmployeeManagementSystem(root)
root.mainloop()
