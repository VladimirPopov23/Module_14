# module_14_3.py
# 23.01.2025 Задача "Витамины для всех!"

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = 'код'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
    ], resize_keyboard=True
)

inline_menu = InlineKeyboardMarkup(row_width=4)
Product1 = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
Product2 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
Product3 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
Product4 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
inline_menu.row(Product1)
inline_menu.insert(Product2)
inline_menu.insert(Product3)
inline_menu.insert(Product4)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for number in range(1, 5):
        with open(f'files/{number}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: Product{number} | Описание: описание {number} | Цена: {number * 100}')
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_menu)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Информация о боте!')


# @dp.message_handler(text='Рассчитать')
# async def main_menu(message):
#     await message.answer('Выберите опцию:', reply_markup=inline_menu)

# @dp.callback_query_handler(text='formulas')
# async def get_formulas(call):
#     await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
#     await call.answer()
#
#
# @dp.callback_query_handler(text='calories')
# async def set_age(call):
#     await call.message.answer('Введите свой возраст:')
#     await call.answer()
#     await UserState.age.set()
#
#
# @dp.message_handler(text='Информация')
# async def inform(message):
#     await message.answer('Информация о боте!')
#
#
# @dp.message_handler(state=UserState.age)
# async def set_growth(message, state):
#     await state.update_data(age=message.text)
#     await message.answer('Введите свой рост:')
#     await UserState.growth.set()
#
#
# @dp.message_handler(state=UserState.growth)
# async def set_weight(message, state):
#     await state.update_data(growth=message.text)
#     await message.answer('Введите свой вес:')
#     await UserState.weight.set()
#
#
# @dp.message_handler(state=UserState.weight)
# async def set_handler(message, state):
#     await state.update_data(weight=message.text)
#     data = await state.get_data()
#     await message.answer(
#         f"Ваша норма калорий {(10 * int(data['weight'])) + (6.25 * int(data['growth'])) - (5 * int(data['age'])) + 5}")
#     await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=start_menu)


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
