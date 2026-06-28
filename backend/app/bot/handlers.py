from aiogram import Router, types, F
from aiogram.types import CallbackQuery

from app.bot.client import get_plans, buy_plan
from app.bot.keyboards import plans_keyboard

router = Router()


@router.message()
async def start(message: types.Message):

    plans = await get_plans()

    keyboard = plans_keyboard(plans)

    await message.answer(
        "💎 پلن‌های موجود:\n\nبرای خرید یکی را انتخاب کن:",
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("buy_"))
async def buy(callback: CallbackQuery):

    plan_id = int(callback.data.split("_")[1])

    result = await buy_plan(
        plan_id=plan_id,
        telegram_id=str(callback.from_user.id)
    )

    await callback.message.answer(
        f"✅ خرید موفق!\n\n"
        f"Order ID: {result['order_id']}\n"
        f"VPN User: {result['vpn_user']}"
    )

    await callback.answer()
