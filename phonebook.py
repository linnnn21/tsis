import psycopg2
import json  # Для преобразования списка пользователей в JSON

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="meouwqq21",
    host="localhost",
    port="5432"
)
cur = conn.cursor() # Создаем объект курсора для выполнения SQL-запросов

# Вставка одного пользователя с использованием SQL-процедуры
def insert_one():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone number: ")
    cur.execute("CALL insert_or_update_user(%s, %s, %s)", (name, surname, phone))
    conn.commit()
    print("User inserted or updated successfully.")

# Вставка нескольких пользователей через JSON (batch insert)
def insert_many():
    users = []
    n = int(input("How many users do you want to insert? "))
    for _ in range(n):
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        users.append({"name": name, "surname": surname, "phone": phone})
    
    # Отправляем список как JSON строку в SQL-процедуру
    cur.execute("CALL insert_many_users(%s::json)", [json.dumps(users)])
    conn.commit()
    print("Batch insert completed.")

#Поиск пользователей по шаблону
def search_by_pattern():
    pattern = input("Enter pattern to search: ")
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

#Получение данных с пагинацией
def paginate():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Delete entry by name, surname or phone
def delete_entry():
    value = input("Enter name, surname or phone to delete: ")
    cur.execute("CALL delete_by_name_or_phone(%s)", (value,))
    conn.commit()
    print("Entry deleted.")

#Главное интерактивное меню
def menu():
    while True:
        print("""
====== PHONEBOOK LAB 11 MENU ======
1. Insert one user
2. Insert many users (batch)
3. Search by pattern
4. View paginated data
5. Delete user
6. Exit
""")
        choice = input("Choose option (1–6): ")

        if choice == "1":
            insert_one()
        elif choice == "2":
            insert_many()
        elif choice == "3":
            search_by_pattern()
        elif choice == "4":
            paginate()
        elif choice == "5":
            delete_entry()
        elif choice == "6":
            break
        else:
            print("Invalid option. Try again.")

    # Close connection
    cur.close()
    conn.close()
    print("Disconnected from database.")

# Run the menu
if __name__ == "__main__":
    menu()
