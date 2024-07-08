# Installation

The application is distributed as a [Docker](https://www.docker.com/) image. Run the following command to install the app:

```bash
docker run -e DISCORD_TOKEN="<YOUR_TOKEN>" ghcr.io/thijsfranck/discord-app-example:latest
```

Replace `<YOUR_TOKEN>` with your Discord bot token. See the [Configuration](configuration.md#discord_token) section for more information.

!!! QUESTION "Where can I find previous versions of the image?"
    Previous versions of the image are available on the [GitHub Container Registry](https://github.com/thijsfranck/discord-app-example/pkgs/container/discord-app-example).
