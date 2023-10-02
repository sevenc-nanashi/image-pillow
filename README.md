# pjsekai_background_gen_pillow
[![Python Versions](https://img.shields.io/pypi/v/pjsekai_background_gen_pillow.svg)](https://pypi.org/project/pjsekai_background_gen_pillow/)

> **Warning**
> This repository is no longer maintained. Please use [pjsekai-background-gen-rust](https://github.com/sevenc-nanashi/pjsekai-background-gen-rust)

Generates PJSekai background image from Image.

## Installation

```
pip install pjsekai_background_gen_pillow
```

## Example

```python
from PIL import Image
import pjsekai_background_gen_pillow as pjbg

generator = pjbg.Generator()
generator.generate(Image.open("path/to/image.png")).save("path/to/output.png")
```

## CLI

You can run `pjsekai_background_gen_pillow`, `pjbg` or `python -m pjsekai_background_gen_pillow` from command line.

```
usage: pjsekai_background_gen_pillow [-h] [-b BACKGROUND] [-f FORMAT] base output

Generates PJSekai background image from Image.

positional arguments:
  base                  Base image file path, or "-" for stdin.
  output                Output image file path, or "-" for stdout.

optional arguments:
  -h, --help            show this help message and exit
  -b BACKGROUND, --background BACKGROUND
                        Background image file path.
  -f FORMAT, --format FORMAT
                        Output image format.
```

## API

### `Generator`

Generater for background images.

##### Parameters

base : PIL.Image

> Base background image.
> Defaults to Built-in background image.

#### `.generate(image)`

Generate background image from source image.

##### Parameters

source : PIL.Image

> Source image.

##### Returns

PIL.Image

## License

This library is licensed under GPLv3. `test.png` is licensed under CC-BY-SA 4.0.
