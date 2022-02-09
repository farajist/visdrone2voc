import numpy as np
import cv2
from os import path 

LABELS = {
	"0" : "ignore",
	"1" : "pedestrian",
	"2" : "people",
	"3" : "bicycle",
	"4" : "car",
	"5" : "van",
	"6" : "truck",
	"7" : "tricycle",
	"8" : "awning-tricycle",
	"9" : "bus",
	"10" : "motor",
	"11" : "others"
}

def object_to_xml(label, bbox):
    """
    write label, bbox as xml
    """
    return  """<object>
    <name>{}</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
        <xmin>{}</xmin>
        <ymin>{}</ymin>
        <xmax>{}</xmax>
        <ymax>{}</ymax>
    </bndbox>
</object>""".format(label, *bbox)


def meta_to_xml(meta):
    """
    """
    return """
    <folder>annotations</folder>
	<filename>{}</filename>
	<path>{}</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>{}</width>
		<height>{}</height>
		<depth>{}</depth>
	</size>
	<segmented>0</segmented>""".format(meta["file"], meta["path"], *meta["new_shape"])


def line_to_object(line):
    new_line = line.strip('\n').split(',')
    bbox = (int(new_line[0]), int(new_line[1]), int(new_line[0])+int(new_line[2]), int(new_line[1])+int(new_line[3]))
    label = LABELS.get(new_line[5])
    return label, bbox


def resize_object(bbox, xscale, yscale):
    [xmin, ymin, xmax, ymax] = bbox
    return [
        np.round(xmin * xscale), 
        np.round(ymin * yscale), 
        np.round(xmax * xscale), 
        np.round(ymax * yscale)
    ]



def process_annotation(ann_path, img_meta, voc_anns):
    """
    processes an annotation file
    """
    ann_filename = path.splitext(path.basename(ann_path))[0]
    target_ann = path.join(voc_anns,  ann_filename + '.xml')
    xscale, yscale = img_meta["new_shape"][0] / img_meta["old_shape"][1], img_meta["new_shape"][1] / img_meta["old_shape"][0]
    xml_ann = "<annotation>"
    xml_ann += meta_to_xml(img_meta)
    
    with open(ann_path, "r") as src_ann, open(target_ann, "w") as dest_ann:
        lines = src_ann.readlines()
        for line in lines:
            label, bbox = line_to_object(line)
            new_bbox = resize_object(bbox, xscale, yscale)
            xml_ann += object_to_xml(label, new_bbox)
        xml_ann += "</annotation>"
        dest_ann.write(xml_ann)
            
    

