from os import error
import discord
import json
from discord.ext import commands, tasks
from datetime import date

bot = commands.Bot(command_prefix='/')
homework = []

with open('data.json', 'r') as jf:
    homework = json.load(jf)

def write_data():
    with open('data.json', 'w') as jf:
        json.dump(homework, jf, indent=4)

@bot.command(name='info')
async def command_info(ctx):
    await ctx.channel.send(' - /homework (Zeigt alle Hasuaufgaben an)')
    await ctx.channel.send(' - /addHomework modul datum beschreibung')
    await ctx.channel.send(' - /removeHomework index')
    await ctx.channel.send('Beispiel:   /addHomework 117 2021-15-09' + ' "Netzwerkdiagramm zeigen"')

@bot.command(name='addHomework')
async def command_add_homework(ctx, module=None, termination_date=None, description=None):
    if module == None or termination_date == None or description == None:
        await ctx.channel.send('Keine gültigen Informationen. Hilfe mit /info') 
        return
    homework.append({
        'module': module,
        'termination_date': termination_date,
        'description': description
    })
    
@bot.command(name='removeHomework')
async def command_remove_homework(ctx, index=None):
    index = int(index)
    try:
        await ctx.channel.send('Hausaufgabe entfernt: '+'   Modul: '+homework[index]['module']+'    Datum: '+homework[index]['termination_date'] + '    Beschreibung: ' + homework[index]['description'])
        homework.pop(index)
        write_data()
    except error:
        await ctx.channel.send('Kein gültiger Index. Hilfe mit /info') 

@bot.command(name='homework')
async def command_show_homework(ctx):
    #homework.sort(key=lambda r: r.date)
    if len(homework) == 0:
        await ctx.channel.send('Keine Hausaufgaben eingetragen.')
        return
    for i in range(len(homework)):
        await ctx.channel.send(str(i)+') '+'    Modul: '+homework[i]['module']+'    Datum: '+homework[i]['termination_date'] + '    Beschreibung: ' + homework[i]['description'])
    write_data()
    
    
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
@bot.event
async def on_command_error(ctx, error):
    print(error)
    await ctx.channel.send('Unknown command. Get help with /info') 

token = ''
bot.run(token)