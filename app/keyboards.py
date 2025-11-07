from aiogram.types import (InlineKeyboardButton,InlineKeyboardMarkup,
                           ReplyKeyboardMarkup, KeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

# /works
works = ['🧮 Ғылыми бағыттары мен зерттеу саласы', '📘 Негізгі ғылыми еңбектері мен оқулықтары', '🎓 Педагогикалық және ағартушылық еңбегі', '🌍 Ғылым мен қоғамдағы рөлі', '🏛 Ғылыми мұрасы мен ықпалы', "Қорытынды"]

# /works
next1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі', callback_data='next_1')],
    [InlineKeyboardButton(text='Басты ақпараттарға', callback_data='to_main')]
])

# /works
next2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі', callback_data='next_2')],
    [InlineKeyboardButton(text='Басты ақпараттарға', callback_data='to_main')]
])

# /works
next3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі', callback_data='next_3')],
    [InlineKeyboardButton(text='Батсы ақпараттарға', callback_data='to_main')]
])

# /works
next4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі', callback_data='next_4')],
    [InlineKeyboardButton(text='Батсы ақпараттарға', callback_data='to_main')]
])

# /works
next5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Батсы ақпараттарға', callback_data='next_5')]
])

# /works
to_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Басты ақпараттарға', callback_data='to_main')]
])

# /help
back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Батсы бетке', callback_data='to_back')]
])

# /biography
biography_stages = [1,2,3,4,5,6,7]
biography_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Батсы кезеңдерге', callback_data='to_main_stages')],
    [InlineKeyboardButton(text='Басты бетке', callback_data="to_back")]
])

# /facts
facts_number = [1,2,3,4,5,6,7,8,9,10]
more_and_main_facts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Толығырақ', callback_data='more')],
    [InlineKeyboardButton(text='Басты фатктілерге', callback_data='main_facts')]
])

# /facts
main_fatcs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Басты фатктілерге', callback_data='main_facts')]
])

# /quotes
great_words = ["🌿 Білім мен ғылым туралы", "⚖️ Еңбек пен табандылық туралы", "💭 Ақыл, парасат және өмір даналығы", "❤️ Адамгершілік пен достық туралы", "🌍 Отан мен ел туралы"]

# /quotes
to_main_words = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Тақырыптарға", callback_data='to_main_words')]
])

next_question_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі', callback_data='next_question_2')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

# /works
next_question_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі', callback_data='next_question_3')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

# /works
next_question_4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі', callback_data='next_question_4')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

# /works
next_question_5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі Сұрақ', callback_data='next_question_5')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

next_question_6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі Сұрақ', callback_data='next_question_6')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

next_question_7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі Сұрақ', callback_data='next_question_7')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

next_question_8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі Сұрақ', callback_data='next_question_8')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

next_question_9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі Сұрақ', callback_data='next_question_9')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

next_question_10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі Сұрақ', callback_data='next_question_10')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

next_question_11 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі Сұрақ', callback_data='next_question_11')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

next_question_12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі Сұрақ', callback_data='next_question_12')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

next_question_13 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі Сұрақ', callback_data='next_question_13')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

next_question_14 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Келесі Сұрақ', callback_data='next_question_14')],
    [InlineKeyboardButton(text='Басты Бетке', callback_data='to_back2')]
])

next_question_15 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Аяқтау', callback_data='to_main_back')]
])

set_chotam = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Ия')],
    [KeyboardButton(text='Жоқ')]
],resize_keyboard=True)

map_keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Қарқаралы", url='https://commons.wikimedia.org/wiki/File:Karkaraly_District_in_Kazakhstan.svg'), InlineKeyboardButton(text="Семей", url="https://www.istanbul-city-guide.com/map/kazakhstan/semey-map.asp")],
    [InlineKeyboardButton(text="Орынбор", url='https://www.mapz.com/maps/%D0%9E%D1%80%D0%B5%D0%BD%D0%B1%D1%83%D1%80%D0%B3'), InlineKeyboardButton(text="Мәскеу", url="https://www.mapz.com/maps/moscow")],
    [InlineKeyboardButton(text="Алматы",url='https://visitalmaty.kz/en/map/?utm_source=chatgpt.com'), InlineKeyboardButton(text='Басты бетке', callback_data='to_back')]

])

# /works
async def about_works_find():
    keyboard = InlineKeyboardBuilder()
    for i in range(len(works)):
        keyboard.add(InlineKeyboardButton(text=works[i], callback_data=f'works_{i}'))
    keyboard.add(InlineKeyboardButton(text='Батсы бетке', callback_data='to_back'))
    return keyboard.adjust(1).as_markup()

# /biography
async def biography_stage():
    keyboard = InlineKeyboardBuilder()
    for i in biography_stages:
        keyboard.add(InlineKeyboardButton(text=str(i), callback_data=f'stage_{str(i)}'))
    keyboard.add(InlineKeyboardButton(text="Басты бетке", callback_data="to_back"))
    return keyboard.adjust(2).as_markup()

# /facts
async def talk_facts_to_user():
    keyboard = InlineKeyboardBuilder()
    for i in facts_number:
        keyboard.add(InlineKeyboardButton(text=str(i), callback_data=f'fact_{str(i)}'))
    keyboard.add(InlineKeyboardButton(text='Батсы бетке', callback_data='to_back'))
    return keyboard.adjust(2).as_markup()

# /quotes
async def get_great_words():
    keyboard = InlineKeyboardBuilder()
    for i in range(len(great_words)):
        keyboard.add(InlineKeyboardButton(text=great_words[i], callback_data=f'great_{i+1}'))
    keyboard.add(InlineKeyboardButton(text='Батсы бетке', callback_data='to_back'))
    return keyboard.adjust(1).as_markup()

# /quiz
