Stable Diffusion AI Image Generator

Generate stunning images from text prompts using Stable Diffusion, with both Tkinter desktop GUI and Gradio web interface options. 
This project leverages Hugging Face Diffusers, PyTorch, and Gradio to provide an interactive AI art generation experience.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Features

Text-to-Image Generation: Generate images from text prompts.
Stable Diffusion Model: Uses a custom Stable Diffusion model (realisticVisionV60B1_v51HyperVAE.safetensors).
Tkinter GUI: Simple desktop application with a dark-themed GUI for local execution.
Gradio Web Interface: Web-based interface suitable for Jupyter Notebooks and Google Colab.
Auto Save Output: Generated images are saved to the output/ directory.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Tech Stack

Python
PyTorch
Hugging Face Diffusers
Tkinter or Gradio

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Installation

1. Clone the repository:

git clone https://github.com/yourusername/stable-diffusion-image-generator.git
cd stable-diffusion-image-generator

2. Install dependencies:

pip install -r requirements.txt


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Usage

Run Tkinter Desktop GUI:

python app_tkinter.py

This will open a desktop GUI where you can enter prompts and generate images.
------------------------------------------------------------------------
Run Gradio Web Interface (Jupyter/Colab):

!pip install -r requirements.txt
# Execute the Gradio code block provided in the repository

This launches a browser-based interface.


--------------------------------------------------------------------------------------------------------------------

 Example Prompt

> "A futuristic city skyline at sunset with flying cars"

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Future Improvements

Image-to-Image (img2img) generation.

Custom settings: resolution, inference steps, guidance scale.

Streamlit deployment.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
‍ Author

Muskan Ron

GitHub: github.com/Muskan210

LinkedIn: linkedin.com/in/muskan-ron



---

> Note: Model weights must be obtained from authorized sources. This project is for educational purposes.

