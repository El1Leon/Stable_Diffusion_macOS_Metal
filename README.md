# Stable Diffusion on macOS with Metal Acceleration

Run **Stable Diffusion XL (SDXL)** natively on Apple Silicon Macs (M1 / M2 / M3) using **PyTorch with Metal (MPS) acceleration**.

This project is based on 🤗 Hugging Face **diffusers** and uses a simple `generate.py` script to prompt and generate images locally on macOS.

---

## 🚀 What This Project Does

- Runs Stable Diffusion **locally** on macOS  
- Uses **Apple Metal (MPS)** instead of CUDA  
- Prompts for text input directly in the terminal  
- Saves generated images automatically  
- Works offline after first model download  

---

## 🔧 Requirements

- macOS **13.1+**
- Apple Silicon (M1, M2, or M3)
- Python **3.10+**
- Xcode Command Line Tools
- `pip` and `virtualenv`

Install Xcode Command Line Tools if needed:

```bash
xcode-select --install
