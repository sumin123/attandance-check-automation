def update_score(data, content):
    lines = content.split('\n')
    for line in lines:
        words = line.split(' ')
        if (words[0] == '출석'):
            update_state(data, words, score=1, history='o', fine=0)
        elif (words[0] == '통보'):
            update_state(data, words, score=0.5, history='-', fine=0)
        elif (words[0] == '결석'):
            update_state(data, words, score=0, history='x', fine=2)
    return data

def update_state(data, words, score, history, fine):
    for name in words[2:]:
        data.setdefault(name, {'점수': 0, '출결현황':'', '잔금': -1, '벌금':0 })
        data[name]['점수'] += score
        data[name]['출결현황'] += history
        data[name]['벌금'] += fine