# N-Body simulation
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
---
## Project description
1. This program is one of three simulations that will be part of a physics engine application.
2. The purposes of this simulation are:
   1. To show in real-time how multiple bodies with mass interact in a gravitational field in real time with scaled values for velocity and displacement metrics
   2. To provide an extensible way to add more functionality to increase the output of information of the bodies as the simulation runs.
3.	For simplicity's sake, the initial velocities, masses and positions of the bodies are generated in a pseudo-random way using the inbuild random functions in python. This makes it easier to run the simulation for higher values of N. For example, If you want to run the simulation for N=100, the program would require you to enter 100 masses, velocity and displacement matrices if the random feature was not used.

4.	The use of environment variables and importing other files as packages was utilised to implement the simulation in a modular fashion. The environment variables provide the directories to be added to the system path allowing the custom modules to be imported into main.py.
### Project structure
The structure of the program is mostly defined in the Body.py and vector2D.py files. These files hold the classes and subclasses that all the simulations, not just the N-body, utilise.\
All the bodies in the simulation are instances of the C4Dynamics datapoint class, c4d.datapoint() (External code, contribution credited at the end). The body is first initialised as an instance of the RegularBody subclass which derives from the Body subclass. The velocity and position attributes of the body object are instances of the vector2D class. Once initialised as an instance of the RegularBody subclass, the __init__ function returns an object of type c4d.datapoint(). The purposes of the use of the vector2D class is to make the code extensible in the context of adding functionality relating to calculations using vectors. The RegularBody class also adds a convenient way to initialise the objects without interacting the C4dynamics directly (as this is an external package so limiting ease of access to code is desirable).

The logic behind using the C4Dynamics package is that integration is required for the mathematics the simulation runs on and this package provides easy to use and convenient methods for integrating both through temporal and spatial conditions (see link provided at the end to C4dyanmics GitHub page).

## Setup
### Base setup
It goes without saying a prerequisite to run this program is having the latest version of python.\
I recommend installing anaconda and using this as the python interpreter and using visual studio code as your IDE.
The remaining setup steps are as follows:
1. In Visual Studio code set up a virtual environment in the same directory as the project.
2. Select the virtual environment as the python interpreter in Visual Studio Code instead of the base interpreter and then open a PowerShell terminal in Visual Studio Code. To enter the virtual environment run the following commands:
   1. Set-ExecutionPolicy Unrestricted -Scope Process
   2. .venv\Scripts\Activate.ps1
3.	Now in the virtual environment, ensure the requirements.txt is in the same directory, then by running the command: pip install -r requirements.txt
### Environment Variables
In the .env file there are the following variables:
1. The parent directory containing all the files and folders of the project
2. The common directory where the Body.py and vector2D.py files are located, this allows them to be imported in the main.py as custom modules.
3. The __init__.py file contains the names of the files to be imported as modules required for the project. This also allows for extensibility when code is added and user customisations can be done this way and through the .env file.
## Starting the application
Once the requirements have been installed, in the virtual environment PowerShell in the directory of the main.py file, run the command "python main.py". The matplotlib window will open and the simulation will show both how the bodies move in real time but also mark the paths.
### Changing N
In the def main() function in main.py, the variable N refers to number of particles, simply change this value and then re-run the simulation to see how N affects the trajectories.
## Testing
TO-DO: A testing file for unit testing utilising pytest will be developed along with a testing mode feature controlled via environment variables.
## Credits
Credit and appreciation to Ziv Meri and all the developers of the C4Dynamics module. The GitHub page for this module:
[C4Dynamics](https://github.com/C4dynamics/C4dynamics)
