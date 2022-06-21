import telebot 
from telebot import types 

bot = telebot.TeleBot('5322220961:AAHuPg46q7v9hmBGA9DEnrOIOSJn8o0jlJo')
BOT_URL = 'https://shifosuv.herokuapp.com/'

markup = telebot.types.ReplyKeyboardMarkup(True)
markup.row('📦 Mahsulotlar', '🎁 Aksiyalar')
markup.row('📞 Biz bilan bog`lanish', '📢 Bizni kuzatib boring')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Bosh menyu', reply_markup=markup)
      
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '📦 Mahsulotlar' or '💧 Suv' or '🅿️ Pompa' or 'Bosh menyu':
        product_markup = telebot.types.ReplyKeyboardMarkup(True)
        product_markup.row('💧 Suv', '🅿️ Pompa')
        product_markup.row('Bosh menyu')
        if message.text == '📦 Mahsulotlar':
            bot.send_message(message.chat.id, 'Siz mahsulotlar bo`limidasiz', reply_markup = product_markup)
        if message.text == '🅿️ Pompa' or '🚍Buyurtma berish' or 'Bosh menyu':
            p_markup = telebot.types.ReplyKeyboardMarkup(True)
            p_markup.row('🚍Buyurtma berish')
            p_markup.row('Bosh menyu')

            if message.text == '🅿️ Pompa':
                p = 'AgACAgIAAxkBAAIKXmKsCA7FDKwjS28OBETTWs4NjVgiAAJZwDEbdsZgScLNBahtZn_LAQADAgADcwADJAQ'  #pompa photo_id
                bot.send_photo(message.chat.id, p, "*Elektron pompa* \n\nNarxi: 70000.00 so'm \n\n🔻Mahsulot haqida:\n✅USB quvvatlagich\n✅ Foydalanishga qulay \n✅ Navoiy bo'ylab yetkazib berish bepul.", parse_mode='Markdown', reply_markup = p_markup) 
            elif message.text =='🚍Buyurtma berish' or 'Ortga qaytish':
                po_markup = telebot.types.ReplyKeyboardMarkup(True)
                po_markup.row('Ortga qaytish')
                if message.text == '🚍Buyurtma berish':
                    bot.send_message(message.chat.id, "Mahsulotga buyurtma berish uchun iltimos biz bilan bog'laning >>>  @Shifosuvuz", reply_markup = po_markup) 
                elif message.text == 'Ortga qaytish':
                    bot.send_message(message.chat.id, 'Mahsulotni tanlang', reply_markup = product_markup)

        if message.text == '💧 Suv' or '🚖Buyurtma berish' or 'Bosh menyu':
            suv_markup = telebot.types.ReplyKeyboardMarkup(True)
            suv_markup.row('🚖Buyurtma berish')
            suv_markup.row('Bosh menyu')
            if message.text == '💧 Suv':
                s = 'AgACAgIAAxkBAAIKYGKsCbY_tvwWHQtbPRU-HGUqk-grAAJawDEbdsZgScMW9g7oj0yvAQADAgADcwADJAQ'    # suv photo_id
                bot.send_photo(message.chat.id, s, "*Shifo Suv - 18.9 L* \n\nNarxi: 10 000 so'm \n\n🔻Mahsulot haqida:\n\n💧🕋 Artezian suvi 7 qirrali maxsus filtrda koreya texnologiyasi asosida o'n ikki bosqichli maxsus filtrda tozalanib, qo'shimcha ravishda minerallashtiriladi. Minerallashtirish jarayonida inson tanasi uchun zarur bo'lgan kalsiy, ftor, yod, kaliy, magniy, natriy bilan suv tarkibi boyitiladi. Bundan tashqari, shifo suv artezian suvi filtrlardan o'tkazilib tayyor ichimlik suv holiga kelgach,  muqaddas Makka shahridan keltirilgan 'Zam-zam' suvi qo'shiladi.\n\n🚚 Navoiy bo'ylab yetkazib berish bepul.", parse_mode='Markdown', reply_markup = suv_markup) 
            elif message.text =='🚖Buyurtma berish' or 'Ortga qaytish':
                order_markup = telebot.types.ReplyKeyboardMarkup(True)
                order_markup.row('◀️Ortga qaytish')
                if message.text == '🚖Buyurtma berish':
                    bot.send_message(message.chat.id, "Mahsulotga buyurtma berish uchun iltimos biz bilan bog'laning >>> @Shifosuvuz", reply_markup = order_markup) 
                elif message.text == '◀️Ortga qaytish':
                    bot.send_message(message.chat.id, 'Mahsulotni tanlang', reply_markup = product_markup)
            elif message.text == 'Bosh menyu':
                bot.send_message(message.chat.id, 'Bosh menyu', reply_markup = markup) 

        if message.text == 'Bosh menyu':
            bot.send_message(message.chat.id, 'Bosh menyu', reply_markup = markup)

    if message.text == '📞 Biz bilan bog`lanish':
        bot.send_message(message.chat.id, 'Kontaktlar:\n+998930351011\n+998992851011\n\nSizga yordam berishdan doim mamnunmiz)', reply_markup = markup)

    if message.text == '📢 Bizni kuzatib boring':
        bot.send_message(message.chat.id, 'Instagram: shifosuv\nFacebook: shifosuv uz\nWebsite: shifosuv.uz', reply_markup = markup)

    if message.text == '🎁 Aksiyalar':
        bot.send_message(message.chat.id, "✔️ Boshlang'ich to'lov(zalog) so'ralmaydi\n✔️ Yetkazib berish bepul", reply_markup = markup)


bot.polling()    











# # bosh menyuga qaytishni bosganda avtomaticeski start 
# # bosilsin
