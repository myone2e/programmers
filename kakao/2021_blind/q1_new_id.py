new_id = "...!@BaT#*..y.abcdefghijklm"
def solution(new_id):
    # step1
    new_id = new_id.lower()
    # step2
    for n in new_id:
        if not n.isalnum() and n not in ['_','-','.']:
            new_id = new_id.replace(n, '')
    # step3
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    # step4
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    # step5
    if new_id =='':
        new_id = 'a'
    # step6
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    # step7
    while len(new_id) <= 2:
        last = new_id[-1]
        new_id = new_id + last

    return new_id