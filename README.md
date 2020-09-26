# python-sunshine


# install modules using anaconda
sudo apt install ffmpeg

conda create -n sunshine python=3.8
conda activate sunshine

conda install -c conda-forge opencv

conda install -c conda-forge uvloop
conda install scipy

conda install -c conda-forge python-sounddevice


# For video capturing
pip install uvloop
pip install vidgear[asyncio] # can be troublesome for ZSH

# for audio

conda env export --name sunshine > python-sunshine.yml

conda env create -f python-sunshine.yml

#update base conda
conda update -n base -c defaults conda