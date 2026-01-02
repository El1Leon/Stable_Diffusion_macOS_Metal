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

Install Xcode CLI tools if needed:

## bash
xcode-select --install

## ⚙️ Setup Instructions

# Clone this repository
git clone https://github.com/El1Leon/Stable_Diffusion_macOS_Metal.git
cd Stable_Diffusion_macOS_Metal

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt


## 🖼️ Generating Images with `generate.py`

Once everything is installed, run:

## bash
python generate.py



