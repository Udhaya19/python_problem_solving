import requests as req
import json
import time
import xmltodict as xml


def quote_print():
    with open("config.json") as config:
        config_file = json.load(config)
    while True:
        lang = config_file['lang']
        format = config_file['format']
        delay = config_file['delay']
        delay = delay.split(" ")
        for value in range(len(delay)):
            value_store = delay[value][-2:]
            time_split = int(delay[value][:-2])
            if value_store == "yr":
                change_year = time_split * 365 * 24 * 60 * 60
            if value_store == "mt":
                change_month = time_split * 24 * 60 * 60
            if value_store == "dy":
                change_day = time_split * 60 * 60
            if value_store == "mi":
                change_minute = time_split * 60
            if value_store == "se":
                seconds = time_split
        delay = change_year + change_month + change_day + change_minute + seconds

        if lang == "en" or lang == "ru":
            if format == "json":
                extracting_details_using_json(lang, format, delay)
            else:
                extracting_details_using_xml(lang, format, delay)
        else:
            lang = "en"
            if format == "json":
                extracting_details_using_json(lang, format, delay)
            else:
                extracting_details_using_xml(lang, format, delay)


def extracting_details_using_json(lang, format, delay):
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=" + lang + "&format=" + format
    res = req.get(url)
    if lang == "ru":
        quote_dictionary = json.loads(res.text)
    if lang == "en":
        quote_dictionary = json.loads(bytes(res.text, "utf-8").decode("unicode_escape"))
    author_name = quote_dictionary['quoteAuthor']
    author_quote = quote_dictionary['quoteText']
    if author_name == '':
        author_name = "Unknown"
        print(author_name, "says", author_quote)
    else:
        print(author_name, "says", author_quote)
    time.sleep(delay)


def extracting_details_using_xml(lang, format, delay):
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=" + lang + "&format=" + format
    res = req.get(url)
    quote_xml = json.loads(json.dumps((xml.parse(res.text))))
    if quote_xml['forismatic']['quote']['quoteAuthor'] == None:
        quote_xml['forismatic']['quote']['quoteAuthor'] = "Unknown"
        print(quote_xml['forismatic']['quote']['quoteAuthor'], "says",
              quote_xml['forismatic']['quote']['quoteText'])
    else:
        print(quote_xml['forismatic']['quote']['quoteAuthor'], "says",
              quote_xml['forismatic']['quote']['quoteText'])
    time.sleep(delay)


quote_print()
