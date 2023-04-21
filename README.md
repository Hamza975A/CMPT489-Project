# CMPT489-Project

The prerequisite for running this project is that CUDA and CUDNN are properly installed and related enviorment variables are properly set. Specific versions are suggested for each model in their README.

The toolkit for the base of this project/competition can be found at this [link](https://github.com/SoccerNet/sn-tracking)

## Repository Structure

ByteTrack_HOME: This folder contains the ByteTrack model with everything installed and files are updated/added for the purpose of this project. The README file inside this folder contains the steps for downloading the dataset, running inference for each sequence, as well as generating and zipping results for online or local evaluation.

ByteTrack_HOME: This folder contains a README file with steps on how to set up the model for this project. The model is not pre set up like the ByteTrack model due to git issues with many of the files after cloning the model.

Milestones: This folder contains the multiple reports created for the milestones of this project.

Random_Python_Scripts_For_Figures: This folder contains some python scripts created to generate figures and analyze the dataset. Some of the figures generated are used in the milestone reports.

### To use either of the models, follow the instructions in the README files within each of their folders

### The list of dependencies are included in each folder's requirements.txt folder. The lists are as follows

ByteTrack Dependencies:

```
numpy
torch>=1.7
opencv_python
loguru
scikit-image
tqdm
torchvision>=0.10.0
Pillow
thop
ninja
tabulate
tensorboard
lap
motmetrics
filterpy
h5py

# verified versions
onnx==1.8.1
onnxruntime==1.8.0
onnx-simplifier==0.3.5
```

DeepSORT Dependencies:

```
tqdm
typeguard ; python_version >= '3.4'
visualdl>=2.1.0 ; python_version <= '3.7'
opencv-python
PyYAML
shapely
scipy
terminaltables
Cython
pycocotools
#xtcocotools==1.6 #only for crowdpose
setuptools>=42.0.0
lap
sklearn
motmetrics
openpyxl
cython_bbox
```
