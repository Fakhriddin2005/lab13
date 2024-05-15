def weather():
 from pyowm import OWM
 from pyowm.utils.config import get_default_config

 config_dict = get_default_config()
 config_dict['language'] = 'ru'

 owm = OWM('d13b1a2d35086b5bea7f3cc2879413c2')
 mgr = owm.weather_manager()

 place = input("Введите ваш город: ")
 country = input("Введите код вашей страны: ")
 country_and_place = place + ", " + country

 observation = mgr.weather_at_place(country_and_place)
 w = observation.weather

 status = w.detailed_status
 wind = w.wind()['speed']
 humidity = w.humidity
 temp = w.temperature('celsius')['temp']


 print("В городе " + place + " сейчас " + status + "\nТемпература " + str(round(temp)) + " градусов по Цельсию" + "\nВлажность составляет " + str(humidity) + "%" + "\nСкорость ветра " + str(wind) + " метров в секунду")

weather()

