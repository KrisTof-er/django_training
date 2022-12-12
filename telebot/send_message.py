import requests
from .models import TeleSettings


def send_telegram_message(tg_name, tg_phone):
    if not TeleSettings.objects.get(pk=1):
        return
    settings = TeleSettings.objects.get(pk=1)
    token = f'{settings.tg_token}'
    chat_id = str(settings.tg_chat)
    text = ''.join(settings.tg_message)
    api = 'https://api.telegram.org/bot'
    method = f'{api}{token}/sendMessage'

    if text.find('{') and text.find('}')+1 and text.rfind('{') and text.rfind('}'):
        part_1 = text[:text.find('{')]
        part_2 = text[text.find('}')+1:text.rfind('{')]
        part_3 = text[text.rfind('}'):-1]

        text_slice = f'{part_1}{tg_name}{part_2}{tg_phone}{part_3}'
    else:
        text_slice = text

    try:
        req = requests.post(method, data={
            'chat_id': chat_id,
            'text': text_slice
        })
    except Exception:
        pass
    finally:
        if req.status_code == 200:
            print("OK")
        elif req.status_code == 500:
            print("ERROR 500")
        else:
            print("!!!Sending ERROR!!!")
