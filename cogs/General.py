import discord
from discord.ext import bridge, commands
from datetime import datetime, date, time 
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


#* ================================================ Info about the bot - "info" command - both / and - =======================================
    @bridge.bridge_command(description="Gives information about the bot")
    async def info(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(title=f"Hi! I am Pocket Diary",
                            description="A bot **currently in development** by <@1363200418552873024>.",
                            color=discord.Colour.blurple()
        )
        embed.add_field(name="Coded in", value="Python", inline=True)
        embed.add_field(name="Library", value="Pycord", inline=True)
        embed.add_field(name="Created on", value="<t:1748347560:D>", inline=True)
        embed.set_footer(text="Learning and Improving everyday")
        embed.set_author(name="61sts")
        embed.set_thumbnail(url="https://img.freepik.com/premium-vector/pixel-art-open-book-icon-game-asset-design_466450-2192.jpg")
        embed.set_image(url="https://i.pinimg.com/originals/4f/d3/0e/4fd30efd8301e3551a3a63da0d9c4d88.gif")
        await ctx.respond(embed=embed)    
    
#* =========================================================== "ping" command - and / ==================================================
    @bridge.bridge_command(description="Gets the ping of bot")
    async def ping(self, ctx):
        latency = (str(self.bot.latency)).split(".")[1][1:3]
        await ctx.respond(f"Pong! Bot responded in {latency} ms")

#* ======================================================== "serverinfo" command, - and / =====================================================
    @bridge.bridge_command(description="Gives info about the server")
    async def serverinfo(self,ctx):
        member_count = ctx.guild.member_count
        members_online = ctx.guild.approximate_presence_count
        created = ctx.guild.created_at.date()
        name = ctx.guild.name
        default_role = ctx.guild.default_role
        guild_id = ctx.guild.id
        owner = ctx.guild.owner
        owner_id = ctx.guild.owner_id
        channels = ctx.guild.channels
        category = ctx.guild.categories
        roles = ctx.guild.roles
        emojis = ctx.guild.emojis
        filesize = (ctx.guild.filesize_limit)
        filesize_mb = filesize / (1024 ** 2)
        server_icon = ctx.guild.icon.url
        embed = discord.Embed(
            title=f"{name}",
            description=f"**{name} is owned by <@{owner_id}>**\nCreated on:`{created}`",
            color=discord.Colour.blurple()
        )
        embed.add_field(name="Total Members",value=f"{member_count}",inline=True)
        embed.add_field(name="Members Online",value=f"{members_online}",inline=True)
        embed.add_field(name="Default role",value=f"{default_role}",inline=True)
        embed.add_field(name="Total Channels",value=len(channels),inline=True)
        embed.add_field(name="Total Categories",value=len(category),inline=True)
        embed.add_field(name="Total Roles",value=len(roles),inline=True)
        embed.add_field(name="Total Emojis",value=len(emojis),inline=True)
        embed.add_field(name="Guild ID",value=f"{guild_id}",inline=True)
        embed.add_field(name="Filesize Limit",value=f"{filesize_mb:.2f} MB",inline=True)
        embed.set_footer(text="By 61sts")
        embed.set_thumbnail(url=f"{server_icon}")
        embed.set_author(name=owner, icon_url=owner.avatar.url)
        await ctx.respond(embed=embed)

#* ======================================================= "avatar" commad - and / =========================================================
    @bridge.bridge_command(description="Gets mentioned user's avatar")
    async def avatar(self, ctx, user:discord.User = None ):
        user = user or ctx.author
        embed = discord.Embed(title=f"{user.name}'s avatar:",
                              color=discord.Color.blurple())
        embed.set_image(url=user.display_avatar.url)
        await ctx.respond(embed=embed)
        ...


#* ======================================================== "about" command - and / =========================================================
    @bridge.bridge_command(description="Gives info about mentioned user")
    async def about(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        name = user.display_name
        created = user.created_at.date()
        color = user.color
        roles = [role.mention for role in user.roles if role.name != "@everyone"]
        sorted_roles = ", ".join(roles) or "No roles"
        user_id = user.id
        muted = user.timed_out
        joined = user.joined_at.date()
        voice = user.voice
        embed = discord.Embed(title=f"## About {name}",
                              description=f"**Has the following roles :** {sorted_roles}",
                              color=discord.Color.blurple())
        embed.add_field(name="Joined server on",value=joined,inline=True)
        embed.add_field(name="Account created on",value=created, inline=True)
        embed.add_field(name="User ID",value=user_id, inline=True)
        embed.add_field(name="Is Muted",value=muted, inline=True)
        embed.add_field(name="Color",value=color, inline=True)
        embed.add_field(name="Voice",value=voice, inline=True)
        embed.set_author(name=user.display_name, icon_url=user.display_avatar.url)
        embed.set_thumbnail(url=user.display_avatar.url)
        await ctx.respond(embed=embed)
                              
#* ========================================================== "help" command - and / ======================================================= 
    @bridge.bridge_command(description="List of commands in bot")
    async def help(self, ctx):
        embed = discord.Embed(title="List of commands",description="**All commands support slash commands as well**",color=discord.Color.blurple())
        embed.add_field(name="General Commands", value="`info`\n`ping`\n`serverinfo`\n`avatar`\n`about`")
        embed.set_footer(text="More commands coming soon!")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(General(bot))
    
