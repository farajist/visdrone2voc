# visdrone2voc 

Convert [VisDrone](https://github.com/VisDrone/VisDrone-Datasetgoo) dataset to [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) format with size configuration.

## Usage

```bash
python main.py -s [visdrone_dataset_path] -d [destination] -w [preferred_width] -l [preferred_height]
```

Note that the width is used calculate the ratio of the height when calculating the height and vice versa.
