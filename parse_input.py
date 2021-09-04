import re
import time

from win32api import TerminateProcess

day_string = {
    '월요일': 0,
    '화요일': 1,
    '수요일': 2,
    '목요일': 3,
    '금요일': 4,
    '토요일': 5,
    '일요일': 6
}

def day_filter_callback(el):
    p = re.compile('2021년')
    m = p.match(el)
    if m:
        return True
    else:
        return False

def get_last_chat_day(chat_list):
    days = filter(day_filter_callback, chat_list)
    days_list = list(days)
    last_day = days_list[-1]
    last_day_index = chat_list.index(last_day)
    last_day_str = day_string[last_day.split(' ')[-1]]
    return last_day_str, last_day_index

def day_check(last_day_str):
    today_str = time.localtime(time.time()).tm_wday
    if last_day_str == today_str:   # 마지막 카톡이 오늘
        return True
    else:
        return False

def get_chat_content(chat):
    p = re.compile(r'출석 ([\s\S]+)')
    m = p.search(chat)
    return m.group()

def is_attandance_callback(chat):
    p = re.compile('출석')
    m = p.search(chat)
    if m:
        return True
    else:
        return False

def get_attandance_chat(splited_chat, last_day_index):
    today_chat_list = splited_chat[last_day_index+1:]
    attandance_chats = list(filter(is_attandance_callback, today_chat_list))
    if len(attandance_chats) == 0:
        return []
    else:
        last_attandance_chat = attandance_chats[-1]
        return last_attandance_chat
    
