# (5) Write a Python program to analyze and process weather data for New York City from 1st August to 10th July in 2024.
# a. Each day’s data includes:
# o Date
# o Maximum temperature (in Celsius)
# o Minimum temperature (in Celsius)
# o Humidity (in percentage)
# (Hint: Store the data in a list of dictionaries.)
# b. Write a function to find the highest and lowest temperatures recorded during the week.
# c. Write a function to determine the number of days with temperatures above 30°C.
# d. Write a function to compute the average humidity over the specified period.

weather_data = [
    {'date': '2024-08-01', 'max_temp': 30, 'min_temp': 22, 'humidity': 60},
    {'date': '2024-08-02', 'max_temp': 31, 'min_temp': 23, 'humidity': 62},
    {'date': '2024-08-03', 'max_temp': 32, 'min_temp': 24, 'humidity': 63},
    {'date': '2024-08-04', 'max_temp': 33, 'min_temp': 25, 'humidity': 65},
    {'date': '2024-08-05', 'max_temp': 34, 'min_temp': 26, 'humidity': 66},
    {'date': '2024-08-06', 'max_temp': 35, 'min_temp': 27, 'humidity': 68},
    {'date': '2024-08-07', 'max_temp': 36, 'min_temp': 28, 'humidity': 70},
    {'date': '2024-08-08', 'max_temp': 37, 'min_temp': 29, 'humidity': 72},
    {'date': '2024-08-09', 'max_temp': 38, 'min_temp': 30, 'humidity': 74},
    {'date': '2024-08-10', 'max_temp': 39, 'min_temp': 31, 'humidity': 76}

]

def find_high_low_temperatures(data):
    max_temp = max(data, key=lambda x: x['max_temp'])
    min_temp = min(data, key=lambda x: x['min_temp'])
    return max_temp['max_temp'], min_temp['min_temp']

def count_days_above_30(data):
    count = sum(1 for day in data if day['max_temp'] > 30)
    return count

def average_humidity(data):
    total_humidity = sum(day['humidity'] for day in data)
    average_humidity = total_humidity / len(data)
    return average_humidity

if __name__ == "__main__":
    max_temp, min_temp = find_high_low_temperatures(weather_data)
    print(f"Highest temperature recorded: {max_temp}°C")
    print(f"Lowest temperature recorded: {min_temp}°C")

    days_above_30 = count_days_above_30(weather_data)
    print(f"Number of days with temperatures above 30°C: {days_above_30}")

    average_humidity = average_humidity(weather_data)
    print(f"Average humidity over the period: {average_humidity:.2f}%")
