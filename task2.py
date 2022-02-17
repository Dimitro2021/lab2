""" Task """

import json

def opening(path: str):
    """ Open .json file
    >>> opening('nesto.json')
    noo
    """
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except:
        print('noo')

def running(data: list or dict, prev_data: list):
    """ 
    Use to run in already python object """
    # print(f'data = {data}, previous_data = {prev_data}')
    if isinstance(data, dict):
        print(f'length of the dict is {len(data)}')
        print(f'here are the keys:')
        print('      '.join(list(data.keys())))
        keey = input('Choose one or type "back"  ')
        if keey in data.keys():
            prev_data.append(data)
            running(data[keey], prev_data)
        elif keey == "back":
            if prev_data == []:
                print('START')
                running(data, prev_data)
            else:
                new = prev_data.pop(-1)
                running(new, prev_data)
        elif keey != 'exit':
            running(data, prev_data)
        else:
            exit
    elif isinstance(data, list):
        print(f'length of the list is {len(data)}')
        flag = input("this is list, it may be long, if you wont to see it, write 'yes'  ")
        if flag == 'yes':
            for indx in range(len(data)):
                print(indx, data[indx])
        index = input(f'print the indexes in the range 0-{len(data)-1} or "back" to move back  ')
        if index in [str(num) for num in range(len(data))]:
            prev_data.append(data)
            running(data[int(index)], prev_data)
        elif index == "back":
            if prev_data == []:
                print('START')
                running(data, prev_data)
            else:
                new = prev_data.pop(-1)
                running(new, prev_data)
        elif index != 'exit':
            running(data, prev_data)
        else:
            exit()
    else:
        rsp = input(f'We have come to this {data}\nTo move back write "back" else exit  ')
        if rsp == "back":
            if prev_data == []:
                print('You are at the start')
            else:
                new = prev_data.pop(-1)
                running(new, prev_data)
        exit()

    if 'exit' == rsp:
        exit()

def main(patz):
    running(opening(patz), [])

if __name__ == '__main__':
    patz = input('Your path: ')
    main(patz)
