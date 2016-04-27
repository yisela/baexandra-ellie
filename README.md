# baexandra-bot
Introducing Baexandra, an onboarding bot inspired on [Ellie](https://github.com/christinac/ellie-slack/tree/master/plugins/ellie). Ellie is Slack's Python-based [real-time messaging bot](https://github.com/slackhq/python-rtmbot) wrapped around  Daniel Connelly's [Python implementation](https://github.com/dhconnelly/paip-python) of Peter Norvig's *Paradigms of AI Programming* Eliza.

Baexandra's role is to onboard new team members through instructions, references and automatic replies. Existing team members can teach Baexandra how to best reply to the usual questions about the project. 

Current implementation: baexandra replies to easy questions
Future: Reference files, links, integrate with Slack API

### Baexandra's replies
All dialog lives in the file baexandra.py
TO DO: Change references from Ellie to Baexandra

### Dependencies
* [websocket-client](https://pypi.python.org/pypi/websocket-client/)
* [python-slackclient](https://github.com/slackhq/python-slackclient)

### Installation (NOT YET IMPLEMENTED)

1. Download Baexandra
 (NOT YET IMPLEMENTED)
  ````
  git clone git@github.com/yisela/baexandra.git
  cd baexandra-slack
  ````

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
