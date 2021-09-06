from send_msg import *
from get_command import *
from parse_input import *
from file_IO_module import *
from update_attandance import *

def main():
    chat_name = '출석스터디'
    
    all_chat = copy_chatroom(chat_name)
    splited_chat = all_chat.split('\r\n')
    last_day, last_day_index = get_last_chat_day(splited_chat)

    if day_check(last_day):
        data = read_score_file()
        last_attandance_chat = get_attandance_chat(splited_chat, last_day_index)
        content = get_chat_content(last_attandance_chat)
        data = update_score(data, content)

    write_score_file(data)
    msg = make_msg(data)
    
    open_chatroom(chat_name)
    kakao_sendtext(chat_name, msg)
    sleep(1)

if __name__ == '__main__':
    main()