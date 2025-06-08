#!/bin/bash

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "📦 uv is not installed. Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Install dependencies
echo "⬇️  Installing dependencies..."
uv sync

# Init git
echo "🔧 Initializing git..."
git init

# Install pre-commit hooks
echo "🪝 Installing pre-commit hooks..."
uv run pre-commit install
