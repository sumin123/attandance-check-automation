import json
import os
from file_IO_module import *
from send_msg import *
import shutil
import time

def main():
    chat_name = '이수민'
    with open('score.json', 'r', encoding='utf-8') as f:
        scores = json.load(f)
    
    new_score = {}
    for key in scores:
        new_score[key] = {'점수': 0, '출결현황':'', '잔금': -1, '벌금':0}
        new_score[key]['잔금'] = scores[key]['잔금'] - scores[key]['벌금']
    
    msg = make_settlement_msg(scores)
    new_file_name = 'score-' + time.strftime('%Y-%m-%d', time.localtime(time.time()))
    shutil.move('score.json', 'history/' + new_file_name + '.json')


    write_score_file(new_score)

    open_chatroom(chat_name)
    kakao_sendtext(chat_name, msg)
    sleep(1)

if __name__ == '__main__':
    main()