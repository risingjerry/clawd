#!/usr/bin/env python3
"""Build Docs/demo.gif from the real Docs/assets images plus HTML overlays.

Frames are rendered by headless Chrome (2x) from demo.html, then assembled with
ffmpeg palettegen/paletteuse. Usage: python3 Docs/demo/build_demo.py
"""
import hashlib, json, os, shutil, subprocess, sys, tempfile, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = os.path.join(HERE, "..", "demo.gif")
FPS = 10
tl = []  # (state, duration seconds)

def add(state, d=1 / FPS): tl.append((state, d))

def fade(a, b, **kw):
    """3-frame crossfade from layer a to layer b (a may be None)."""
    for i in range(1, 4):
        t = i / 4
        op = {b: t}
        if a: op[a] = 1 - t
        add(dict(op=op, **kw))

def hold(layer, d, **kw): add(dict(op={layer: 1}, **kw), d)

C1 = "A <span>pixel pet</span> for your desktop: timer, to-dos, bedtime"
C2 = "Press <span>Start Work</span>: a 30-minute timer starts"
C2b = "<span>12 pixel work scenes</span> switch at random"
C3a = "Time is up: Clawd takes over the screen"
C3 = "<span>Forced rest</span>: the screen is covered for 3 minutes"
C4 = "<span>Todo board</span>: your open Apple Reminders, 5 by default"
C5a = "<span>Bedtime guard</span> warns 1 hour, 30 and 5 minutes before"
C5 = "Then a 15-minute screen takeover, then lock and display sleep"

hold("pet", 2.2, step=1, cap=C1)
fade("pet", "work", step=2, cap=C2)
hold("work", 2.2, step=2, cap=C2)
fade("work", "grid", step=2, cap=C2b, n=0)
for n in range(1, 13):
    add(dict(op={"grid": 1}, step=2, cap=C2b, n=n), 0.15)
hold("grid", 0.8, step=2, cap=C2b, n=12)
fade("grid", "black", step=3, cap=C3a, bt="30 minutes later", bs="rest time")
hold("black", 0.9, step=3, cap=C3a, bt="30 minutes later", bs="rest time")
fade("black", "brk", step=3, cap=C3)
hold("brk", 2.6, step=3, cap=C3)
fade("brk", "todo", step=4, cap=C4)
hold("todo", 2.6, step=4, cap=C4)
fade("todo", "warn", step=5, cap=C5a)
hold("warn", 2.2, step=5, cap=C5a)
fade("warn", "bed", step=5, cap=C5)
hold("bed", 3.0, step=5, cap=C5)

def shot(state, path):
    url = "file://" + os.path.join(HERE, "demo.html") + "#" + urllib.parse.quote(json.dumps(state))
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--window-size=1000,620", "--virtual-time-budget=400", f"--screenshot={path}", url],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    keep = os.environ.get("DEMO_FRAMES_DIR")  # optional: reuse rendered frames between runs
    tmp = keep or tempfile.mkdtemp(prefix="demo-frames-")
    os.makedirs(tmp, exist_ok=True)
    try:
        cache, lines = {}, []
        for st, d in tl:
            key = json.dumps(st, sort_keys=True)
            if key not in cache:
                p = os.path.join(tmp, "f" + hashlib.md5(key.encode()).hexdigest()[:12] + ".png")
                if not os.path.exists(p): shot(st, p)
                cache[key] = p
            lines.append((cache[key], d))
        lst = os.path.join(tmp, "list.txt")  # ffmpeg concat: last duration is honoured only if the file is repeated
        with open(lst, "w") as f:
            for i, (p, d) in enumerate(lines):
                if i == len(lines) - 1: d /= 2  # the repeated last file below repeats this duration
                f.write(f"file '{p}'\nduration {d:.3f}\n")
            f.write(f"file '{lines[-1][0]}'\n")  # concat needs a repeated last file to honour the final hold
        pal = os.path.join(tmp, "pal.png")
        vf = "fps=10,scale=960:-1:flags=lanczos"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-vf", vf + ",palettegen=max_colors=128:stats_mode=diff", pal], check=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-i", pal, "-lavfi", vf + "[x];[x][1:v]paletteuse=dither=none:diff_mode=rectangle", OUT], check=True)
        if shutil.which("gifsicle"):
            subprocess.run(["gifsicle", "-O3", "-b", OUT], check=True, stderr=subprocess.DEVNULL)
        print("wrote", os.path.normpath(OUT), os.path.getsize(OUT) // 1024, "KB,", sum(d for _, d in tl), "s")
    finally:
        if not keep: shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    sys.exit(main())
