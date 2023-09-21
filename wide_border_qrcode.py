import segno

qr_code = segno.make_qr("Hello, World")
qr_code.save(
    "wide_border_qr_code.png",
    scale=5,
    border=10,
)
