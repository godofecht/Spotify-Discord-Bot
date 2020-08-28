import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

bot = commands.Bot(command_prefix='>')
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


bot_creds = '' #fill this in


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def get_art(ctx,name):
    results = spotify.search(q='artist:' + name, type='artist')
    artists = results['artists']['items']
    if len(artists) > 0:
        artist = artists[0]
        artist_uri = artists[0]['uri']

        albums = spotify.artist_albums(artist_uri,album_type='album')
        for album in albums:
            await ctx.send(album['images'][0]['url'])

bot.run(bot_creds)
