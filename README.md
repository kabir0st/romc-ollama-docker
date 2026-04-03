# Ollama + Open WebUI Docker Setup

Docker Compose setup for running **Ollama** with **Open WebUI** on AMD GPUs (ROCm).

## Services

| Service | Image | Port |
|---------|-------|------|
| Ollama | `ollama/ollama:rocm` | `11434` |
| Open WebUI | `ghcr.io/open-webui/open-webui:main` | `3000` |

## Prerequisites

- Docker and Docker Compose
- AMD GPU with ROCm drivers installed
- `/dev/kfd` and `/dev/dri` devices available

## Quick Start

```bash
git clone https://github.com/kabir0st/romc-ollama-docker/
cd romc-ollama-docker
docker compose up -d
```

## Access

- **Open WebUI**: http://localhost:3000
- **Ollama API**: http://localhost:11434

## Pull a Model

```bash
docker exec ollama ollama pull deepseek-r1:8b
```

## Stop Services

```bash
docker compose down
```

To also remove stored data (models, conversations):

```bash
docker compose down -v
```

## Continue IDE Integration

Copy `continue-config.json` to your Continue config directory to use Ollama as a local coding assistant.
