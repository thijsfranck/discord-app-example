# Discord App Example

This is a simple example of a Discord bot using the [discord.py](https://discordpy.readthedocs.io/en/latest/) library.

## Installation

The application is distributed as a [Docker](https://www.docker.com/) image. Run the following command to install the latest version:

```bash
docker run ghcr.io/thijsfranck/discord-app-example:latest
```

> [!NOTE]
> Previous versions of the image are available on the [GitHub Container Registry](https://github.com/thijsfranck/discord-app-example/pkgs/container/discord-app-example).

## Configuration

The following environment variables are available to configure the bot:

| Variable        | Description                                                              | Required | Default |
| --------------- | ------------------------------------------------------------------------ | -------- | ------- |
| `DISCORD_TOKEN` | The Discord bot token.                                                   | Yes      | -       |
| `LOG_LEVEL`     | The minimum log level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`). | No       | `INFO`  |

> [!IMPORTANT]
> You can obtain a Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
> Your token should have the `bot` scope. Do not share your token with anyone!

## Development

See the [contribution guide](./CONTRIBUTING.md) for instructions and guidelines on setting up the development environment and working on the project.

## License

This project is licensed under the [MIT license](./LICENSE).
