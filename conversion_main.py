import rawpy
import imageio
import os

import config

output_folder = os.path.join(config.input_folder, 'compressed')
output_file_format = 'tiff'

for picname in os.listdir(config.input_folder):
    if picname.lower().endswith('.arw'):
        picpath_old = os.path.join(config.input_folder, picname)
        picpath_new = os.path.join(output_folder, '{}.{}'.format(picname.split('.')[0], output_file_format))
        raw = rawpy.imread(picpath_old)
        rgb = raw.postprocess()
        imageio.imsave(picpath_new, rgb)
        print('Converted %s' % picname)
print('Finished converting all pictures. Check it out: {}'.format(output_folder))
