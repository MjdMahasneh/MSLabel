import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import cv2
import numpy as np
import getImageList as glist
import convert_string_to_list as stl
import Write_ARs_Xml_All as wxml
import Write_ARs_Xml_Separatly as wsxml
from helpers import check_dir_setup



check_dir_setup()




class LabelMe(QDialog):
    def __init__(self):
        super(LabelMe,self).__init__()
        loadUi('LabelMe_layout_3.ui', self)
        self.setWindowTitle('LabelMe')
        self.NextButton.clicked.connect(self.NextButton_clicked)
        self.BackButton.clicked.connect(self.BackButton_clicked)

        self.SaveButton.clicked.connect(self.SaveButton_clicked)
        self.x, self.y, self.width, self.height = 100, 100, 950, 650
        self.initUI()
        self.image_number = -1
        self.flag = 0 

    @pyqtSlot()
    def empty_cache(self):
        file_path = 'cache/temp.txt'
        file = open(file_path,'w')
        entry = ('')
        file.write(entry)
        file.close()
        return()
    
    def initUI(self):
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.show()

        self.empty_cache()


        
    def showMessageBox(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()



    def SaveButton_clicked(self):

        try:
            base_path_1 = os.path.dirname(os.path.realpath(__file__))
            xml_file_1 = os.path.join(base_path_1, "annotation_files/annotation_for_All_files.xml")

            base_path_2 = os.path.dirname(os.path.realpath(__file__))
            output_file_path = 'annotation_files\\'+current_image_name[:-4]+'_annotation.xml'
            xml_file_2 = os.path.join(base_path_2, output_file_path)

            file_path = 'cache/temp.txt'
            file = open(file_path,'r')
            ARs_BB = file.read()
            if len(ARs_BB) == 0:
                print('no data available to be saved')
                self.showMessageBox('Attention','no data available to be saved')
            else:
                rects = stl.string_to_list(ARs_BB)
                wxml.write_ARs(xml_file_1, current_image_name, rects)
                wsxml.write_ARs(xml_file_2, current_image_name, rects, w, h)

                file_name = 'annotation_files/'+current_image_name
                cv2.imwrite(file_name, saved_img)
                

                
                print('list of rects',rects)
                print(current_image_name, ' rects are saved')
                print('SAVING DONE!')
                if self.saving_status_label.text() == '':
                    self.saving_status_label.setText('Changes were saved successfully!')
                else:
                    pass
        except Exception as e:
            print('ops!! something went wrong : ',e)
            self.showMessageBox('ops!! something went wrong : ',e)



            

    def BackButton_clicked(self):
        
        cv2.destroyAllWindows()
        cv2.destroyWindow('Select RoI')


        self.empty_cache()
        
        imlist = glist.get_imlist('images/band_1')

        if self.saving_status_label.text() == 'Changes were saved successfully!':
            self.saving_status_label.setText('')


        
        if  not (self.image_number<=0):
            self.image_number-=1

            img_name = imlist[self.image_number]
            print('image name :',img_name)

            if self.img_name_label.text() != img_name:
                self.img_name_label.setText('Image being processed : ' + img_name.split('\\')[-1])
            else:
                pass
            
            global current_image_name
            current_image_name  = img_name.split('\\')[-1]

            if (self.image_number+1) <= (len(imlist)-1):
                
                img_path = imlist[self.image_number+1]
                print('img_path >>>> : ', img_path)
                self.NextTimeSeries_1.setPixmap(QPixmap(img_path))
                self.LabelNextTimeSeries_1.setText(img_path.split('\\')[-1])
            else:
                self.NextTimeSeries_1.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelNextTimeSeries_1.setText('')

            if (self.image_number+2) <= (len(imlist)-1):
                img_path = imlist[self.image_number+2]
                self.NextTimeSeries_2.setPixmap(QPixmap(img_path))
                self.LabelNextTimeSeries_2.setText(img_path.split('\\')[-1])
            else:
                self.NextTimeSeries_2.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelNextTimeSeries_2.setText('')

            if (self.image_number+3) <= (len(imlist)-1):
                img_path = imlist[self.image_number+3]
                self.NextTimeSeries_3.setPixmap(QPixmap(img_path))
                self.LabelNextTimeSeries_3.setText(img_path.split('\\')[-1])
            else:
                self.NextTimeSeries_3.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelNextTimeSeries_3.setText('')



            if (self.image_number - 3) >= 0:
                img_path = imlist[self.image_number-3]
                self.PrevTimeSeries_1.setPixmap(QPixmap(img_path))
                self.LabelPrevTimeSeries_1.setText(img_path.split('\\')[-1])
            else:
                self.PrevTimeSeries_1.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelPrevTimeSeries_1.setText('')
                
            if (self.image_number - 2) >= 0:
                img_path = imlist[self.image_number-2]
                self.PrevTimeSeries_2.setPixmap(QPixmap(img_path))
                self.LabelPrevTimeSeries_2.setText(img_path.split('\\')[-1])
            else:
                self.PrevTimeSeries_2.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelPrevTimeSeries_2.setText('')

            if (self.image_number - 1) >= 0:
                img_path = imlist[self.image_number-1]
                self.PrevTimeSeries_3.setPixmap(QPixmap(img_path))
                self.LabelPrevTimeSeries_3.setText(img_path.split('\\')[-1])
            else:
                self.PrevTimeSeries_3.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelPrevTimeSeries_3.setText('')

            self.bound_img(img_name)
            
        else:
            self.showMessageBox('Attention','No more images to Annotate, you can only go to next image')






    def NextButton_clicked(self):
        cv2.destroyAllWindows()

        self.empty_cache()
        
        imlist = glist.get_imlist('images/band_1')


        if self.saving_status_label.text() == 'Changes were saved successfully!':
            self.saving_status_label.setText('')

        if  not (self.image_number>=int(len(imlist)-1)):
            self.image_number+=1


            
            img_name = imlist[self.image_number]
            print('image name :',img_name)


            if self.img_name_label.text() != img_name:
                self.img_name_label.setText('Image being processed : ' + img_name.split('\\')[-1])


            
            global current_image_name
            current_image_name = img_name.split('\\')[-1]


            if (self.image_number+1) <= (len(imlist)-1):
                
                img_path = imlist[self.image_number+1]
                print('img_path >>>> : ', img_path)
                self.NextTimeSeries_1.setPixmap(QPixmap(img_path))
                self.LabelNextTimeSeries_1.setText(img_path.split('\\')[-1])
            else:
                self.NextTimeSeries_1.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelNextTimeSeries_1.setText('')

            if (self.image_number+2) <= (len(imlist)-1):
                img_path = imlist[self.image_number+2]
                self.NextTimeSeries_2.setPixmap(QPixmap(img_path))
                self.LabelNextTimeSeries_2.setText(img_path.split('\\')[-1])
            else:
                self.NextTimeSeries_2.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelNextTimeSeries_2.setText('')

            if (self.image_number+3) <= (len(imlist)-1):
                img_path = imlist[self.image_number+3]
                self.NextTimeSeries_3.setPixmap(QPixmap(img_path))
                self.LabelNextTimeSeries_3.setText(img_path.split('\\')[-1])
            else:
                self.NextTimeSeries_3.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelNextTimeSeries_3.setText('')


            if (self.image_number - 3) >= 0:
                img_path = imlist[self.image_number-3]
                self.PrevTimeSeries_1.setPixmap(QPixmap(img_path))
                self.LabelPrevTimeSeries_1.setText(img_path.split('\\')[-1])
            else:
                self.PrevTimeSeries_1.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelPrevTimeSeries_1.setText('')
                
            if (self.image_number - 2) >= 0:
                img_path = imlist[self.image_number-2]
                self.PrevTimeSeries_2.setPixmap(QPixmap(img_path))
                self.LabelPrevTimeSeries_2.setText(img_path.split('\\')[-1])
            else:
                self.PrevTimeSeries_2.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelPrevTimeSeries_2.setText('')

            if (self.image_number - 1) >= 0:
                img_path = imlist[self.image_number-1]
                self.PrevTimeSeries_3.setPixmap(QPixmap(img_path))
                self.LabelPrevTimeSeries_3.setText(img_path.split('\\')[-1])
            else:
                self.PrevTimeSeries_3.setPixmap(QPixmap('cache/no_image_available.jpg'))
                self.LabelPrevTimeSeries_3.setText('')

            self.bound_img(img_name)
        else:
            self.showMessageBox('Attention','No more images to Annotate, you can only go to previous image')


    def bound_img(self,img_name):

        img = cv2.imread(img_name)

        global saved_img
        saved_img = img

        global h, w, channels 
        h, w, channels = img.shape

        try:
            print('img_name is here aha!!  >>>>>  : ', img_name)
            aux_img = get_auxiliary_band(img_name)

            concatenatinated = np.concatenate((img, aux_img), axis=1)
        except Exception:
            print('Caution : this image does not have a corrosponding auxiliary image.')
            self.showMessageBox('Caution','this image does not have a corrosponding auxiliary image.')
            concatenatinated = np.concatenate((img, img), axis=1)
            pass

        count = 0
        showCrosshair = False
        fromCenter = False

        rects = []
        while True :
            cv2.namedWindow('Select RoI',cv2.WINDOW_NORMAL)

            dispHeight, dispWidth = int(h/2), int(w)
            cv2.resizeWindow("Select RoI", dispWidth, dispHeight)


            rect  = cv2.selectROI("Select RoI", concatenatinated, fromCenter, showCrosshair)
            print('this is a rect ' ,rect)

            if (rect[0] > w) or ((rect[0]+rect[2]) > w):
                print('The coordinates of the bounding box can not be outside image')
                self.showMessageBox('Warning','The coordinates of the bounding box can not be outside image.')
            else:


                x2 = rect[0] + rect[2]
                y2 = rect[1] + rect[3]
                cv2.rectangle(concatenatinated,(rect[0],rect[1]), (x2, y2),(0,255,0),3)
                print('here >>')

                if rect != (0,0,0,0):
                    rects.append(rect)
                    file_path = 'cache/temp.txt'
                    file = open(file_path,'w')
                    entry = (str(rects))
                    file.write(entry)
                    file.close()
                    
                    
                count+=1
                print('list of rects ',rects)
                print('count',count)
                print('rects', len(rects))
                print ('rect',rect)

        cv2.destroyWindow('Select RoI')



def get_list_of_files_starting_with(path, start):
  return [os.path.join(path, f) for f in os.listdir(path) if f.startswith(start) and f.endswith('.png')]


def get_auxiliary_band(img_name):
    img_name = img_name.split('\\')[-1]
    aux_image_ID = img_name.split('_')[0]
    print('aux_image_ID -> :', aux_image_ID)
    aux_image_path = get_list_of_files_starting_with('images/band_2', aux_image_ID)[0]

    aux_img = cv2.imread(aux_image_path)

    return(aux_img)


def create_output_dirs():
    if not os.path.exists('cache'):
        os.makedirs('cache')
    if not os.path.exists('annotation_files'):
        os.makedirs('annotation_files')
    return



create_output_dirs()
app = QApplication(sys.argv)
widget=LabelMe()
widget.show()
sys.exit(app.exec_())

