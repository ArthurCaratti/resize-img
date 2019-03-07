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

    print('\tA imagem original: {wide}  x {height} '.format(wide = w, height = h))
 
    original_image.thumbnail((width, height), Image.ANTIALIAS)
    
    name = os.path.basename(input_image_path)
    nameNoExtension = os.path.splitext(name)[0]
    fPathLarge = os.path.join(output_image_path, tamanho, nameNoExtension + '_' + tamanho + '.jpg')
	
    original_image.save(fPathLarge)
    
    print('\t\tSalvando em: {path}'.format(path = fPathLarge))
    print('\t\tTamanho: {w}x{h} '.format(w = width, h = height))


if __name__ == '__main__':

    (input_folder, output_folder) = (sys.argv[1], sys.argv[2])    

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pathsOutput = ['large', 'promo', 'thumbnail', 'small']

    for path in pathsOutput:
        if not os.path.exists(os.path.join(output_folder , path)):
            os.makedirs(os.path.join(output_folder , path))

    for subdir, dirs, files in os.walk(input_folder):    
        (width, height) = (500, 500)    
        for path in pathsOutput:            
            for file in files:  
                filepath = subdir + os.sep + file
                scale_image(filepath, output_folder, path, width, height)
            width -= 150
            height -= 150

