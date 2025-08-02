import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Environment variables থেকে Token এবং Channel ID নেওয়া
TOKEN = os.getenv("8368866867:AAFfOiHEuOcy83Zrou1tq43M53E46BP3QYA")
CHANNEL_ID = os.getenv("@ha2131")

if not TOKEN or not CHANNEL_ID:
    print("Error: TELEGRAM_BOT_TOKEN এবং TELEGRAM_CHANNEL_ID সেট করা হয়নি।")
    exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args

    user_info = (
        f"🔔 নতুন ইউজার এসেছে!\n"
        f"নাম: {user.full_name}\n"
        f"ইউজারনেম: @{user.username if user.username else 'N/A'}\n"
        f"ইউজার আইডি: {user.id}\n"
        f"স্টার্ট আর্গুমেন্ট: {' '.join(args) if args else 'কোনো নেই'}"
    )

    # চ্যানেলে মেসেজ পাঠানো
    await context.bot.send_message(chat_id=CHANNEL_ID, text=user_info)

    # ইউজারকে রিপ্লাই
    await update.message.reply_text("✅ তোমার তথ্য সংগ্রহ করা হয়েছে, ধন্যবাদ!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()

