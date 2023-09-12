FROM python:3.10
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN pip install websocket-client
RUN pip install rel
RUN pip install requests
RUN pip install python-tado

WORKDIR /publish_device_temp_data_tado
COPY publish_device_temp_data_tado.py /publish_device_temp_data_tado

CMD ["python", "publish_device_temp_data_tado.py"]