import asyncio
import logging
import requests
import os

from openai import OpenAI

import discord
from discord.ext import commands

from loguru import logger

from configs.config import bot_settings, gemini_settings

from gemini.handler import handle_attachments_and_request, handle_text_request


logger.remove()
logger.add("bot.log", format="{time} {level} {message}", level="DEBUG", colorize=True)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=bot_settings.discord_bot_prefix, intents=intents)


@bot.command(name='prompt')
async def get_prompt(ctx):
    message = ctx.message.content

    if ctx.message.attachments:
        await handle_attachments_and_request(ctx, message)
    else:
        await handle_text_request(ctx, message)


if __name__ == "__main__":
    logger.info("Starting the bot...")

    logger.debug(f"Starting the openai agent with openrouter token {gemini_settings.gemini_debug_version}")
    logger.debug(f"Starting the discord bot with bot token {bot_settings.discord_bot_token} using prefix: {bot_settings.discord_bot_prefix}")

    bot.run(token=bot_settings.discord_bot_token)
