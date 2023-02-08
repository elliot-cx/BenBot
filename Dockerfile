FROM python:3

ADD main.py /

RUN pip install pystrich
RUN pip install discord
RUN pip install openai
RUN pip install dotenv 

ENV KEY=
ENV TOKEN=

CMD [ "python", "./main.py" ]