import datetime
import json
import os
import sys

from telethon import TelegramClient
from telethon.tl.types import Channel, Message

path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
print('Loading config from: {}'.format(path))
with open(path, 'r') as fp:
    data = fp.read()
cfg = json.loads(data)

client = TelegramClient(cfg['session_name'], cfg['api_id'], cfg['api_hash'])
client.connect()


def login():
    result = client.send_code_request(cfg['phone_number'])
    print('phone_code_hash (use it for --signin): {}'
          .format(result.phone_code_hash))


def signin(code, phone_code_hash):
    client.sign_in(cfg['phone_number'], code, phone_code_hash=phone_code_hash)


def getme():
    print(client.get_me())


def test():
    date = datetime.datetime.utcnow()
    client.send_message('resurtm',
                        'Testing message from MessageWiperNG: {}'.format(date))


def wipe():
    # todo: don't fetch all the 1000 dialogs at once, make something more wise here
    dialogs, dialog = client.get_dialogs(1000)[1], None
    for dlg in dialogs:
        if type(dlg) is not Channel or dlg.id != cfg['mega_group_id']:
            continue
        dialog = dlg
        break
    if dialog is None:
        raise RuntimeError('Cannot find needed dialog')

    # todo: don't fetch all the 1000 messages at once, make something more wise here
    _, messages, _ = client.get_message_history(dialog, limit=1000,
                                                min_id=cfg['from_message_id'])
    for message in messages:
        if type(message) is not Message:
            continue
        client.delete_messages(dialog, [message.id])

    client.send_message(dialog, cfg['afterward_message'])


if len(sys.argv) == 2 and sys.argv[1] == '--login':
    login()
elif len(sys.argv) == 4 and sys.argv[1] == '--signin':
    signin(int(sys.argv[2]), str(sys.argv[3]))
elif len(sys.argv) == 2 and sys.argv[1] == '--test':
    test()
elif len(sys.argv) == 2 and sys.argv[1] == '--getme':
    getme()
elif len(sys.argv) == 2 and sys.argv[1] == '--wipe':
    wipe()
else:
    print('Nothing to do')
