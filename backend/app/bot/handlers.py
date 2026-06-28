from aiogram import Router, types, F
from aiogram.types import CallbackQuery

from app.bot.client import login_user, get_plans, buy_plan
from app.bot.keyboards import plans_keyboard

router = Router()

# حافظه ساده (بعداً Redis می‌کنیم)
user_tokens = {}


@router.message()
async def start(message: types.Message):

    telegram_id = str(message.from_user.id)

    login = await login_user(telegram_id)

    token = login["access_token"]

    user_tokens[telegram_id] = token

    plans = await get_plans()

    keyboard = plans_keyboard(plans)

    await message.answer(
        "💎 پلن‌های موجود:\n\nبرای خرید انتخاب کن:",
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("buy_"))
async def buy(callback: CallbackQuery):

    telegram_id = str(callback.from_user.id)
    plan_id = int(callback.data.split("_")[1])

    token = user_tokens.get(telegram_id)

    if not token:
        await callback.message.answer("خطا: دوباره /start بزن")
        return

    result = await buy_plan(plan_id, token)

    await callback.message.answer(
        f"✅ خرید موفق!\n\n"
        f"Order ID: {result['order_id']}\n"
        f"VPN User: {result['vpn_user']}"
    )

    await callback.answer()
