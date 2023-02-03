#!/usr/bin/env python3


def main():
  print('**** CHOOSE YOUR OWN MISADVENTURE ****')
  print('(Press ctrl-c to quit at any time)')

  # Get the player's name.
  name = input('What is your name? ')

  current_scene_key = 'home'

  while True: # The main game loop.
    scene = scenes[current_scene_key]
    choices = scene['choices']
    print(f'\n{scene["title"]:}')
    print(scene['desc'])
    if not choices: break # End the game.
    for i, choice in enumerate(choices):
      print(f'{i+1}: {choice["desc"]}')
    while True: # The input loop.
      choice_str = input('> ')
      try: choice_idx = int(choice_str)
      except ValueError: continue
      if choice_idx >= 1 and choice_idx <= len(choices): break
      print(f'Invalid choice {name}. Please choose again.')
    choice = choices[choice_idx-1]
    current_scene_key = choice['goto']


# Scenes is a dictionary mapping scene keys to scene dictionaries.
# Each scene dictionary is a pseudo-structure consisting of title string, description string, and choices array.
# Each choice dictionary is a pseudo-structure consisting of description string and destination key, mapping into the `scenes` dictionary.

scenes = {
  'home' : {
    'title': 'At Home',
    'desc': 'You are at home listening to Green Day.',
    'choices': [
      { 'desc': 'Open the Mumble dating app for nerds',
        'goto': 'mumble' },
      { 'desc': 'Go to the bar down the street',
        'goto': 'bar' },
      { 'desc': 'Go to sleep',
        'goto': 'sleep' }]},
  
  'sleep' : {
    'title': 'Going to sleep',
    'desc': 'You decide there is nothing left to do but go to sleep. The End.',
    'choices': []},

  'mumble': {
    'title': 'Mumble: Dating for Nerds',
    'desc': 'You sit on the couch and swipe through pictures of potential dates. You are so in love with this app. You love it.',
    'choices': [
      { 'desc': 'Give up',
        'goto': 'home' },
      { 'desc': 'Message every person you see',
        'goto': 'mumble_respond' }]},

  'mumble_respond': {
    'title': 'They wrote back!',
    'desc': 'Every single person you contacted has responded to your message. You are now a Mumble dating nerd.',
    'choices': [
      { 'desc': 'Reset the Mumble dating app',
        'goto': 'mumble' },
      { 'desc': 'Go to the bar down the street',
        'goto': 'bar' },
      { 'desc': 'Go to sleep pleased with yourself',
        'goto': 'sleep' }]},

  'bar': {
    'title': 'At the Bar',
    'desc': 'You are at the bar. You are not a Mumble dating nerd.',
    'choices': [
      { 'desc': 'Talk to everyone there',
        'goto': 'bar_talk' },
      { 'desc': 'Go home',
        'goto': 'home' }]},

  'bar_talk': {
    'title': 'At the Bar',
    'desc': 'You make some friends at the bar. You are not in love with that app. You are in love with the bar.',
    'choices': [
      { 'desc': 'Go home',
        'goto': 'home' },
      { 'desc': 'Ask someone out',
        'goto': 'bar_ask' }]},

  'bar_ask': {
    'title': 'Get a date IRL',
    'desc': 'You approach someone and ask them out.',
    'choices': [
      { 'desc': 'Say something nice',
        'goto': 'bar_date_nice' },
      { 'desc': 'Say something provocative',
        'goto': 'bar_date_provocative' }]},
  
  'bar_date_nice': {
    'title': 'Being nice',
    'desc': 'You say something nice and friendly to the person you just met. You are in love with that person. You love everyone.',
    'choices': [
      { 'desc': 'Go home',
        'goto': 'home' }]},

  'bar_date_provocative': {
    'title': 'Being provocative',
    'desc': 'You say something provocative to the person you just met. They respond with a slap. You are in love with that person.',
    'choices': [
      { 'desc': 'Go home',
        'goto': 'home' }]}
}


if __name__ == '__main__': main()