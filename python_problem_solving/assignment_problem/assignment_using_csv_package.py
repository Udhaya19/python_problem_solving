import csv
import datetime
from collections import Counter

store_name = []
build_area = []
date_of_opening = []
store_pin_code = []
location_pin_code = []
city_name = []
country_name = []


def store_list():
    with open('/home/udhaya/Downloads/store.csv', 'r') as store:
        reader = csv.reader(store)
        for row in reader:
            store_name.append(row[0])
            date_of_opening.append((row[2]))
            store_pin_code.append(row[3])
            build_area.append(row[1])

    store.close()


store_list()


def location_list():
    with open('/home/udhaya/Downloads/location.csv', 'r') as location:
        reader = csv.reader(location)
        for row in reader:
            location_pin_code.append(row[0])
            city_name.append(row[1])
            country_name.append(row[2])
    location.close()


location_list()


def remove_names_list():
    store_name.pop(0)
    build_area.pop(0)
    date_of_opening.pop(0)
    store_pin_code.pop(0)
    location_pin_code.pop(0)
    city_name.pop(0)
    country_name.pop(0)


remove_names_list()

build_area_list = list(map(float, build_area))


def stores_greater_than_4000():
    build_area_list = list(map(float, build_area))
    list_store = dict(zip(store_name, build_area_list))
    final_store_name = []

    for key, value in list_store.items():
        if value > 4000:
            final_store_name.append(key)
    print(final_store_name)


stores_greater_than_4000()


def total_build_area_last_year():
    now = datetime.datetime.now()
    current_year = now.year
    previous_year = current_year - 1
    previous_year = str(previous_year)
    previous_year = previous_year[-2:]

    date_of_openning = []
    date_and_area = dict(zip(date_of_opening, build_area_list))

    for key, value in date_and_area.items():
        month, day, year = (int(x) for x in key.split('/'))
        year = str(year)
        year = year[-2:]
        if previous_year == year:
            date_of_openning.append(value)
    print(date_of_openning)
    for values in range(0, len(date_of_openning)):
        total_build_area = sum(date_of_openning)
    print(total_build_area)


total_build_area_last_year()


def store_opened_weekend():
    weekend_day1 = 'Saturday'
    weekend_day2 = 'Sunday'
    store_and_date = dict(zip(store_name, date_of_opening))
    build_area_dict = {}
    store_weekend_opened = []
    for key, value in store_and_date.items():
        month, day, year = (int(x) for x in value.split('/'))
        if year == 00:
            year = 2000
            ans = datetime.date(year, month, day)
            value_type = ans.strftime("%A")
            build_area_dict[key] = value_type
        else:
            ans = datetime.date(year, month, day)
            value_type = ans.strftime("%A")
            build_area_dict[key] = value_type
    for key, value in build_area_dict.items():
        if weekend_day1 in value or weekend_day2 in value:
            store_weekend_opened.append(key)

    print(store_weekend_opened)


store_opened_weekend()


def city_contain_z_character():
    s1 = 'z'
    s2 = 'Z'
    character_city_list = []
    store_name_and_pincode = dict(zip(store_pin_code, store_name))
    pincode_and_city = dict(zip(location_pin_code, city_name))
    result_store = []
    for key, value in pincode_and_city.items():
        if s1 in value or s2 in value:
            character_city_list.append(key)

    for row, column in store_name_and_pincode.items():
        for number in range(len(character_city_list)):
            if row == character_city_list[number]:
                result_store.append(column)
    print(result_store)


city_contain_z_character()


def store_number_city():
    location_code_and_city = dict(zip(location_pin_code, city_name))
    pin_code = Counter(store_pin_code)
    code_count = dict(pin_code)
    final_store_count = {}
    for key, value in location_code_and_city.items():
        for row, column in code_count.items():
            if key == row:
                final_store_count[value] = column
    print(final_store_count)


store_number_city()


def number_stores():
    i = 0
    store_pin = Counter(store_pin_code)
    store_count = dict(store_pin)
    most_number_stores(i, store_count)


def most_number_stores(i, store_count):
    store_value = dict(zip(location_pin_code, city_name))
    # # store_value={"pin code":"city name"}
    maximum_number_list = []
    # maximum_number_list=[count of store]
    high_value = []
    # high_value=[pin code of maximum number]
    country_list = []
    for row, column in store_count.items():
        maximum_number_list.append(column)
    maximum_number_list = sorted(maximum_number_list, reverse=True)
    # maximum_number_list=[reversed number count of store]
    for row, column in store_count.items():
        if column == maximum_number_list[i]:
            high_value.append(row)
    for key, value in store_value.items():
        if key in high_value:
            country_list.append(value)
    if len(country_list) == 0:
        i = i + 1
        most_number_stores(i, store_count)
    else:
        print(country_list)


number_stores()
