


# Конвертация в 24-часовой формат
from datetime import datetime

input_time_list = ['8/20/2020 4:17:05 PM', '01.05.2021 14:22']
for input_time in input_time_list:
    if "AM" in input_time or "PM" in input_time:
        converted_time = datetime.strptime(input_time, "%m/%d/%Y %I:%M:%S %p").strftime("%Y-%d-%m %H:%M:%S")
        print(converted_time)
        print(type(converted_time))
    else:
        converted_time = datetime.strptime(input_time, "%d.%m.%Y %H:%M").strftime("%Y-%d-%m %H:%M:%S")
        print(converted_time)
        print(type(converted_time))
