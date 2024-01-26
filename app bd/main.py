import customtkinter
from CTkMessagebox import CTkMessagebox
import mysql.connector
from . import *

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    port='3306',
    password='12345678',
    database='app')

cursor = connection.cursor()

create_questions = """CREATE TABLE IF NOT EXISTS questions (id INT AUTO_INCREMENT PRIMARY KEY, question TEXT, answer TEXT)"""

cursor.execute(create_questions)


def next_question():
    global question_number
    question_number += 1

    cursor.execute("SELECT * FROM questions WHERE id=%s", (question_number,))
    question = cursor.fetchone()

    if question:
        question_label.configure(text=question[1])
    else:
        msg = CTkMessagebox(title="Викторина", message="Вопросы закончились!", option_1="Ok")
        response = msg.get()

        if response == "Ok":
            root.quit()
def check_answer():
    cursor.execute("SELECT * FROM questions WHERE id=%s", (question_number,))
    question = cursor.fetchone()

    if answer_entry.get().lower() == question[2].lower():
        CTkMessagebox(title="Викторина", message="Правильный ответ!")

    else:
        CTkMessagebox(title="Викторина", message="Неправильный ответ!")

    answer_entry.delete(0, customtkinter.END)
    next_question()

root = customtkinter.CTk()
root.title("Викторина")
root.geometry("600x200+400+400")

question_number = 0
answer_number = 0

question_label = customtkinter.CTkLabel(root, text="")
question_label.pack(anchor="center", padx=20)

answer_entry = customtkinter.CTkEntry(root)
answer_entry.pack(anchor="center", pady=10)

submit_button = customtkinter.CTkButton(root, text="Ответить", command=check_answer)
submit_button.pack(anchor="center", pady=10)

next_question()

root.mainloop()

connection.close()
