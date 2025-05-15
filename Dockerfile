FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN conda install -c conda-forge openbabel -y
RUN pip install rdkit==2023.9.2
RUN pip install pandas==1.3.5
RUN pip install protobuf==3.19.6
RUN pip install scikit-learn==1.0.2
RUN pip install TensorFlow==2.11.0
RUN pip install Keras==2.11.0
RUN pip install numpy==1.23.5

WORKDIR /repo
COPY . /repo