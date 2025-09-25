# Python Boilerplate

A modern Python project boilerplate with professional development tooling and workflow.

## ✨ Features

- **Modern Python Stack**: Built with Python 3.13+ and UV package manager
- **Code Quality Tools**: Integrated ruff (formatting/linting), mypy (type checking), and pre-commit hooks
- **Configuration Management**: YAML-based configuration with Pydantic validation
- **Developer Experience**: One-command setup and hot-reload development server via Makefile
- **Professional Workflow**: Structured project layout following Python best practices

## 📁 Project Structure

```
python-boilerplate/
├── src/                    # Source code
│   ├── core/              # Core application modules
│   ├── models/            # Data models
│   ├── schemas/           # Pydantic schemas and data validation
│   │   └── common.py      # Common configuration schemas
│   ├── utils/             # Utility functions
│   │   ├── config.py      # Configuration loading utilities
│   │   └── logging.py     # Logging setup utilities
│   ├── config/            # Configuration files
│   │   └── settings.yaml  # Application settings
│   └── main.py           # Main application entry point
├── notebooks/             # Jupyter notebook examples
│   └── basic_usage.ipynb  # Basic usage examples
├── tests/                 # Test files
├── logs/                  # Application logs (created at runtime)
├── Makefile              # Development automation
├── pyproject.toml        # Project configuration and dependencies
├── ruff.toml            # Ruff linting and formatting configuration
├── .pre-commit-config.yaml # Pre-commit hooks configuration
└── README.md            # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- Git (for version control)
- Make (for running Makefile commands)

### Setup

Run the setup command to get everything configured:

```bash
make setup
```

This command will:

- 📦 Install `uv` package manager (if not already installed)
- ⬇️ Install all project dependencies
- 🔧 Initialize git repository (if not already initialized)
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
make dev
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

## 📋 Available Make Commands

### `make setup`

- Sets up the entire development environment
- Installs UV package manager and dependencies
- Configures git and pre-commit hooks
- **When to use**: First time setup or when adding new developers

### `make dev`

- Starts the development server with hot-reload
- Monitors file changes and auto-restarts
- **When to use**: Daily development work

### `make help`

- Shows all available make targets
- **When to use**: To see what commands are available

## 🎯 Getting Started with Development

1. **Clone and Setup**:

   ```bash
   git clone <repository-url>
   cd python-boilerplate
   make setup
   ```

2. **Start Development**:

   ```bash
   make dev
   ```

3. **Make Changes**: Edit files in `src/` and see changes automatically reflected

4. **Quality Checks**: Pre-commit hooks will run automatically, or run them manually:
   ```bash
   uv run ruff check src/
   uv run mypy src/
   ```

## 🔧 Configuration

The project uses a YAML-based configuration system with Pydantic validation:

- **Configuration File**: `src/config/settings.yaml`
- **Schema Definition**: `src/schemas/common.py`
- **Loading Utilities**: `src/utils/config.py`

The configuration system automatically finds the project root and loads settings with proper type validation.

## 🤝 Contributing

This project follows modern Python development practices:

- Code is automatically formatted with ruff
- Type hints are used throughout
- Pre-commit hooks ensure quality
- All changes should include appropriate tests

## 📚 Additional Resources

- **PyProject.toml**: Modern Python project configuration with UV dependency management
- **UV**: Fast Python package manager and project manager
- **Ruff**: The fastest Python linter and formatter with comprehensive rule set
- **MyPy**: Static type checking for Python with strict configuration
- **Pydantic**: Data validation and settings management using Python type annotations
- **Pre-commit**: Git hook framework for code quality automation
