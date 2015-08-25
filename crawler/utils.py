# coding: utf-8

import datetime


def clear_list(data):
    return [item.strip() for item in data]


def convert_to_datetime(date):
    return datetime.datetime.strptime(date, '%Y%m%d')
