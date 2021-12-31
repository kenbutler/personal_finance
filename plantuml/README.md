# Purpose
This directory is intended to consolidate all the PlantUML diagrams for this project.

# Requirements
- Java
- GraphViz (for sequence and activity diagrams)

# How to Run
Simply execute `./export.sh` from this directory.
This script will produce PNG images in a local `out` directory.

# Known Errors
1. If you see the following message, it means that you need to install GraphViz
```buildoutcfg
java.io.IOException: Cannot run program "/opt/local/bin/dot": error=2, No such file or directory
```