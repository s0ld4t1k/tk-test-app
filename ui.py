import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import os

students = []
stri = ''

def studentData(file):
    student = str(file.decode()).split('/')
    student = student[len(student) - 1][:-4]
    res = []
    students.append({"name": student, "id": len(students) + 1, "info": "", "results": []})  # Добавляем "results"
    global stri
    stri += student.center(30, '*') + '\n'
    try:
        with open(file, 'rb') as fl:
            for line in fl.readlines():
                ln = line.decode().strip().split(':')
                if len(ln) == 1 and len(ln[0]) > 0:
                    lesson = ln[0]
                    res.append([lesson, 0, 0, 0, {}])
                    themes = {}
                    themesCor = {}
                elif len(ln) > 1:
                    res[len(res) - 1][1] += 1
                    res[len(res) - 1][2] += int(ln[2])
                    res[len(res) - 1][3] = (100 * res[len(res) - 1][2]) / res[len(res) - 1][1]
                    try:
                        themes[ln[1]] += 1
                        themesCor[ln[1]] += int(ln[2])
                    except:
                        themes[ln[1]] = 1
                        themesCor[ln[1]] = int(ln[2])
                    res[len(res) - 1][4][ln[1]] = (100 * themesCor[ln[1]]) / themes[ln[1]]
    except Exception as e:
        print(f'error  {e}')
    res = sorted(res, key=lambda item: item[3], reverse=True)
    results = []
    k = 0
    for rs in res:
        k += 1
        rs[4] = sorted(rs[4].items(), key=lambda item: item[1], reverse=False)[0]
        talyp = student
        sapak = rs[0]
        baha = rs[3]
        worst = rs[4][0]
        stri += f'{k}.{sapak} {baha}% {worst}\n'
        info =f'''
         * gowy bilyan sapagy {res[0][0]}.\n
        {(res[0][0]).title()} shu sapagy siz gowy bilyarsiniz we siz bu sapakdan kamilleship durli ders basleshiklerine hem gatnashyp bilersiniz.\n
        {(res[0][0]).title()} shu dersin shu {res[0][4][0]} temadan yetishiginiz pes, has gowy tayyarlanmagynyzy maslahat beryaris.\n\n
         * erbet bilyan sapagy {res[len(res)-1][0]}.\n
         {(res[len(res)-1][0]).title()} dersinden yetishiginiz pes, shu sapakdan gowy tayyarlyk gormegini we esaslaryny(bazalaryny) owrenmeginizi maslahat beryaris.\n\n
        '''
        results.append({
            'talyp': talyp,
            'sapak': sapak,
            'baha': baha,
            'worst': worst,
            'info':info
        })
    stri += '\n'
    stri += f'gowy bilyan sapagy {res[0][0]}.\n'
    stri += f'{(res[0][0]).title()} shu dersin shu {res[0][4][0]} temadan yetishiginiz pes, has gowy tayyarlanmagynyzy maslahat beryaris.\n'
    stri += f'{(res[0][0]).title()} shu sapagy siz gowy bilyarsiniz we siz bu sapakdan kamilleship durli ders basleshiklerine hem gatnashyp bilersiniz.\n\n'
    stri += f'erbet bilyan sapagy {res[len(res)-1][0]}.\n'
    stri += f'{(res[len(res)-1][0]).title()} dersinden yetishiginiz pes, shu sapakdan gowy tayyarlyk gormegini we esaslaryny(bazalaryny) owrenmeginizi maslahat beryaris.\n\n'
    for student_data in students:
        if student_data["name"] == student:
            student_data["results"] = results
            break
    return results

def fetch(dir, stri):
    for root, _, files in os.walk(dir):
        for file in files:
            file = os.path.join(root, file)
            studentData(file)
            stri += ''.center(50, '-') + '\n\n'
    try:
        with open('./result.html', 'w') as html:
            html.write(f'''
                    <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width-device-width, initial-scale=1.0">
                            <title>Test</title>
                        </head>
                        <body>
                            {stri}
                        </body>
                        </html>
                    ''')
    except:
        print('gen html')

def show_student_info(student_id):
    for student in students:
        if student["id"] == student_id:
            
            info_window = tk.Toplevel(root)
            info_window.title(student["name"])
            info_text = tk.Text(info_window, wrap=tk.WORD)
            info_text.pack(padx=10, pady=10)
            info_text.insert(tk.END, f"Ady: {student['name']}\n\n")
            if student["results"]:
                info_text.insert(tk.END, "Netijeler:\n")
                for result in student["results"]:
                    info_text.insert(tk.END, f"  {result['sapak']}: {result['baha']}%, \nIn pes temasy: {result['worst']}\n")
                info_text.insert(tk.END, f'info: {result['info']}')
            else:
                info_text.insert(tk.END, "Нет доступных результатов.")
            info_text.config(state=tk.DISABLED)
            break

def edit_student(student_id):
    for student in students:
        if student["id"] == student_id:
            name = simpledialog.askstring("Редактировать", "Имя", initialvalue=student["name"])
            address = simpledialog.askstring("Редактировать", "Адрес", initialvalue=student["address"])
            info = simpledialog.askstring("Редактировать", "Информация", initialvalue=student["info"])
            if name and address and info:
                student["name"] = name
                student["address"] = address
                student["info"] = info
                update_listbox()
                show_student_info(student_id)
            break

def update_listbox():
    listbox.delete(0, tk.END)
    for student in students:
        listbox.insert(tk.END, student["name"])

def search_student():
    search_term = search_entry.get().lower()
    listbox.delete(0, tk.END)
    for student in students:
        if search_term in student["name"].lower():
            listbox.insert(tk.END, student["name"])

dir = b'./test/'
fetch(dir, stri)

root = tk.Tk()
root.title("Talyplar")
root.geometry("600x400")
# root.config(bg="#e0f2f7")
search_frame = tk.Frame(root)
search_frame.pack(pady=5)

search_label = tk.Label(search_frame, text="Gozle:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT)

search_button = tk.Button(search_frame, text="Tapmak", command=search_student)
search_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root)
listbox.pack()

update_listbox()

def on_select(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        student_id = students[index]["id"]
        show_student_info(student_id)

listbox.bind("<Double-1>", on_select)

root.mainloop()