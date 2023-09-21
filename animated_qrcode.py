import segno
from urllib.request import urlopen

slts_qr_code = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
nirvana_url = urlopen(
    "https://media3.giphy.com/media/4RFtzk2QARanuk2nwB/giphy.gif?cid=ecf05e4796r7whqrsn2r7h8k2nscfm9vc25opc26bqhfuz1m&ep=v1_gifs_search&rid=giphy.gif&ct=g")
slts_qr_code.to_artistic(
    background=nirvana_url,
    target="animated_qr_code.gif",
    scale=10,
)
