# baexandra-bot
Introducing Baexandra, an onboarding bot based on Ellie-slack. Ellie is Slack's Python-based [real-time messaging bot](https://github.com/slackhq/python-rtmbot) wrapped around  Daniel Connelly's [Python implementation](https://github.com/dhconnelly/paip-python) of Peter Norvig's *Paradigms of AI Programming* Eliza.

Baexandra's role is to onboard new team members through instructions, references and replies.

### Baexandra's customisations
All dialog will be executed in the file baexandra.py

### Dependencies
* [websocket-client](https://pypi.python.org/pypi/websocket-client/)
* [python-slackclient](https://github.com/slackhq/python-slackclient)

### Installation
1. Download Ellie/Baexandra

  ````
  git clone git@github.com:christinac/ellie-slack.git
  cd ellie-slack
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

4. Run it! (You've got to keep her running so long as you'd like her to keep chattering; something like [nohup](http://linux.die.net/man/1/nohup) might be helpful.)

````
  python rtmbot.py
````

## (Original) Ellie in action
![Ellie in action](screenshot.png)
