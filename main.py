#Programa Simples: Só tirar as '#'
#imagem = qrcode.make("link desejado")
#imagem.save("qrcode-imagem.png")#Nome do arquivo que vai ser gerado

import qrcode

print("===========GERADOR QRCODE ==========")
link = input("Digite o Link que você quer gerar o QRCode: ")

imagem = qrcode.make(link)
imagem.save("nome_arquivo.png")

print("QRCode Gerado!")
