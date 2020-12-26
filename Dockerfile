FROM python:3.8

ENV COUNTRY "Switzerland"
ENV DATA "recovered"

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY data ./data

CMD ["sh", "-c", "python main.py --country=$COUNTRY --data=$DATA"]