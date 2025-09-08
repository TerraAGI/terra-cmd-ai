# Contributing to Terra Command AI

Thank you for your interest in contributing to Terra Command AI! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Code Style](#code-style)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors
- Help create a positive community

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- OpenAI API key (optional, for AI features)

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

   ```bash
   git clone https://github.com/YOUR_USERNAME/terra-commands.git
   cd terra-commands
   ```

3. Set up the upstream remote:

   ```bash
   git remote add upstream https://github.com/terra-agi/terra-commands.git
   ```

## Development Setup

### Installation

1. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install in development mode:

   ```bash
   make install-dev
   # or
   pip install -e .[dev]
   ```

3. Set up pre-commit hooks (optional):

   ```bash
   pip install pre-commit
   pre-commit install
   ```

### Configuration

Edit `.env` and add your OpenAI API key and Model if you have one:

   ```bash
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL=your_open_ai_model
   ```

## Making Changes

### Branch Naming

Use descriptive branch names:

- `feature/add-new-command-patterns`
- `bugfix/fix-os-detection-linux`
- `docs/update-installation-guide`
- `refactor/split-monolithic-class`

### Commit Messages

Follow conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:

- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Testing related changes
- `chore`: Maintenance tasks

Examples:

```
feat: add support for Windows command patterns
fix: correct OS detection on Ubuntu systems
docs: update installation instructions for macOS
```

## Testing

### Running Tests

```bash
# Run all tests
make test

# Run with verbose output
make test-verbose

# Run with coverage
make test-coverage

# Run specific test file
python -m pytest tai/tests/test_os_detector.py -v
```

### Writing Tests

- Place tests in `tai/tests/` directory
- Name test files as `test_*.py`
- Use descriptive test method names: `test_should_handle_invalid_command`
- Include docstrings for test methods
- Use `unittest.mock` for mocking dependencies

Example:

```python
import unittest
from unittest.mock import patch

class TestOSDetector(unittest.TestCase):
    def test_should_detect_linux_distribution(self):
        """Test that Linux distribution is correctly detected."""
        # Test implementation
        pass
```

### Test Coverage

Aim for high test coverage, especially for:

- Core business logic
- Error handling paths
- Edge cases
- Integration points

## Code Style

### Python Style

This project uses:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

### Formatting

```bash
# Format code
make format

# Check style
make lint
```

### Type Hints

Use type hints for all function parameters and return values:

```python
from typing import Optional, List, Dict

def process_command(command: str, timeout: Optional[int] = None) -> bool:
    """Process a shell command."""
    pass
```

### Docstrings

Use Google-style docstrings:

```python
def execute_command(command: str, dry_run: bool = False) -> Tuple[bool, str, str]:
    """Execute a shell command safely.

    Args:
        command: The shell command to execute
        dry_run: If True, only show what would be executed

    Returns:
        A tuple of (success, stdout, stderr)

    Raises:
        CommandTimeoutError: If command exceeds timeout
    """
```

## Documentation

### Code Documentation

- All public methods and classes must have docstrings
- Include type hints for parameters and return values
- Document exceptions that may be raised
- Provide usage examples where appropriate

### README Updates

When making changes that affect users:

- Update the README.md with new features
- Add examples for new functionality
- Update installation instructions if needed
- Update troubleshooting section for common issues

## Submitting Changes

### Pull Request Process

1. Ensure your branch is up to date with main:

   ```bash
   git checkout main
   git pull upstream main
   git checkout your-branch
   git rebase main
   ```

2. Run tests and linting:

   ```bash
   make test
   make lint
   ```

3. Commit your changes:

   ```bash
   git add .
   git commit -m "feat: add new command pattern support"
   ```

4. Push to your fork:

   ```bash
   git push origin your-branch
   ```

5. Create a Pull Request on GitHub with:
   - Clear title describing the change
   - Detailed description of what was changed and why
   - Screenshots or examples if UI changes
   - Reference to any related issues

### Pull Request Checklist

- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Commit messages follow conventional format
- [ ] Branch is up to date with main
- [ ] No merge conflicts
- [ ] CI checks pass

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

- **Description**: Clear description of the issue
- **Steps to reproduce**: Step-by-step instructions
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, Terra Command AI version
- **Logs**: Any relevant error messages or logs

### Feature Requests

For feature requests, please include:

- **Description**: What feature you'd like to see
- **Use case**: Why this feature would be useful
- **Implementation ideas**: Any suggestions for implementation
- **Alternatives**: Other solutions you've considered

## Development Workflow

1. **Choose an issue** from the issue tracker or create one
2. **Create a branch** for your work
3. **Write tests** for your changes
4. **Implement the feature/fix**
5. **Run tests** and ensure they pass
6. **Update documentation** if needed
7. **Submit a pull request**

## Getting Help

If you need help:

- Check the [README.md](README.md) for documentation
- Search existing issues and pull requests
- Ask questions in discussions
- Reach out to maintainers

Thank you for contributing to Terra Commands AI!
