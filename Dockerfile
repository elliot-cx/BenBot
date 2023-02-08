FROM python:3

RUN pip install pystrich
RUN pip install discord
RUN pip install openai

ENV KEY=
ENV TOKEN=

COPY . .

CMD [ "python", "./main.py" ]