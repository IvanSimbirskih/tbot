import telebot
bot = telebot.TeleBot('7938901294:AAFqfuxf18hU9cstRrt0CfUaoH1sXbSKnno')

@bot.message_handler(commands=['start'])



def main(message):
    bot.send_message(message.chat.id, 'Напиши сюда сообщение, которое хотел бы отослать Ивану 📩💌✉️')

    



@bot.message_handler()
def anon(message):
    bot.send_message(1998656773, f'Получено новое анонимное сообщение:\n\n {message.text} \n\n Отправить свое анонимное сообщение можно через бота 🤖🤖 🤖🤖 @ivan68anon_bot')
    bot.send_message(1998656773, f'Это сообщение от {message.from_user.username}')
    bot.reply_to(message, 'Ваше сообщение успешно отправлено. Ожидайте ответа в канале 🥰😏🙃😁')


bot.infinity_polling
