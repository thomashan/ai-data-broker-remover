.PHONY: install-miniforge setup create-conda-env activate-conda-env help

# OS Detection
DETECTED_OS := $(shell uname -s)

# Install miniforge based on operating system
install-miniforge:
	@echo "Installing miniforge for $(DETECTED_OS)..."
	@case "$(DETECTED_OS)" in \
		Darwin) \
			echo "Detected macOS - installing via Homebrew..."; \
			if ! command -v brew >/dev/null 2>&1; then \
				echo "❌ Homebrew is not installed. Please install Homebrew first."; \
				exit 1; \
			fi; \
			brew install --cask miniforge; \
			;; \
		Linux) \
			echo "Detected Linux - detecting architecture..."; \
			ARCH=$$(uname -m); \
			case "$$ARCH" in \
				x86_64) MINIFORGE_URL="https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh";; \
				aarch64) MINIFORGE_URL="https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh";; \
				*) echo "❌ Unsupported Linux architecture: $$ARCH"; exit 1;; \
			esac; \
			echo "Detecting package manager to install dependencies..."; \
			if command -v apt-get >/dev/null 2>&1; then \
				echo "Using apt (Ubuntu/Debian)..."; \
				sudo apt-get update && sudo apt-get install -y wget; \
			elif command -v yum >/dev/null 2>&1; then \
				echo "Using yum (RHEL/CentOS)..."; \
				sudo yum install -y wget; \
			elif command -v dnf >/dev/null 2>&1; then \
				echo "Using dnf (Fedora)..."; \
				sudo dnf install -y wget; \
			elif command -v pacman >/dev/null 2>&1; then \
				echo "Using pacman (Arch Linux)..."; \
				sudo pacman -S --noconfirm wget; \
			elif command -v zypper >/dev/null 2>&1; then \
				echo "Using zypper (openSUSE)..."; \
				sudo zypper install -y wget; \
			else \
				echo "❌ Unsupported Linux distribution. Please install wget manually."; \
				exit 1; \
			fi; \
			echo "Downloading Miniforge from $$MINIFORGE_URL..."; \
			wget $$MINIFORGE_URL -O miniforge.sh; \
			bash miniforge.sh -b -u -p $$HOME/miniforge3; \
			rm miniforge.sh; \
			;; \
		*) \
			echo "❌ Unsupported operating system: $(DETECTED_OS)"; \
			exit 1; \
			;; \
	esac
	@echo "✅ Miniforge installed successfully"
	@echo "Please restart your terminal or run the conda init command for your shell."

# Setup: check if miniforge exists, and install if missing
setup:
	@echo "Checking if Miniforge is installed..."
	@if ! (command -v conda >/dev/null 2>&1 && conda info | grep -q "conda-forge"); then \
		echo "Miniforge not found. Installing..."; \
		$(MAKE) install-miniforge; \
	else \
		echo "✅ Miniforge is already installed."; \
		conda --version; \
	fi

# Create conda environment with Python 3.13
create-conda-env:
	@echo "Creating conda environment 'ai-data-broker-remover' with Python 3.13..."
	@if conda env list | grep -q "ai-data-broker-remover"; then \
		echo "✅ Environment 'ai-data-broker-remover' already exists"; \
	else \
		echo "Creating new environment..."; \
		conda create -n ai-data-broker-remover python=3.13 -y; \
		echo "✅ Environment 'ai-data-broker-remover' created successfully"; \
		echo "To activate the environment, run:"; \
		echo "  conda activate ai-data-broker-remover"; \
	fi

# Activate conda environment
activate-conda-env: create-conda-env
	@echo "To activate the environment, run the following command:"
	@echo "conda activate ai-data-broker-remover"

help:
	@echo "Available targets:"
	@echo "  setup              - Installs Miniforge if not already present."
	@echo "  create-conda-env   - Creates the conda environment. Run this after 'setup' and after restarting your terminal."
	@echo "  activate-conda-env - Shows the command to activate the conda environment."
	@echo "  install-miniforge  - Install miniforge using platform-specific method"
	@echo "  help               - Show this help message"
	@echo ""
	@echo "Supported platforms:"
	@echo "  - macOS: Uses Homebrew (brew install --cask miniforge)"
	@echo "  - Linux: Downloads and installs from GitHub releases"
	@echo "    - Ubuntu/Debian (apt-get)"
	@echo "    - RHEL/CentOS (yum)"
	@echo "    - Fedora (dnf)"
	@echo "    - Arch Linux (pacman)"
	@echo "    - openSUSE (zypper)"