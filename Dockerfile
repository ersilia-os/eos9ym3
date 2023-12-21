FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit
#RUN conda install -c conda-forge openbabel
RUN wget https://anaconda.org/conda-forge/openbabel/3.0.0/download/linux-64/openbabel-3.0.0-py27hdef5451_1.tar.bz2
RUN conda install openbabel-3.0.0-py27hdef5451_1.tar.bz2 -y
RUN pip install numpy==1.21.6
RUN pip install pandas==1.3.5
RUN pip install protobuf==3.19.6
RUN pip install scikit-learn==1.0.2
RUN pip install TensorFlow==2.11.0
RUN pip install Keras==2.11.0

WORKDIR /repo
COPY . /repo