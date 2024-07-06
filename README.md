# Discord App Example

This is a simple example of a Discord bot using the [discord.py](https://discordpy.readthedocs.io/en/latest/) library.

## Installation

The application is distributed as a Docker image. It is available from the [GitHub Container Registry](https://github.com/thijsfranck?tab=packages&repo_name=discord-app-example):

```bash
docker pull ghcr.io/thijsfranck/discord-app-example:latest
```

## Usage

The bot requires a Discord bot token to run. This token can be provided as an environment variable:

```bash
docker run -e DISCORD_TOKEN=your_token ghcr.io/thijsfranck/discord-app-example:latest
```

## Development

Follow the steps below to set up a development environment for the bot. Start by cloning the repository:

```bash
git clone https://github.com/thijsfranck/discord-app-example.git
```

### Automated Setup

The project includes a [development container](https//containers.dev) to automatically set up your development environment.

To get started, refer to the setup guide for your IDE:

- [Visual Studio Code](https://code.visualstudio.com/docs/devcontainers/tutorial)
- [PyCharm](https://www.jetbrains.com/help/pycharm/connect-to-devcontainer.html)

> [!TIP]
> Alternatively, you can use a [GitHub Codespace](https://docs.github.com/en/codespaces/getting-started/quickstart) to set up your development environment in the cloud.

### Manual Setup

To set up the project locally, first install the dependencies:

```bash
poetry install
```

It is also recommended to install the pre-commit hooks:

```bash
pre-commit install
```

### Discord Bot Token

The bot requires a Discord bot token to run. You can create a new bot and obtain a token from the [Discord Developer Portal](https://discord.com/developers/applications).

> [!IMPORTANT]
> Your token should have the `bot` scope. Do not share your token with anyone.

The token should be stored in a `.env` file in the project root directory:

```plaintext
DISCORD_TOKEN=your_token
```

### Running the Bot

With your development environment set up, you can run the bot using the following command:

```bash
poetry run python main.py
```

## Release

To build and push a new version of the Docker image, create a new release on GitHub along with a new tag. The GitHub Actions workflow will automatically build and push the image to the registry.

> [!NOTE]
> Tags should follow the [Semantic Versioning](https://semver.org/) format. For example, `v1.0.0`.
