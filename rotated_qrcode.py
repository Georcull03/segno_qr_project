import segno

qr_code = segno.make_qr("45 degree turn")

qr_code_rotated = qr_code.to_pil().rotate(45)
qr_code_rotated.save("rotated_qr_code.png")
