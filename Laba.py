import tkinter as tk
from tkinter import Label, ttk
from tkinter import messagebox
import Datas


#Создание окна
root = tk.Tk()
root.title("Кальулятор мебели")

#Вызов функций хранения параметров
Datas.Variables()
Datas.Sizes()
Datas.PriceList()

#Кнопка для расчета
Result_btn = ttk.Button(root, text = "Рассчитать")
Result_btn.grid(row=5, columnspan=2)

#результат
global result_label
result_label = ttk.Label(root,text="Себестоимость: 0 рублей")
result_label.grid(row=6,columnspan=2)

#кнопка выхода
exit_button = ttk.Button(root,text = "Выход",command=root.quit)
exit_button.grid(row=7,columnspan=2)

root.mainloop()