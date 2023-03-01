import subprocess
import chardet


def ping(addres):
    ARGS = ['ping', addres]
    YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
    for line in YA_PING.stdout:
        res = chardet.detect(line)
        print(line.decode(res['encoding']))


ping("yandex.ru")
ping("youtube.com")
