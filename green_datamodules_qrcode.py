import segno

qr_code = segno.make_qr("Algae")
qr_code.save(
    "green_data_modules_qr_code.png",
    scale=5,
    light="lightblue",
    dark="darkblue",
    data_dark="orange",
    data_light="green",
)
