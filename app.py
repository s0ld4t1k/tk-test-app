import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# rel=[]
tests = {
    "Matemamatika": [
        {
            "question": "Логарифм 100 по основанию 10 равен...",
            "options": ["1", "2", "3", "4"],
            "correct_answer": "2",
            "theme": "logarifm"
        },
        {
            "question": "Интеграл от x по dx равен...",
            "options": ["x", "x^2/2", "x^3/3", "ln(x)"],
            "correct_answer": "x^2/2",
            "theme": "integral"
        },
        {
            "question": "Чему равна 1/2 + 1/4?",
            "options": ["1/8", "1/6", "3/4", "1"],
            "correct_answer": "3/4",
            "theme": "drobi"
        },
        {
            "question": "Вектор (3, 4) имеет длину...",
            "options": ["5", "6", "7", "8"],
            "correct_answer": "5",
            "theme": "wektorlar"
        },
        {
            "question": "Чему равен косинус 0 градусов?",
            "options": ["0", "1", "-1", "1/2"],
            "correct_answer": "1",
            "theme": "Trigonometriya"
        }
    ],
    "Fizika": [
        {
            "question": "Скорость измеряется в...",
            "options": ["м/с", "Н", "Па", "Ом"],
            "correct_answer": "м/с",
            "theme": "Tizlik"
        },
        {
            "question": "Давление измеряется в...",
            "options": ["м/с", "Н", "Па", "Ом"],
            "correct_answer": "Па",
            "theme": "Basys"
        },
        {
            "question": "Сила измеряется в...",
            "options": ["м/с", "Н", "Па", "Ом"],
            "correct_answer": "Н",
            "theme": "Kuwwat"
        },
        {
            "question": "Сопротивление измеряется в...",
            "options": ["м/с", "Н", "Па", "Ом"],
            "correct_answer": "Ом",
            "theme": "Om"
        },
         {
            "question": "Что такое мощность?",
            "options": ["Работа, деленная на время", "Масса, умноженная на ускорение", "Сила, деленная на площадь", "Расстояние, деленное на время"],
            "correct_answer": "Работа, деленная на время",
            "theme": "Guyc"
        }
    ],
    "Turkemn dili": [
        {
            "question": "Гласные звуки в туркменском языке...",
            "options": ["Согласные", "Гласные", "Дифтонги", "Трифтонги"],
            "correct_answer": "Гласные",
            "theme": "Fonetika"
        },
        {
            "question": "Падежи в туркменском языке...",
            "options": ["4", "5", "6", "7"],
            "correct_answer": "6",
            "theme": "Grammatika"
        },
        {
            "question": "Глаголы в туркменском языке изменяются по...",
            "options": ["Родам", "Числам", "Временам", "Все перечисленное"],
            "correct_answer": "Все перечисленное",
            "theme": "Islikler"
        },
        {
            "question": "Что такое причастие?",
            "options": ["Форма глагола", "Форма существительного", "Форма прилагательного", "Форма наречия"],
            "correct_answer": "Форма глагола",
            "theme": "Islikler"
        },
        {
            "question": "Что такое деепричастие?",
            "options": ["Форма глагола", "Форма существительного", "Форма прилагательного", "Форма наречия"],
            "correct_answer": "Форма глагола",
            "theme": "Grammatika"
        }
    ]
}

class TestApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Тест")


        self.name = ""
        self.subject = ""

        self.current_question = 0
        self.score = 0
        self.res=[]

        self.name_label = tk.Label(root, text="Talybyn ady:")
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)

        self.subject_label = tk.Label(root, text="Sapak:")
        self.subject_label.pack(pady=5)

        self.subject_combobox = ttk.Combobox(root, values=list(tests.keys()))
        self.subject_combobox.pack(pady=5)

        self.start_button = tk.Button(root, text="Baslat", command=self.start_test)
        self.start_button.pack(pady=10)

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12))

    def start_test(self):
        self.name = self.name_entry.get()
        self.subject = self.subject_combobox.get()

        if not self.name or not self.subject:
            messagebox.showerror("Error", "Adynyzy giririzin")
            return

        if self.subject not in tests:
            messagebox.showerror("Error", "Adynyzy girizin")
            return

        self.tests = tests[self.subject]
        self.current_question = 0
        self.score = 0

        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.subject_label.pack_forget()
        self.subject_combobox.pack_forget()
        self.start_button.pack_forget()

        self.question_label.pack(pady=10)
        for i in range(4):
            radio_button = tk.Radiobutton(self.root, text="", variable=self.radio_var, value="", font=("Arial", 12))
            self.radio_buttons.append(radio_button)
            radio_button.pack(anchor=tk.W)
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.current_question < len(self.tests):
            question = self.tests[self.current_question]
            self.question_label.config(text=f"{question['theme']}: {question['question']}")
            for i in range(4):
                self.radio_buttons[i].config(text=question["options"][i], value=question["options"][i])
            self.radio_var.set(None)
        else:
            self.show_results()

    def next_question(self):
        question = self.tests[self.current_question]
        global res
        if self.radio_var.get() == question["correct_answer"]:
            self.res.append([question['theme'], 1])
            self.score += 1
        else:
            self.res.append([question['theme'], 0])
        self.current_question += 1
        self.show_question()

    def show_results(self):
        messagebox.showinfo("Netije", f"Talyp: {self.name}\nSapak: {self.subject}\nNetije: {self.score}/{len(self.tests)}")

        print(self.res)
        try:
            with open(f'./test/{self.name}.txt','a+')as file:

                file.write(f'{self.subject}\n')
                for i in self.res:
                    file.write(f'1:{i[0]}:{i[1]}\n')
        except Exception as e:
            print(f'gen txt {e}')

root = tk.Tk()
root.geometry("600x400")
app = TestApp(root)
root.mainloop()