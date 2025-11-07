from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from app import keyboards as kb
import database.requests as rq

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer_photo('https://www.google.com/imgres?q=%D3%99%D0%BB%D1%96%D0%BC%D1%85%D0%B0%D0%BD%20%D0%B5%D1%80%D0%BC%D0%B5%D0%BA&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fru%2F6%2F68%2F%25D0%2590%25D0%25BB%25D0%25B8%25D0%25BC%25D1%2585%25D0%25B0%25D0%25BD_%25D0%2595%25D1%2580%25D0%25BC%25D0%25B5%25D0%25BA%25D0%25BE%25D0%25B2.jpg&imgrefurl=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2F%25D0%2595%25D1%2580%25D0%25BC%25D0%25B5%25D0%25BA%25D0%25BE%25D0%25B2%2C_%25D0%2590%25D0%25BB%25D0%25B8%25D0%25BC%25D1%2585%25D0%25B0%25D0%25BD_%25D0%2590%25D0%25B1%25D0%25B5%25D1%2583%25D0%25BE%25D0%25B2%25D0%25B8%25D1%2587&docid=K25lqs709fd0xM&tbnid=F-uNZDMnS53jNM&vet=12ahUKEwjuldKQ0bWQAxX2IxAIHUlNJSkQM3oECBUQAA..i&w=240&h=317&hcb=2&ved=2ahUKEwjuldKQ0bWQAxX2IxAIHUlNJSkQM3oECBUQAA')
    with open('messages/start.txt', 'r', encoding='utf-8') as file:
        try:
            await message.answer(file.read())
            await message.answer("Сізге қандай көмек бере аламын?")
        except Exception:
            await message.answer("Сәлем! Мен Әлімхан Ермеков туралы ботпын 🤖")

@router.message(Command('help'))
async def give_help(message: Message):
    with open('messages/help.txt', 'r', encoding='utf-8') as file:
        try:
            await message.answer(file.read())
        except Exception as e:
            await message.answer(f"Бір жерде қателік бар: {e}")

@router.message(Command('works'))
async def about_works(message: Message):
    await message.answer('Не туралы білгіңіз келеді?', reply_markup= await kb.about_works_find())

@router.message(Command('biography'))
async def tell_about_life(message: Message):
    with open('messages/biography.txt', 'r', encoding='utf-8') as file:
        await message.answer(file.read(), reply_markup=await kb.biography_stage())

@router.message(Command('facts'))
async def show_facts(message: Message):
    await message.answer("Сізге қызық болуы мүмкін Әлімхан Ермеков туралы 10 факт бар! Қайсысын оқығыңыз келеді? 👀", reply_markup=await kb.talk_facts_to_user())

@router.message(Command('quotes'))
async def show_topics(message:Message):
    await message.answer("Әлімхан Ермековтың нақыл сөздері көп. Қандай тақырыпқа көз тіктіңіз 👀?", reply_markup=await kb.get_great_words())

@router.message(Command('map'))
async def get_map(message: Message):
    with open('messages/map.txt', 'r', encoding='utf-8') as file:
        await message.answer(file.read(), reply_markup= kb.map_keyboards)

@router.message(Command('about'))
async def show_about_bot(message: Message):
    with open('messages/about.txt', 'r', encoding='utf-8') as file:
        await message.answer(file.read(), reply_markup= kb.back)

@router.message(Command("quiz"))
async def quiz_handler(message: Message):
    from main import bot
    next_question, options, correct_option, explanation = await rq.get_questions(1)

    await bot.send_poll(
        chat_id=message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup= kb.next_question_2
    )