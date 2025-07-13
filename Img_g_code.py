import os, torch, uuid
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
import gradio as gr

# === Config ===
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
model_path = "./realisticVisionV60B1_v51HyperVAE.safetensors"
device = "cuda" if torch.cuda.is_available() else "cpu"

# === Dummy safety checker ===
def dummy_checker(images, **kwargs):
    return images, [False] * len(images)

# === Load Model ===
print("Loading model …")
try:
    pipe = StableDiffusionPipeline.from_single_file(
        model_path,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None
    ).to(device)
    pipe.safety_checker = dummy_checker
    pipe.enable_attention_slicing()
    pipe.enable_vae_slicing()
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    

# === Image Generation Function ===
def generate_image(prompt):
    if not prompt:
        return "Prompt is empty!", None

    print(f"Generating image for prompt: {prompt}")
    output = pipe(prompt)
    image = output.images[0]

    filename = f"generated_{uuid.uuid4().hex[:8]}.png"
    save_path = os.path.join(OUTPUT_DIR, filename)
    image.save(save_path)

    return f"Image saved to: {save_path}", image

# === Gradio Interface ===
interface = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=[gr.Textbox(label="Status"), gr.Image(label="Generated Image")],
    title="AI Image Generator By Muskan",
    description="It'll Generate images using a Stable Diffusion model via text prompts.",
)

interface.launch(share=True)
