FROM pypy:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY b.py .

CMD [ "pypy3", "./b.py" ]

