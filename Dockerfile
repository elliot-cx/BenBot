FROM python:3

RUN pip install pystrich
RUN pip install discord
RUN pip install openai
RUN pip install dotenv 

ENV KEY=
ENV TOKEN=

COPY . .

CMD [ "python", "./main.py" ]