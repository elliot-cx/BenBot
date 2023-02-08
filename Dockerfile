FROM python:3

COPY . .

RUN pip install pystrich
RUN pip install discord
RUN pip install openai
RUN pip install dotenv 

ENV KEY=
ENV TOKEN=

CMD [ "python", "./main.py" ]