import telebot


bot = telebot.TeleBot('6109199376:AAFvDq_SPBjg2pXyr9EXZAKF-XqrzuKHTJk')


def send_message(message):
    with open('subscribers.txt') as f:
        subscribers = f.read().splitlines()
    for subscriber in subscribers:
        bot.send_message(chat_id=subscriber, text=message)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text.lower()
    if user_message == 'subscribe':
        with open('subscribers.txt', 'a') as f:
            f.write(f'{message.chat.id}\n')
        bot.send_message(
            message.chat.id, "You have been subscribed! Be ready to receive some spam!")
    elif "hello" in user_message:
        bot.send_message(message.chat.id, "Hi there!")
    elif "goodbye" in user_message:
        bot.send_message(message.chat.id, "Goodbye!")
    else:
        bot.send_message(
            message.chat.id, "I'm sorry, I didn't understand what you said.")


if __name__ == '__main__':
    bot.polling()
