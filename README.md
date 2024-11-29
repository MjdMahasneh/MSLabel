# MSLabel

**MSLabel** is a tool for bounding box labeling of multi-spectral (multi-layer, and possibly time-series) imagery. This tool is particularly useful when visual inspection of two bands, simultaneously, is required to create labels. 

For example, in the figure below, we can visually inspect the right-hand side image (image from band 2 that temporally corresponds/associates with the target image from band 1) to annotate the target image from band 1 (target band).

![Screenshot](samples/sample.png)

---




## Installation and Setup

### Clone the Repository
   Clone the project repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/MSLabel.git
   cd MSLabel
   ```

### Requirements
The following libraries are required to run the application:

- Python 3.7+
- PyQt5
- OpenCV
- NumPy

Install them using pip:
```bash
pip install PyQt5 opencv-python numpy
```



### Set Up the Directory Structure
Ensure the directory is structured following expected format:

```
images/
├── band1/
│   ├── band_1_image_1.png
│   ├── band_1_image_2.png
│   ├── band_1_image_3.png
│   └── ...
├── band2/
│   ├── band_2_image_1.png
│   ├── band_2_image_2.png
│   ├── band_2_image_3.png
│   └── ...
└── 
```



### Run the Application
Launch the tool by executing:

```bash
python main.py
```

### How to Use
- Launch the Tool
- Run the application using the command above. The graphical user interface (GUI) will open.
- Navigate Between Images: Use the "Next" and "Back" buttons to cycle through images in the dataset.
- Draw Bounding Boxes: Use your mouse to select regions of interest (ROIs) on the target image. The auxiliary band image is displayed alongside the target band for better labeling accuracy.
- Save Annotations: Aave your bounding boxes by clicking the "Save" button.
- Annotations are stored in the annotation_files/ directory in XML format.

### Output
- Bounding box annotations for each image are saved as XML files.
- Saved annotations are stored in the annotation_files/ directory.
- Each XML file corresponds to a specific image, containing its bounding box data.


---

## Citation

If you use this tool, please consider citing the following works:

- [MLMT-CNN - Object Detection and Segmentation in Multi-layer and Multi-spectral images](https://doi.org/10.1007/s00138-021-01261-y)
- [Active Region Detection in Multi-spectral Solar Images](https://www.scitepress.org/Link.aspx?doi=10.5220/0010310504520459)
- [MSMT-CNN for Solar Active Region Detection with Multi-Spectral Analysis](https://doi.org/10.1007/s42979-022-01088-y)


