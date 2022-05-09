import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=30,
    border=2,
)

qr.add_data('https://discord.gg/FNJHE9u2pD')
qr.make(fit=True)

imagem = qr.make_image(fill_color='green', back_color='black')
imagem.save('qrcode.png')
