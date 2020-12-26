# These lines that start with the # are called comments. They don't affect the way the code runs.
# In this tutorial file, I put comments above the relevant lines.

# Before we begin, it's worth noting that the name of this file, sample.py, will cause it to never run.
# You will have to rename it to "_sample.py".
# Putting an underscore as the first character of a grammar Python file will tell dragonfly
# that you want this file to run all the time. Grammars that run all the time are good way to start.
# The alternative is making grammars for specific programs that only trigger when the programs are active.

# You can skip down to the next comment, for now this is not important...

from dragonfly import (BringApp, Key, Function, Grammar, Playback, 
                       IntegerRef, Dictation, Choice, WaitWindow, MappingRule, Text, Mouse,)

def my_function(n, text):
    print("put some Python logic here: " + str(text))

class MainRule(MappingRule):

    mapping = {
    # It is this section that you want to fiddle around with if you're new: mapping, extras, and defaults
    "swindle": Playback([(["caster", "sleep"], 0.0)])+Key("c-win"),
    "snooze": Playback([(["caster", "sleep"], 0.0)]),
    "poke": Key("p, y, t, h, o, n, space"),
    '(cinema | cinnamon)': Key("c-c"),
    "diamond": Key("c-d"),
    "scrawny": Playback([(["scree", "dunce"], 0.0)]),
    "scruffy": Playback([(["scree", "sauce"], 0.0)]),
    '(pounds|pound)': Key("pagedown"),
    "puppy": Key("pageup"),
    "stoke": Key("w-v"),
    }

# this stuff is required too-- where I have the word "sample" below, each grammar file should have external unique
grammar = Grammar('swindle')
grammar.add_rule(MainRule())
grammar.load()