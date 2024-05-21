import tkinter as tk
from tkinter import ttk
from pyowm import OWM
from pyowm.utils.config import get_default_config

def get_weather():
    config_dict = get_default_config()
    config_dict['language'] = 'ru'

    owm = OWM('d13b1a2d35086b5bea7f3cc2879413c2')
    mgr = owm.weather_manager()

    place = entry_city.get()
    country = entry_country.get()
    country_and_place = place + ", " + country

    try:
        observation = mgr.weather_at_place(country_and_place)
        w = observation.weather

        status = w.detailed_status
        wind = w.wind()['speed']
        humidity = w.humidity
        temp = w.temperature('celsius')['temp']

        result_label.config(text="В городе " + place + " сейчас " + status + "\nТемпература " + str(round(temp)) + " градусов по Цельсию" + "\nВлажность составляет " + str(humidity) + "%" + "\nСкорость ветра " + str(wind) + " метров в секунду")

    except Exception as e:
        result_label.config(text="Произошла ошибка: " + str(e))

root = tk.Tk()
root.title("Погода")
root.geometry("400x300")

style = ttk.Style()
style.configure('TButton', font=('calibri', 12, 'bold'), foreground='blue')
style.configure('TLabel', font=('calibri', 12), foreground='black')

label_city = ttk.Label(root, text="Введите ваш город:")
label_city.pack(pady=10)

entry_city = ttk.Entry(root, font=('calibri', 12))
entry_city.pack(pady=5)

label_country = ttk.Label(root, text="Введите код вашей страны:")
label_country.pack(pady=10)

entry_country = ttk.Entry(root, font=('calibri', 12))
entry_country.pack(pady=5)

button = ttk.Button(root, text="Получить погоду", command=get_weather)
button.pack(pady=20)

result_label = ttk.Label(root, text="", wraplength=380)
result_label.pack(pady=20)

root.mainloop()
