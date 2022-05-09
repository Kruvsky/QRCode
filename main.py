import qrcode

imagem_qrcode = qrcode.make("https://discord.gg/FNJHE9u2pD")
imagem_qrcode.save("qrcode_python.png")
