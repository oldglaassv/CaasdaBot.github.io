from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import BOT_TOKEN, WEBAPP_URL
from database import cursor, conn

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    cursor.execute(
        "INSERT OR IGNORE INTO users VALUES (?,?)",
        (user.id, user.username)
    )
    conn.commit()

    keyboard = [[
        InlineKeyboardButton(
            "📱 Открыть фитнес приложение",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]

    await update.message.reply_text(
        "💪 Fitness Bot",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("BOT STARTED")

    app.run_polling()

if __name__ == "__main__":
    main()