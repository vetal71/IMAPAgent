"""
Алгоритм работы
1. Соединение с сервером по протоколу IMAP
2. Авторизация
3. Получение списка папок с сервера
4. Парсинг списка 
5. Декодирование наименований папок

"""



from imaplib import IMAP4_SSL
from pprint import pprint

long = int  # long is just int in python3

HOST = 'mail01.hoster.by'
USERNAME = 'postmaster@sarmont.by'
PASSWORD = 'hHTAUOOp6486451'

server = IMAP4_SSL(HOST)
server.login(USERNAME, PASSWORD)

(typ, folder_data) = server.list()
pprint(folder_data)
"""
folder_data = [item for item in folder_data if item not in ('', None)]

ret = []
parsed = parse_response(folder_data)
while parsed:
    # TODO: could be more efficient
    flags, delim, name = parsed[:3]
    parsed = parsed[3:]

    if isinstance(name, (int, long)):
        # Some IMAP implementations return integer folder names
        # with quotes. These get parsed to ints so convert them
        # back to strings.
        name = str(name)   

    ret.append((flags, delim, name))

pprint(ret)
"""