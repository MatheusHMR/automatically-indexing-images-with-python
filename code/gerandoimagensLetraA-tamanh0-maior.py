from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os, sys


# Defina o diretório de saída para salvar as imagens
# diretorio_saida = r'/home/matheus/Documentos/5º PERÍODO/NRSERVICOS-GERANDO-IMAGENS/AdesivosLetraA-101-200-NR-SERVICOS'
other_pc_root_path = r'C:\Users\Matheus Ramos\Documents\Pessoal\automatically-indexing-images-with-python\outputs'
image_path = r'automatically-indexing-images-with-python\inputs'
font_path = r'automatically-indexing-images-with-python\inputs\fonte\open-sans'
root_path = other_pc_root_path

# COLOCAR PASTA DO OUTPUT DESEJADO:
folder_name = 'P_250_ao_300'
diretorio_saida = f'{root_path}\\{folder_name}'

# Verificando se o diretório existe. Se não existir, criá-lo.
if not os.path.exists(diretorio_saida):
    os.makedirs(diretorio_saida)


# Carregando a imagem base
# imagem_base = Image.open(r'/home/matheus/Documentos/5º PERÍODO/NRSERVICOS-GERANDO-IMAGENS/FotoBaseLogoLetraA-TAMANHO-MAIOR.png')
imagem_base = Image.open(f'{image_path}\FotoBaseLogoLetraP-tamanho-maior.png')

# Definindo o número inicial para gerar as imagens
numero_inicial = 250

# Definindo o número de imagens desejadas
num_imagens = 50

# O número de imagens deve ser somada ao número inicial
num_imagens += numero_inicial


# Converter para o modo de cores RGB
imagem_base_RGBA = imagem_base.convert('RGBA')

# Definindo a fonte para o número de identificação
# (Foram baixadas várias fontes para criar diferentes tipos de stickers)
# fonte = ImageFont.truetype(r'/home/matheus/Documentos/5º PERÍODO/NRSERVICOS-GERANDO-IMAGENS/fonte/open-sans/OpenSans-Bold.ttf', 95)
fonte = ImageFont.truetype(f'{font_path}\OpenSans-Bold.ttf', 95)

for i in range(numero_inicial, num_imagens):
    
    # Criando uma cópia da imagem 
    imagem = imagem_base_RGBA.copy()

    # Criando um objeto ImageDraw para desenhar na imagem
    desenho = ImageDraw.Draw(imagem)

    # Posicionando o número na imagem
    i_formatado = str(i).zfill(3) # Preenchendo o número de forma a formatá-lo adequadamente baseado na variação solicitada
    identificacao = str(i_formatado)
    
    # Posicao = (x, y) --> quanto maior o valor de x, mais pra direita
    # Quanto maior o valor de y, mais pra baixo
    
    # LETRA A
    # posicao = (660, 965) 

    # LETRA P
    posicao = (660, 325) 
    # Cor em rgb hex 343569, cor em rgb (52, 53, 105) -- azul marinho

    
    desenho.text(posicao, identificacao, fill= (52, 53, 105), font=fonte)

    # Salvando a imagem com o número de identificação
    nome_arquivo = f"imagem_{identificacao}.pdf" # A extensão colocada ao fim da string define a extensão da imagem gerada.
    caminho_arquivo = os.path.join(diretorio_saida, nome_arquivo)
    # Cria um "melhorador" de imagens para aumentar a qualidade da imagem
    enhancer = ImageEnhance.Sharpness(imagem)
    imagem = enhancer.enhance(2.0)
    imagem.save(caminho_arquivo)


os.system('cls')
print()
print(f"{num_imagens - numero_inicial} imagens criadas e salvas em {diretorio_saida}, do número {num_imagens - numero_inicial} ao {num_imagens}.")
print()
print()