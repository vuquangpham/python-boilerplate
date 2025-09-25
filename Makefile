.PHONY: setup install-uv sync-deps init-git install-hooks help

# Default target
setup: install-uv sync-deps init-git install-hooks
	@echo "✅ Setup complete!"

# Development mode
dev: 
	@echo "🚀 Starting development server..."
	@uv run watchfiles 'bash -c "clear && echo \"🔄 Restarting application...\" && python3 -m src.main"' src/


# Check if uv is installed, install if not
install-uv:
	@if ! command -v uv &> /dev/null; then \
		echo "📦 uv is not installed. Installing uv..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	else \
		echo "📦 uv is already installed"; \
	fi

# Install dependencies
sync-deps:
	@echo "⬇️  Installing dependencies..."
	@uv sync

# Initialize git repository
init-git:
	@echo "🔧 Initializing git..."
	@git init

# Install pre-commit hooks
install-hooks:
	@echo "🪝 Installing pre-commit hooks..."
	@uv run pre-commit install

# Show help
help:
	@echo "Available targets:"
	@echo "  setup        - Run complete setup (default)"
	@echo "  install-uv   - Install uv package manager"
	@echo "  sync-deps    - Install project dependencies"
	@echo "  init-git     - Initialize git repository"
	@echo "  install-hooks - Install pre-commit hooks"
	@echo "  dev          - Start development server"
	@echo "  help         - Show this help message"
