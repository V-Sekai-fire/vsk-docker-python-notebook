# vsk-docker-python-notebook

This guide streamlines setting up a Python notebook using Docker, ensuring all dependencies are self-contained.

**Build the Image:**

1. Clone the repository:
    ```bash
    git clone https://github.com/V-Sekai-fire/vsk-docker-python-notebook.git
    cd vsk-docker-python-notebook
    ```
2. Build the Docker image:
    ```bash
    docker build -t vsk-python-notebook:latest .
    ```

**Run the Container:**

Launch the container with:
```bash
docker run -it --gpus all -p 8888:8888 -v $(pwd):/workspace -v ~/.cache/huggingface:/root/.cache/huggingface --env ROBOFLOW_API_KEY= --env HUGGING_FACE_HUB_TOKEN=<your_huggingface_token> --name vsk-python-notebook vsk-python-notebook:latest
```
Key options:
- `--gpus all`: Enables GPU acceleration (requires NVIDIA Container Toolkit).
- `-p 8888:8888`: Maps the Jupyter Notebook port.
- `-v $(pwd):/workspace`: Mounts your project directory.
- `-v ~/.cache/huggingface:/root/.cache/huggingface`: Shares the Hugging Face cache.
- `--env ROBOFLOW_API_KEY=...`: Provides your token for gated models.
- `--env HUGGING_FACE_HUB_TOKEN=...`: Provides your token for gated models.
- `--name vsk-python-notebook`: Specifies the container name.

**Hugging Face Token:**

Your models may be gated. Generate a token with "Read access to contents" at https://huggingface.co/settings/tokens.

**Access Jupyter Notebook:**

Once started, a URL (e.g., `http://127.0.0.1:8888/?token=<your_token_here>`) will display. Open it in your browser to use the notebook.

