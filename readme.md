# Officebot

Mattermost bot that allows the team to track who is in the office, what people do for lunch and if they are in for beers.

To see the list of commands, check the [commands documentation](docs/commands.md).

## Configuration
Before running the bot for the first time, copy the contents of the `.env-dist` file to a file called `.env`
in the root of the project and fill in the following values.
* `MATTERMOST_URL`: The URL of the Mattermost server.
* `MATTERMOST_PORT`: The port where the Mattermost server is running.
* `BOT_TEAM`: The name of the Mattermost team where the bot belongs.
* `MATTERMOST_API_PATH`: The path of the Mattermost API. (you can remove this one if the api path is the default)
* `BOT_TOKEN`: The token of the bot user.

You can change the other settings to your preference in the `config.py` file located in the `bot` folder.

## Build
In order to build the bot docker image, just run the `build.sh` script.

If you are running the image in a development environment, add the `--dev` parameter when running the script. This will
install the extra development dependencies.

## Run
In order to run the bot, just run the `run.sh` script.

If you are developing, add the `--dev` parameter when running the script. This will create a volume
with the code, so you don't need to rebuild the image every time you make a change.

You can add `bash` at the end of the command to run the container in interactive mode.
