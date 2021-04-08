duration = int(input("Введите время: "))
if duration <= 60:
    print(f"Время: {duration} сек.")
elif (duration // 60)<60:
    print(f"Время: {duration//60} мин., {duration%60} сек.")
elif (duration // 3600)<24:
    print(f"Время: {duration//3600} час., {duration%3600//60} мин., {duration%60} сек.")
elif (duration // 86400)<30:
    print(f"Время: {duration//86400} дней, {duration%86400//3600} час., {duration%3600//60} мин., {duration%60} сек.")
elif (duration // 2592000)<12:
    print(f"Время: {duration//2592000} месяц., {duration%2592000//86400} дней, {duration%86400//3600} час., {duration%3600//60} мин., {duration%60} сек.")
else:
    print(f"Время: {duration//31104000} год., {duration%31104000//2592000} месяц., {duration % 2592000//86400} дней, {duration% 86400//3600} час., {duration%3600//60} мин., {duration%60} сек.")
