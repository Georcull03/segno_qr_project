import segno
from urllib.request import urlopen

slts_qr_code = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
slts_qr_code.to_artistic(
    background=nirvana_url,
    target="animated_qr_code.gif",
    scale=5,
)