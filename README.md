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

Follow the steps below to get started with the development environment.

### Cloning the Repository

To clone the repository, run the following command:

```bash
git clone https://github.com/thijsfranck/discord-app-example.git
```

### Environment Setup

You can set up the development environment using either the automated or manual setup process.

#### Automated Setup

The project includes a [development container](https//containers.dev) to automatically set up your development environment.

To get started, refer to the setup guide for your IDE:

- [Visual Studio Code](https://code.visualstudio.com/docs/devcontainers/tutorial)
- [PyCharm](https://www.jetbrains.com/help/pycharm/connect-to-devcontainer.html)

> [!TIP]
> Alternatively, you can use a [GitHub Codespace](https://docs.github.com/en/codespaces/getting-started/quickstart) to set up your development environment in the cloud.

#### Manual Setup

If you prefer to set up the development environment manually, follow the steps below.

> [!IMPORTANT]
> Please ensure [Python 3.12](https://www.python.org) and [Poetry](https://python-poetry.org) are installed on your system.

Start by installing the project dependencies using Poetry:

```bash
poetry install
```

It is also recommended to install the pre-commit hooks:

```bash
poetry run pre-commit install
```

### Discord Bot Token

Your Discord bot token should be stored in a `.env` file in the project root directory:

```plaintext
DISCORD_TOKEN=your_token
```

See the [Usage](#usage) section on how to obtain a Discord bot token.

### Running the Bot

With your development environment set up, you can run the bot using the following command:

```bash
poetry run python main.py
```

### Release

To build and push a new version of the Docker image, create a new release on GitHub along with a new tag. The GitHub Actions workflow will automatically build and push the image to the registry.

> [!NOTE]
> Tags should follow the [Semantic Versioning](https://semver.org/) format. For example, `v1.0.0`.

## License

This project is licensed under the [MIT license](./LICENSE).
