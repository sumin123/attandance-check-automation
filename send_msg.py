from time import sleep
import win32con
import win32api
import win32gui

def kakao_sendtext(chatroom_name, text):

    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)



def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


def open_chatroom(chatroom_name):

    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)


    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    sleep(1)
    SendReturn(hwndkakao_edit3)
    sleep(1)

def make_msg(data):
    msg = '이름\t점수\t출결\n'
    rows = []
    for key, value in data.items():
        rows.append(key + '\t' + str(value['점수']) + '\t' + str(value['출결현황']))
    msg += '\n'.join(rows)
    return msg

def make_settlement_msg(data):
    msg = '이름\t점수\t보증금\t벌금\t잔금\n'
    rows = []
    sorted_data = sorted(data.items(), key=lambda x: x[1]['점수'], reverse=True)
    for key, value in sorted_data:
        rows.append(key + '\t' + str(value['점수']) + '\t' + str(value['잔금']) + '\t' + str(value['벌금']) + '\t' + str(value['잔금']-value['벌금']))
    msg += '\n'.join(rows)
    return msg