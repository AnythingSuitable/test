from telethon import TelegramClient, sync
import time
import socks

HITS = 0
FAILED = 0
BAL = '0.0 Dogecoin'
proxy_url = "http://proxy.server:3128"
proxy=(socks.SOCKS5, 'proxy.server', 3128)
MSG = '🎁 Bonus'

while True:

    api_id = '3806967'
    api_hash = '84807c26ab61c89db4dca410c8baec2d'
    client = TelegramClient('doge_test', api_id, api_hash,proxy=(socks.HTTP, 'proxy.server',3128))
    client.start()
    client.send_message(entity='Doge_Four_Ever_bot', message=MSG)
    time.sleep(2)
    messages = client.get_messages('Doge_Four_Ever_bot')
    messages[0].click(0)
    time.sleep(2)
    messages = client.get_messages('Doge_Four_Ever_bot')
    client.disconnect()
    message = str(messages[0])
    BAL = str(message.split("message='💳 Your Balance: ")[1].split("',")[0])
    HITS += 1
    print(f'Hits Done : {HITS}, Failed : {FAILED}, Balance : {BAL}', end='\r')
    time.sleep(32)