# Configuration

The following environment variables are available to configure the bot:

| Variable        | Description                                     | Required | Default |
| --------------- | ------------------------------------------------| -------- | ------- |
| `DISCORD_TOKEN` | The Discord bot token.                          | Yes      | -       |
| `LOG_LEVEL`     | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` | No       | `INFO`  |

## `DISCORD_TOKEN`

You can obtain a Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
Your token should have the following scopes:

- `bot`

!!! DANGER "Security Warning"
    Do not share your token with anyone!

## `LOG_LEVEL`

The minimum log level to display messages in the console. The available log levels are:

- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

By default, the log level is set to `INFO`.
