from sqlalchemy import TEXT, JSON
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine('sqlite+aiosqlite:///bot.db')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(TEXT)

class Biography(Base):
    __tablename__ = "byography_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    info: Mapped[str] = mapped_column(TEXT)

class Word(Base):
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(primary_key=True)
    said_word: Mapped[str] = mapped_column(TEXT)

class Fact(Base):
    __tablename__ = "facts"

    id: Mapped[int] = mapped_column(primary_key=True)
    intersting_fact: Mapped[str] = mapped_column(TEXT)
    more_info: Mapped[str] = mapped_column(TEXT)

class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    next_question: Mapped[str] = mapped_column(TEXT)
    options: Mapped[list[str]] = mapped_column(JSON)
    correct_option: Mapped[int] = mapped_column()
    explanation: Mapped[str] = mapped_column(TEXT)
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
