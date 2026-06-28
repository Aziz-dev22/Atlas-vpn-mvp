from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def plans_keyboard(plans):
    keyboard = []

    for plan in plans:
        keyboard.append([
            InlineKeyboardButton(
                text=f"{plan['name']} - ${plan['price']}",
                callback_data=f"buy_{plan['id']}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
