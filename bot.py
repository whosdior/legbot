import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True  # Necessary for managing nicknames
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.command()
async def register(ctx, *, name: str):
    try:
        # Create the new nickname format
        new_nickname = f"{name} (0)"
        
        # Change the user's nickname
        await ctx.author.edit(nick=new_nickname)
        
        # Create an embed for successful registration
        embed = discord.Embed(
            title="Registration Successful",
            description=f"{ctx.author.mention}, you have registered successfully!",
            color=discord.Color.green()
        )
        
        await ctx.send(embed=embed)
    
    except discord.Forbidden:
        await ctx.send("I don't have permission to change your nickname.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred while changing your nickname: {e}")

# Run the bot
bot.run("YOUR_BOT_TOKEN")
