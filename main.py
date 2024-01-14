import tkinter as tk

def multiply():
    number = int(entry_number.get())
    start = int(entry_start.get())
    end = int(entry_end.get())

    listbox.delete(0, tk.END)

    for i in range(start, end + 1):
        result = number * i
        text = f"{number} * {i} = {result}"
        listbox.insert(tk.END, text)

root = tk.Tk()
root.title("Таблица умножения")

root.option_add('*Font', 'Arial 13')

label_number = tk.Label(root, text="Введите число:")
label_number.pack()

entry_number = tk.Entry(root)
entry_number.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

label_range = tk.Label(root, text="Введите диапазон множителей:")
label_range.pack()

entry_start = tk.Entry(root)
entry_start.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

entry_end = tk.Entry(root)
entry_end.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

button = tk.Button(root, text="Показать таблицу", command=multiply)
button.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

root.mainloop()