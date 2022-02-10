import argparse


from os import path, listdir, makedirs

from annotation import process_annotation
from image import process_image

visdrone_sets = [('2019', 'DET', 'train'), ('2019', 'DET', 'val'), ('2019', 'DET', 'test-dev')]

parser = argparse.ArgumentParser()

parser.add_argument('-s', '--src', dest='visdrone_path', help='path to visdrone dataset', required=True)
parser.add_argument('-d', '--dest', dest='voc_path', help='path to VOC dataset', required=True)
parser.add_argument('-w', '--width', dest='w', help='new image width', required=True, type=int)
parser.add_argument('-l', '--height', dest='h', help='new image height', required=True, type=int)

args = parser.parse_args()

def visdrone2voc():
    for s in visdrone_sets:
        print(f'[VisDrone/{s}] processing started ...')
        set_name = "-".join(s)
        set_anns_path = path.join(args.visdrone_path, f"VisDrone{set_name}", "annotations")
        set_imgs_path = path.join(args.visdrone_path, f"VisDrone{set_name}", "images")

        ann_list = [path.join(set_anns_path, a) for a in listdir(set_anns_path)]
        img_list = [path.join(set_imgs_path, i) for i in listdir(set_imgs_path)]
        voc_images = path.join(args.voc_path, "VOC2007", "JPEGImages")
        voc_anns = path.join(args.voc_path, "VOC2007", "Annotations")
        # make sure destination structure exists
        makedirs(voc_images, exist_ok=True)
        makedirs(voc_anns, exist_ok=True)

        for src_ann, src_img in zip(sorted(ann_list), sorted(img_list)):
            img_meta = process_image(src_img, (args.w, args.h, 3), voc_images)
            process_annotation(src_ann, img_meta, voc_anns)
            print(f'done processing {img_meta["file"]}')
        print(f'[VisDrone/{s}] processing done.')

if __name__ == '__main__':
    visdrone2voc()
