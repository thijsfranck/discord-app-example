# Contributing

To ensure a smooth collaboration, we have outlined some guidelines to follow when making contributions. Your adherence to these guidelines helps us maintain the quality and clarity of the project.

## Getting Started

Follow the steps below to get started with the development environment.

### Cloning the Repository

To clone the repository, run the following command:

```bash
git clone https://github.com/thijsfranck/discord-app-example.git
```

### Environment Setup

You can set up the development environment using either the automated or manual setup process.

#### Automated Setup

The project includes a [development container](https://containers.dev) to automatically set up your development environment.

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

Next, install the pre-commit hooks:

```bash
poetry run pre-commit install
```

### Discord Bot Token

Your Discord bot token should be stored in a `.env` file in the project root directory:

```plaintext
DISCORD_TOKEN=your_token
```

See the [Usage section of the README](README.md#usage) on how to obtain a Discord bot token.

## Running the Bot

With your development environment and the Discord bot token set up, you can run the bot using the following command:

```bash
poetry run python main.py
```

## Version Control

When making changes to the project, follow these guidelines to ensure a smooth contribution process.'

### Creating a new Branch

Always create a new branch for your changes. This makes it easier to handle multiple contributions simultaneously.

First, pull the latest changes from the `master` branch:

```bash
git pull master
```

Next, create a new branch. Name it descriptively:

```bash
git checkout -b BRANCH_NAME
```

Once you have committed your changes, push the branch to the repository:

```bash
git push -u origin BRANCH_NAME
```

### Commit Guidelines

Commits should follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. This helps maintain a clean and structured commit history.

Here's an example of a good commit message:

```plaintext
feat: add uptime command

Add a new command to display the bot's uptime.
```

Try to keep your commits focused on a single task. If you need to make multiple changes, create separate commits for each change.

> [!TIP]
> The development container includes [Commitizen](https://commitizen-tools.github.io/commitizen/) to help you write conventional commit messages. Run `cz commit` to create a commit message interactively.

### Pre-commit Hooks

The project includes pre-commit hooks to ensure your code meets the quality standards. These hooks run automatically before each commit.

The pre-commit hooks include:

- Linting and formatting with [Ruff](https://docs.astral.sh/ruff/)
- Commit message validation with [Commitlint](https://commitlint.js.org)

> [!NOTE]
> If the pre-commit hooks fail, you will need to address the issues before committing your changes.

### Pull Requests

Once you have completed your changes, it's time to create a pull request. A pull request allows your changes to be reviewed and merged into the `master` branch.

Before creating a pull request, ensure your branch is up to date with the latest changes from the `master` branch:

```bash
git pull master
```

Next, push your changes to the repository:

```bash
git push
```

Finally, [create a pull request on GitHub](https://github.com/thijsfranck/discord-app-example/compare). Select your branch as the source and the `master` branch as the base.

In the pull request description, provide a brief overview of the changes and any relevant information for reviewers.

#### Automated Checks

The project includes automated checks to ensure the code meets the quality standards. These checks include:

- All [pre-commit hooks](#pre-commit-hooks) must pass
- Type checking with [Pyright](https://github.com/microsoft/pyright)
- Unit tests with [pytest](https://docs.pytest.org/en/stable/)

> [!NOTE]
> If any of the automated checks fail, please address the issues before requesting a review.

#### Code Review

All pull requests should be reviewed by at least one other team member before merging. The reviewer will provide feedback and suggestions for improvement.

> [!TIP]
> Request a review from a team member by assigning them to the pull request.

A code review should focus on the following aspects:

- Correctness and functionality
- Code quality and readability
- Adherence to the project guidelines

Once the reviewer approves the pull request, you can merge it into the `master` branch.

##### Giving Feedback

When providing feedback on a pull request, be constructive and specific. Point out areas for improvement and suggest possible solutions. If you have any questions or concerns, don't hesitate to ask the author for clarification.

> [!IMPORTANT]
> Always be respectful and considerate when giving feedback.
> Remember that the goal is to improve the code and help the author grow as a developer.
>
> Don't forget to acknowledge the positive aspects of the contribution as well!

Here are some examples of good code review feedback:

```plaintext
- Great work on the new command! The implementation looks good overall.
- I noticed a small typo in the docstring. Could you update it to fix the typo?
- The logic in the new command is a bit complex. Consider breaking it down into smaller functions for clarity.
- The tests cover most of the functionality, but we are missing a test case for edge case X. Could you add a test for that?
```

### Release

To build and push a new version of the Docker image, create a new release on GitHub along with a new tag. The GitHub Actions workflow will automatically build and push the image to the registry.

> [!NOTE]
> Tags should follow the [Semantic Versioning](https://semver.org/) format. For example, `v1.0.0`.

## Code Documentation

Good code documentation aids understanding and speeds up the development process. It also helps boost our final score 😁.

### What to Document

Always document the following elements of your code:

1. **Classes**: including their **attributes and public methods**
2. **Module-level functions and constants**

Prioritize documenting public methods and attributes (those not starting with an underscore). However, private methods with complex logic should also be documented for clarity.

### Docstring Format

This project uses numpy-style docstrings. When documenting your code, please adhere to this style.

> [!TIP]
> Refer to the [style guide](https://numpydoc.readthedocs.io/en/latest/format.html) for the full specification and detailed examples.

For reference, here's a complete example of a function or method docstring in numpy-style:

```python
def example_function(param1: int, param2: str):
    """
    One-line summary of the function.

    Detailed functional description of what the function does. Can span
    multiple lines.

    Parameters
    ----------
    param1 : int
        Description of the first parameter.
    param2 : str
        Description of the second parameter.

    Returns
    -------
    bool
        Description of the return value.

    Raises
    ------
    ValueError
        Description of the error.

    Examples
    --------
    >>> example_function(1, "test")
    True
    """
    ...
```

For classes and attributes:

```python
class Example:
    """
    Class-level docstring describing the class.

    Attributes
    ----------
    attribute : int
        Description of the attribute.
    """

    attribute: int
```

### Type Annotations

Python type annotations are strongly encouraged to improve code readability and maintainability. Use type hints for all parameters and return values, as well as class attributes.

## Unit Testing

Unit tests are key to our success, since they allow us to catch bugs early, run sections of code in isolation, and accelerate our development pace.

We use the [`pytest`](https://docs.pytest.org) framework for writing and running our tests.

### Structure

Test modules should be located in the same directory as the module they cover. Test modules should be named `test__*.py` (e.g.,` test__example.py`). Individual test methods within those modules should be prefixed with `test__` (e.g., `test__my_function`). See the example below:

```plaintext
project_root/
├── discord_app_example/
│   ├── __init__.py
│   ├── example.py
│   └── test__example.py
├── conftest.py
└── ...
```

### What to Test

Unit tests should cover the following aspects of your code:

- Input validation
- Correctness of output (or outcome) given a valid input
- Error handling

> [!TIP]
> When writing tests, consider edge cases, invalid inputs, and unexpected behavior. These are often the areas where bugs are most likely to occur.

Some parts of the code may be more critical than others. Focus on writing tests for the most critical parts of the codebase, such as complex algorithms, core functionality or user-facing features.

### Writing Tests

Each test case should be self-contained and independent of other tests. This means that each test should set up its own data and clean up after itself. Avoid relying on the state of other tests or the order in which tests are run.

When writing tests, follow these guidelines:

- Use descriptive test names that clearly indicate what is being tested.
- Limit each test to a single logical concept.
- Use the `assert` statement to check the expected outcome of the test.
- Aim for one `assert` statement per test.
- Use [fixtures](https://docs.pytest.org/en/latest/explanation/fixtures.html) to set up common data or resources that multiple tests need.

> [!TIP]
> The `conftest.py` file at the root of the project can be used to define fixtures that are available to all test modules.
>
> The `examples` folder includes [sample tests](./examples/test__example.py) that you can use as a base for your own test.

### Running Tests

To run the tests, use the following command from the root of the project:

```bash
poetry run pytest
```

This command will discover and run all the tests that match the pattern `test__*.py`.

### Unit Testing and Type Annotations

You can reduce the need for unit tests by indicating the expected types of input arguments and return values as type annotations. While they don't replace unit tests, type annotations can reduce the number of tests you might need to write, particularly those related to input validation.

For instance, consider the following function without type annotations:

```python
def add(a, b):
    return a + b
```

Without type annotations, you might write multiple tests to ensure that the function behaves correctly with different types of input, like strings, integers, or floats. But with type annotations:

```python
def add(a: int, b: int) -> int:
    return a + b
```

The function's expected behavior is clearer. You know that both `a` and `b` should be integers, and the return value will also be an integer. With these type annotations in place, there's less need to write unit tests checking for behaviors with non-integer inputs since the static type checker can catch those mistakes for you.
