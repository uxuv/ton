import asyncio, requests
from pyrogram import Client, filters

api_id = 27250559
api_hash = "3cca5d87b91b4f80ed57999b5c715114"
bot_token = "8337154319:AAFC18HP11UHH1nlOdClC0jDGoL_zUTY4Yg"
channel = "@ToooNPrice"
url = "https://api.binance.com/api/v3/ticker/price?symbol=TONUSDT"

app = Client("bot", api_id, api_hash, bot_token=bot_token)

@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    p = float(requests.get(url).json()["price"])
    await message.reply_text(f"{p:.2f}$")

async def price_loop():
    while True:
        p = float(requests.get(url).json()["price"])
        await app.send_message(channel, f"{p:.2f}$")
        await asyncio.sleep(300)

async def main():
    await app.start()
    asyncio.create_task(price_loop())  # تشغيل الحلقة بشكل غير متزامن
    await app.idle()  # يبقي البوت يعمل

asyncio.run(main())
