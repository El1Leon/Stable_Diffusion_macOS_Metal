# Stable Diffusion on macOS (Metal Accelerated)

This project demonstrates how to run **Stable Diffusion XL** locally on macOS using **Metal (MPS)** acceleration via PyTorch. It's optimized for Apple Silicon (M1/M2/M3) Macs.

## ✨ Features

- ✅ Apple Metal backend (MPS) support
- ✅ SDXL image generation using Hugging Face’s `diffusers`
- ✅ Works without CUDA or external GPU
- ✅ Offline capable after model download

## 🧠 Requirements

- macOS 13+ (Apple Silicon preferred)
- Python 3.10+
- Xcode Command Line Tools
- [Hugging Face account](https://huggingface.co)

## 🔧 Setup

```bash
# Clone the repo
git clone https://github.com/El1Leon/Stable_Diffusion_macOS_Metal.git
cd Stable_Diffusion_macOS_Metal

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
