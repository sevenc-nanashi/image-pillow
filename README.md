# pjsekai_background_gen_pillow
[![Python Versions](https://img.shields.io/pypi/v/pjsekai_background_gen_pillow.svg)](https://pypi.org/project/pjsekai_background_gen_pillow/)

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