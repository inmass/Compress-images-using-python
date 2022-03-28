from PIL import ImageFile, Image
ImageFile.LOAD_TRUNCATED_IMAGES = True
import glob
import os, sys
paths = [
    '/PATH/TO_FOLDER/*', # path to folder with images
    '/PATH/TO_FOLDER/*/*', # paths to subfolders with images (if folder contains subfolders with images)
]
image_list = []
not_compressed = []
errors = []
# create new folder     
for path in paths:
    for filename in glob.glob(path):
        
        # check if filename is image
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            
            try:
                print(filename)
                oldsize = os.stat(filename).st_size
                picture=Image.open(filename)
                picture = picture.convert('RGB')
                image_name = filename.split('\\')[-1]
                print(image_name)
                image_list.append(picture)
                
                
                dim = picture.size
                picture.save(filename,format = None,optimize=True,quality=65)
                newsize = os.stat(os.path.join(os.getcwd(),filename)).st_size
                percent = (oldsize-newsize)/float(oldsize)*100
                if percent == 0:
                    not_compressed.append(filename+ 'Not compressed: ' + str(percent) + '%')
                print(f"File compressed from {oldsize} to {newsize} or {percent}%")
                print('-------NEXT-------')
            except:
                errors.append('Error with file: ' + filename + ' -- Error: ' + str(sys.exc_info()))
    

print('Compressed ' + str(len(image_list)-len(errors)))
print('Not compressed ' + str(len(not_compressed)))
print(not_compressed)
print(str(len(errors)) + ' errors')
print(errors)