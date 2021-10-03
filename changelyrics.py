import sys
import os.path
import configparser
import easygui

rep = easygui.enterbox("Change selected note(s) to lyric:")

ust = configparser.RawConfigParser(allow_no_value=True)
ust.optionxform = lambda option: option
ust.read(sys.argv[1])

config = configparser.RawConfigParser(allow_no_value=True)
config.optionxform = lambda option: option

if ('#NEXT' in ust):
    first_note_dex = int(ust.sections()[3][-4:])
    last_note_count = len(ust.sections())-5
    partial = True
else:
    first_note_dex = int(ust.sections()[2][-4:])
    last_note_count = len(ust.sections())-4
    partial = False

if ('#NEXT' in ust):
    first_note_dex = int(ust.sections()[3][-4:])
    last_note_count = len(ust.sections())-5
    partial = True
else:
    first_note_dex = int(ust.sections()[2][-4:])
    last_note_count = len(ust.sections())-4
    partial = False

note_count = 0

for note in ust.sections():
    if ((note != '#VERSION') and (note != '#SETTING') and (note != '#PREV') and (note != '#NEXT')):
    
        current_note_dex = str(first_note_dex + note_count).zfill(4)

        s = ust['#'+current_note_dex]['Lyric']
        if ('R' in s) or ('r' in s):
            pass
        else:
            ust['#'+current_note_dex]['Lyric'] = rep

        note_count += 1

with open(sys.argv[1], 'w') as output:
    ust.write(output, space_around_delimiters=False)