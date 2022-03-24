import os
from PIL import Image, ImageOps

assets_dir = os.path.dirname(__file__) + "/assets"
base_normal = Image.open(assets_dir + "/background-base.png")
mask_img = Image.open(assets_dir + "/mask.png").convert("L")
side_mask = Image.open(assets_dir + "/side-mask.png")
frame = Image.open(assets_dir + "/frame.png")


class Deformer:
    """
    Class for ImageOps.deform. Should be used only in internal functions.
    """

    def __init__(self, dist: tuple[int]):
        self.dist = dist

    def getmesh(self, im: Image):
        return [((0, 0, *im.size), self.dist)]


def set_alpha(img, al):
    """
    Set alpha channel of an image. Should be used only in internal functions.
    """
    imga = img.copy()
    imga.putalpha(round(255 * al))
    return imga


class Generator:
    """
    Generater for background images.

    Parameters
    ----------
    base : PIL.Image
        Base background image.
        Defaults to Built-in background image.
    """

    def __init__(self, base: Image = None):
        if base:
            assert base.size == (2048, 1261), "Base image must be 2048x1261"
            self.base = base
        else:
            self.base = base_normal

    def generate(self, source: Image) -> Image:
        """
        Generate background image from source image.

        Parameters
        ----------
        source : PIL.Image
            Source image.

        Returns
        -------
        PIL.Image
        """
        jacket = source.convert("RGBA")
        base = self.base.copy().convert("RGBA")
        base2 = Image.new("RGBA", base.size, (0, 0, 0, 0))
        base3 = Image.new("RGBA", base.size, (0, 0, 0, 0))
        shift = -30
        base3.paste(
            set_alpha(
                ImageOps.deform(
                    jacket.resize((703, 708)),
                    deformer=Deformer((0, -18, -6, 720, 704, 719, 704, 2)),
                ),
                0.8,
            ),
            (449, 98),
        )
        base3.paste(
            set_alpha(
                ImageOps.deform(
                    jacket.resize((618, 706)),
                    deformer=Deformer((1, -43, -5, 707, 621, 721, 616, 2)),
                ),
                0.8,
            ),
            (1019, 48),
        )
        shift = 10
        base2.paste(
            set_alpha(
                ImageOps.deform(
                    jacket,
                    deformer=Deformer(
                        (0, 0, -shift, jacket.height, jacket.width + shift, jacket.height, jacket.width, 0)
                    ),
                ).resize((470, 450)),
                0.8,
            ),
            (787, 189),
        )
        base2.paste(
            set_alpha(
                ImageOps.deform(
                    jacket,
                    deformer=Deformer((0, jacket.height, 0, 0, jacket.width, 0, jacket.width, jacket.height)),
                ).resize((450, 450)),
                0.7,
            ),
            (797, 683),
        )

        # base.save(dir + f"/../dist/bg/{name}.png")
        # base.paste(base2, (0, 0), mask=mask_img)
        buffer = Image.alpha_composite(base, base2)
        buffer.paste(base3, (0, 0), mask=side_mask)
        res = Image.new("RGBA", mask_img.size)
        diff = (buffer.height - mask_img.height) // 2
        # print(buffer.crop((0, diff, base.width, base.height - diff)).size, mask_img.size)
        res.paste(base.crop((0, diff, base.width, base.height - diff - 1)), (0, 0))
        res.paste(buffer.crop((0, diff, base.width, base.height - diff - 1)), (0, 0), mask=mask_img)
        res.paste(frame, (0, -diff), mask=frame)
        res = res.convert("RGB")
        return res
