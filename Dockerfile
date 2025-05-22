FROM pypy:3

WORKDIR /app

COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pythainlp
RUN pip install tornado
RUN pip install asyncio


COPY b.py .

CMD [ "pypy3", "./b.py" ]
