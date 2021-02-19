FROM registry.access.redhat.com/ubi8/python-36
COPY requirements.txt /opt/app-root/src/requirements.txt
RUN pip install -r /opt/app-root/src/requirements.txt
COPY image_utils.py /opt/app-root/src/image_utils.py
COPY model.py /opt/app-root/src/model.py
COPY app.py /opt/app-root/src/app.py
RUN mkdir /opt/app-root/src/data && mkdir /opt/uploads
COPY test-positive-nsfw.jpg /opt/app-root/src/uploads/test-positive-nsfw.jpg
COPY data/open_nsfw-weights.npy data/open_nsfw-weights.npy
CMD [ "./app.py" ]