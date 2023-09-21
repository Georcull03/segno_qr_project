import segno

qr_code = segno.make_qr("Invincible is a great show!")
qr_code.save(
    "light_blue_qr_code.png",
    scale=5,
    # Light can be set using RGB format or using hexadecimal value
    light="lightblue",
)
