# ./main.py

from andromeda_weao import Client; client = Client()
import dotenv; dotenv.load_dotenv()
import os
import json
import discord
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="latest")
async def latest(interaction: discord.Interaction):
    embed = discord.Embed(
        title="**Latest Roblox Version**",
        description=f"```json\n{json.dumps(client._get_current_version(), indent=4, sort_keys=True)}\n```",
        color=discord.Color.darker_grey()
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)



bot.run(os.getenv("AUTH_TOKEN"))