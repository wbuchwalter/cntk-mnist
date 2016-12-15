FROM alfpark/cntk:2.0beta4-gpu-openmpi

RUN apt-get update
RUN apt-get install -qq build-essential libssl-dev libffi-dev python-dev
RUN pip install Flask
RUN pip install azure-storage
RUN sudo apt-get install -qq python-qt4

COPY ./src /code
ADD entry.sh /code/
RUN chmod +x /code/entry.sh

EXPOSE 80

ENTRYPOINT ["/code/entry.sh"]







