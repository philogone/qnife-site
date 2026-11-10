"""Génère public/og-default.jpg (1200x630) depuis la photo hero et les polices de la marque."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FONTS = os.path.join(ROOT, '..', '_work', 'fonts')
W, H, PW = 1200, 630, 520
bg = Image.new('RGB', (W, H), (13, 13, 14))
ph = Image.open(os.path.join(ROOT, 'public', 'img', 'hero-chef-1200.webp')).convert('RGB')
crop_h = int(1200 * H / PW)
r = ph.crop((0, 300, 1200, 300 + crop_h)).resize((PW, H))
bg.paste(r, (W - PW, 0))
fade = Image.new('L', (160, H))
for x in range(160):
    fade.paste(int(255 * (1 - x / 160)), (x, 0, x + 1, H))
bg.paste(Image.new('RGB', (160, H), (13, 13, 14)), (W - PW, 0), fade)
d = ImageDraw.Draw(bg)
q = ImageFont.truetype(os.path.join(FONTS, 'PetitFormalScript-Regular.ttf'), 180)
t = ImageFont.truetype(os.path.join(FONTS, 'Mostra Nuova', 'Mostra Nuova Bold.otf'), 64)
s = ImageFont.truetype(os.path.join(FONTS, 'Mostra Nuova', 'Mostra Nuova Light.otf'), 32)
paper = (244, 242, 238)
d.text((70, 70), 'Q', font=q, fill=paper)
d.text((70, 330), 'Votre histoire,', font=t, fill=paper)
d.text((70, 405), 'votre couteau.', font=t, fill=paper)
d.text((70, 520), 'Coutelier des Hauts-de-France · qnife.fr', font=s, fill=(190, 190, 190))
bg.save(os.path.join(ROOT, 'public', 'og-default.jpg'), quality=86)
print('og ok')
