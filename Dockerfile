FROM python:3.8
WORKDIR /workspace
COPY ./ /workspace
RUN pip install pipenv
RUN pipenv sync
CMD ["pipenv", "shell"]