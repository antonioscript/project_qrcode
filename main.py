#Programa Simples: Só tirar as '#'
#imagem = qrcode.make("link desejado")
#imagem.save("qrcode-imagem.png") #Nome do arquivo que vai ser gerado

import qrcode #Importe essa biblioteca

print("===========GERADOR QRCODE ==========")
link = input("Digite o Link que você quer gerar o QRCode: ") #Coloque seu link aqui

imagem = qrcode.make(link)
imagem.save("nome_arquivo.png") #nome do arquivo que será criado

print("QRCode Gerado!")
