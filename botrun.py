import disnake
import discord
from discord.ext import commands
from disnake.ext import commands
import os, sqlite3
import transliterate

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Бураня {bot.user.name} на месте!')
    global base, cur
    base = sqlite3.connect('albaeva_enemy.db')
    cur = base.cursor()
    if base:
        print('Db connected...OK')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return  # Игнорируем сообщения от бота

    if bot.user.mentioned_in(message) and "переведи" in message.content.lower():
        # Проверяем упоминание бота и команду "переведи"
        # Получаем сообщение, на которое бот отвечает
        ref_message = message.reference.resolved if message.reference else None
        if ref_message:
            
            alphabet_eng = ['&', "'",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.', ' ', ';', '?', ')', '[', ']', '{', '}', '`', '~']
            alphabet_ru = ['?', 'э', 'ф', 'и', 'с', 'в', 'у', 'а', 'п', 'р', 'ш', 'о', 'л', 'д', 'ь', 'т', 'щ', 'з', 'й', 'к', 'ы', 'е', 'г', 'м', 'ц', 'ч', 'н', 'я', 'б', 'ю', ' ', 'ж', '?', ')', 'х', 'ъ', 'Х', 'Ъ', 'ё', 'Ё']
            string_ru = ''
            flag = True
            while(flag):
                string_eng = ref_message.content
                string_eng = string_eng.lower()
                for i in range(len(string_eng)):
                    try:
                        string_ru += alphabet_ru[alphabet_eng.index(string_eng[i])]
                    except Exception:
                        string_ru += string_eng[i]

                arg = string_ru
                await message.channel.send(f'\n{string_ru}')
                flag = False

    # Проверяем, содержит ли сообщение символы латинского алфавита
    if any(char.isalpha() and char.lower() in "abcdefghijklmnopqrstuvwxyz,.'[]" for char in message.content) and '://' not in message.content and '<:' not in message.content:
        # Если есть символы латиницы, транслитерируем текст
            alphabet_eng = ['&', "'",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.', ' ', ';', '?', ')', '[', ']', '{', '}', '`', '~']
            alphabet_ru = ['?', 'э', 'ф', 'и', 'с', 'в', 'у', 'а', 'п', 'р', 'ш', 'о', 'л', 'д', 'ь', 'т', 'щ', 'з', 'й', 'к', 'ы', 'е', 'г', 'м', 'ц', 'ч', 'н', 'я', 'б', 'ю', ' ', 'ж', '?', ')', 'х', 'ъ', 'Х', 'Ъ', 'ё', 'Ё']
            string_ru = ''
            flag = True
            while(flag):
                string_eng = message.content
                string_eng = string_eng.lower()
                for i in range(len(string_eng)):
                    try:
                        string_ru += alphabet_ru[alphabet_eng.index(string_eng[i])]
                    except Exception:
                        string_ru += string_eng[i]

                arg = string_ru
                await message.channel.send(f'\n{string_ru}')
                flag = False

    attachments = message.attachments
    urls = "gay"

    for attch in attachments:
        urls = attch.url
    # Проверяем, что сообщение содержит ссылку с "shorts" и отправлено пользователем с ролью "new role"
    if "Клоунесса" in [role.name for role in message.author.roles] and "/voice-message.ogg" in urls:
        #flag1=False
        #for att in message.attachments:
            #if att: print(1) 
            #if att.is_voice_message(): flag1 = True
        # Получаем ID текстового канала
        text_channel_id = message.channel.id
    
        # Удаляем голосовое сообщение
        await message.delete()
        print(f'Удалено голосовое сообщение от пользователя {message.author}')
        
        # Отправляем сообщение в указанный текстовый канал
        text_channel = bot.get_channel(text_channel_id)
        if text_channel:
            await text_channel.send(f'ТЕБЕ РУКИ ДЛЯ ЧЕГО СУКА???')

    if "Клоунесса" in [role.name for role in message.author.roles] and "shorts" in message.content:
        # Получаем ID текстового канала
        text_channel_id = message.channel.id
    
        # Удаляем сообщение с ссылкой
        await message.delete()
        print(f'Удалена ссылка от пользователя {message.author}')
        
        # Отправляем сообщение в указанный текстовый канал
        text_channel = bot.get_channel(text_channel_id)
        if text_channel:
            await text_channel.send(f'ТВОИ ШОРТСЫ НИКОМУ НАХУЙ НЕ ВСРАЛИСЬ!!!')
    await bot.process_commands(message)


@bot.slash_command(description="перевести транслит на человеческий")
async def translit(ctx, *, text: str):
    args_str = ''.join(text)
    alphabet_eng = ['&', "'",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.', ' ', ';', '?', ')', '[', ']', '{', '}', '`', '~']
    alphabet_ru = ['?', 'э', 'ф', 'и', 'с', 'в', 'у', 'а', 'п', 'р', 'ш', 'о', 'л', 'д', 'ь', 'т', 'щ', 'з', 'й', 'к', 'ы', 'е', 'г', 'м', 'ц', 'ч', 'н', 'я', 'б', 'ю', ' ', 'ж', '?', ')', 'х', 'ъ', 'Х', 'Ъ', 'ё', 'Ё']
    string_ru = ''
    flag = True
    while(flag):
        string_eng = args_str
        string_eng = string_eng.lower()
        for i in range(len(string_eng)):
            try:
                string_ru += alphabet_ru[alphabet_eng.index(string_eng[i])]
            except Exception:
                string_ru += string_eng[i]

        arg = string_ru
        await ctx.send(string_ru)
        flag = False

@bot.slash_command(description="ВОТ ЧТО Я МОГУ")
async def help(ctx):
    await ctx.send("1)есть команда /translit - переведу транслитную хуйню\n2)можешь обратиться ко мне через @ и сказать 'перведи' чтобы реплаем перевести сообщение пидора\n3)если альбаева высрет шортс или гс )))))")

#@bot.slash_command()
#async def testo(ctx, *, arg: str):
#    await ctx.send(f'Введенный текст: {arg}')

bot.run(os.getenv('TOKEN'))