import psycopg2
import csv
from connect import DB_host, DB_base, DB_user, DB_pass

conn = psycopg2.connect(
    host=DB_host,
    database=DB_base,
    user=DB_user,
    password=DB_pass,
    port="5432"
)

cur = conn.cursor()

command = """
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
);
"""
cur.execute(command)
conn.commit()

while True:
    print("\n--- PhoneBook ---")
    print("1. Show all contacts")
    print("2. Add contact (console)")
    print("3. Import from csv")
    print("4. Search")
    print("5. Update phone by name")
    print("6. Update name by phone")
    print("7. Delete by name")
    print("8. Delete by phone")
    print("0. Exit")

    choose = input("Choose an option: ").strip()

    try:
        if choose == "1":
            cur.execute("SELECT * FROM phonebook ORDER BY id")
            results = cur.fetchall()
            if not results:
                print("(no contacts)")
            else:
                for c in results:
                    print(f"[{c[0]}] {c[1]} - {c[2]}")

        elif choose == "2":
            print("Please input first name and phone number")
            f_name = input("Input first name: ").strip()
            ph_number = input("Input phone number: ").strip()

            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                (f_name, ph_number)
            )
            conn.commit()
            print("Contact added.")

        elif choose == "3":
            file_name = input("Input file name: ").strip()

            with open(file_name, newline='', encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None)  # skip header if it exists

                for row in reader:
                    if len(row) != 2:
                        continue
                    first_name, phon = row
                    cur.execute(
                        "INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                        (first_name.strip(), phon.strip())
                    )

            conn.commit()
            print("CSV imported successfully.")

        elif choose == "4":
            print("\nSearch contacts by filter:")
            print("1. Search by partial name or phone")
            print("2. Search by exact name")
            print("3. Search by phone prefix")
            sub = input("Choose filter: ").strip()

            if sub == "1":
                pattern = input("Enter part of name or phone: ").strip()
                like_pattern = f"%{pattern}%"
                cur.execute(
                    "SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s ORDER BY id",
                    (like_pattern, like_pattern)
                )

            elif sub == "2":
                name = input("Enter exact name: ").strip()
                cur.execute(
                    "SELECT * FROM phonebook WHERE name = %s ORDER BY id",
                    (name,)
                )

            elif sub == "3":
                prefix = input("Enter phone prefix: ").strip()
                cur.execute(
                    "SELECT * FROM phonebook WHERE phone LIKE %s ORDER BY id",
                    (f"{prefix}%",)
                )

            else:
                print("Invalid filter option")
                continue

            results = cur.fetchall()
            if not results:
                print("(no contacts found)")
            else:
                for c in results:
                    print(f"[{c[0]}] {c[1]} - {c[2]}")

        elif choose == "5":
            name = input("Input name to update phone: ").strip()
            new_phone = input("Input new phone: ").strip()

            command = "UPDATE phonebook SET phone = %s WHERE name = %s"
            cur.execute(command, (new_phone, name))
            conn.commit()
            print(f"Updated {cur.rowcount} row(s)")

        elif choose == "6":
            phone = input("Input phone to update name: ").strip()
            new_name = input("Input new name: ").strip()

            command = "UPDATE phonebook SET name = %s WHERE phone = %s"
            cur.execute(command, (new_name, phone))
            conn.commit()
            print(f"Updated {cur.rowcount} row(s)")

        elif choose == "7":
            name = input("Input name for deleting: ").strip()
            command = "DELETE FROM phonebook WHERE name = %s"
            cur.execute(command, (name,))
            conn.commit()
            print(f"Deleted {cur.rowcount} row(s)")

        elif choose == "8":
            phone = input("Input phone for deleting: ").strip()
            command = "DELETE FROM phonebook WHERE phone = %s"
            cur.execute(command, (phone,))
            conn.commit()
            print(f"Deleted {cur.rowcount} row(s)")

        elif choose == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid syntax")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

cur.close()
conn.close()