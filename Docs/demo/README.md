# Demo GIF

`../demo.gif` is built from the real images in `Docs/assets/` (hero, `features/`, `states/`) plus HTML overlays (step list, captions, crossfades, the "30 minutes later" card). No UI is drawn that the app does not have; captions use the wording of the README.

Rebuild (macOS, needs Google Chrome, ffmpeg and gifsicle; does not run the app):

```sh
python3 Docs/demo/build_demo.py
```

Set `DEMO_FRAMES_DIR=/some/dir` to cache rendered frames between runs.
