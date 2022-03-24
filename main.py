# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:

seconds = int(input('введите секунды: '))
day = seconds // 86400
hour = (seconds // 3600) % 24
minutes = (seconds // 60) % 60
sec = seconds % 60
print(day, 'дн', hour, 'час', min, 'мин', sec, 'сек')