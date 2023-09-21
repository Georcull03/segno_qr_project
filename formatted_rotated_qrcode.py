import segno

qr_code = segno.make_qr("Green Lantern")
qr_code_rotated = qr_code.to_pil(
    scale=5,
    light="lightblue",
    dark="green"
).rotate(45, expand=True)
qr_code_rotated.save("formatted_rotated_qr_code.png")
