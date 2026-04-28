Completed TSIS1: PhoneBook Extended Contact Management project.

Implemented all required tasks from the specification:

1. Updated database schema:
- Created contacts table
- Created phones table for multiple phone numbers per contact
- Created groups table for categories
- Added email and birthday fields
- Added foreign keys and relational structure

2. Added multiple phone numbers support:
- One contact can store mobile, home, and work phones
- Separate phones table with one-to-many relationship

3. Added contact groups:
- Family
- Work
- Friend
- Other

4. Implemented advanced console features:
- Add new contact
- Add phone to existing contact
- Move contact to another group
- Search by name
- Search by email
- Search by phone number
- Filter by group
- Sort by name
- Sort by birthday
- Sort by date added

5. Implemented pagination:
- next
- prev
- quit

6. Implemented CSV import:
- Extended CSV format:
name,email,birthday,group,phones

7. Implemented JSON export:
- Export all contacts with phones and groups to contacts_export.json

8. Implemented JSON import:
- Duplicate handling with skip / overwrite options

9. Implemented PostgreSQL stored procedures:
- add_phone
- move_to_group

10. Implemented PostgreSQL function:
- search_contacts

11. Added GitHub project structure:
- phonebook.py
- config.py
- connect.py
- schema.sql
- procedures.sql
- contacts.csv
- contacts_export.json
- README.md

12. Project tested and working correctly.

Technologies used:
Python, PostgreSQL, psycopg2, SQL, PL/pgSQL, CSV, JSON, GitHub.
