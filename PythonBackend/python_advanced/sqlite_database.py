# from sqlite3 import connect
#
# with connect("contact.db") as db:
#     cursor = db.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS contacts (
#             first_name VARCHAR,
#             last_name VARCHAR,
#             phone_number VARCHAR
#         )
#     """
#     )
#     # cursor.execute(
#     #     """
#     #     INSERT INTO contacts (first_name, last_name, phone_number)
#     #     VALUES ('Adam', 'Smith', '+987654321')
#     #     """
#     # )
#
#     cursor.execute(
#         """
#         SELECT *
#         FROM contacts
#         where first_name = "Adam"
#         """
#     )
#     rows = cursor.fetchall()
#     print(rows)


import sys
import sqlite3


class ContactsRepo:
    def __init__(self, dp):
        self.dp = dp

    def add(self, first_name, last_name, phone_number):
        pass

    def list(self):
        pass

    def search(self, first_name):
        pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Only 1 argument is required")

    available_commands = ("add", "list", "search")
    command = sys.argv[1]

    if command not in available_commands:
        sys.exit(
            f"Unknown command: {command}\nAvailable commands: {available_commands}"
        )

    print(f"Executing command: {command}")

    with sqlite3.connect("contacts.db") as conn:
        re
