from tkinter import messagebox

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
root.title("Авторизация")
root.geometry("300x200+400+400")

def submitout():
    global user
    Name = name.get()
    Pass = password.get()
    if Name != "" and Pass != "":
        vals = (Name, Pass)
        select_query = "SELECT * FROM `users` WHERE `name` = %s and `password` = %s"
        cursor.execute(select_query, vals)
        user = cursor.fetchone()
    else:
        messagebox.showwarning('Ошибка', 'Проверьте правильность ввода данных')
    if user is not None:
        root.destroy()
        os.system('python main.py')



name_label = customtkinter.CTkLabel(root, text="Введите ваше имя")
name_label.pack(pady=1)

name = customtkinter.CTkEntry(root)
name.pack(pady=2)

password_label = customtkinter.CTkLabel(root, text="Введите ваш пароль")
password_label.pack(pady=3)

password = customtkinter.CTkEntry(root)
password.pack(pady=4)

submit_button = customtkinter.CTkButton(root,text="Войти", command=submitout)
submit_button.pack(pady=5)


root.mainloop()