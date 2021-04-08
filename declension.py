percent = int(input("Введите колличество процентов от 1 до 20: "))
percent_options = ["процентов", "проент", "процента"]
elem = 0
if percent == 1: elem = 1
elif 1 < percent < 5: elem = 2
print(percent, percent_options[elem])