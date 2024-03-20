import tkinter as tk
from tkinter import ttk, filedialog, messagebox, PhotoImage
from classifier_model import predict
from styles import load_themes


# Темы и оформление -----------------------------------------------

def toggle_theme():
    if current_theme.get() == "light":
        set_dark_theme()
    else:
        set_light_theme()


def set_light_theme():
    style.theme_use('light_theme')
    text_input.configure(background="#eeeeee", 
                         foreground="#212121", 
                         border=0, 
                         borderwidth=0)
    result_text.configure(background="#ffffff", 
                          foreground="#212121",
                          border=0, 
                          borderwidth=0)
    current_theme.set("light")


def set_dark_theme():
    style.theme_use('dark_theme')
    text_input.configure(background="#3b4157", 
                         foreground="#f5f5f5",
                         border=0, 
                         borderwidth=0)
    result_text.configure(background="#24293d", 
                          foreground="#f5f5f5",
                          border=0, 
                          borderwidth=0) 
    current_theme.set("dark")

# Методы работы с текстовыми полями и полем ввода ------------------------

def insert_text(event):
    text_input.insert('end', event.char)


def clear_text():
    text_input.delete(1.0, tk.END)


def submit_text():
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    if not text_input.get(1.0, tk.END):
        messagebox.showwarning("Упс!", "Пустой ввод!")
        return

    user_input = text_input.get(1.0, tk.END)

    if not user_input.strip():
        messagebox.showwarning("Упс!", "Пустой ввод!")
        return

    try:
        result = predict(user_input, checkbox_var.get())
        result_text.insert(tk.END, result)
        result_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showwarning("Упс!", f"Текст ошибки: {e}")

# Сообщения ---------------------------------------------------------

def ask_save():
    result = messagebox.askquestion("Сохранение", "Сохранить результаты?")
    if result == "yes":
        save_result()
    else:
        clear_text()

# Кнопки меню и их вспомогательные методы ------------------------------
    
def save_result():
    try:
        file_dialog = filedialog.asksaveasfilename(
            defaultextension=".txt", 
            filetypes=[("Text files", "*.txt")])

        if file_dialog:
            with open(file_dialog, "w") as fd:
                fd.write(text_input.get(1.0, tk.END))
                fd.write('\n')
                fd.writelines(result_text.get(1.0, tk.END))

        messagebox.showinfo("Сохранение", "Результаты сохранены")
    except Exception as e:
        messagebox.showwarning("Упс!", f"Текст ошибки: {e}")

# Описание окна и его конфигурации -------------------------------------

WIDTH = 1000
HEIGTH = 600

root = tk.Tk()
root.title("DevTextClassifier | Классификация текста")
root.geometry("1000x600")
root.resizable(False, False)

style = ttk.Style()

load_themes()

current_theme = tk.StringVar()
current_theme.set("light")  

# Верхнее меню --------------------------------------------------

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Новая генерация", command=ask_save)
file_menu.add_command(label="Сохранить", 
                      command=save_result)
file_menu.add_separator()
file_menu.add_command(label="Закрыть", command=lambda: root.quit())
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)

# Верхняя горизонтальная панель -----------------

top_frame = ttk.Frame(root, height=60, style='Custom.TFrame')
top_frame.pack(fill=tk.X)

checkbox_var = tk.BooleanVar()
show_probabiliteis = ttk.Checkbutton(top_frame, 
                                     text="Показать вероятности", variable=checkbox_var, 
                                     padding=5)
show_probabiliteis.pack(side=tk.LEFT, padx=10)

theme_button_bg = tk.PhotoImage(file="UI/button_themes.png")

theme_button = ttk.Button(top_frame, 
                          text="Тема", 
                          command=toggle_theme, 
                          style='Gray.TButton', 
                          image=theme_button_bg)
theme_button.pack(side=tk.RIGHT, padx=10, pady=4)

# Главный фрейм -----------------------------------------------------

main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Левый фрейм -------------------------------------------------------

left_frame = ttk.Frame(main_frame, width=root.winfo_width() // 2)
left_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)

# Поле ввода --------------------------------------------------------

text_input = tk.Text(left_frame, wrap=tk.WORD, width=30)
text_input.bind('<Control-v>', insert_text)
text_input.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Кнопки с отдельным стилем -----------------------------------------

button_submit_bg = tk.PhotoImage(file="UI/button_go_.png")
button_clear_bg = tk.PhotoImage(file="UI/button_clear_.png")

buttons_frame = ttk.Frame(left_frame, width=50, height=90)
buttons_frame.pack(expand=True, padx=10, pady=10)

clear_button = ttk.Button(buttons_frame, 
                          text="Очистить", 
                          style='Custom.TButton', 
                          command=clear_text, 
                          image=button_clear_bg)
clear_button.pack(side=tk.RIGHT, padx=1, pady=10)

submit_button = ttk.Button(buttons_frame, 
                           text="Готово", 
                           style='Custom.TButton', 
                           command=submit_text, 
                           image=button_submit_bg)
submit_button.pack(side=tk.LEFT, padx=1, pady=10)

# Правый фрейм ------------------------------------------------------

right_frame = ttk.Frame(main_frame, width=200)
right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

label = ttk.Label(right_frame, text="Предполагаемое направление")
label.pack(side=tk.TOP, padx=10, pady=10)

result_text = tk.Text(right_frame, wrap=tk.WORD, state=tk.DISABLED)
result_text.configure(font=("Century Gothic", 10), borderwidth=0)
result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

set_light_theme()
root.mainloop()
