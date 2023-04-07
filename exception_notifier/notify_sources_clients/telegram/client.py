import requests

from exception_notifier.config import settings


def notify_to_telegram(message: str, bot_token: str = None, chat_id: str = None):
    """send message with telegram bot to specific chat"""

    bot_token = settings.BOT_TOKEN if bot_token is None else bot_token
    chat_id = settings.CHAT_ID if chat_id is None else chat_id

    telegram_bot_link = f'https://api.telegram.org/bot{bot_token}/sendMessage?' \
                        f'chat_id={chat_id}&' \
                        f'text={message}&' \
                        f'parse_mode=markdown'
    requests.get(telegram_bot_link)
