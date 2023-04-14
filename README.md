## pycord-bb
basic preconfigured discord-bot startup script  

pycord-bb is meant to be used as a universal base for development and distribution of pycord cogs

pycord-bb is a basic discord bot with some build in functionality:

- preconfigured logger
- filesystem access using ez-storage
- version check on startup

**extensions** from ```./extensions/``` will be loaded on startup. [how to create extensions]()

### Installation:
_Automated Installation:_

autoinstaller scripts assuming you have Python > 3.9.x and Git installed

download the autoinstaller [here]()

_Manual Installation:_

- Install Python > 3.9.x 
- create a Folder and move in 
- Download repository :  https://github.com/Lainupcomputer/pycord-bb
- create venv ```python -m venv venv```
- activate venv ```./venv/bin/activate```
- move back to created Folder
- Install requirements: ```pip install -r requirements.txt```
- set bot token ```cd /helper``` -> ```python set_bot_token.py```
- set bot prefix ```cd /helper``` -> ```python set_bot_prefix.py```
- start the bot with ```python bot.py```

_Docker Installation:_

- download repo 
- add your token and prefix in ```Dockerfile```
- ```docker build -t mybot .```
- ```docker run mybot ```



### Support:
if you need support please join our [Discord](https://discord.gg/aYD4sewxyb)

submit a Bug [Here](https://github.com/Lainupcomputer/pycord-bb/issues/new)
 