from aiogram import Router, types
from app.bot.client import create_or_get_user

router = Router()


@router.message()
async def start_handler(message: types.Message):

    user_data = {
        "telegram_id": str(message.from_user.id),
        "username": message.from_user.username,
        "full_name": message.from_user.full_name
    }

    user = await create_or_get_user(user_data)

    await message.answer(
        f"سلام {message.from_user.full_name} 👋\n"
        f"حساب شما ساخته شد یا قبلاً وجود داشت.\n\n"
        f"User ID: {user.get('id')}"
    )
