FROM python:3.12-slim

RUN addgroup --system discord-app-example && \
  adduser --system --ingroup discord-app-example discord-app-example

WORKDIR /app

COPY dist/*.whl .

RUN pip install --no-cache-dir *.whl && \
  rm *.whl

COPY --chown=discord-app-example:discord-app-example --chmod=0400 main.py .

USER discord-app-example

CMD ["python", "main.py"]
