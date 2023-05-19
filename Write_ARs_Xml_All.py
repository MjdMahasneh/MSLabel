import xml.etree.ElementTree as et
from pathlib import Path

def write_xml_into_existing_file(xml_file, img_name, top_x, top_y, bottom_x, bottom_y):
    
    tree = et.parse(xml_file)

    root = tree.getroot()

    Active_region = et.SubElement(root, "Active_region", attrib={"observation_time": img_name})

    Active_region_ID = et.SubElement(Active_region, "Active_region_ID")
    top_X = et.SubElement(Active_region, "top_X")
    top_Y = et.SubElement(Active_region, "top_Y")
    bottom_X = et.SubElement(Active_region, "bottom_X")
    bottom_Y = et.SubElement(Active_region, "bottom_Y")

    Active_region_ID.text = "1"
    top_X.text = str(top_x)
    top_Y.text = str(top_y)
    bottom_X.text = str(bottom_x)
    bottom_Y.text = str(bottom_y)

    
    tree.write(xml_file)

    return()

def create_and_write_into_xml(xml_file):

    filename = xml_file

    root = et.Element("Data")

    Active_region = et.Element("Active_region", attrib={"observation_time": "observation_time" })
    root.append(Active_region)

    Active_region_ID = et.SubElement(Active_region, "Active_region_ID")
    top_X = et.SubElement(Active_region, "top_X")
    top_Y = et.SubElement(Active_region, "top_Y")
    bottom_X = et.SubElement(Active_region, "bottom_X")
    bottom_Y = et.SubElement(Active_region, "bottom_Y")

    Active_region_ID.text = "ID"
    top_X.text = "top_X"
    top_Y.text = "top_Y"
    bottom_X.text = "bottom_X"
    bottom_Y.text = "bottom_Y"

    tree = et.ElementTree(root)
    tree.write(filename)

    return()


def Empty_img_old_info(xml_file, img_name):

    tree = et.parse(xml_file)

    root = tree.getroot()

    for Active_region in root.findall('Active_region'):
        observation_time = Active_region.get('observation_time')

        if observation_time == img_name:
            root.remove(Active_region)
    tree.write(xml_file)
    return()

def write_ARs(xml_file, img_name, rects):
    my_file = Path(xml_file)
    
    if my_file.is_file():
        Empty_img_old_info(xml_file, img_name)
        for AR in rects: 
            top_x, top_y, bottom_x, bottom_y = AR[0], AR[1], AR[0]+ AR[2], AR[1]+ AR[3]
            write_xml_into_existing_file(xml_file, img_name, top_x, top_y, bottom_x, bottom_y)
    else:
            create_and_write_into_xml(xml_file)
            for AR in rects:
                top_x, top_y, bottom_x, bottom_y = AR[0], AR[1], AR[0]+ AR[2], AR[1]+ AR[3]
                write_xml_into_existing_file(xml_file, img_name, top_x, top_y, bottom_x, bottom_y)







        


    
