# 🚀 Ollama + Open WebUI Docker Setup 🖥️

Welcome to the **Ollama + Open WebUI Docker Setup** repository! This project provides a seamless way to deploy **Ollama** and **Open WebUI** using Docker Compose. Whether you're a developer, researcher, or just curious, this setup will get you up and running in no time! 🎉

---

## 📦 Services Overview

This setup includes two main services:

1. **Ollama** 🦙  
   - **Image**: `ollama/ollama:rocm`  
   - **Port**: `11434`  
   - **Description**: Ollama is a powerful service for running large language models locally.  

2. **Open WebUI** 🌐  
   - **Image**: `ghcr.io/open-webui/open-webui:cuda`  
   - **Port**: `3000` (mapped to `8080` inside the container)  
   - **Description**: Open WebUI provides a user-friendly interface to interact with Ollama's models.  

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:
- **Docker** 🐳  
- **Docker Compose** 🐙  
- **AMD GPU Drivers** (for ROCm support)  

---

## 🚀 Quick Start

1. **Clone this repository**:
   ```bash
   git clone https://github.com/kabir0st/romc-ollama-docker/
   cd romc-ollama-docker
    ```
   
2. **Start service**:
   ```bash
   docker compose up
    ```
   
3. **Access the service**:
   - Ollama API: http://10.1.0.2:11434
   - Open WebUI: http://10.1.0.2:8080

---

