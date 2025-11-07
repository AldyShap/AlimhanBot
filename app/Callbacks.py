from aiogram.types import CallbackQuery
from aiogram import F
from aiogram import Router
import app.keyboards as kb
import database.requests as rq
router2 = Router()
id_info = 1

# /works
@router2.callback_query(F.data.startswith('works_'))
async def works_i(callback: CallbackQuery):
    await callback.answer()
    index = int(callback.data.split('_')[1])+1
    if index == 6:
        with open('messages/works/conclusionwork.txt', 'r', encoding='utf-8') as file:
            await callback.message.edit_text(file.read(), reply_markup=kb.to_main)
    if index == 2:
        with open('messages/works/mainworks/mainworks1.txt', 'r', encoding='utf-8') as file:
            await callback.message.edit_text(file.read(),reply_markup=kb.next1)
    else:
        with open(f'messages/works/works{index}.txt', 'r', encoding='utf-8') as file:
            await callback.message.edit_text(file.read(),reply_markup=kb.to_main)
# /works
@router2.callback_query(F.data == 'next_1')
async def next_page(callback: CallbackQuery):
    await callback.answer()
    index = int(callback.data.split('_')[1])+1
    with open(f'messages/works/mainworks/mainworks{index}.txt', 'r', encoding='utf-8') as file:
        await callback.message.edit_text(file.read(),reply_markup=kb.next2)
# /works
@router2.callback_query(F.data == 'next_2')
async def next_page(callback: CallbackQuery):
    await callback.answer()
    index = int(callback.data.split('_')[1])+1
    with open(f'messages/works/mainworks/mainworks{index}.txt', 'r', encoding='utf-8') as file:
        await callback.message.edit_text(file.read(),reply_markup=kb.next3)
# /works
@router2.callback_query(F.data == 'next_3')
async def next_page(callback: CallbackQuery):
    await callback.answer()
    index = int(callback.data.split('_')[1])+1
    with open(f'messages/works/mainworks/mainworks{index}.txt', 'r', encoding='utf-8') as file:
        await callback.message.edit_text(file.read(),reply_markup=kb.next4)
# /works
@router2.callback_query(F.data == 'next_4')
async def next_page(callback: CallbackQuery):
    await callback.answer()
    index = int(callback.data.split('_')[1])+1
    with open(f'messages/works/mainworks/mainworks{index}.txt', 'r', encoding='utf-8') as file:
        await callback.message.edit_text(file.read(),reply_markup=kb.next5)
# /works
@router2.callback_query(F.data == 'next_5')
async def next_page(callback: CallbackQuery):
    await callback.answer()
    index = int(callback.data.split('_')[1])
    with open(f'messages/works/mainworks/mainworks{index}.txt', 'r', encoding='utf-8') as file:
        await callback.message.edit_text(file.read(),reply_markup=kb.to_main)

# /works
@router2.callback_query(F.data == 'to_main')
async def to_main_callback(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Сізге не қызықтырады?", reply_markup=await kb.about_works_find())


# /help
@router2.callback_query(F.data == 'to_back')
async def to_main_callback(callback:CallbackQuery):
    await callback.answer()
    with open('messages/start.txt', 'r', encoding='utf-8') as file:
        await callback.message.edit_text(file.read())

# /biography
@router2.callback_query(F.data.startswith('stage_'))
async def show_stage(callback:CallbackQuery):
    await callback.answer()
    id = int(callback.data.split('_')[1])
    biografy = await rq.select_stage_life(id)
    if biografy:
        await callback.message.edit_text(biografy, reply_markup= kb.biography_main)
    else:
        await callback.message.answer("Uppps..., somthing went wrong :(")

# /biography
@router2.callback_query(F.data == "to_main_stages")
async def show_main_stages(callback: CallbackQuery):
    await callback.answer()
    with open('messages/biography.txt', 'r', encoding='utf-8') as file:
        await callback.message.edit_text(file.read(), reply_markup=await kb.biography_stage())

#/facts
@router2.callback_query(F.data.startswith('fact_'))
async def get_fact(callback: CallbackQuery):
    await callback.answer()
    global id_info
    id = int(callback.data.split('_')[1])
    id_info = id
    fact = await rq.get_fatc(id)
    if fact:
        await callback.message.edit_text(fact, reply_markup=kb.more_and_main_facts)
    else:
        await callback.message.answer("Uppps..., somthing went wrong :(")

#/facts
@router2.callback_query(F.data == "main_facts")
async def to_main_facts(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Бізде Әлімхан Ермеков туралы 10 факт бар. Қайсыларын білгіңіз келеді?", reply_markup=await kb.talk_facts_to_user())

#/facts
@router2.callback_query(F.data == 'more')
async def get_more_information(callback: CallbackQuery):
    await callback.answer()
    global id_info
    more_info_g = await rq.get_more_info(id_info)
    await callback.message.edit_text(more_info_g, reply_markup=kb.main_fatcs)

#/words
@router2.callback_query(F.data == "to_main_words")
async def show_main_words(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Тағы тақырыптарды қарастырғыңыз келе ме?", reply_markup=await kb.get_great_words())

#/words
@router2.callback_query(F.data.startswith("great_"))
async def get_words(callback: CallbackQuery):
    await callback.answer()
    id_word = int(callback.data.split('_')[1])
    words = await rq.get_said_word(id_word)
    if words:
        await callback.message.edit_text(words, reply_markup=kb.to_main_words)
    else:
        await callback.message.answer("uppss... something went wrong :(")

@router2.callback_query(F.data.startswith('next_question_2'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(2)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_3
    )

@router2.callback_query(F.data.startswith('next_question_3'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(3)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_4
    )
@router2.callback_query(F.data.startswith('next_question_4'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(4)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_5
    )
@router2.callback_query(F.data.startswith('next_question_5'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(5)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_6
    )
@router2.callback_query(F.data.startswith('next_question_6'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(6)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_7
    )
@router2.callback_query(F.data.startswith('next_question_7'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(7)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_8
    )
@router2.callback_query(F.data.startswith('next_question_8'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(8)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_9
    )
@router2.callback_query(F.data.startswith('next_question_9'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(9)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_10
    )

@router2.callback_query(F.data.startswith('next_question_10'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(10)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_11
    )

@router2.callback_query(F.data.startswith('next_question_11'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(11)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_12
    )
@router2.callback_query(F.data.startswith('next_question_12'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(12)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_13
    )
@router2.callback_query(F.data.startswith('next_question_13'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(13)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_14
    )
@router2.callback_query(F.data.startswith('next_question_14'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(14)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_15
    )
@router2.callback_query(F.data.startswith('next_question_15'))
async def to_next_question(callback:CallbackQuery):
    from main import bot
    await callback.answer()
    next_question, options, correct_option, explanation = await rq.get_questions(15)

    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=next_question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation=explanation,
        is_anonymous=False,
        reply_markup=kb.next_question_15
    )
@router2.callback_query(F.data.startswith("to_main_back"))
async def to_next_question(callback:CallbackQuery):
    await callback.answer()
    with open('messages/finish_quiz.txt', 'r', encoding='utf-8') as file:
        await callback.message.answer(file.read(), reply_markup=kb.back)

@router2.callback_query(F.data == "to_back2")
async def to_back2(callback:CallbackQuery):
    await callback.answer()
    with open('messages/help.txt', 'r', encoding='utf-8') as file:
        await callback.message.answer(file.read())
        await callback.message.answer("Сізге не қызықтырады?")