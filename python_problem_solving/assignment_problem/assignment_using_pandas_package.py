import datetime
import pandas
from collections import Counter

store = pandas.read_csv('/home/udhaya/Downloads/store.csv')
location = pandas.read_csv('/home/udhaya/Downloads/location.csv')


# a. List all stores which have ​ build_area ​ greater than 4000

def stores_greater_than_4000():
    for key, row in store.iterrows():
        if row[1] < 4000:
            print("{}=={}".format(row[0], row[1]))


stores_greater_than_4000()


# b. Find ​ country​ having the most number of stores

def number_stores():
    i = 0
    store_ = []
    # store_=[pin_number]
    store_count = {}
    # store_count={"pin_number":count}
    for key, value in store.iterrows():
        store_.append(value[3])
    for pin_number in store_:
        store_count[pin_number] = store_.count(pin_number)
    most_number_stores(i, store_count)


def most_number_stores(i, store_count):
    store_value = {}
    # store_value={"pin code":"city name"}
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


#
# # c. Find the total ​ build_area​ of all stores built last year

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


# # d. Find all stores which were opened on a ​ weekend

def store_opened_weekend():
    weekend_day1 = 'Saturday'
    weekend_day2 = 'Sunday'
    build_area_dict = {}
    # build_area_dict={"storename":"weekdays"}
    store_weekend_opened = []
    # store_weekend_opened=[store_name]
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


#
# # e. List stores which are located in a city containing character `​ z ​ ` in it
#
def city_contain_z_character():
    city_contain_z = []
    # city_contain_z=[city names]
    s1 = 'z'
    s2 = 'Z'
    character = []
    # charater=[only have a z character]
    pin_code = []
    # pin_code=[z character pincode]
    result_store_list = []
    # result_store_list=[store_name city have z character]
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


# f. Calculate ​ number of stores​ in each ​ City

def store_number_city():
    pin_number = []
    # pin_number=[list of pincode]
    pin_code_occurence = {}
    # pin_code_occurence={"pincode":"count of pincode"}
    city_name = {}
    # city_name={"pincode":"city name"}
    final_store_count = {}
    # final_store_count={"city name":"store count"}
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


# g.list the count of store in each country

def country_store_count():
    pin_code = []
    store_name = {}
    country_list = {}
    for key, value in store.iterrows():
        pin_code.append(value[3])
    pin_code_value = Counter(pin_code)
    pin_code_count = dict(pin_code_value)
    # print(pin_code_count)
    for row, column in location.iterrows():
        if column[2] in country_list:
            country_list[column[2]].append(column[0])
        else:
            country_list[column[2]] = [column[0]]
    # print(country_list)
    for key, value in country_list.items():
        current_value = value
        sum_count = 0
        for pin in range(len(current_value)):
            for row, column in pin_code_count.items():
                if current_value[pin] == row:
                    sum_count = sum_count + column
        store_name[key] = sum_count
    print(store_name)
    max_value = [(value, key) for key, value in store_name.items()]
    print(max(max_value)[1])

country_store_count()
