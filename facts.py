import wikipedia

def get_city_info(city):
    try:
        wikipedia.set_lang("ru")
        city_page = wikipedia.page(city)
        first_paragraph = city_page.summary.split('\n')[0]  # Получаем первый абзац информации
        return first_paragraph
    except wikipedia.exceptions.PageError:
        return f"Информация о городе {city} не найдена на Википедии."

request = input("Введите название города: ")
city_info = get_city_info(request)

print(f"Информация о {request}:")
print(city_info)


