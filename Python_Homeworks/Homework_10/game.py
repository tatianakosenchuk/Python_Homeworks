from telegram.ext import ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from utils import keyboard

board = [
    [InlineKeyboardButton(' ', callback_data='0,0'),
     InlineKeyboardButton(' ', callback_data='0,1'),
     InlineKeyboardButton(' ', callback_data='0,2')],

    [InlineKeyboardButton(' ', callback_data='1,0'),
     InlineKeyboardButton(' ', callback_data='1,1'),
     InlineKeyboardButton(' ', callback_data='1,2')],

    [InlineKeyboardButton(' ', callback_data='2,0'),
     InlineKeyboardButton(' ', callback_data='2,1'),
     InlineKeyboardButton(' ', callback_data='2,2')]
]

async def start_game(update, _):
    global board
    await update.message.reply_text('Игра началась!', reply_markup=InlineKeyboardMarkup(board))
    await update.message.reply_text(f"Ваш ход X")
    return "CHOOSING_X"


def Win_list(board):
    if (board[0][0] == board[0][1] == board[0][2]) or (board[1][0] == board[1][1] == board[1][2]) or\
        (board[2][0] == board[2][1] == board[2][2]) or (board[0][0] == board[1][0] == board[2][0]) or\
        (board[0][1] == board[1][1] == board[2][1]) or (board[0][2] == board[1][2] == board[2][2]) or\
            (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        return 'Win'
    else:
        counter = 0
        for i in board:
            for j in i:
                if (str(j).find('X') == -1) and (str(j).find('O') == -1):
                    counter += 1
        if counter == 0:
            return 'Nobody'
        else:
            return 'Cont'


async def cross(update, _):
    query = update.callback_query
    await query.answer()
    if query.data not in 'OX':
        board[int(list(query.data.split(','))[0])][int(list(query.data.split(','))[
            1])] = InlineKeyboardButton('X', callback_data='X')
        print(type(Win_list(board)))
        print(Win_list(board))
    else:
        await update.callback_query.message.reply_text("Ячейка занята")
        return f"CHOOSING_X"
    if Win_list(board)=='Nobody':
        await update.callback_query.message.reply_text(f"Ничья", reply_markup=InlineKeyboardMarkup(board))
    elif Win_list(board)=='Win':
            await update.callback_query.message.reply_text(f"Победил X", reply_markup=InlineKeyboardMarkup(board))
            return ConversationHandler.END
    else:
            await update.callback_query.message.reply_text(f"Ваш ход O", reply_markup=InlineKeyboardMarkup(board))
            return "CHOOSING_O"
        

async def zero(update, _):
    query = update.callback_query
    await query.answer()
    if query.data not in 'OX':
        board[int(list(query.data.split(','))[0])][int(list(query.data.split(','))[
            1])] = InlineKeyboardButton('O', callback_data='O')
        print(Win_list(board))
    else:
        await update.callback_query.message.reply_text("Ячейка занята")
        return f"CHOOSING_O"
    if Win_list(board) == 'Win':
        await update.callback_query.message.reply_text(f"Победил O!", reply_markup=InlineKeyboardMarkup(board))
        return ConversationHandler.END
    elif Win_list(board) == 'Cont':
        await update.callback_query.message.reply_text(f"Ваш ход X", reply_markup=InlineKeyboardMarkup(board))
    return "CHOOSING_X"
