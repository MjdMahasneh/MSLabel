import xml.etree.ElementTree as et


def create_and_write_into_xml(xml_file, img_name, rects, img_width, img_height):

    root = et.Element("annotation")

    folder = et.SubElement(root, "folder")
    filename = et.SubElement(root, "filename")
    path = et.SubElement(root, "path")

    folder.text = "images"
    filename.text = img_name
    path.text = "Unknown"

    source = et.Element("source")
    root.append(source)

    database = et.SubElement(source, "database")
    database.text = 'Unknown'

    size = et.Element("size")
    root.append(size)

    width = et.SubElement(size, "width")
    height = et.SubElement(size, "height")
    depth = et.SubElement(size, "depth")
    
    width.text = str(img_width)
    height.text = str(img_height)
    depth.text = '1'

    segmented = et.SubElement(root, "segmented")
    
    segmented.text = "0"


    for AR in rects:
        top_x, top_y, bottom_x, bottom_y = AR[0], AR[1], AR[0]+ AR[2], AR[1]+ AR[3]

        obj = et.Element("object")
        root.append(obj)

        name = et.SubElement(obj, "name")
        pose = et.SubElement(obj, "pose")
        truncated = et.SubElement(obj, "truncated")
        difficult = et.SubElement(obj, "difficult")
        bndbox = et.SubElement(obj, "bndbox")

        name.text = 'AR'
        pose.text = 'Unspecified'
        truncated.text = '0' 
        difficult.text = '0'

        xmin = et.SubElement(bndbox, "xmin")
        ymin = et.SubElement(bndbox, "ymin")
        xmax = et.SubElement(bndbox, "xmax")
        ymax = et.SubElement(bndbox, "ymax")

        xmin.text = str(top_x)
        ymin.text = str(top_y)
        xmax.text = str(bottom_x)
        ymax.text = str(bottom_y)


    tree = et.ElementTree(root)
    tree.write(xml_file)
    
    return()

def write_ARs(xml_file, img_name, rects, img_width, img_height):
    create_and_write_into_xml(xml_file, img_name, rects, img_width, img_height)






        


    
