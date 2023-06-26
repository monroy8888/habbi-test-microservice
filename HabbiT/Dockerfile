FROM python:3.9 as base_python

WORKDIR /app
COPY requirements.txt .

COPY /poetry.lock .
COPY /pyproject.toml .

RUN pip install -r requirements.txt
RUN poetry config virtualenvs.create false
RUN poetry install

COPY /api_habbi ./app/

CMD ["poetry", "run", "uvicorn", "api_habbi.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
