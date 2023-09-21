import segno

qr_code = segno.make_qr("Kryptonite")
qr_code.save(
    "green_data_dark_qr_code.png",
    scale=5,
    light="lightblue",
    dark="darkblue",
    data_dark="green",
)
