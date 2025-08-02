from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 তোমার বটের টোকেন বসাও
TOKEN = '8368866867:AAFfOiHEuOcy83Zrou1tq43M53E46BP3QYA'

# 📢 চ্যানেলের ইউজারনেম বা আইডি বসাও (যেমন @yourchannel বা -1001234567890)
CHANNEL_ID = '@ha2131'  # অথবা -100xxxxxxxxxxxx

# /start কমান্ড হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args  # /start command-এর পর যেকোনো আর্গুমেন্ট

    user_info = (
        f"🔔 নতুন ইউজার:\n"
        f"👤 নাম: {user.full_name}\n"
        f"📛 ইউজারনেম: @{user.username if user.username else 'N/A'}\n"
        f"🆔 ইউজার আইডি: {user.id}\n"
        f"🔗 স্টার্ট আর্গুমেন্ট: {' '.join(args) if args else 'কোনো নেই'}"
    )

    # ✅ চ্যানেলে মেসেজ পাঠাও
    await context.bot.send_message(chat_id=CHANNEL_ID, text=user_info)

    # ✅ ইউজারকে উত্তর দাও
    await update.message.reply_text("✅ তোমার তথ্য সংগ্রহ করা হয়েছে। ধন্যবাদ!")

# ▶️ মেইন ফাংশন
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running...")
    app.run_polling()

# 🔁 প্রোগ্রাম চালাও
if __name__ == '__main__':
    main()
