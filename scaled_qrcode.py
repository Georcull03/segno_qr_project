import segno

qr_code = segno.make_qr("Hello, World")
qr_code.save(
    "scaled_qr_code.png",
    scale=5,
)
