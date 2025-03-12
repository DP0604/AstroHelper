# AstroHelper

AstroHelper is a tool created to provide for clean, easy to understand and comprehensive help to observational astronomy.

## Introduction
This code has been developed to help amateur astronomers easily find the best observable objects at their location and at the best observation time. We (the creators) are physics/astronomy students ourselves as well as amateur astronomers. We have found it inconvenient to always have to pull up Stellarium or other sky viewing programs/apps to view one object at a time. Our project has the goal to create a somewhat simpler and versatile tool to help amateur astronomers, especially astrophotographers.

## Build locally
To build the AstroHelper locally do following:
```
python -m pip install --upgrade build
python -m build
pip install .
```
To then test the code, run ```run.py``` file. There is a bug in the ```min_zenith_distance``` I am fixing

## Concept
To get started you should call the function ```getStarted()```. There a brief explanation will be printed as to what variables should be defined and if they are not defined then what the standard values are. There are a handful functions which produce an output useful for the user. They all have documentation explaining what they do.

### Future
The code has been written as a package under the name AstroHelper. The next large step would be creating a GUI for easier interaction.

## Contributing
We welcome contributions to develop the code further and create a better tool for the users. If you want to contribute pull requests are welcome. For pull requests please use the template!

## License
This project falls under the MIT license.