from aiogram import Dispatcher, types
from aiogram import filters
from aiogram.types import InputFile
import subprocess
import os

t = ['Найти', 'Знайти', 'Find']

async def find_song(message: types.Message):
    name = message.text.split(sep=' ')[1:]
    cwd = os.getcwd()
    if not os.path.isdir(str(message.chat.id)):
        os.mkdir(str(message.chat.id))
    os.chdir(str(message.chat.id))
    process = subprocess.run(['spotdl', f'{"".join(name)}'])
    files = os.listdir()
    for file in files:
        mus = InputFile(file)
        await message.answer_audio(mus)
        os.remove(file)

async def down_song(message: types.Message):
    cwd = os.getcwd()
    if not os.path.isdir(str(message.chat.id)):
        os.mkdir(str(message.chat.id))
    os.chdir(str(message.chat.id))
    process = subprocess.run(['spotdl', f'{message.text}'])
    files = os.listdir()
    for file in files:
        mus = InputFile(file)
        await message.answer_audio(mus)
        os.remove(file)



def register_spotify(dp: Dispatcher):
    dp.register_message_handler(find_song, filters.Text(startswith=t, ignore_case=True))
    dp.register_message_handler(down_song, filters.Text(contains='spotify', ignore_case=True))