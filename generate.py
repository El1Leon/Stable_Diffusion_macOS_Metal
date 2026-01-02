# generate.py
import torch
from diffusers import DiffusionPipeline
from datetime import datetime
import os

# Force MPS on Apple Silicon
device = "mps" if torch.backends.mps.is_available() else "cpu"

print(f"✅ Using device: {device.upper()}")

# Load the SDXL Turbo pipeline
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/sdxl-turbo",
    torch_dtype=torch.float16,
    variant="fp16",
)
pipe.to(device)

# Prompt input
prompt = input("📝 Enter your prompt: ").strip()
if not prompt:
    print("⚠️ Prompt cannot be empty.")
    exit()

# Generate image
print("🎨 Generating image with SDXL Turbo...")
image = pipe(prompt=prompt, num_inference_steps=4, guidance_scale=0.0).images[0]

# Save with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"turbo_output_{timestamp}.png"
image.save(filename)
print(f"✅ Image saved as: {filename}")
