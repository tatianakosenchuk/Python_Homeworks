from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,CallbackQueryHandler

async def start(update, _):
    await update.message.reply_text(f'Здравствуйте, {update.effective_user.first_name}!\n'
                                    'Приветствую Вас в игре "Крестики-нолики".\n')
    await update.message.reply_text('Пожалуйста, введите команду и два числа через пробел:\n'
                                    '/sum  - "+ Сложение"\n'
                                    '/sub  - "- Вычитание"\n'
                                    '/mult - "* Умножение"\n'
                                    '/div  - "/ Деление"\n'
                                    '/pow  - "x¹x²x³ Возведение в степень"\n'
                                    '/sqrt - "√ Квадратный корень - введите одно число"\n')


async def sum_bot(update, _):
    msg = update.message.text
    nums = msg.split()
    a,b = int(nums[1]),int(nums[2])
    await update.message.reply_text(f'{a} + {b} = {(a+b)}')
    logging.info(f'{a} + {b} = {a+b}')


async def sub_bot(update, _):
   msg = update.message.text
   nums = msg.split()
   a,b = int(nums[1]),int(nums[2])
   await update.message.reply_text(f'{a} - {b} = {(a- b)}')
   logging.info(f'{a} - {b} = {a-b}')


async def mult_bot(update, _):
   msg = update.message.text
   nums = msg.split()
   a,b = int(nums[1]),int(nums[2])
   await update.message.reply_text(f'{a} * {b} = {(a* b)}')
   logging.info(f'{a} * {b} = {a*b}')

async def div_bot(update, _):
   msg = update.message.text
   nums = msg.split()
   a,b = int(nums[1]),int(nums[2])
   if b:
        await update.message.reply_text(f'{a} / {b} = {(a/ b)}')
        logging.info(f'{a} / {b} = {a/b}') 
   else:
        await update.message.reply_text('Недопустимая операция: деление на 0!')
        logging.warning('Недопустимая операция: деление на 0!')



async def pow_bot(update, _):
   msg = update.message.text
   nums = msg.split()
   a,b = int(nums[1]),int(nums[2])
   await update.message.reply_text(f'{a} ^ {b} = {(a** b)}')
   logging.info(f'{a} ** {b} = {a**b}')


async def sqrt_bot(update, _):
   msg = update.message.text
   nums = msg.split()
   a = int(nums[1])
   await update.message.reply_text(f'√{a} = {(int(a**0.5))}')
   logging.info(f'sqrt {a} = {a**0.5}')
