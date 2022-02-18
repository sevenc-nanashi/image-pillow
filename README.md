# pjsekai_background_gen_pillow

Generates PJSekai background image from Image.

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
