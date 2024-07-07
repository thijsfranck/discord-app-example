# Discord App Example

This is a simple example of a Discord bot using the [discord.py](https://discordpy.readthedocs.io/en/latest/) library.

## Installation

The application is distributed as a Docker image. It is available from the [GitHub Container Registry](https://github.com/thijsfranck?tab=packages&repo_name=discord-app-example):

```bash
docker pull ghcr.io/thijsfranck/discord-app-example:latest
```

## Usage

Once you have pulled the Docker image, you can run the bot using the following command:

```bash
docker run -e DISCORD_TOKEN=your_token ghcr.io/thijsfranck/discord-app-example:latest
```

> [!IMPORTANT]
> The bot requires a Discord bot token to run. You can create a new bot and obtain a token from the [Discord Developer Portal](https://discord.com/developers/applications).
>
> Your token should have the `bot` scope. Do not share your token with anyone!

## Development

See the [contribution guide](./CONTRIBUTING.md) for instructions and guidelines on setting up the development environment and working on the project.

## License

This project is licensed under the [MIT license](./LICENSE).
