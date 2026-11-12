"""Génère les icônes PNG (écran d'accueil, onglets) : Q en Petit Formal Script sur fond encre.
Usage : python scripts/make-icons.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FONT = os.path.join(ROOT, '..', '_work', 'fonts', 'PetitFormalScript-Regular.ttf')
INK = (13, 13, 14)
PAPER = (244, 242, 238)


def icon(size, out):
    im = Image.new('RGB', (size, size), INK)
    f = ImageFont.truetype(FONT, int(size * 0.78))
    d = ImageDraw.Draw(im)
    box = d.textbbox((0, 0), 'Q', font=f)
    w, h = box[2] - box[0], box[3] - box[1]
    d.text(((size - w) / 2 - box[0], (size - h) / 2 - box[1]), 'Q', font=f, fill=PAPER)
    im.save(os.path.join(ROOT, 'public', out))


icon(180, 'apple-touch-icon.png')
icon(32, 'favicon-32.png')
print('icons ok')
