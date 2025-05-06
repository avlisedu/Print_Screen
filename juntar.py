import img2pdf
import os
import re

# Lista e ordena as imagens
imagens = [f for f in os.listdir() if re.match(r'captura_\d+\.png', f)]
imagens.sort(key=lambda x: int(re.search(r'\d+', x).group()))

# Converte para PDF mantendo a qualidade
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert(imagens))
