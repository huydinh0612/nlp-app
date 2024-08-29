FROM python:3.10.11-slim-buster

WORKDIR /nlp-app

RUN apt-get -y update && apt-get install -y curl 

COPY prod_requirements.txt .

# install requirements
RUN pip install --no-cache-dir -r prod_requirements.txt
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# copy source code
COPY /src ./src
COPY run.py .

# expose port for documenting
EXPOSE 8080

CMD [ "python", "run.py"]