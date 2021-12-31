#!/bin/bash

echo "Exporting Miniconda environment..."
conda env export > environment.yml

if [[ $? ]]
then
  echo "Export successful!"
else
  echo "Export failed!"
fi