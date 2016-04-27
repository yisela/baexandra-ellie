# Baexandra

Hi there! I'm Baexandra, an *onboarding bot* closely related to [Ellie](https://github.com/christinac/ellie-slack/tree/master/plugins/ellie), Slack's Python-based [real-time messaging bot](https://github.com/slackhq/python-rtmbot) which is wrapped around Daniel Connelly's [Python implementation](https://github.com/dhconnelly/paip-python) of Peter Norvig's *Paradigms of AI Programming* Eliza.

**My role is to onboard new team members through instructions, references and automatic replies that I learn from other people in the company (well, actual people with bodies)**. Feel free to teach me what you know! While I appreciate wittiness and a certain sense of humanity, please do not turn me into one of those racist bots. 

I currently only reply to simple questions, but I hope I can soon provide references to files, sites and integrate with the Slack API. 


## How to educate Baexandra

Users are encouraged to teach Baexandra anything they consider relevant. The way to do this is by pulling, editing and pushing requests for the file [baexandra.py](https://github.com/yisela/baexandra/blob/master/plugins/ellie/baexandra.py). 

You can create new dialog options and replies by using this format (you can just copy and paste from a previous one):

````
"?*x hey ?*y": [
        "Hey! I'm Baexandra, but you can call me Bae.",
        "Hey! I'm Baexandra, nice to meet you."
        ],

?*x  =  Start new question/dialog
?*y  =  Equivalent of "*" for filling in content
,    =  Multiple answers
````


## How to install Baexandra 

### Dependencies
* [websocket-client](https://pypi.python.org/pypi/websocket-client/)
* [python-slackclient](https://github.com/slackhq/python-slackclient)

NOTE: Baexandra is not finished, so she will probably NOT work at this point. 

1. Download Baexandra

2. Install dependencies

  ````
  pip install -r requirements.txt
  ````

3. Configure rtmbot ([Slack instructions](https://christinac.slack.com/services/new/bot).) From the Slack console, you'll get to choose your bot's name and icon. Though we've become partial to Ellile, bot-naming is up to you.

  ````
  cp example-config/rtmbot.conf .
  vi rtmbot.conf
  SLACK_TOKEN: "xoxb-11111111111-222222222222222"
  ````

4. Run it! (Baexandra needs to be kept running to work, something like [nohup](http://linux.die.net/man/1/nohup) might be helpful.)

````
  python rtmbot.py
````
