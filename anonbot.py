import telebot
bot = telebot.TeleBot('7938901294:AAFqfuxf18hU9cstRrt0CfUaoH1sXbSKnno')

@bot.message_handler(commands=['start'])



def main(message):
    bot.send_message(message.chat.id, 'Напиши сюда сообщение, которое хотел бы отослать Ивану 📩💌✉️')

    



@bot.message_handler(content_types = ['text'])
def anon(message):
    bot.send_message(1998656773, f'Получено новое анонимное сообщение:\n\n {message.text} \n\n Отправить свое анонимное сообщение можно через бота 🤖🤖 🤖🤖 @ivan68anon_bot')
    bot.send_message(1998656773, f'Это сообщение от {message.from_user.username}, {message.from_user.first_name}')
    bot.reply_to(message, 'Ваше сообщение успешно отправлено. Ожидайте ответа в канале 🥰😏🙃😁')

@bot.message_handler(content_types = ["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"])
def video(message):
    bot.send_message(message.chat.id, 'Вы ввели не текст!!!!')


    
bot.infinity_polling()
