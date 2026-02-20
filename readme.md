# FlowFree

FlowFree is a local SDXL image generation app with a Gradio web UI.

## Project layout

- `src/flowfree/`: application entrypoints and runtime wiring.
- `modules/`: generation pipeline, config, metadata, UI helpers.
- `extras/`: auxiliary models and preprocessors.
- `ldm_patched/`: patched diffusion/runtime internals.
- `models/`: checkpoints, loras, vae, controlnet, prompt expansion assets.
- `presets/`: preset defaults.
- `sdxl_styles/`: style definitions and sample previews.
- `javascript/`, `css/`, `language/`: web UI assets.

## Run

1. Install Python 3.10 and dependencies:

```bash
pip install -r requirements_versions.txt
```

2. Start app:

```bash
python flowfree_entry.py
```

3. Open browser at `http://127.0.0.1:7865`.

## Notes

- Keep model files inside `models/` subfolders.
- Use `presets/*.json` to change defaults.
- Main launcher wrappers remain in repo root for compatibility, while source entrypoints live in `src/flowfree/`.
