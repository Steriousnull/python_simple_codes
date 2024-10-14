import sqlite3

# Connect to the SQLite database or create a new one if it doesn't exist
conn = sqlite3.connect('virtual_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table if it does not exist
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    print("Table created successfully.")

# Create (Insert) operation
def add_admin(name, email, age):
    try:
        cursor.execute('''
            INSERT INTO admin_data (name, email, age)
            VALUES (?, ?, ?)
        ''', (name, email, age))
        conn.commit()
        print(f"Admin '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Admin with email '{email}' already exists.")

# Read (Fetch) operation
def view_admins():
    cursor.execute('SELECT * FROM admin_data')
    rows = cursor.fetchall()
    if rows:
        print("Admins List:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Age: {row[3]}")
    else:
        print("No admins found.")

# Update operation
def update_admin(admin_id, name=None, email=None, age=None):
    updates = []
    params = []

    if name:
        updates.append("name = ?")
        params.append(name)
    if email:
        updates.append("email = ?")
        params.append(email)
    if age:
        updates.append("age = ?")
        params.append(age)

    if updates:
        params.append(admin_id)
        query = f"UPDATE admin_data SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, params)
        conn.commit()
        print(f"Admin with ID '{admin_id}' updated successfully.")
    else:
        print("No updates provided.")

# Delete operation
def delete_admin(admin_id):
    cursor.execute('DELETE FROM admin_data WHERE id = ?', (admin_id,))
    conn.commit()
    print(f"Admin with ID '{admin_id}' deleted successfully.")

# Main function to demonstrate CRUD operations
def main():
    create_table()
    
    while True:
        print("\nAdmin CRUD Operations:")
        print("1. Add Admin")
        print("2. View Admins")
        print("3. Update Admin")
        print("4. Delete Admin")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter admin name: ")
            email = input("Enter admin email: ")
            age = int(input("Enter admin age: "))
            add_admin(name, email, age)
        elif choice == '2':
            view_admins()
        elif choice == '3':
            admin_id = int(input("Enter admin ID to update: "))
            name = input("Enter new name (leave blank to skip): ") or None
            email = input("Enter new email (leave blank to skip): ") or None
            age = input("Enter new age (leave blank to skip): ")
            age = int(age) if age else None
            update_admin(admin_id, name, email, age)
        elif choice == '4':
            admin_id = int(input("Enter admin ID to delete: "))
            delete_admin(admin_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
