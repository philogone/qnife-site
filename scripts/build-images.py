"""Optimise la sélection de photos : WebP, 3 tailles, + manifeste JSON.
Usage (depuis qnife-site/) :  python scripts/build-images.py
Sources hors dépôt : ../assets-source et ../instagram-export
"""
import json, os, glob
from PIL import Image, ImageOps

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
IG = os.path.join(ROOT, 'instagram-export')
CJ = os.path.join(ROOT, 'assets-source', 'OneDrive_2_10-11-2026', "Photos Capture d'un jour")
OUT = os.path.join(ROOT, 'qnife-site', 'public', 'img')
posts = json.load(open(os.path.join(ROOT, '_work', 'posts.json'), encoding='utf-8'))
os.makedirs(OUT, exist_ok=True)

def ig(post, k=0):
    return os.path.join(IG, posts[post]['imgs'][k])

def cj(n):
    return os.path.join(CJ, f'2024_04_02_Qnife_{n:05d}.jpg')

# (slug, source, alt, catégorie, nom du couteau)
KNIVES = [
    ('gabriel',  ig(3),  "Couteau Gabriel, lame inox et manche en bois sur planche", 'table', 'Gabriel'),
    ('jules',    ig(8),  "Couteau Jules posé sur une assiette ancienne", 'table', 'Jules'),
    ('jules-bois-rose', ig(42), "Trio de couteaux Jules, manches en bois de rose", 'table', 'Jules'),
    ('table-fete', ig(32, 1), "Huit couteaux de table sur un set tressé", 'table', 'Couteaux de table'),
    ('saucisson', ig(17, 1), "Couteau à saucisson, lame forgée et manche en hêtre échauffé", 'table', 'Couteau à saucisson'),
    ('gaston',   ig(49), "Couteau de cuisine Gaston sur planche avec citron vert", 'cuisine', 'Gaston'),
    ('basile',   ig(52), "Couteau de cuisine Basile devant un mur de briques et des herbes", 'cuisine', 'Basile'),
    ('igor',     ig(25), "Couteau de cuisine forgé Igor à côté de pommes", 'forge', 'Igor'),
    ('gyuto',    ig(36, 1), "Gyuto revisité avec manche en bois sur tissu", 'cuisine', 'Gyuto'),
    ('cuisine-macassar', ig(60), "Couteau de cuisine forgé, manche en ébène de macassar", 'cuisine', 'Couteau de cuisine'),
    ('auguste',  ig(13, 1), "Couteau Auguste, manche en ébène grenadille", 'forge', 'Auguste'),
    ('come',     ig(15), "Couteau Côme, lame forgée et manche en érable stabilisé noir", 'forge', 'Côme'),
    ('saucisson-forge', ig(66), "Couteau forgé à saucisson, mitre en laiton et manche en gaïac", 'forge', 'Couteau forgé'),
    ('raoul',    ig(56), "Couteau Raoul sur fond de paille tressée", 'cuisine', 'Raoul'),
    ('cyrus',    ig(16), "Couteau pliant Cyrus en chêne", 'pliant', 'Cyrus'),
    ('louis',    ig(20), "Couteau pliant Louis, manche en bois, sur torchon", 'pliant', 'Louis'),
    ('higonokami', ig(34), "Higonokami personnalisé en laiton gravé", 'pliant', 'Higonokami'),
    ('pliant-ziricote', ig(72), "Couteau pliant à cran forcé en ziricote", 'pliant', 'Pliant ziricote'),
    ('roger',    ig(48), "Couteau pliant Roger posé sur une souche", 'pliant', 'Roger'),
]

ATELIER = [
    ('hero-chef',   cj(59), "Le coutelier présente un couteau de chef dans son atelier"),
    ('forge',       cj(13), "La forge à gaz incandescente"),
    ('etincelles',  cj(18), "Étincelles pendant le meulage d'une lame"),
    ('martelage',   cj(21), "Une lame chauffée au rouge sur l'enclume"),
    ('bois',        cj(27), "Un bloc de bois pour manche tenu en main"),
    ('lame-main',   cj(35), "Une lame brute présentée dans la paume"),
    ('portrait',    cj(75), "Portrait du coutelier dans l'atelier, bras croisés"),
    ('ponceuse',    cj(1),  "Passage d'une lame sur la ponceuse à bande"),
    ('etabli',      cj(39), "Le coutelier à l'établi, concentré sur un manche"),
    ('detail-lame', cj(47), "Détail d'une lame en cours de finition"),
    ('chef-manche', cj(63), "Un manche en os blanc fixé sur une lame"),
]

SIZES = [480, 800, 1200]
manifest = {'knives': [], 'atelier': []}

def export(slug, src, alt):
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    W, H = im.size
    widths = []
    for w in SIZES:
        if w > W:
            w = W
        if w in widths:
            continue
        h = round(H * w / W)
        im.resize((w, h), Image.LANCZOS).save(os.path.join(OUT, f'{slug}-{w}.webp'), 'WEBP', quality=78, method=6)
        widths.append(w)
    return {'slug': slug, 'alt': alt, 'widths': widths, 'w': W, 'h': H}

for slug, src, alt, cat, name in KNIVES:
    d = export(slug, src, alt); d.update(cat=cat, name=name); manifest['knives'].append(d)
for slug, src, alt in ATELIER:
    manifest['atelier'].append(export(slug, src, alt))

os.makedirs(os.path.join(ROOT, 'qnife-site', 'src', 'data'), exist_ok=True)
json.dump(manifest, open(os.path.join(ROOT, 'qnife-site', 'src', 'data', 'photos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(os.path.getsize(f) for f in glob.glob(OUT + '/*.webp'))
print(len(os.listdir(OUT)), 'fichiers,', round(tot / 1e6, 1), 'Mo')
