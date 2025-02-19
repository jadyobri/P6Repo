# P6Repo

## Creating Virtual Environment
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
source venv/bin/activate
```
Next, run the following to install all of the needed packages for the assignment:
```
python3 -m pip install -r requirements.txt
```
Make sure you have sufficient storage for these packages and the images.  

Exit the virtual enviroment using the `deactivate` command.

## Initial Network
![Graph](P6/assets/graph.png "Initial Network")