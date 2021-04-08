import finnhub
import random

finnhub_client = finnhub.Client(api_key="c1ev9t748v6vvsb4450g")

currency_list = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 
'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 
'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 
'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 
'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 
'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 
'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 
'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 
'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 
'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 
'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 
'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']

def add_digits(num):
        return (num - 1) % 9 + 1 if num > 0 else 0

def reduce_string(string):
    strPrice = ""
    for char in string:
        if char.isdigit():
            strPrice += char
    
    return int(strPrice)

def get_random_digit():
    prandom_currency = currency_list[random.randrange(0, len(currency_list) - 1)]

    base_amount = random.uniform(1.13, 2.09)

    prandom_currency_dict = finnhub_client.forex_rates(base=prandom_currency)
    prandom_currency_rate = prandom_currency_dict['quote'][prandom_currency]
    prandom_currency_rate_1 = prandom_currency_dict['quote'][currency_list[random.randrange(0, len(currency_list) - 1)]]

    conversion_value = base_amount * prandom_currency_rate * prandom_currency_rate_1

    for _ in range(random.randint(4, 10)):
        conversion_value *= prandom_currency_dict['quote'][currency_list[random.randrange(0, len(currency_list) - 1)]]

    random_digit = add_digits(reduce_string(str(conversion_value)))
    return random_digit
