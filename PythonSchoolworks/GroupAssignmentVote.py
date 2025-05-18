import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkfont
import sqlite3
import sys
from datetime import datetime


class AboutDialog:
    def __init__(self, parent):
        # Create a top-level window
        self.about_window = tk.Toplevel(parent)
        self.about_window.title("About the System")
        self.about_window.geometry("400x200")
        self.about_window.resizable(False, False)
        self.about_window.transient(parent)  # Set as transient to parent window
        self.about_window.grab_set()  # Modal behavior

        # Center the window on screen
        self.center_window()

        # Create a frame to hold content
        main_frame = tk.Frame(self.about_window, bd=1, relief=tk.SOLID)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Add title
        title_label = tk.Label(main_frame, text="About the System", font=("Arial", 12, "bold"))
        title_label.pack(pady=10)

        # Add description text
        description = tk.Label(main_frame,
                               text="Voting System\n\nA system designed for managing and recording votes\nwith precinct-based organization and candidate selection.")
        description.pack(pady=10)

        # Add close button
        close_button = tk.Button(
            main_frame,
            text="Close",
            command=self.close,
            bg="#4CAF50",  # Green color
            fg="white",
            width=10,
            height=1,
            relief=tk.RAISED
        )
        close_button.pack(pady=20)

    def center_window(self):
        self.about_window.update_idletasks()
        width = self.about_window.winfo_width()
        height = self.about_window.winfo_height()
        x = (self.about_window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.about_window.winfo_screenheight() // 2) - (height // 2)
        self.about_window.geometry(f'{width}x{height}+{x}+{y}')

    def close(self):
        self.about_window.destroy()

class AuthorDialog:
    def __init__(self, parent):
        # Create a top-level window
        self.about_window = tk.Toplevel(parent)
        self.about_window.title("Author of the System")
        self.about_window.geometry("400x200")
        self.about_window.resizable(False, False)
        self.about_window.transient(parent)  # Set as transient to parent window
        self.about_window.grab_set()  # Modal behavior

        # Center the window on screen
        self.center_window()

        # Create a frame to hold content
        main_frame = tk.Frame(self.about_window, bd=1, relief=tk.SOLID)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Add title
        title_label = tk.Label(main_frame, text="About the System", font=("Arial", 12, "bold"))
        title_label.pack(pady=10)

        # Add description text
        description = tk.Label(main_frame,
                               text="Authors\n\nBorgy Misael K. Palermo\nBernardo G. Sales III\nTyronne Jake S. Medina")
        description.pack(pady=3)

        # Add close button
        close_button = tk.Button(
            main_frame,
            text="Close",
            command=self.close,
            bg="#4CAF50",  # Green color
            fg="white",
            width=10,
            height=1,
            relief=tk.RAISED
        )
        close_button.pack(pady=20)

    def center_window(self):
        self.about_window.update_idletasks()
        width = self.about_window.winfo_width()
        height = self.about_window.winfo_height()
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

        # Global variable to track current voter
        self.current_voter_id = None

        # Create search section
        self.create_search_section()

        # Create data frame
        self.create_data_frame()

        # Center the window
        self.center_window()

    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def create_search_section(self):
        search_section = tk.Frame(self.window)
        search_section.pack(fill=tk.BOTH, padx=20, pady=20)

        # Search title
        search_title = tk.Label(search_section, text="Search", font=("Arial", 12, "bold"))
        search_title.pack(anchor="w")

        # Search instruction
        search_instruction = tk.Label(search_section,
                                    text="• Input Voter's ID Number and search in the DB")
        search_instruction.pack(anchor="w", padx=20)

        # Search field frame
        search_field_frame = tk.Frame(search_section)
        search_field_frame.pack(fill=tk.X, pady=10)

        # ID label and entry
        id_label = tk.Label(search_field_frame, text="Voter's ID Number:")
        id_label.pack(side=tk.LEFT, padx=10)

        self.search_entry = tk.Entry(search_field_frame, width=20)
        self.search_entry.pack(side=tk.LEFT, padx=10)

        # Search button
        search_button = tk.Button(
            search_field_frame,
            text="Search",
            bg="purple",
            fg="white",
            padx=20,
            command=self.search_voter
        )
        search_button.pack(side=tk.LEFT, padx=10)

    def create_data_frame(self):
        self.data_frame = tk.Frame(self.window, bd=1, relief=tk.SOLID)

        # Data header
        header_label = tk.Label(self.data_frame, text="Voter's Data", font=("Arial", 11))
        header_label.pack(fill=tk.X, pady=5)

        separator = tk.Frame(self.data_frame, height=1, bg="black")
        separator.pack(fill=tk.X)

        # Voter info
        info_frame = tk.Frame(self.data_frame)
        info_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.name_label = tk.Label(info_frame, text="Welcome")
        self.name_label.pack(pady=5)

        self.precinct_label = tk.Label(info_frame, text="Your voting precinct is at _______________.")
        self.precinct_label.pack(pady=5)

        # Action buttons
        button_frame = tk.Frame(self.data_frame)
        button_frame.pack(fill=tk.X, pady=10)

        edit_button = tk.Button(
            button_frame,
            text="Edit",
            bg="#00AAFF",
            fg="white",
            padx=30,
            pady=5,
            command=self.edit_voter
        )
        edit_button.pack(side=tk.LEFT, padx=(100, 20))

        delete_button = tk.Button(
            button_frame,
            text="Delete",
            bg="#00AAFF",
            fg="white",
            padx=30,
            pady=5,
            command=self.delete_voter
        )
        delete_button.pack(side=tk.LEFT)
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

        confirm = messagebox.askyesno("Confirm Delete",
                                     f"Are you sure you want to remove voter {self.current_voter_id}?")

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

        # Form fields
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
                cursor.execute('''
                UPDATE Votes SET voteName = ?, precNo = ? WHERE voteID = ?
                ''', (updated_name, updated_precinct, self.current_voter_id))
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Voter information updated successfully")
                edit_window.destroy()
                self.search_voter()  # Refresh the display
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Buttons
        save_button = tk.Button(
            edit_window,
            text="Save",
            bg="#00AAFF",
            fg="white",
            padx=20,
            pady=5,
            command=save_changes
        )
        save_button.grid(row=3, column=0, padx=10, pady=20)

        cancel_button = tk.Button(
            edit_window,
            text="Cancel",
            bg="light gray",
            fg="black",
            padx=20,
            pady=5,
            command=edit_window.destroy
        )
        cancel_button.grid(row=3, column=1, padx=10, pady=20)


class LoginSystem:
    def __init__(self, root, valid_credentials, max_attempts=3):
        self.root = root
        self.valid_credentials = valid_credentials  # Dictionary of valid username/password pairs
        self.max_attempts = max_attempts
        self.current_attempts = 0

        # Center the login window
        window_width = 300
        window_height = 170
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # Create the login frame
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Username row
        self.entry_label = ttk.Label(self.frame, text="Username:")
        self.entry_label.grid(row=0, column=0, padx=5, pady=5)

        self.username_entry = ttk.Entry(self.frame, width=30)
        self.username_entry.grid(row=0, column=1, pady=5)

        # Password row
        self.password_label = ttk.Label(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)

        self.password_entry = ttk.Entry(self.frame, width=30, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)

        # Attempts counter label
        self.attempts_label = ttk.Label(self.frame, text=f"Remaining attempts: {self.max_attempts}")
        self.attempts_label.grid(row=2, column=0, columnspan=2, pady=5)

        # Login button
        self.login_button = ttk.Button(self.frame, text="Login", command=self.attempt_login)
        self.login_button.grid(row=3, column=0, pady=10)

        # Cancel button
        self.cancel_button = ttk.Button(self.frame, text="Cancel", command=root.quit)
        self.cancel_button.grid(row=3, column=1, pady=10)

        # Bind Enter key to login
        root.bind('<Return>', lambda event: self.attempt_login())

        # Set focus to username entry
        self.username_entry.focus_set()

    def attempt_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if credentials are valid
        if username in self.valid_credentials and self.valid_credentials[username] == password:
            messagebox.showinfo("Success", "Login successful!")
            self.root.withdraw()  # Hide login window
            MainWindow()  # Open main window
        else:
            self.current_attempts += 1
            remaining = self.max_attempts - self.current_attempts

            if remaining > 0:
                messagebox.showerror("Login Failed",
                                     f"Invalid username or password.\n\nRemaining attempts: {remaining}")
                self.attempts_label.config(text=f"Remaining attempts: {remaining}")
                self.password_entry.delete(0, tk.END)  # Clear password field
                self.password_entry.focus_set()  # Set focus back to password field
            else:
                messagebox.showerror("Access Denied",
                                     "Maximum login attempts exceeded.\nThe application will exit.")
                self.root.quit()
                sys.exit()


def create_database():
    conn = sqlite3.connect('Votes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Votes (
            voteID TEXT PRIMARY KEY,
            voteName TEXT,
            precNo INTEGER,
            selCandid TEXT,
            totVotesPrec INTEGER,
            grandTotVotes INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_to_database(voter_id, voter_name, precinct, selected_candidates):
    if len(selected_candidates) > 8:
        messagebox.showerror("Error", "Maximum of 8 candidates can be selected!")
        return False

    try:
        conn = sqlite3.connect('Votes.db')
        cursor = conn.cursor()

        # Get current vote counts
        cursor.execute("SELECT COUNT(*) FROM Votes WHERE precNo=?", (precinct,))
        prec_votes = cursor.fetchone()[0] + 1  # Add 1 for current vote

        cursor.execute("SELECT COUNT(*) FROM Votes")
        total_votes = cursor.fetchone()[0] + 1  # Add 1 for current vote

        # Save the vote
        cursor.execute('''
            INSERT INTO Votes (voteID, voteName, precNo, selCandid, totVotesPrec, grandTotVotes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            voter_id,
            voter_name,
            precinct,
            ','.join(selected_candidates),
            prec_votes,
            total_votes
        ))

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

    # Create main frame
    main_frame = tk.Frame(form_window, bd=2, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Create title header
    header_frame = tk.Frame(main_frame, bg='#f0f0f0', height=30)
    header_frame.pack(fill=tk.X)

    header_label = tk.Label(header_frame, text="New Record Form", font=("Arial", 12), bg='#f0f0f0')
    header_label.pack(side=tk.LEFT, padx=5, pady=5)

    # Create form content
    form_frame = tk.Frame(main_frame)
    form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # ID Number
    id_label = tk.Label(form_frame, text="Voter's ID Number:", anchor='w')
    id_label.grid(row=0, column=0, sticky='w', pady=5)

    id_entry = tk.Entry(form_frame, width=30)
    id_entry.grid(row=0, column=1, sticky='w', pady=5)

    # Voter's Name
    name_label = tk.Label(form_frame, text="Voter's Name:", anchor='w')
    name_label.grid(row=1, column=0, sticky='w', pady=5)

    name_entry = tk.Entry(form_frame, width=60)
    name_entry.grid(row=1, column=1, sticky='w', pady=5)

    # Precinct Number
    precinct_label = tk.Label(form_frame, text="Precinct Number:", anchor='w')
    precinct_label.grid(row=2, column=0, sticky='w', pady=5)

    precinct_frame = tk.Frame(form_frame)
    precinct_frame.grid(row=2, column=1, sticky='w', pady=5)

    precinct_values = ["245", "367", "641", "179"]
    precinct_var = tk.StringVar()
    precinct_dropdown = ttk.Combobox(precinct_frame,
                                   textvariable=precinct_var,
                                   values=precinct_values,
                                   width=27,
                                   state='readonly')
    precinct_dropdown.set("Select Precinct")
    precinct_dropdown.pack(side=tk.LEFT)

    # Candidates Label
    candidates_label = tk.Label(form_frame, text="Candidates:", anchor='w')
    candidates_label.grid(row=3, column=0, sticky='nw', pady=5)

    # Candidates Checkboxes (3 columns)
    candidates_frame = tk.Frame(form_frame)
    candidates_frame.grid(row=3, column=1, sticky='w', pady=5)

    candidates = [
        "Superman", "Wolverine", "Iron Man",
        "Batman", "Cyclops", "Spiderman",
        "Aquaman", "Phoenix", "Capt. America",
        "Flash", "Iceman", "Scarlet Witch"
    ]

    candidate_vars = {}
    for i, candidate in enumerate(candidates):
        row_num = i // 3
        col_num = i % 3

        var = tk.BooleanVar(value=False)
        candidate_vars[candidate] = var

        cb = tk.Checkbutton(
            candidates_frame,
            text=candidate,
            variable=var,
            highlightthickness=0
        )
        cb.grid(row=row_num, column=col_num, sticky='w', padx=(0, 15), pady=2)

    # Buttons
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

        # Create confirmation window
        confirm_window = tk.Toplevel()
        confirm_window.title("Vote Confirmation")
        confirm_window.geometry("400x300")
        confirm_window.configure(bg="white")

        # Add voter information
        info_frame = tk.Frame(confirm_window, bg="white")
        info_frame.pack(fill=tk.X, padx=10, pady=5)

        voter_info = tk.Label(
            info_frame,
            text=f"Voter ID: {id_entry.get()}\nVoter Name: {name_entry.get()}\nPrecinct: {precinct_var.get()}",
            justify=tk.LEFT,
            bg="white",
            font=("Arial", 10)
        )
        voter_info.pack(anchor=tk.W)

        # Add a separator
        separator = tk.Frame(confirm_window, height=2, bg="gray")
        separator.pack(fill=tk.X, padx=10, pady=5)

        # Create a frame for selected candidates
        candidates_frame = tk.Frame(confirm_window, bg="white")
        candidates_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Add header for selected candidates
        tk.Label(
            candidates_frame,
            text="Selected Candidates:",
            font=("Arial", 12, "bold"),
            bg="white"
        ).pack(anchor=tk.W, pady=(0, 10))

        # Display selected candidates
        for candidate in selected_candidates:
            tk.Label(
                candidates_frame,
                text=f"• {candidate}",
                bg="white",
                font=("Arial", 10)
            ).pack(anchor=tk.W, pady=2)

        def confirm_and_save():
            if save_to_database(
                id_entry.get(),
                name_entry.get(),
                int(precinct_var.get()),
                selected_candidates
            ):
                messagebox.showinfo("Success", "Your vote has been recorded!")
                confirm_window.destroy()
                clear_form()

        # Create buttons frame
        button_frame = tk.Frame(confirm_window, bg="white")
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        # Cast My Votes button
        cast_button = tk.Button(
            button_frame,
            text="Cast My Votes",
            bg="#ff0000",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            borderwidth=0,
            padx=20,
            pady=8,
            command=confirm_and_save
        )
        cast_button.pack(side=tk.LEFT, padx=5)

        # Cancel button
        cancel_button = tk.Button(
            button_frame,
            text="Cancel",
            bg="#ff0000",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            borderwidth=0,
            padx=20,
            pady=8,
            command=confirm_window.destroy
        )
        cancel_button.pack(side=tk.LEFT, padx=5)

    def confirm_votes(review_window, selected_candidates, voter_id, voter_name, precinct):
        # Create confirmation window
        confirm_window = tk.Toplevel()
        confirm_window.title("Vote Confirmation")
        confirm_window.geometry("400x300")
        confirm_window.configure(bg="white")

        # Create confirmation message
        message = f"Vote Successfully Cast!\n\n"
        message += f"Voter Information:\n"
        message += f"ID: {voter_id}\n"
        message += f"Name: {voter_name}\n"
        message += f"Precinct: {precinct}\n\n"
        message += "Selected Candidates:\n"
        message += "\n".join(f"• {candidate}" for candidate in selected_candidates)

        # Add confirmation message
        tk.Label(
            confirm_window,
            text=message,
            justify=tk.LEFT,
            bg="white",
            font=("Arial", 10),
            pady=20
        ).pack(padx=20)

        # Add OK button
        tk.Button(
            confirm_window,
            text="OK",
            command=lambda: [confirm_window.destroy(), review_window.destroy()],
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=30
        ).pack(pady=10)

        # Center the confirmation window
        confirm_window.update_idletasks()
        width = confirm_window.winfo_width()
        height = confirm_window.winfo_height()
        x = (confirm_window.winfo_screenwidth() // 2) - (width // 2)
        y = (confirm_window.winfo_screenheight() // 2) - (height // 2)
        confirm_window.geometry(f'{width}x{height}+{x}+{y}')

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

    review_button = tk.Button(
        button_frame,
        text="Review My\nVotes",
        bg="#4CAF50",
        fg="white",
        width=15,
        height=2,
        command=review_votes
    )
    review_button.grid(row=0, column=0, padx=20)

    clear_button = tk.Button(
        button_frame,
        text="Clear My\nChoices",
        bg="#4CAF50",
        fg="white",
        width=15,
        height=2,
        command=clear_choices
    )
    clear_button.grid(row=0, column=1, padx=20)

    cancel_button = tk.Button(
        button_frame,
        text="Cancel",
        bg="#4CAF50",
        fg="white",
        width=15,
        height=2,
        command=cancel
    )
    cancel_button.grid(row=1, column=0, padx=20, pady=20)

    close_button = tk.Button(
        button_frame,
        text="Close",
        bg="#4CAF50",
        fg="white",
        width=15,
        height=2,
        command=close
    )
    close_button.grid(row=1, column=1, padx=20, pady=20)

    return form_window


class VoterSearchWindow:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Voter Search")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        # Add header label
        header_label = tk.Label(self.root, text="Voter Search", font=("Arial", 12, "bold"))
        header_label.pack(fill=tk.X, pady=(10, 5))

        # Add separator line
        separator = tk.Frame(self.root, height=2, bg="black")
        separator.pack(fill=tk.X, padx=10)

        # Create frame for search components
        search_frame = tk.Frame(self.root)
        search_frame.pack(fill=tk.X, padx=20, pady=20)

        # Add ID label
        id_label = tk.Label(search_frame, text="Voter's ID Number:")
        id_label.grid(row=0, column=0, sticky="w", pady=10)

        # Add entry field
        self.id_entry = tk.Entry(search_frame, width=30)
        self.id_entry.grid(row=0, column=1, padx=10)

        # Add search button
        search_button = tk.Button(
            search_frame,
            text="Search",
            bg="purple",
            fg="white",
            padx=20,
            pady=5,
            command=self.search_voter
        )
        search_button.grid(row=0, column=2, padx=10)

        # Create result frame
        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Initially hide the result frame
        self.result_frame.pack_forget()

        # Create text widget to display results
        self.result_text = tk.Text(self.result_frame, height=10, width=50)
        self.result_text.pack(fill=tk.BOTH, expand=True)
        self.result_text.config(state=tk.DISABLED)

        # Add cancel button
        cancel_button = tk.Button(
            self.root,
            text="Close",
            bg="red",
            fg="white",
            padx=40,
            pady=5,
            command=self.root.destroy
        )
        cancel_button.pack(pady=20)

        # Center the window
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
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

        # Clear the result frame and text
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete('1.0', tk.END)

        if result:
            # Format and display the voter information
            self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

            voter_info = f"Voter ID: {result[0]}\n"
            voter_info += f"Name: {result[1]}\n"
            voter_info += f"Precinct: {result[2]}\n"

            if result[3]:  # If there are selected candidates
                voter_info += f"\nSelected Candidates:\n"
                candidates = result[3].split(',')
                for i, candidate in enumerate(candidates, 1):
                    voter_info += f"{i}. {candidate}\n"

            voter_info += f"\nPrecinct Vote Count: {result[4]}\n"
            voter_info += f"Total Votes: {result[5]}"

            self.result_text.insert('1.0', voter_info)
        else:
            self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            self.result_text.insert('1.0', "No voter found with this ID.")

        self.result_text.config(state=tk.DISABLED)

def MainWindow():
    # Create main window
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

    # Create menubar
    menubar = tk.Menu(mainwindow)
    mainwindow.config(menu=menubar)

    # Create File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=open_new_form)
    file_menu.add_command(label="View", command=open_search_window)
    file_menu.add_separator()
    file_menu.add_command(label="Logout", command=lambda: logout(mainwindow))

    # Create Edit menu
    edit_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Search", command=lambda: VoterManagementWindow())

    # Create Help menu
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=lambda: AboutDialog(mainwindow))
    help_menu.add_command(label="Authors", command=lambda: AuthorDialog(mainwindow))

    # Create main frame
    main_frame = ttk.Frame(mainwindow, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Create and style the precinct label
    precinct_label = ttk.Label(main_frame, text="Select Precinct:", font=('Arial', 12))
    precinct_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

    # Create the precinct combobox
    precincts = ["245", "367", "641", "179", "All"]
    precinct_combo = ttk.Combobox(main_frame, values=precincts, state="readonly", width=30)
    precinct_combo.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    precinct_combo.set("Select Precinct")

    # Create a frame for result
    result_frame = ttk.LabelFrame(main_frame, padding="10")
    result_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')

    # Create the text area for results
    result_text = tk.Text(result_frame,
                      width=40,
                      height=5,
                      wrap=tk.WORD,
                      font=('Arial', 11),
                      relief="solid",
                      borderwidth=1)
    result_text.grid(row=0, column=0, pady=(0, 10), sticky='nsew')
    result_text.config(state='disabled')

    # Create clear button
    def clear_text():
        result_text.config(state='normal')
        result_text.delete('1.0', tk.END)
        result_text.config(state='disabled')
        precinct_combo.set("Select Precinct")

    clear_button = ttk.Button(result_frame, text="Clear", command=clear_text)
    clear_button.grid(row=1, column=0, pady=(0, 5))

    # Event handler for precinct selection
    def on_precinct_selected(event):
        selected_precinct = precinct_combo.get()
        result_text.config(state='normal')
        result_text.delete('1.0', tk.END)
        result_text.insert('1.0', f"Selected Precinct: {selected_precinct}")
        result_text.config(state='disabled')

    # Bind the selection event
    precinct_combo.bind('<<ComboboxSelected>>', on_precinct_selected)

    # Center the window
    window_width = 400
    window_height = 300
    screen_width = mainwindow.winfo_screenwidth()
    screen_height = mainwindow.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    mainwindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def logout(mainwindow):
    mainwindow.destroy()
    vote.deiconify()


# Set up valid credentials
valid_credentials = {"admin": "password123"}

# Create the main application window
vote = tk.Tk()
vote.title("Login")

# Create the database when the application starts
create_database()

# Initialize the login system with valid credentials
login_system = LoginSystem(vote, valid_credentials)

# Start the main loop
vote.mainloop()