FROM nvidia/cuda:11.3.0-runtime-ubuntu20.04

WORKDIR /nlp-api
COPY . . 

RUN apt update
RUN apt install -y python3-pip

RUN pip install -r requirements.txt
ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
