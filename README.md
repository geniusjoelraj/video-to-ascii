# Video-to-ASCII

Convert videos or GIFs into ASCII art animations directly in your terminal.

## Features

- Easy setup with Python and dependencies.
- Quick conversion and real-time ASCII rendering.

## Requirements

- Python 3.8+
- [uv](https://pypi.org/project/uv/) (Python task runner)

## Installation & Usage

```bash
# 1. Clone the repository
git clone --depth 1 https://github.com/your-username/video-to-ascii.git
cd video-to-ascii

# 2. Install dependencies
uv add -r requirements.txt

# 3. Prepare your video
mkdir -p videos
# Copy your video or GIF into the videos/ folder

# 4. Run the converter
uv run main.py videos/<your_video>
```
## Custom Kanji-to-ASCII Mapping

This project allows you to use **custom characters** instead of regular ASCII symbols.  
You can map Kanji characters, emojis, or any symbols for a unique video effect.

### Example Configuration

```python
# Kanji characters to use
kanji = "夢希雨光山はしこのいうっ"

# ASCII characters for mapping
ascii_chars = "#$@(+_-."
ascii_inverse = ascii_chars[::-1]  # optional: reversed mapping

# Reverse Kanji if needed
kanji_inverse = kanji[::-1]

# Characters used for rendering
chars = kanji_inverse

# Rendering settings
quality = 170        # Resolution/quality of ASCII output
speed = 0.66         # Frame speed for video/GIF playback
recache = True       # Reprocess frames for caching
recache_ascii = True # Reprocess ASCII conversion for caching
colored = True       # Render ASCII in color
```
