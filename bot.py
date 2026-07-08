import discord
from discord import app_commands
from discord.ext import tasks
from ai import english_support

from config import ALERT_CHANNEL_ID
from config import TOKEN



intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    try:
        synced = await tree.sync()

        print(f"✅ Synced {len(synced)} commands")

        for cmd in synced:
            print(cmd.name)
        

    except Exception as e:
        print(e)

    print(f"Logged in as {client.user}")

# =========================
# /english
# ========================
@tree.command(
    name="english",
    description="Improve English like a professional support engineer"
)
@app_commands.describe(
    prompt="Enter your sentence or request"
)
async def english(
    interaction: discord.Interaction,
    prompt: str
):

    await interaction.response.defer()
    print(f"Received prompt: {prompt}")
    answer = english_support(prompt)

    MAX = 1900

    for i in range(0, len(answer), MAX):
        await interaction.followup.send(answer[i:i+MAX])


client.run(TOKEN)