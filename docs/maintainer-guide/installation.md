# Installation

This section provides instructions on how to install the application.

!!! NOTE "Prerequisites"
    The application is distributed as a [Docker](https://www.docker.com/) image. Please ensure that you have Docker
    installed on your system.

Open your terminal and run the following command to install the latest version of the application:

```bash
docker run -e DISCORD_TOKEN="<YOUR_TOKEN>" ghcr.io/thijsfranck/discord-app-example:latest
```

Replace `<YOUR_TOKEN>` with your Discord bot token.

The application will start and connect to Discord using the provided token. You can now interact with the bot
in your Discord server.

!!! QUESTION "Where do I find my Discord bot token?"
    See the configuration section for instructions on [how to obtain a Discord bot token](./configuration.md#discord_token).

!!! QUESTION "What other options are available?"
    The application supports additional environment variables that you can use to customize its behavior. Refer
    to the [configuration](configuration.md) section for a list of available options.

!!! QUESTION "Where can I find previous versions of the image?"
    Previous versions of the image are available on the [GitHub Container Registry](https://github.com/thijsfranck/discord-app-example/pkgs/container/discord-app-example).
