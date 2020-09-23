# python-sunshine


# install modules using anaconda
sudo apt install ffmpeg

conda create -n sunshine python=3.8
conda activate sunshine

conda install -c conda-forge opencv

conda install -c conda-forge uvloop


# For video capturing
pip install uvloop
pip install vidgear[asyncio] # can be troublesome for ZSH

# for audio