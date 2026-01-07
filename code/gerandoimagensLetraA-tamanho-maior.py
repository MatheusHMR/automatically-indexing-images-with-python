from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os, sys

# Defina o diretório de saída para salvar as imagens
root_path = os.path.dirname(os.path.abspath(__file__))
output_folder_name = '../outputs'
input_folder_name = '../inputs'
font_folder_name = '../inputs/fonte/open-sans'
font_file_name = 'OpenSans-Bold.ttf'
image_file_name = 'FotoBaseLogoLetraP-tamanho-maior.png'
output_subfolder_name = 'P_401_ao_450_Motos'

# Caminhos relativos
output_path = os.path.join(root_path, output_folder_name, output_subfolder_name)
image_path = os.path.join(root_path, input_folder_name, image_file_name)
font_path = os.path.join(root_path, input_folder_name, font_folder_name, font_file_name)

if not os.path.exists(output_path):
    os.makedirs(output_path)

# Carregando a imagem base
imagem_base = Image.open(image_path)

# Definindo o número inicial para gerar as imagens
numero_inicial = 401

# Definindo o número de imagens desejadas
num_imagens = 50

# O número de imagens deve ser somada ao número inicial
num_imagens += numero_inicial

# Converter para o modo de cores RGB
imagem_base_RGBA = imagem_base.convert('RGBA')

# Definindo a fonte para o número de identificação
fonte = ImageFont.truetype(font_path, 95)

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

    desenho.text(posicao, identificacao, fill=(52, 53, 105), font=fonte)

    # Salvando a imagem com o número de identificação
    nome_arquivo = f"imagem_{identificacao}.pdf" # A extensão colocada ao fim da string define a extensão da imagem gerada.
    caminho_arquivo = os.path.join(output_path, nome_arquivo)
    # Cria um "melhorador" de imagens para aumentar a qualidade da imagem
    enhancer = ImageEnhance.Sharpness(imagem)
    imagem = enhancer.enhance(2.0)
    imagem.save(caminho_arquivo)

os.system('cls')
print()
print(f"{num_imagens - numero_inicial} imagens criadas e salvas em {output_path}, do número {numero_inicial} ao {num_imagens - 1}.")
print()
print()
