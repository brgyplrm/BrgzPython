import tkinter as tk
from tkinter import scrolledtext, messagebox


def center_window(window, width, height):
    # Get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate position coordinates
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set window geometry
    window.geometry(f'{width}x{height}+{x}+{y}')


def main():
    # Create main window
    root = tk.Tk()
    root.title("Area Code")

    # Set window size - INCREASED WIDTH
    window_width = 800  # Increased from 500 to 800
    window_height = 600  # Increased height too

    # Center the window
    center_window(root, window_width, window_height)

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(padx=20, pady=20, anchor='nw')

    # Area code data
    area_code = {
        "MLA1": ["MANILA 1"],
        "MLA2": ["MANILA 2"],
        "MKT": ["MAKATI"],
        "LPN": ["LAS PINAS"],
        "MDN": ["MANDALUYONG"],
        "SNJ": ["SAN JUAN"],
        "QZN": ["QUEZON CITY"]
    }

    areaname = list(area_code.keys())

    # Create area code label
    area_label = tk.Label(main_frame, text="Area Code:")
    area_label.grid(row=0, column=0, sticky="w", pady=5)

    # Create area dropdown in row 0, column 1
    area_var = tk.StringVar()
    area_dropdown = tk.OptionMenu(main_frame, area_var, *areaname)
    area_dropdown.grid(row=0, column=1, sticky="w", padx=(10, 0), pady=5)

    area_label2 = tk.Label(main_frame, text="Area Name:")
    area_label2.grid(row=1, column=0, sticky="w", pady=5)

    # Create area name text field (Entry widget) - INCREASED WIDTH
    area_name_var = tk.StringVar()
    area_name_entry = tk.Entry(main_frame, textvariable=area_name_var, width=40,
                               state='readonly')  # Increased from 25 to 40
    area_name_entry.grid(row=1, column=1, sticky="w", padx=(10, 0), pady=5)

    # Callback function to update area name when area code is selected
    def update_area_name(*args):
        selected_code = area_var.get()
        if selected_code in area_code:
            # Get the area name (first item in the list)
            area_name = area_code[selected_code][0]
            area_name_var.set(area_name)
        else:
            area_name_var.set("")

    # Bind the callback to the area_var
    area_var.trace('w', update_area_name)

    sales_label = tk.Label(main_frame, text="Employee Number:")
    sales_label.grid(row=2, column=0, sticky="w", pady=5)

    # Create area name text field (Entry widget) - INCREASED WIDTH
    sales_num_var = tk.StringVar()
    sales_num_entry = tk.Entry(main_frame, textvariable=sales_num_var, width=40)  # Increased from 25 to 40
    sales_num_entry.grid(row=2, column=1, sticky="w", padx=(10, 0), pady=5)

    def search_employee():
        # Placeholder function for search functionality
        print(f"Searching for employee: {sales_num_var.get()}")

    search_button = tk.Button(main_frame, text="Search", command=search_employee)
    search_button.grid(row=2, column=2, sticky="w", pady=5, padx=5)

    sales_label2 = tk.Label(main_frame, text="Employee Name:")
    sales_label2.grid(row=3, column=0, sticky="w", pady=5)

    # Create area name text field (Entry widget) - INCREASED WIDTH
    sales_name_var = tk.StringVar()
    sales_name_entry = tk.Entry(main_frame, textvariable=sales_name_var, width=40)  # Increased from 25 to 40
    sales_name_entry.grid(row=3, column=1, sticky="w", padx=(10, 0), pady=5)

    # Add Quarterly checkboxes section
    quarterly_label = tk.Label(main_frame, text="Quarterly:")
    quarterly_label.grid(row=4, column=0, sticky="w", pady=(20, 5))

    # Create frame for checkboxes to organize them better
    checkbox_frame = tk.Frame(main_frame)
    checkbox_frame.grid(row=4, column=1, sticky="w", padx=(10, 0), pady=(20, 5))

    # Create checkbox variables
    q1_var = tk.BooleanVar()
    q2_var = tk.BooleanVar()
    q3_var = tk.BooleanVar()
    q4_var = tk.BooleanVar()

    # Create checkboxes
    q1_checkbox = tk.Checkbutton(checkbox_frame, text="1st", variable=q1_var)
    q1_checkbox.grid(row=0, column=0, sticky="w")

    q2_checkbox = tk.Checkbutton(checkbox_frame, text="2nd", variable=q2_var)
    q2_checkbox.grid(row=0, column=1, sticky="w", padx=(10, 0))

    q3_checkbox = tk.Checkbutton(checkbox_frame, text="3rd", variable=q3_var)
    q3_checkbox.grid(row=1, column=0, sticky="w")

    q4_checkbox = tk.Checkbutton(checkbox_frame, text="4th", variable=q4_var)
    q4_checkbox.grid(row=1, column=1, sticky="w", padx=(10, 0))

    # Function to get selected quarters
    def get_selected_quarters():
        selected = []
        if q1_var.get():
            selected.append("1st")
        if q2_var.get():
            selected.append("2nd")
        if q3_var.get():
            selected.append("3rd")
        if q4_var.get():
            selected.append("4th")
        return selected

    qsales_label = tk.Label(main_frame, text="Quarterly Sales:")
    qsales_label.grid(row=5, column=0, sticky="w", pady=(10, 5))

    # INCREASED WIDTH
    qsales_name_var = tk.StringVar()
    qsales_name_entry = tk.Entry(main_frame, textvariable=qsales_name_var, width=40)  # Increased from 25 to 40
    qsales_name_entry.grid(row=5, column=1, sticky="w", padx=(10, 0), pady=5)

    # Create scrolled text widget for multi-line text input - INCREASED WIDTH
    text_box = scrolledtext.ScrolledText(main_frame, width=60, height=12,
                                         wrap=tk.WORD)  # Increased from 35 to 60 width, 8 to 12 height
    text_box.grid(row=6, column=0, columnspan=3, sticky="ew", padx=(10, 0), pady=(20, 5))

    # Button functions
    def save_data():
        # Get all form data
        quarters = get_selected_quarters()
        area = area_var.get()
        area_name = area_name_var.get()
        emp_num = sales_num_var.get()
        emp_name = sales_name_var.get()
        quarterly_sales = qsales_name_var.get()
        notes = text_box.get("1.0", tk.END).strip()

        # For demonstration, print the data (you can modify this to save to file/database)
        print("=== SAVED DATA ===")
        print(f"Area: {area} - {area_name}")
        print(f"Employee: {emp_num} - {emp_name}")
        print(f"Quarterly Sales: {quarterly_sales}")
        print(f"Selected Quarters: {', '.join(quarters) if quarters else 'None'}")
        print(f"Notes: {notes}")
        print("==================")

        messagebox.showinfo("Save", "Data saved successfully!")

    def view_data():
        # Display current form data in the text box
        quarters = get_selected_quarters()
        area = area_var.get()
        area_name = area_name_var.get()
        emp_num = sales_num_var.get()
        emp_name = sales_name_var.get()
        quarterly_sales = qsales_name_var.get()

        # Create table header with proper spacing
        header = f"{'Area':<10} {'Number':<5} {'Name':<18} {'Quarter':<10} {'Sales':<10}\n"
        separator = "-" * 60 + "\n"

        # Create data row with truncated values to fit columns
        area_display = f"{area}-{area_name}" if area and area_name else ""
        area_display = area_display[:17] if len(area_display) > 17 else area_display

        emp_num_display = emp_num[:14] if len(emp_num) > 14 else emp_num
        emp_name_display = emp_name[:17] if len(emp_name) > 17 else emp_name

        quarters_display = ', '.join(quarters) if quarters else 'None'
        quarters_display = quarters_display[:11] if len(quarters_display) > 11 else quarters_display

        sales_display = quarterly_sales[:9] if len(quarterly_sales) > 9 else quarterly_sales

        data_row = f"{area_display:<18} {emp_num_display:<15} {emp_name_display:<18} {quarters_display:<12} {sales_display:<10}\n"

        view_text = header + separator + data_row

        # Clear the text box and insert the view data
        text_box.delete("1.0", tk.END)
        text_box.insert("1.0", view_text)

    def exit_app():
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            root.destroy()

    # Create button frame
    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=7, column=0, columnspan=3, sticky="w", padx=(10, 0), pady=20)

    # Create buttons - INCREASED BUTTON WIDTH
    save_button = tk.Button(button_frame, text="Save", command=save_data, width=12)  # Increased from 8 to 12
    save_button.grid(row=0, column=0, padx=(0, 10))

    view_button = tk.Button(button_frame, text="View", command=view_data, width=12)  # Increased from 8 to 12
    view_button.grid(row=0, column=1, padx=10)

    exit_button = tk.Button(button_frame, text="Exit", command=exit_app, width=12)  # Increased from 8 to 12
    exit_button.grid(row=0, column=2, padx=(10, 0))

    # Configure column weights for better resizing
    main_frame.columnconfigure(1, weight=1)

    # Start the main loop
    root.mainloop()


main()