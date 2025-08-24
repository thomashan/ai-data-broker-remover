# Project Structure

ai-data-broker-remover/
└── app/
    └── brokers/
        ├── pyproject.toml         # Core config for uv: dependencies, project info
        ├── uv.lock                # Ensures reproducible builds
        ├── .venv/                 # Virtual environment created and managed by uv
        ├── src/
        │   └── brokers/           # Your installable source package
        │       ├── crewai/
        │       ├── __init__.py
        │       ├── main.py
        │       └── ...
        ├── tests/
        │   ├── __init__.py
        │   └── test_main.py       # Your tests, written first
        ├── .gitignore
        ├── Dockerfile
        └── ... (prompts, resources, .env files, etc.)
