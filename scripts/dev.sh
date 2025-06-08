#!/bin/bash

# Function to run the app with console clearing
run_app() {
    clear
    echo "🔄 Restarting application..."
    python3 -m app.main
}

# Start development server
echo "🚀 Starting development server..."
uv run watchfiles 'bash -c "clear && echo \"🔄 Restarting application...\" && python3 -m app.main"' src/

# Stop development server
echo "✅ Development server stopped"
