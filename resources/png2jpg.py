import os
from PIL import Image


if __name__ == "__main__":
    dirs = ['bear', 'car', 'cat', 'girls', 'horse', 'spiderman']
    for dir in dirs:
        new_dir = '{}_jpg'.format(dir)
        os.makedirs(new_dir, exist_ok=True)
        for filename in os.listdir(dir):
            if filename.endswith('.png'):
                img = Image.open(os.path.join(dir, filename))
                new_filename = os.path.splitext(filename)[0] + '.jpg'
                img.convert('RGB').save(os.path.join(new_dir, new_filename), 'JPEG')



