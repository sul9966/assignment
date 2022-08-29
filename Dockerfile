FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD main.py /

ENTRYPOINT ["python","main.py"]

CMD [ "at_hsS9wtlmTl9NLZ5SCZFio7D271vgp", "44:38:39:ff:ef:57" ]