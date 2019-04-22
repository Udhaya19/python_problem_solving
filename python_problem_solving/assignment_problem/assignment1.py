import datetime

import pandas

store = pandas.read_csv('/home/udhaya/Downloads/store.csv')
location = pandas.read_csv('/home/udhaya/Downloads/location.csv')


def stores_greater_than_4000():
    for key, row in store.iterrows():
        if row[1] > 4000:
            print("{}=={}".format(row[0], row[1]))


stores_greater_than_4000()


def number_stores():
    i = 0
    store_count = {}
    store_ = []

    for key, value in store.iterrows():
        store_.append(value[3])
    for pin_number in store_:
        store_count[pin_number] = store_.count(pin_number)
    most_number_stores(i, store_count)


def most_number_stores(i, store_count):
    store_value = {}
    maximum_number_list = []
    high_value = []
    country_list = []
    for row, column in store_count.items():
        maximum_number_list.append(column)
    maximum_number_list = sorted(maximum_number_list, reverse=True)
    for row, column in store_count.items():
        if column == maximum_number_list[i]:
            high_value.append(row)
    for key, value in location.iterrows():
        store_value[value[0]] = value[1]
    for key, value in store_value.items():
        if key in high_value:
            country_list.append(value)
    if len(country_list) == 0:
        i = i + 1
        most_number_stores(i, store_count)
    else:
        print(country_list)


number_stores()


def total_build_area_last_year():
    now = datetime.datetime.now()
    current_year = now.year
    previous_year = current_year - 1
    previous_year = str(previous_year)
    previous_year = previous_year[-2:]

    date_of_openning = []
    for key, value in store.iterrows():
        date_value = value[2]
        month, day, year = (int(x) for x in date_value.split('/'))
        year = str(year)
        year = year[-2:]
        if previous_year == year:
            date_of_openning.append(value[1])
    print(date_of_openning)
    for values in range(0, len(date_of_openning)):
        total_build_area = sum(date_of_openning)
    print(total_build_area)


total_build_area_last_year()


def store_opened_weekend():
    weekend_day1 = 'Saturday'
    weekend_day2 = 'Sunday'
    build_area_dict = {}
    store_weekend_opened = []
    for key, value in store.iterrows():
        date_value = value[2]
        month, day, year = (int(x) for x in date_value.split('/'))
        if year == 00:
            year = 2000
            ans = datetime.date(year, month, day)
            value_type = ans.strftime("%A")
            build_area_dict[value[0]] = value_type
        else:
            ans = datetime.date(year, month, day)
            value_type = ans.strftime("%A")
            build_area_dict[value[0]] = value_type
    for key, value in build_area_dict.items():
        if weekend_day1 in value or weekend_day2 in value:
            store_weekend_opened.append(key)

    print(store_weekend_opened)


store_opened_weekend()


def city_contain_z_character():
    city_contain_z = []
    s1 = 'z'
    s2 = 'Z'
    character = []
    pin_code = []
    result_store_list = []
    for key, value in location.iterrows():
        city_contain_z.append(value[1])
    for i in range(0, len(city_contain_z)):
        if s1 in city_contain_z[i] or s2 in city_contain_z[i]:
            character.append(city_contain_z[i])
    for key, value in location.iterrows():
        for row in range(0, len(character)):
            if character[row] == value[1]:
                pin_code.append(value[0])
    for key, value in store.iterrows():
        for row in range(0, len(pin_code)):
            if pin_code[row] == value[3]:
                result_store_list.append(value[0])
    print(result_store_list)


city_contain_z_character()


def store_number_city():
    pin_number = []
    pin_code_occurence = {}
    city_name = {}
    final_store_count = {}
    for key, value in store.iterrows():
        pin_number.append(value[3])
    for pin_code in pin_number:
        pin_code_occurence[pin_code] = pin_number.count(pin_code)
    for key, value in location.iterrows():
        city_name[value[0]] = value[1]
    for key, value in pin_code_occurence.items():
        for row, column in city_name.items():
            if key == row:
                final_store_count[column] = value

    print(final_store_count)


store_number_city()
