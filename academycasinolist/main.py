import logging
import schedule
import time
import asyncio
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application

# Telegram bot token
TOKEN = '7515913003:AAEs1yaiFhmuztMsBhrkuH4DBrQ58P-9l2w'

# Görsel dosyası ve chat ID
IMAGE_PATH = 'ROULETTE.png'  # Yüklenen görsel dosya yolu
CHAT_ID = '-1002488268265'

# Bonus butonlarını içeren fonksiyon
def get_bonus_buttons():
    buttons = [
        [InlineKeyboardButton("🚀 Stake Daily Bonus", url="https://stake.com/?c=9dd9dbc553")],
        [InlineKeyboardButton("🎲 Slottica %200 Bonus", url="https://gopartner.link/?a=205678&c=184089&s1=6028")],
        [InlineKeyboardButton("💰 Mostbet 1000$ Bonus", url="https://t.ly/eAL_1")],
        [InlineKeyboardButton("🎰 Marsbahis Daily %10 Bonus", url="https://bit.ly/3RF81eI")],
        [InlineKeyboardButton("🎯 Billybets 100% Deposit Bonus", url="https://billytraff.com/ge40c56a1")]
    ]
    return InlineKeyboardMarkup(buttons)

# Asenkron mesaj ve görsel gönderme fonksiyonu
async def send_message_and_image(bot):
    with open(IMAGE_PATH, 'rb') as image:
        await bot.send_photo(chat_id=CHAT_ID, photo=image, caption="BEST CASINO SITE LIST!", reply_markup=get_bonus_buttons())

# Her 60 saniyede bir çalışacak iş (asenkron)
async def job():
    bot = Bot(token=TOKEN)
    await send_message_and_image(bot)
    print("Mesaj ve görsel gönderildi.")

# Logger ayarı
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Mevcut olay döngüsünü kontrol eden ve başlatan fonksiyon
def run_async_job():
    loop = asyncio.get_event_loop()  # Mevcut olay döngüsünü al
    if loop.is_closed():  # Eğer olay döngüsü kapalıysa yeni bir döngü başlat
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    loop.run_until_complete(job())  # Asenkron görevi çalıştır

# Zamanlama ayarı
def schedule_jobs():
    schedule.every(4).hours.do(run_async_job)  # Asenkron görevi zamanla

# Botun sürekli çalışmasını sağlayan döngü
if __name__ == '__main__':
    print("Bot çalışıyor...")

    # Zamanlama işlemlerini başlat
    schedule_jobs()

    # Sürekli kontrol et ve görevleri zamanla
    while True:
        schedule.run_pending()
        time.sleep(1)
