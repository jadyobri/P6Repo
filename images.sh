#!/bin/bash
curl -L -o P6/src/kaggle.zip https://www.kaggle.com/api/v1/datasets/download/msambare/fer2013

mkdir -p P6/src/kaggle

tar -xf P6/src/kaggle.zip -C P6/src/kaggle

rm P6/src/kaggle.zip

rm -rf P6/src/kaggle/test/angry P6/src/kaggle/test/disgust P6/src/kaggle/test/fear P6/src/kaggle/test/sad

rm -rf P6/src/kaggle/train/angry P6/src/kaggle/train/disgust P6/src/kaggle/train/fear P6/src/kaggle/train/sad