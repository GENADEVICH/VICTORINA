from tkinter import messagebox, StringVar
import customtkinter
import mysql.connector
import os

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    port='3306',
    password='12345678',
    database='app')

cursor = connection.cursor()

create_users = """CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)"""
cursor.execute(create_users)


root = customtkinter.CTk()
root.title("Регистрация")
root.geometry("300x200+400+400")

def get_password():
    password = passw.get()
    masked_password = '*' * len(password)
    print("Введенный пароль:", masked_password)

def entry_bd():
    password = passw.get()
    Name = name.get()
    if password != "" and Name != "":
        vals = (Name, password)
        createUser = "INSERT INTO `users`(`name`, `password`) VALUES(%s, %s)"
        cursor.execute(createUser, vals)
        connection.commit()
        root.destroy()
        os.system('python avtoriz.py')
    else:
        messagebox.showwarning('Ошибка', 'Проверьте правильность ввода данных')

name_label = customtkinter.CTkLabel(root, text="Введите ваше имя")
name_label.pack(pady=1)

name = customtkinter.CTkEntry(root)
name.pack(pady=2)

password_label = customtkinter.CTkLabel(root, text="Введите ваш пароль")
password_label.pack(pady=3)

passw = customtkinter.CTkEntry(root)
passw.pack(pady=4)

submit_button = customtkinter.CTkButton(root, text="Зарегистрироваться", command=entry_bd)
submit_button.pack(pady=5)

root.mainloop()