from telegram.ext import Application, MessageHandler, filters
import logging
import os

BOT_TOKEN = os.environ.get("7947508096:AAG1uXhoOlB0OyBMgikOa0-edRMFXkBP8ow")
SOURCE_CHAT_ID = os.environ.get("14916411379")
DESTINATION_CHAT_ID = os.environ.get("4846336460")

logging.basicConfig(level=logging.INFO)

async def forward_message(update, context):
    try:
        await context.bot.forward_message(
            chat_id=int(DESTINATION_CHAT_ID),
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )
        print("✅ Сообщение переслано!")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def main():
    if not all([BOT_TOKEN, SOURCE_CHAT_ID, DESTINATION_CHAT_ID]):
        print("❌ Ошибка: Не установлены переменные окружения!")
        return
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.Chat(int(SOURCE_CHAT_ID)), forward_message))
    print("🤖 Бот запущен!")
    app.run_polling()

if _name_ == "__main__":
    main()
