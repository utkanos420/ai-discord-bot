import asyncio
import logging
from openai import OpenAI

import discord
from discord.ext import commands

from loguru import logger

from configs.config import bot_settings, openai_settings


logger.remove()
logger.add(
    sink=lambda msg: print(msg, end=""),  # Вывод в stdout
    format="<level>[{time:YYYY-MM-DD HH:mm:ss}] #{level:<8} {file.name}:" 
           "{line} - {name} - {message}</level>",
    level="DEBUG",
    colorize=True
)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True  
bot = commands.Bot(command_prefix=bot_settings.discord_bot_prefix, intents=intents)


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openai_settings.openai_gemini_token,
)


@bot.command(name="prompt")
async def get_prompt(ctx):
    await ctx.send("")

if __name__ == "__main__":
    logger.info("Starting the bot...")

    logger.debug(f"Starting the openai agent with openrouter token {openai_settings.openai_debug_version}")
    logger.debug(f"Starting the discord bot with bot token {bot_settings.discord_bot_token} using prefix: {bot_settings.discord_bot_prefix}")

    bot.run(token=bot_settings.discord_bot_token)




