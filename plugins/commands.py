#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Group", url="https://t.me/moviesfactory_group"),
                        InlineKeyboardButton("Channel", url="https://t.me/movies_factory_all"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🌀 Contact my Creator 🌀", url="https://t.me/YouCan_CallMe_Leo")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Group", url="https://t.me/MoviesFactory_group"),
                        InlineKeyboardButton("Channel", url="https://t.me/movies_factory_all"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🌀 Contact my Creator 🌀", url="https://t.me/YouCan_CallMe_Leo")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(" Group", url="https://t.me/moviesfactory_group"),
                        InlineKeyboardButton("Channel", url="https://t.me/movies_factory_all"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🌀 Contact my Creator 🌀", url="https://t.me/YouCan_CallMe_Leo")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass
