# Python Project

A modern Python project template with professional development tooling and workflow.

## ✨ Features

- **Modern Python Stack**: Built with Python 3.13+ and modern package management
- **Code Quality Tools**: Integrated ruff (formatting/linting), mypy (type checking), and pre-commit hooks
- **Developer Experience**: One-command setup and hot-reload development server
- **Professional Workflow**: Structured project layout following Python best practices

## 📁 Project Structure

```
python-project/
├── src/                    # Source code
│   ├── app/               # Main application package
│   └── basic_usage.ipynb  # Jupyter notebook examples
├── scripts/               # Development scripts
│   ├── setup.sh          # Project setup script
│   └── dev.sh            # Development server script
├── tests/                 # Test files
├── dist/                 # Distribution files
├── pyproject.toml        # Project configuration
├── ruff.toml            # Ruff configuration
├── .pre-commit-config.yaml # Pre-commit hooks
└── README.md            # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- Git (for version control)

### Setup

Run the setup script to get everything configured:

```bash
./scripts/setup.sh
```

This script will:

- 📦 Install `uv` package manager (if not already installed)
- ⬇️ Install all project dependencies
- 🔧 Initialize git repository
- 🪝 Set up pre-commit hooks

### Verify Installation

After setup, you can verify everything works:

```bash
uv run start
```

## 🛠️ Development Workflow

### Development Server

Start the development server with hot-reload:

```bash
./scripts/dev.sh
```

This will:

- 🚀 Start a development server
- 👀 Watch for file changes in `src/`
- 🔄 Automatically restart when code changes
- 🧹 Clear console on each restart for better visibility

The development server uses `watchfiles` to monitor your source code and automatically restarts the application when you make changes.

## 🔧 Development Tools

This project uses modern Python development tools for code quality and consistency:

### Ruff (Formatting & Linting)

- **Purpose**: Fast Python linter and formatter
- **Usage**: Automatically formats code and catches common issues
- **Config**: See `ruff.toml` for configuration
- **Run manually**: `uv run ruff check` and `uv run ruff format`

### MyPy (Type Checking)

- **Purpose**: Static type checking for Python
- **Usage**: Ensures type safety and catches type-related bugs
- **Run manually**: `uv run mypy src/`

### Pre-commit Hooks

- **Purpose**: Automatically run quality checks before commits
- **Usage**: Installed automatically during setup
- **Benefits**: Prevents committing code that doesn't meet quality standards

These tools work together to maintain high code quality and consistency across the project.

## 📋 Project Scripts

### `scripts/setup.sh`

- Sets up the entire development environment
- Installs dependencies and tools
- Configures git and pre-commit hooks
- **When to use**: First time setup or when adding new developers

### `scripts/dev.sh`

- Starts the development server with hot-reload
- Monitors file changes and auto-restarts
- **When to use**: Daily development work

## 🎯 Getting Started with Development

1. **Clone and Setup**:

   ```bash
   git clone <repository-url>
   cd python-project
   ./scripts/setup.sh
   ```

2. **Start Development**:

   ```bash
   ./scripts/dev.sh
   ```

3. **Make Changes**: Edit files in `src/` and see changes automatically reflected

4. **Quality Checks**: Pre-commit hooks will run automatically, or run them manually:
   ```bash
   uv run ruff check src/
   uv run mypy src/
   ```

## 🤝 Contributing

This project follows modern Python development practices:

- Code is automatically formatted with ruff
- Type hints are used throughout
- Pre-commit hooks ensure quality
- All changes should include appropriate tests

## 📚 Additional Resources

- **PyProject.toml**: Modern Python project configuration
- **UV**: Fast Python package manager and project manager
- **Ruff**: The fastest Python linter and formatter
- **MyPy**: Optional static typing for Python
