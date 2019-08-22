import json
import time
import random
import urllib.request

# статические данные о аккаунте и твитче
host = "irc.chat.twitch.tv"
port = 6667
bot_username = "bot_name"
oauth_token = "oauth:oauth_token"
channel_name = "channel_name"
moderator_list = {}
# подключение к чату твитча
def connection(socket):
    socket.connect((host, port))
    socket.send("PASS {}\r\n".format(oauth_token).encode())
    socket.send("NICK {}\r\n".format(bot_username).encode())
    socket.send("JOIN #{}\r\n".format(channel_name).encode())
# заполнение и обновление списка "особенных" пользователей
def fill_moderator_list():
    while True:
        try:
            url = "http://tmi.twitch.tv/group/user/" + channel_name + "/chatters"
            req = urllib.request.Request(url, headers={"accept": "*/*"})
            res = urllib.request.urlopen(req).read()
            if res.find("502 bad gateway".encode()) == -1:
                data = json.loads(res)
                moderator_list.clear()
                for user in data["chatters"]["broadcaster"]:
                    moderator_list[user] = "broadcaster"
                for user in data["chatters"]["moderators"]:
                    moderator_list[user] = "moderator"
                for user in data["chatters"]["global_mods"]:
                    moderator_list[user] = "global_mod"
                for user in data["chatters"]["admins"]:
                    moderator_list[user] = "admin"
                for user in data["chatters"]["staff"]:
                    moderator_list[user] = "staff"
        except Exception:
            print("Moderator list update error")
        time.sleep(10)
# проверка на число и преобразование в него
def intTryParse(string):
    try:
        return int(string), True
    except ValueError:
        return string, False
# проверка на возможные комманды
def check_command(sock, username, msg):
    if username in moderator_list:
        if msg[:4] == "!msg":
            message(sock, msg[5:])
        elif msg[:5] == "!roll":
            if len(msg) == 5:
                roll(sock, username)
            elif intTryParse(msg[6:])[1] == True:
                user_roll(sock, username, intTryParse(msg[6:])[0])   
            elif intTryParse(msg[6:])[1] == False:
                message(sock, "Роллить можно только числа")
    else:
        if msg[:4] == "!msg":
            message(sock, "У вас нет таких прав в этом чате")
# отправка сообщения в чат
def message(socket, msg):
    socket.send("PRIVMSG #{} : {}\r\n".format(channel_name, msg).encode())
# произвольный ролл
def user_roll(socket, user, msg):
    message(socket, "{} roll {}".format(user, random.randint(1, msg)))
# ролл
def roll(socket, user):
    message(socket, "{} roll {}".format(user, random.randint(1, 100)))