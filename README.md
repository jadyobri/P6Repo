# P6Repo
## 1) Download Required Images
**NEEDS TO BE DONE LOCALLY**  

Run the bash script to download and setup the image directories.
```
chmod +x images.sh  
bash images.sh
```
Then, run the following to export the first 5000 elements of the target categories as specified.
```
python3 P6/src/export_dataset.py
```
## 2) Creating Virtual Environment
Make sure you have [`pip`](https://packaging.python.org/en/latest/tutorials/installing-packages/) installed (should already have).

Run the command in the repo directory to create the virtual environment `venv`.
```
virtualenv venv -p $(which python3.8)
```
This is pretty much required to use the deprecated packages used for the assignment.
Newer versions of Python / package managers will not find or install the packages
in the `requirements.txt` file.  

Then, run the following to start the virtual environment.
```
## Mac / Unix:
source venv/bin/activate 

## Windows
source venv/Scripts/activate
```
Next, run the following to install all of the needed packages for the assignment:
```
python3 -m pip install -r requirements.txt
```
Make sure you have sufficient storage for these packages and the images.  

Exit the virtual enviroment using the `deactivate` command.
