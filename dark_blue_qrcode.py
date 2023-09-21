import segno

qr_code = segno.make_qr("Ocean")
qr_code.save(
    "dark_blue_qr_code.png",
    scale=5,
    dark="darkblue"
)
