import socket
import re
from _thread import start_new_thread
import utils

def main():
    # установка соединения
    sock = socket.socket()
    utils.connection(sock)
    # проверка списка модераторов
    start_new_thread(utils.fill_moderator_list, ())
    # установка пформы для прообразования сообщений из чата
    chat_message = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    # пропуск приветствия Твитча
    while True:
        res = str(sock.recv(1024))
        if "End of /NAMES list" in res:
            break
    # основной цикл работы с переадресовкой на вызванные функции
    while True:
        # получение сообщения из чата
        try:
            res = sock.recv(1024).decode()
        except Exception:
            print("Can't recive message")
        # проверка сообщения на пинг
        if res == "PING :tmi.twitch.tv\r\n":
            sock.send("POND :tmi.twitch.tv\r\n".encode())
        # обработка всех остальных сообщений кроме пинга
        else:
            try:
                username = re.search(r"\w+", res).group(0)
                message = chat_message.sub("", res)
                message = message.strip()
                utils.check_command(sock, username, message)
            except Exception as msg:
                print("#ERROR", msg)

if __name__ == "__main__":
    main()