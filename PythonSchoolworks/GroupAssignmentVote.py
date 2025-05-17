import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
        
        if not id_entry.get():
            messagebox.showwarning("Missing Information", "Please enter Voter's ID Number")
            return
            
        if not name_entry.get():
            messagebox.showwarning("Missing Information", "Please enter Voter's Name")
            return
            
        if not precinct_var.get() or precinct_var.get() == "Select Precinct":
            messagebox.showwarning("Missing Information", "Please select a Precinct Number")
            return
            
        if not selected_candidates:
            messagebox.showwarning("No Selection", "Please select at least one candidate")
            return
            
        message = f"Voter ID: {id_entry.get()}\n"
        message += f"Voter Name: {name_entry.get()}\n"
        message += f"Precinct: {precinct_var.get()}\n\n"
        message += "Selected Candidates:\n"
        for candidate in selected_candidates:
            message += f"- {candidate}\n"
            
        messagebox.showinfo("Vote Review", message)
    
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

def MainWindow():
    voter_form = None
    
    # Hide login window
    vote.withdraw()

    # Create main window
    mainwindow = tk.Toplevel()
    mainwindow.title("Main Form")
    mainwindow.geometry("400x300")

    def open_new_form():
        nonlocal voter_form
        if voter_form is None or not tk.Toplevel.winfo_exists(voter_form):
            voter_form = create_voter_record_form()
        else:
            voter_form.lift()

    # Create menubar
    menubar = tk.Menu(mainwindow)
    mainwindow.config(menu=menubar)

    # Create File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=open_new_form)
    file_menu.add_command(label="View")
    file_menu.add_separator()
    file_menu.add_command(label="Logout", command=lambda: logout(mainwindow))

    # Create Edit menu
    edit_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Search")

    # Create Help menu
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About")
    help_menu.add_command(label="Authors")

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

# Create login window
vote = tk.Tk()
vote.title("Login")
vote.geometry("300x150")

# Center the login window
window_width = 300
window_height = 150
screen_width = vote.winfo_screenwidth()
screen_height = vote.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
vote.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

frame = ttk.Frame(vote, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Username row
entry_label = ttk.Label(frame, text="Username:")
entry_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = ttk.Entry(frame, width=30)
username_entry.grid(row=0, column=1, pady=5)

# Password row
password_label = ttk.Label(frame, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = ttk.Entry(frame, width=30, show="*")
password_entry.grid(row=1, column=1, pady=5)

# Login button
login = ttk.Button(frame, text="Login", command=MainWindow)
login.grid(row=2, column=0, pady=10)

cancel = ttk.Button(frame, text="Cancel", command=vote.quit)
cancel.grid(row=2, column=1, pady=10)

# Bind Enter key to login
vote.bind('<Return>', lambda event: MainWindow())

vote.mainloop()