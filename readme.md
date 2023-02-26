# Officebot

Mattermost bot that allows the team to track who is in the office, what people do for lunch and if they are in for beers.

To see the list of commands, check the [commands documentation](docs/commands.md).

## Configuration
Before running the bot for the first time, you need to set at least the following variables in the `config.pyp` file located inside the
`bot` folder:
* `MATTERMOST_URL`: The URL of the Mattermost server.
* `MATTERMOST_PORT`: The port where the Mattermost server is running.
* `BOT_TEAM`: The name of the Mattermost team where the bot belongs.
* `MATTERMOST_API_PATH`: The path of the Mattermost API.
* `BOT_TOKEN`: The token of the bot user.

You can change the other settings to your preference.

## Build
In order to build the bot docker image, just run the `build.sh` script.

If you are running the image in a development environment, add the `--dev` parameter when running the script. This will
install the extra development dependencies.

## Run
In order to run the bot, just run the `run.sh` script.

If you are developing, add the `--dev` parameter when running the script. This will create a volume
with the code, so you don't need to rebuild the image every time you make a change.

You can add `bash` at the end of the command to run the container in interactive mode.
