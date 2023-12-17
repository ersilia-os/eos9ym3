FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit
RUN conda install -c conda-forge openbabel
RUN pip install numpy
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install TensorFlow
RUN pip install Keras


WORKDIR /repo
COPY . /repo
