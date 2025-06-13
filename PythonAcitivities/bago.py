import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import datetime # Import datetime module for timestamps

# Initialize or connect to the database
def init_db():
    conn = sqlite3.connect("employee_db.sqlite")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employee (
                    empno TEXT PRIMARY KEY,
                    empname TEXT,
                    dept TEXT,
                    section TEXT)''')
    # Create a new table for deleted employee history
    c.execute('''CREATE TABLE IF NOT EXISTS deleted_employee_history (
                    empno TEXT,
                    empname TEXT,
                    dept TEXT,
                    section TEXT,
                    deleted_at TEXT)''') # To store the timestamp of deletion
    conn.commit()
    conn.close()

# Add employee to the database
def add_employee(empno, empname, dept, section):
    if not empno or not empname or not dept or not section:
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    try:
        conn = sqlite3.connect("employee_db.sqlite")
        c = conn.cursor()
        c.execute("INSERT INTO employee (empno, empname, dept, section) VALUES (?, ?, ?, ?)",
                  (empno, empname, dept, section))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Employee added successfully.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Employee Number already exists.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# View all employees
def view_employees(text_area):
    conn = sqlite3.connect("employee_db.sqlite")
    c = conn.cursor()
    c.execute("SELECT * FROM employee")
    records = c.fetchall()
    conn.close()
    text_area.delete(1.0, tk.END) # Clear existing text
    if records:
        text_area.insert(tk.END, "--- Current Employees ---\n")
        for row in records:
            text_area.insert(tk.END, f"EmpNo: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Section: {row[3]}\n")
    else:
        text_area.insert(tk.END, "No current employee records found.\n")

    # Also display deleted history
    view_deleted_history(text_area)

def edit_employee(empno, empname, dept, section):
    conn = sqlite3.connect("employee_db.sqlite")
    c = conn.cursor()
    # Check if the employee exists before attempting to update
    c.execute("SELECT empno FROM employee WHERE empno = ?", (empno,))
    if c.fetchone():
        c.execute("UPDATE employee SET empname = ?, dept = ?, section = ? WHERE empno = ?",
                  (empname, dept, section, empno))
        conn.commit()
        messagebox.showinfo("Success", "Employee updated successfully.")
    else:
        messagebox.showerror("Error", "Employee Number not found for editing.")
    conn.close()


def delete_employee(empno, text_area):
    conn = sqlite3.connect("employee_db.sqlite")
    c = conn.cursor()

    # First, retrieve the employee's data before deleting
    c.execute("SELECT * FROM employee WHERE empno = ?", (empno,))
    record_to_delete = c.fetchone()

    if record_to_delete:
        # Insert into deleted history table
        deleted_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO deleted_employee_history (empno, empname, dept, section, deleted_at) VALUES (?, ?, ?, ?, ?)",
                  (record_to_delete[0], record_to_delete[1], record_to_delete[2], record_to_delete[3], deleted_at))

        # Now, delete from the main employee table
        c.execute("DELETE FROM employee WHERE empno = ?", (empno,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Employee deleted successfully.")
        view_employees(text_area) # Refresh the view to show updated employee list and history
    else:
        messagebox.showerror("Error", "Employee not found for deletion.")
        conn.close()


# View deleted employee history
def view_deleted_history(text_area):
    conn = sqlite3.connect("employee_db.sqlite")
    c = conn.cursor()
    c.execute("SELECT * FROM deleted_employee_history")
    deleted_records = c.fetchall()
    conn.close()

    text_area.insert(tk.END, "\n--- Deleted Employee History ---\n")
    if deleted_records:
        for row in deleted_records:
            text_area.insert(tk.END, f"EmpNo: {row[1]}, Name: {row[2]}, Dept: {row[3]}, Section: {row[4]}\n")
    else:
        text_area.insert(tk.END, "No deleted records found.\n")

# Search for an employee
def search_employee(empno, text_area):
    conn = sqlite3.connect("employee_db.sqlite")
    c = conn.cursor()
    c.execute("SELECT * FROM employee WHERE empno = ?", (empno,))
    record = c.fetchone()
    conn.close()
    text_area.delete(1.0, tk.END)
    if record:
        text_area.insert(tk.END, f"EmpNo: {record[0]}, Name: {record[1]}, Dept: {record[2]}, Section: {record[3]}")
    else:
        messagebox.showerror("Not Found", "Employee not found in current records.")

def main():
    init_db()

    root = tk.Tk()
    root.title("Employee Information")

    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill="both", expand=True)

    emp_num_label = ttk.Label(main_frame, text="Employee Number:")
    emp_num_label.grid(row=0, column=0, sticky="w", pady=5)

    emp_num_entry = ttk.Entry(main_frame, width=20)
    emp_num_entry.grid(row=0, column=1, sticky="w", pady=5)
    emp_num_entry.focus()

    emp_name_label = ttk.Label(main_frame, text="Employee Name:")
    emp_name_label.grid(row=1, column=0, sticky="w", pady=5)

    emp_name_entry = ttk.Entry(main_frame, width=20)
    emp_name_entry.grid(row=1, column=1, sticky="w", pady=5)

    dept_label = ttk.Label(main_frame, text="Department:")
    dept_label.grid(row=2, column=0, sticky="w", pady=5)

    department_sections = {
        "Accounting": ["Payroll", "Fund Management"],
        "MIS": ["Computer Operation", "DB Management", "Network"],
        "Production": ["Operation", "Manufacturing"],
        "Sales": ["Marketing", "Advertisement"]
    }

    departments = list(department_sections.keys())

    def update_sections(event=None):
        sections_listbox.delete(0, tk.END)
        selected_dept = dept_combo.get()
        if selected_dept in department_sections:
            for section in department_sections[selected_dept]:
                sections_listbox.insert(tk.END, section)

    dept_combo = ttk.Combobox(main_frame, width=18, values=departments, state="readonly")
    dept_combo.grid(row=2, column=1, sticky="w", pady=5)
    dept_combo.bind("<<ComboboxSelected>>", update_sections)

    section_label = ttk.Label(main_frame, text="Sections:")
    section_label.grid(row=3, column=0, sticky="nw", pady=5)

    listbox_frame = ttk.Frame(main_frame)
    listbox_frame.grid(row=3, column=1, columnspan=2, sticky="w", pady=5)

    scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    sections_listbox = tk.Listbox(listbox_frame, width=30, height=6, yscrollcommand=scrollbar.set)
    sections_listbox.pack(side="left", fill="both")
    scrollbar.config(command=sections_listbox.yview)

    text_frame = ttk.Frame(main_frame)
    text_frame.grid(row=4, column=0, columnspan=3, sticky="w", pady=5)

    text_scrollbar = ttk.Scrollbar(text_frame)
    text_scrollbar.pack(side="right", fill="y")

    text_area = tk.Text(text_frame, height=8, width=36, wrap="word", yscrollcommand=text_scrollbar.set)
    text_area.pack(side="left", fill="both", expand=True)
    text_scrollbar.config(command=text_area.yview) # Corrected line

    buttons_frame1 = ttk.Frame(main_frame)
    buttons_frame1.grid(row=5, column=0, columnspan=3, pady=10)

    buttons_frame2 = ttk.Frame(main_frame)
    buttons_frame2.grid(row=6, column=0, columnspan=3, pady=10)

    def handle_add():
        empno = emp_num_entry.get().strip()
        empname = emp_name_entry.get().strip()
        dept = dept_combo.get()
        try:
            section = sections_listbox.get(sections_listbox.curselection())
        except tk.TclError: # Catch the error if no item is selected
            section = ""
        add_employee(empno, empname, dept, section)

        # Clear all input fields after adding
        emp_num_entry.delete(0, tk.END)
        emp_name_entry.delete(0, tk.END)
        dept_combo.set('')  # Clear department selection
        sections_listbox.delete(0, tk.END)  # Clear section listbox
        view_employees(text_area) # Refresh the view after adding

    def handle_view():
        view_employees(text_area)

        # Clear all input fields after viewing
        emp_num_entry.delete(0, tk.END)
        emp_name_entry.delete(0, tk.END)
        dept_combo.set('')  # Clear department selection
        sections_listbox.delete(0, tk.END)  # Clear section listbox

    def handle_search():
        empno = emp_num_entry.get().strip()
        if not empno:
            messagebox.showwarning("Input Error", "Enter an Employee Number to search.")
            return
        search_employee(empno, text_area)

        # Clear the employee number and employee name after searching
        emp_num_entry.delete(0, tk.END)  # Clear empno field after search
        emp_name_entry.delete(0, tk.END)  # Clear empname field after search

    def handle_edit():
        empno = emp_num_entry.get().strip()
        empname = emp_name_entry.get().strip()
        dept = dept_combo.get()
        try:
            section = sections_listbox.get(sections_listbox.curselection())
        except tk.TclError:
            section = ""

        if not empno:
            messagebox.showwarning("Input Error", "Enter an Employee Number to edit.")
            return
        edit_employee(empno, empname, dept, section)
        view_employees(text_area)

    def handle_delete():
        empno = emp_num_entry.get().strip()
        if not empno:
            messagebox.showwarning("Input Error", "Enter an Employee Number to delete.")
            return
        delete_employee(empno, text_area)
        emp_num_entry.delete(0, tk.END)

    add_button = ttk.Button(buttons_frame1, text="Add", width=10, command=handle_add)
    edit_button = ttk.Button(buttons_frame1, text="Edit", width=10, command=handle_edit)
    delete_button = ttk.Button(buttons_frame1, text="Delete", width=10, command=handle_delete)

    add_button.grid(row=0, column=0, padx=5)
    edit_button.grid(row=0, column=1, padx=5)
    delete_button.grid(row=0, column=2, padx=5)

    view_button = ttk.Button(buttons_frame2, text="View", width=10, command=handle_view)
    exit_button = ttk.Button(buttons_frame2, text="Exit", width=10, command=root.quit)
    search_button = ttk.Button(main_frame, text="Search", command=handle_search)

    search_button.grid(row=0, column=2, sticky="w", pady=5)
    view_button.grid(row=0, column=0, padx=5)
    exit_button.grid(row=0, column=1, padx=5)

    root.minsize(300, 400)
    root.mainloop()

if __name__ == "__main__":
    main()