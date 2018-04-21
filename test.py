import os
import sys
from PIL import Image

def scale_image(input_image_path,
                output_image_path,
                tamanho=None,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print('	A imagem original: {wide}  x {height} '
          .format(wide=w, height=h))
 
    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')
 
 		#Thumbnail muda o tamanho
    original_image.thumbnail(max_size, Image.ANTIALIAS)

    # Pega caminho completo: PASTA + novo nome
    name=os.path.basename(input_image_path)
    nameNoExtension=os.path.splitext(name)[0]
    fPathLarge=output_image_path + '\\' + tamanho + '\\' + nameNoExtension + '_' + tamanho + '.jpg'
	# Salva
    original_image.save(fPathLarge)
    print('		Salvando em: ' + fPathLarge)
    print('		tamanho: ' + str(width) + 'x' + str(height))
if __name__ == '__main__':
	# seta os argumentos
	input_folder=sys.argv[1]
	output_folder=sys.argv[2]


	#criar pastas	
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
	if not os.path.exists(output_folder + '\\large'):
		os.makedirs(output_folder + '\\large')
	if not os.path.exists(output_folder + '\\' + 'small'):
		os.makedirs(output_folder + '\\' + 'small')
	if not os.path.exists(output_folder + '\\' + 'promo'):
		os.makedirs(output_folder + '\\' + 'promo')
	if not os.path.exists(output_folder + '\\' + 'thumbnail'):
		os.makedirs(output_folder + '\\' + 'thumbnail')

	# loop entre os arquivos da pasta 
	for subdir, dirs, files in os.walk(input_folder):
		
		for file in files:  
			filepath = subdir + os.sep + file
			scale_image(input_image_path=filepath,output_image_path=output_folder,tamanho='large',width=500, height=500)	
		for file in files:  
			filepath = subdir + os.sep + file
			scale_image(input_image_path=filepath,output_image_path=output_folder,tamanho='small',width=50, height=50)
		for file in files:  
			filepath = subdir + os.sep + file
			scale_image(input_image_path=filepath,output_image_path=output_folder,tamanho='promo',width=300, height=300)
		for file in files:  
			filepath = subdir + os.sep + file
			scale_image(input_image_path=filepath,output_image_path=output_folder,tamanho='thumbnail',width=200, height=200)	