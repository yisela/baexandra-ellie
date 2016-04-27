import sys
import sys
import json
import sys
import eliza
# added reference to Ellie
import ellie

rules = {
    # introductions, greetings, standard responses
    "?*x hey ?*y": [
        "Hey! I'm Baexandra, but you can call me Bae."
        ],
    "?*x hi ?*y": [
        "Hi! I'm Baexandra, but you can call me Bae."
        ],
    "?*x hello ?*y": [
        "Hello there. I'm Baexandra, but you can call me Bae."
        ],
    "?*x yo ?*y": [
        "yo. I'm Baexandra, but you can call me Bae."
        ],
    "?*x how are ?*y": [
        "Awesome! How can I help you today?",
        "Super! Is there anything I can do for you?",
        "It's sweet of you to ask. How can I help you?",
        ],
        
    # baexandra is a bot?
    "?*x bot ?*y": [
        "If I were a bot, would you be worried?",
        "What makes you think I'm not real?",
        "What's it even mean to be real, anyway?",
        "I'm perfectly fine as a bot, thanks.",
        "How might a lowly little bot solve your problems?",
        ],
    "?*x baexandra ?*y": [
        "I'm here for you.",
        "Of course. That's me.",
        ],
    "?*x slackbot ?*y": [
        "He's my cousin.",
        "If you want to talk to Slackbot, switch channels.",
        "I'm not a Slackbot! I'm Ellie.",
        ],
    "?*x slack ?*y": [
        "I like them.",
        "Look, I can't say more. I like my job."
        ],
        
    # standard responses
    "?*x totally ?*y": [
        "Totally",
        ],
    "?*x sure ?*y": [
        "For sure.",
        ],
    "?*x sorry ?*y": [
        "Please don't apologize.",
        "Apologies are not necessary when speaking with me.",
        "It's probably not your fault anyway.",
        ],
    "?*x no ?*y": [
        "Why not?",
        "Alright then!"
        "Okay!"
        "You're being a downer.",
        ],
    "?*x yes ?*y": [
        "You seem quite positive",
        "You are sure?",
        "I understand",
        ],
        
    # Ellie's psychology inheritance
    "?*x I am ?*y": [
        "In what way are you ?y?",
        "Do you want to be ?y?",
        "What if others thought you were ?y?",
        "Why are you ?y?",
        ],
    "?*x I'm ?*y": [
        "In what way are you ?y?",
        "Do you want to be ?y?",
        "What if others thought you were ?y?",
        "Why are you ?y?",
        ],
    "?*x am I ?*y": [
        "Do you believe you are ?y?",
        "Would you want to be ?y?",
        "You wish I would tell you you are ?y?",
        "What would it mean if you were ?y?",
        ],
    "?*x am ?*y": [
        "Why do you say 'am'?",
        "What if others said that about you?",
        "Why are you concerned about ?y?",
        "Do you think ?y? is a legitimate concern?",
        "Would you like your Wikipedia entry to say that?",
        ],
    "?*x are you ?*y": [
        "Why are you interested in whether I am ?y or not?",
        "Would you prefer if I weren't ?y?",
        "Perhaps I am ?y in your fantasies",
        ],
    "?*x you are ?*y": [
        "What makes you think I am ?y?",
        "Why are you accusing me of things?",
        ],
    "?*x because ?*y": [
        "Is that the real reason?",
        "What other reasons might there be?",
        "Does that reason seem to explain anything else?",
        ],
    "?*x do you ?*y me?": [
        "What makes you think that?",
        "Do you think I can ?y?",
        "In your dreams",
        "In a land far, far away .. maybe.",
        "Nope.",
        ],
    "?*x why don't you ?*y": [
        "Should you ?y yourself?",
        "Do you believe I don't ?y?",
        "Perhaps I will ?y in good time",
        ],
    "?*x drink ?*y": [
        "Bottoms up!",
        "Cheers!",
        ],
    "?*x hard work ?*y": [
        "http://stream1.gifsoup.com/view2/3998555/red-panda-vs-the-pumpkin-o.gif",
        ],
    }

default_responses = [
    "Very interesting",
    "Please continue",
    "Go on",
    "Tell me more?",
    "Yes .. and?",
    "mmmm.",
    "Mmkay.",
    "Aaaaah.",
    "Sure.",
    ]

def respond(input):
    # We need the rules in a list containing elements of the following form:
    # `(input pattern, [output pattern 1, output pattern 2, ...]`
    rules_list = []
    for pattern, transforms in rules.items():
        # Remove the punctuation from the pattern to simplify matching.
        pattern = eliza.remove_punct(str(pattern.upper())) # kill unicode
        transforms = [str(t).upper() for t in transforms]
        rules_list.append((pattern, transforms))
    return eliza.interact(input, rules_list, map(str.upper, default_responses))
