import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import sys

class AboutDialog:
    def __init__(self, parent):
        self.about_window = tk.Toplevel(parent)
        self.about_window.title("About the System")
        self.about_window.geometry("400x200")
        self.about_window.resizable(False, False)
        self.about_window.transient(parent)
        self.about_window.grab_set()
        self.center_window()
        main_frame = tk.Frame(self.about_window, bd=1, relief=tk.SOLID)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        tk.Label(main_frame, text="About the System", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(main_frame, text="Voting System\n\nA system designed for managing and recording votes\nwith precinct-based organization and candidate selection.").pack(pady=10)
        tk.Button(main_frame, text="Close", command=self.close, bg="#4CAF50", fg="white", width=10, height=1, relief=tk.RAISED).pack(pady=20)

    def center_window(self):
        self.about_window.update_idletasks()
        width, height = self.about_window.winfo_width(), self.about_window.winfo_height()
        x = (self.about_window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.about_window.winfo_screenheight() // 2) - (height // 2)
        self.about_window.geometry(f'{width}x{height}+{x}+{y}')

    def close(self):
        self.about_window.destroy()

class AuthorDialog:
    def __init__(self, parent):
        self.about_window = tk.Toplevel(parent)
        self.about_window.title("Author of the System")
        self.about_window.geometry("400x200")
        self.about_window.resizable(False, False)
        self.about_window.transient(parent)
        self.about_window.grab_set()
        self.center_window()
        main_frame = tk.Frame(self.about_window, bd=1, relief=tk.SOLID)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        tk.Label(main_frame, text="About the System", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(main_frame, text="Authors\n\nBorgy Misael K. Palermo\nBernardo G. Sales III\nTyronne Jake S. Medina").pack(pady=3)
        tk.Button(main_frame, text="Close", command=self.close, bg="#4CAF50", fg="white", width=10, height=1, relief=tk.RAISED).pack(pady=20)

    def center_window(self):
        self.about_window.update_idletasks()
        width, height = self.about_window.winfo_width(), self.about_window.winfo_height()
        x = (self.about_window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.about_window.winfo_screenheight() // 2) - (height // 2)
        self.about_window.geometry(f'{width}x{height}+{x}+{y}')

    def close(self):
        self.about_window.destroy()

class VoterManagementWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Voter Management System")
        self.window.geometry("600x500")
        self.current_voter_id = None
        self.create_search_section()
        self.create_data_frame()
        self.center_window()

    def center_window(self):
        self.window.update_idletasks()
        width, height = self.window.winfo_width(), self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def create_search_section(self):
        search_section = tk.Frame(self.window)
        search_section.pack(fill=tk.BOTH, padx=20, pady=20)
        tk.Label(search_section, text="Search", font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(search_section, text="• Input Voter's ID Number and search in the DB").pack(anchor="w", padx=20)
        search_field_frame = tk.Frame(search_section)
        search_field_frame.pack(fill=tk.X, pady=10)
        tk.Label(search_field_frame, text="Voter's ID Number:").pack(side=tk.LEFT, padx=10)
        self.search_entry = tk.Entry(search_field_frame, width=20)
        self.search_entry.pack(side=tk.LEFT, padx=10)
        tk.Button(search_field_frame, text="Search", bg="purple", fg="white", padx=20, command=self.search_voter).pack(side=tk.LEFT, padx=10)

    def create_data_frame(self):
        self.data_frame = tk.Frame(self.window, bd=1, relief=tk.SOLID)
        tk.Label(self.data_frame, text="Voter's Data", font=("Arial", 11)).pack(fill=tk.X, pady=5)
        tk.Frame(self.data_frame, height=1, bg="black").pack(fill=tk.X)
        info_frame = tk.Frame(self.data_frame)
        info_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        self.name_label = tk.Label(info_frame, text="Welcome")
        self.name_label.pack(pady=5)
        self.precinct_label = tk.Label(info_frame, text="Your voting precinct is at _______________.")
        self.precinct_label.pack(pady=5)
        button_frame = tk.Frame(self.data_frame)
        button_frame.pack(fill=tk.X, pady=10)
        tk.Button(button_frame, text="Edit", bg="#00AAFF", fg="white", padx=30, pady=5, command=self.edit_voter).pack(side=tk.LEFT, padx=(100, 20))
        tk.Button(button_frame, text="Delete", bg="#00AAFF", fg="white", padx=30, pady=5, command=self.delete_voter).pack(side=tk.LEFT)

    def search_voter(self):
        voter_id = self.search_entry.get().strip()
        if not voter_id:
            messagebox.showerror("Error", "Please enter a Voter ID")
            return
        conn = sqlite3.connect('Votes.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Votes WHERE voteID = ?', (voter_id,))
        result = cursor.fetchone()
        conn.close()
        if not result:
            messagebox.showerror("Not Found", "Voter does not exist!")
            self.clear_data_frame()
        else:
            self.display_voter_data(result)

    def display_voter_data(self, voter_data):
        self.clear_data_frame()
        self.data_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.name_label.config(text=f"Welcome {voter_data[1]}")
        self.precinct_label.config(text=f"Your voting precinct is at {voter_data[2]}.")
        self.current_voter_id = voter_data[0]

    def clear_data_frame(self):
        self.data_frame.pack_forget()
        self.name_label.config(text="Welcome")
        self.precinct_label.config(text="Your voting precinct is at _______________.")

    def delete_voter(self):
        if not self.current_voter_id:
            messagebox.showerror("Error", "No voter selected")
            return
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to remove voter {self.current_voter_id}?")
        if confirm:
            try:
                conn = sqlite3.connect('Votes.db')
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Votes WHERE voteID = ?', (self.current_voter_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Voter information deleted successfully")
                self.clear_data_frame()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def edit_voter(self):
        if not self.current_voter_id:
            messagebox.showerror("Error", "No voter selected")
            return
        try:
            conn = sqlite3.connect('Votes.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Votes WHERE voteID = ?', (self.current_voter_id,))
            voter_data = cursor.fetchone()
            conn.close()
            if not voter_data:
                messagebox.showerror("Error", "Voter not found")
                return
            self.create_edit_window(voter_data)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def create_edit_window(self, voter_data):
        edit_window = tk.Toplevel(self.window)
        edit_window.title("Edit Voter Record")
        edit_window.geometry("400x250")
        tk.Label(edit_window, text="Voter ID:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        id_entry = tk.Entry(edit_window, width=30)
        id_entry.insert(0, voter_data[0])
        id_entry.config(state='readonly')
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(edit_window, text="Name:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        name_entry = tk.Entry(edit_window, width=30)
        name_entry.insert(0, voter_data[1])
        name_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(edit_window, text="Precinct:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        precinct_entry = tk.Entry(edit_window, width=30)
        precinct_entry.insert(0, voter_data[2])
        precinct_entry.grid(row=2, column=1, padx=10, pady=10)

        def save_changes():
            updated_name = name_entry.get().strip()
            updated_precinct = precinct_entry.get().strip()
            if not updated_name or not updated_precinct:
                messagebox.showerror("Error", "All fields are required")
                return
            try:
                conn = sqlite3.connect('Votes.db')
                cursor = conn.cursor()
                cursor.execute('UPDATE Votes SET voteName = ?, precNo = ? WHERE voteID = ?', (updated_name, updated_precinct, self.current_voter_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Voter information updated successfully")
                edit_window.destroy()
                self.search_voter()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        tk.Button(edit_window, text="Save", bg="#00AAFF", fg="white", padx=20, pady=5, command=save_changes).grid(row=3, column=0, padx=10, pady=20)
        tk.Button(edit_window, text="Cancel", bg="light gray", fg="black", padx=20, pady=5, command=edit_window.destroy).grid(row=3, column=1, padx=10, pady=20)

class LoginSystem:
    def __init__(self, root, valid_credentials, max_attempts=3):
        self.root = root
        self.valid_credentials = valid_credentials
        self.max_attempts = max_attempts
        self.current_attempts = 0
        window_width, window_height = 300, 170
        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
        center_x, center_y = int(screen_width / 2 - window_width / 2), int(screen_height / 2 - window_height / 2)
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        tk.Label(self.frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = ttk.Entry(self.frame, width=30)
        self.username_entry.grid(row=0, column=1, pady=5)
        tk.Label(self.frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(self.frame, width=30, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)
        self.attempts_label = ttk.Label(self.frame, text=f"Remaining attempts: {self.max_attempts}")
        self.attempts_label.grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(self.frame, text="Login", command=self.attempt_login).grid(row=3, column=0, pady=10)
        tk.Button(self.frame, text="Cancel", command=root.quit).grid(row=3, column=1, pady=10)
        root.bind('<Return>', lambda event: self.attempt_login())
        self.username_entry.focus_set()

    def attempt_login(self):
        username, password = self.username_entry.get(), self.password_entry.get()
        if username in self.valid_credentials and self.valid_credentials[username] == password:
            messagebox.showinfo("Success", "Login successful!")
            self.root.withdraw()
            MainWindow()
        else:
            self.current_attempts += 1
            remaining = self.max_attempts - self.current_attempts
            if remaining > 0:
                messagebox.showerror("Login Failed", f"Invalid username or password.\n\nRemaining attempts: {remaining}")
                self.attempts_label.config(text=f"Remaining attempts: {remaining}")
                self.password_entry.delete(0, tk.END)
                self.password_entry.focus_set()
            else:
                messagebox.showerror("Access Denied", "Maximum login attempts exceeded.\nThe application will exit.")
                self.root.quit()
                sys.exit()

def create_database():
    conn = sqlite3.connect('Votes.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Votes (voteID TEXT PRIMARY KEY, voteName TEXT, precNo INTEGER, selCandid TEXT, totVotesPrec INTEGER, grandTotVotes INTEGER)''')
    conn.commit()
    conn.close()

def save_to_database(voter_id, voter_name, precinct, selected_candidates):
    if len(selected_candidates) > 8:
        messagebox.showerror("Error", "Maximum of 8 candidates can be selected!")
        return False
    try:
        conn = sqlite3.connect('Votes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Votes WHERE precNo=?", (precinct,))
        prec_votes = cursor.fetchone()[0] + 1
        cursor.execute("SELECT COUNT(*) FROM Votes")
        total_votes = cursor.fetchone()[0] + 1
        cursor.execute('''INSERT INTO Votes (voteID, voteName, precNo, selCandid, totVotesPrec, grandTotVotes) VALUES (?, ?, ?, ?, ?, ?)''', (voter_id, voter_name, precinct, ','.join(selected_candidates), prec_votes, total_votes))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Voter ID already exists!")
        return False
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return False

def create_voter_record_form():
    form_window = tk.Toplevel()
    form_window.title("Voter Record Form")
    form_window.geometry("600x550")
    form_window.resizable(False, False)
    main_frame = tk.Frame(form_window, bd=2, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    header_frame = tk.Frame(main_frame, bg='#f0f0f0', height=30)
    header_frame.pack(fill=tk.X)
    tk.Label(header_frame, text="New Record Form", font=("Arial", 12), bg='#f0f0f0').pack(side=tk.LEFT, padx=5, pady=5)
    form_frame = tk.Frame(main_frame)
    form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    tk.Label(form_frame, text="Voter's ID Number:", anchor='w').grid(row=0, column=0, sticky='w', pady=5)
    id_entry = tk.Entry(form_frame, width=30)
    id_entry.grid(row=0, column=1, sticky='w', pady=5)
    tk.Label(form_frame, text="Voter's Name:", anchor='w').grid(row=1, column=0, sticky='w', pady=5)
    name_entry = tk.Entry(form_frame, width=60)
    name_entry.grid(row=1, column=1, sticky='w', pady=5)
    tk.Label(form_frame, text="Precinct Number:", anchor='w').grid(row=2, column=0, sticky='w', pady=5)
    precinct_frame = tk.Frame(form_frame)
    precinct_frame.grid(row=2, column=1, sticky='w', pady=5)
    precinct_values = ["245", "367", "641", "179"]
    precinct_var = tk.StringVar()
    precinct_dropdown = ttk.Combobox(precinct_frame, textvariable=precinct_var, values=precinct_values, width=27, state='readonly')
    precinct_dropdown.set("Select Precinct")
    precinct_dropdown.pack(side=tk.LEFT)
    tk.Label(form_frame, text="Candidates:", anchor='w').grid(row=3, column=0, sticky='nw', pady=5)
    candidates_frame = tk.Frame(form_frame)
    candidates_frame.grid(row=3, column=1, sticky='w', pady=5)
    candidates = ["Superman", "Wolverine", "Iron Man", "Batman", "Cyclops", "Spiderman", "Aquaman", "Phoenix", "Capt. America", "Flash", "Iceman", "Scarlet Witch"]
    candidate_vars = {}
    for i, candidate in enumerate(candidates):
        row_num, col_num = i // 3, i % 3
        var = tk.BooleanVar(value=False)
        candidate_vars[candidate] = var
        tk.Checkbutton(candidates_frame, text=candidate, variable=var, highlightthickness=0).grid(row=row_num, column=col_num, sticky='w', padx=(0, 15), pady=2)

    button_frame = tk.Frame(form_frame)
    button_frame.grid(row=4, column=0, columnspan=2, pady=30)

    def review_votes():
        selected_candidates = [c for c, v in candidate_vars.items() if v.get()]
        if len(selected_candidates) > 8:
            messagebox.showwarning("Warning", "You can only select up to 8 candidates!")
            return
        if not id_entry.get():
            messagebox.showwarning("Missing Information", "Please enter Voter's ID Number")
            return
        if not name_entry.get():
            messagebox.showwarning("Missing Information", "Please enter Voter's Name")
            return
        if precinct_var.get() == "Select Precinct":
            messagebox.showwarning("Missing Information", "Please select a Precinct Number")
            return
        if not selected_candidates:
            messagebox.showwarning("No Selection", "Please select at least one candidate")
            return
        confirm_window = tk.Toplevel()
        confirm_window.title("Vote Confirmation")
        confirm_window.geometry("400x300")
        confirm_window.configure(bg="white")
        info_frame = tk.Frame(confirm_window, bg="white")
        info_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(info_frame, text=f"Voter ID: {id_entry.get()}\nVoter Name: {name_entry.get()}\nPrecinct: {precinct_var.get()}", justify=tk.LEFT, bg="white", font=("Arial", 10)).pack(anchor=tk.W)
        tk.Frame(confirm_window, height=2, bg="gray").pack(fill=tk.X, padx=10, pady=5)
        candidates_frame = tk.Frame(confirm_window, bg="white")
        candidates_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        tk.Label(candidates_frame, text="Selected Candidates:", font=("Arial", 12, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 10))
        for candidate in selected_candidates:
            tk.Label(candidates_frame, text=f"• {candidate}", bg="white", font=("Arial", 10)).pack(anchor=tk.W, pady=2)

        def confirm_and_save():
            if save_to_database(id_entry.get(), name_entry.get(), int(precinct_var.get()), selected_candidates):
                messagebox.showinfo("Success", "Your vote has been recorded!")
                confirm_window.destroy()
                clear_form()

        button_frame = tk.Frame(confirm_window, bg="white")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text="Cast My Votes", bg="#ff0000", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED, borderwidth=0, padx=20, pady=8, command=confirm_and_save).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", bg="#ff0000", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED, borderwidth=0, padx=20, pady=8, command=confirm_window.destroy).pack(side=tk.LEFT, padx=5)

    def clear_choices():
        for var in candidate_vars.values():
            var.set(False)
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        precinct_dropdown.set("Select Precinct")
        messagebox.showinfo("Cleared", "All choices have been cleared")

    def cancel():
        if messagebox.askyesno("Cancel", "Are you sure you want to cancel?"):
            clear_choices()

    def close():
        if messagebox.askyesno("Close", "Are you sure you want to close the form?"):
            form_window.destroy()

    def clear_form():
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        precinct_var.set("Select Precinct")
        for var in candidate_vars.values():
            var.set(False)

    tk.Button(button_frame, text="Review My\nVotes", bg="#4CAF50", fg="white", width=15, height=2, command=review_votes).grid(row=0, column=0, padx=20)
    tk.Button(button_frame, text="Clear My\nChoices", bg="#4CAF50", fg="white", width=15, height=2, command=clear_choices).grid(row=0, column=1, padx=20)
    tk.Button(button_frame, text="Cancel", bg="#4CAF50", fg="white", width=15, height=2, command=cancel).grid(row=1, column=0, padx=20, pady=20)
    tk.Button(button_frame, text="Close", bg="#4CAF50", fg="white", width=15, height=2, command=close).grid(row=1, column=1, padx=20, pady=20)

    return form_window

class VoterSearchWindow:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Voter Search")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        tk.Label(self.root, text="Voter Search", font=("Arial", 12, "bold")).pack(fill=tk.X, pady=(10, 5))
        tk.Frame(self.root, height=2, bg="black").pack(fill=tk.X, padx=10)
        search_frame = tk.Frame(self.root)
        search_frame.pack(fill=tk.X, padx=20, pady=20)
        tk.Label(search_frame, text="Voter's ID Number:").grid(row=0, column=0, sticky="w", pady=10)
        self.id_entry = tk.Entry(search_frame, width=30)
        self.id_entry.grid(row=0, column=1, padx=10)
        tk.Button(search_frame, text="Search", bg="purple", fg="white", padx=20, pady=5, command=self.search_voter).grid(row=0, column=2, padx=10)
        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.result_frame.pack_forget()
        self.result_text = tk.Text(self.result_frame, height=10, width=50)
        self.result_text.pack(fill=tk.BOTH, expand=True)
        self.result_text.config(state=tk.DISABLED)
        tk.Button(self.root, text="Close", bg="red", fg="white", padx=40, pady=5, command=self.root.destroy).pack(pady=20)
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        width, height = self.root.winfo_width(), self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def search_voter(self):
        voter_id = self.id_entry.get().strip()
        if not voter_id:
            messagebox.showerror("Error", "Please enter a Voter ID")
            return
        conn = sqlite3.connect('Votes.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Votes WHERE voteID = ?', (voter_id,))
        result = cursor.fetchone()
        conn.close()
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete('1.0', tk.END)
        if result:
            self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            voter_info = f"Voter ID: {result[0]}\nName: {result[1]}\nPrecinct: {result[2]}\n"
            if result[3]:
                voter_info += f"\nSelected Candidates:\n"
                candidates = result[3].split(',')
                for i, candidate in enumerate(candidates, 1):
                    voter_info += f"{i}. {candidate}\n"
            voter_info += f"\nPrecinct Vote Count: {result[4]}\nTotal Votes: {result[5]}"
            self.result_text.insert('1.0', voter_info)
        else:
            self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            self.result_text.insert('1.0', "No voter found with this ID.")
        self.result_text.config(state=tk.DISABLED)

def MainWindow():
    mainwindow = tk.Toplevel()
    mainwindow.title("Main Form")
    mainwindow.geometry("400x300")
    voter_form = None

    def open_new_form():
        nonlocal voter_form
        if voter_form is None or not tk.Toplevel.winfo_exists(voter_form):
            voter_form = create_voter_record_form()
        else:
            voter_form.lift()

    def open_search_window():
        VoterSearchWindow()

    def open_management_window():
        VoterManagementWindow()

    menubar = tk.Menu(mainwindow)
    mainwindow.config(menu=menubar)
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=open_new_form)
    file_menu.add_command(label="View", command=open_search_window)
    file_menu.add_separator()
    file_menu.add_command(label="Logout", command=lambda: logout(mainwindow))
    edit_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Search", command=lambda: VoterManagementWindow())
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=lambda: AboutDialog(mainwindow))
    help_menu.add_command(label="Authors", command=lambda: AuthorDialog(mainwindow))

    main_frame = ttk.Frame(mainwindow, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    tk.Label(main_frame, text="Select Precinct:", font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky='w')
    precincts = ["245", "367", "641", "179", "All"]
    precinct_combo = ttk.Combobox(main_frame, values=precincts, state="readonly", width=30)
    precinct_combo.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    precinct_combo.set("Select Precinct")
    result_frame = ttk.LabelFrame(main_frame, padding="10")
    result_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
    result_text = tk.Text(result_frame, width=40, height=5, wrap=tk.WORD, font=('Arial', 11), relief="solid", borderwidth=1)
    result_text.grid(row=0, column=0, pady=(0, 10), sticky='nsew')
    result_text.config(state='disabled')

    def clear_text():
        result_text.config(state='normal')
        result_text.delete('1.0', tk.END)
        result_text.config(state='disabled')
        precinct_combo.set("Select Precinct")

    tk.Button(result_frame, text="Clear", command=clear_text).grid(row=1, column=0, pady=(0, 5))

    def on_precinct_selected(event):
        selected_precinct = precinct_combo.get()
        result_text.config(state='normal')
        result_text.delete('1.0', tk.END)
        result_text.insert('1.0', f"Selected Precinct: {selected_precinct}")
        result_text.config(state='disabled')

    precinct_combo.bind('<<ComboboxSelected>>', on_precinct_selected)
    window_width, window_height = 400, 300
    screen_width, screen_height = mainwindow.winfo_screenwidth(), mainwindow.winfo_screenheight()
    center_x, center_y = int(screen_width/2 - window_width/2), int(screen_height/2 - window_height/2)
    mainwindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def logout(mainwindow):
    mainwindow.destroy()
    vote.deiconify()

valid_credentials = {"admin": "password123"}
vote = tk.Tk()
vote.title("Login")
create_database()
login_system = LoginSystem(vote, valid_credentials)
vote.mainloop()
