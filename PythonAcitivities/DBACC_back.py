import sqlite3 as sq

class EmployeeDB:
    def __init__(self):
        self.conn = sqlite3.connect('employee.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS employees (empno INTEGER PRIMARY KEY, empname TEXT NOT NULL, position TEXT NOT NULL, empsal DECIMAL(10,2) NOT NULL)')
        self.conn.commit()
        self.cursor.execute("SELECT COUNT(*) FROM employees")

    def view_all(self):
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()

    def search(self, empno):
        self.cursor.execute("SELECT * FROM employees WHERE empno = ?", (empno,))
        return self.cursor.fetchone()

    def add(self, empno, empname, position, salary):

        try:
            if position.lower() == 'clerk':
                salary = 20000.00
            elif position.lower() == 'accountant':
                salary = 25000.00
            elif position.lower() == 'sales manager':
                salary = 40000.00
            elif position.lower() == 'production staff':
                salary = 22000.00
            else:
                salary = 50000.00

            self.cursor.execute(
                "INSERT INTO employees VALUES (?, ?, ?, ?)",
                (empno, empname, position, salary)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    # options
    def update(self, empno, empname, position, salary):
        self.cursor.execute(
            "UPDATE employees SET empname = ?, position = ?, empsal = ? WHERE empno = ?",
            (empname, position, salary, empno)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete(self, empno):
        # Delete a record from the database
        self.cursor.execute("DELETE FROM employees WHERE empno = ?", (empno,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def __del__(self):
        self.conn.close()