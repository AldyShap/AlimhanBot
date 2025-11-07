from database.models import async_session
from database.models import User, Biography, Word, Fact, Question
from sqlalchemy import select

async def select_user(id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id == id))

        if not user:
            session.add(User(id = id))
            await session.commit()

async def select_stage_life(id):
    async with async_session() as session:
        return await session.scalar(select(Biography.info).where(Biography.id == id))

async def get_fatc(id):
    async with async_session() as session:
        return await session.scalar(select(Fact.intersting_fact).where(Fact.id == id))

async def get_more_info(id):
    async with async_session() as session:
        return await session.scalar(select(Fact.more_info).where(Fact.id == id))

async def get_said_word(id):
    async with async_session() as session:
        return await session.scalar(select(Word.said_word).where(Word.id == id))

async def get_questions(id):
    async with async_session() as session:
        next_question = await session.scalar(select(Question.next_question).where(Question.id == id))
        options_json = await session.scalar(select(Question.options).where(Question.id == id))
        correct_option = await session.scalar(select(Question.correct_option).where(Question.id == id))
        explanation = await session.scalar(select(Question.explanation).where(Question.id == id))

        return next_question, options_json, correct_option, explanation