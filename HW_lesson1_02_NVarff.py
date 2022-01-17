#2. Пользователь вводит время в секундах.
# ереведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input('введите произвольное время в секундах'))
hours = time_in_seconds//3600
print('количество часов', hours)
minutes = (time_in_seconds - hours*3600)//60
print('количество минут',minutes)
seconds = (time_in_seconds-hours*3600-minutes*60)
print('количество секунд',seconds)
print(f"{hours}:{minutes}:{seconds}")
