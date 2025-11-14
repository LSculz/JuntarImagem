from PIL import Image

img1 = Image.open("imagem1.jpg")
img2 = Image.open("imagem2.jpg")

if img1.height != img2.height:
    nova_largura = int(img2.width * img1.height / img2.height)
    img2 = img2.resize((nova_largura, img1.height), Image.LANCZOS)

nova_largura_total = img1.width + img2.width
imagem_final = Image.new('RGB', (nova_largura_total, img1.height))
imagem_final.paste(img1, (0, 0))
imagem_final.paste(img2, (img1.width, 0))

imagem_final.save("imagem_combinada.png")

print("Imagem salva com alta qualidade!")

