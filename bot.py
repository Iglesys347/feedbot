import discord
from discord.ext import commands, tasks
from datetime import date

from manage_notes import Notes
from graph import NoteGraph

notes = Notes()

bot = commands.Bot(command_prefix = "!", description = "Feedback bot")

# must be changed to suit the server
SERVER_ID = 804359800623595572
CHANNEL_ID = 804359800623595577
LOOP_HOURS = 168

BOT_TOKEN = open(".token").read()

@bot.event
async def on_ready():
    print("I'm ready !")

@tasks.loop(hours=168)
async def feedback():
    channel = bot.get_guild(SERVER_ID).get_channel(CHANNEL_ID)
    await channel.send("<@Etudiant> **Time for feedback !**")
    await channel.send("Please use the command `!note [0-5]` to evaluate how you felt this week.")

@feedback.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

@bot.command()
async def graph(ctx):
    note_graph = NoteGraph()
    note_graph.make_graph("Graph.png")
    await ctx.send(file=discord.File("Graph.png"))

@bot.command()
async def note(ctx, note):
    note = int(note)
    name = ctx.author.name
    week_nb = date.today().isocalendar()[1]
    if note <= 5 and note >= 0:
        # try:
        notes.add_note(name, week_nb, note)
        await ctx.send(f"Thank you {name} for giving your opinion ! :smile:")
        if note <= 1:
            await ctx.send(f"Don't worry {name}, whatever obstacles you find on your way, keep going, keep believing, hope will be your greatest victory. :muscle:")
        # except AttributeError as e:
            # await ctx.send(f"{name}, you already gave a note for this week.")
            # print(e)
    else:
        await ctx.send(f"Sorry {name}, but your note isn't valid (your note must be an integer between 0 and 5)")

feedback.start()
bot.run(BOT_TOKEN)
