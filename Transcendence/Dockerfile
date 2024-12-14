FROM ubuntu:latest

# Çalışma dizinini belirleyin
WORKDIR /usr/src/app

# Ubuntu paket listelerini güncelleyin ve gerekli bağımlılıkları yükleyin
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y python3 python3-pip python3-venv bash dos2unix

RUN apt-get update && apt-get install -y dos2unix
# Python sanal ortamı oluşturun
RUN python3 -m venv /opt/venv

# Sanal ortamı etkinleştirme
ENV PATH="/opt/venv/bin:$PATH"

# Django için çevresel değişkenler
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE Transcendence.settings

# requirements.txt dosyasını kopyalayın
COPY ./requirements.txt .

# pip'i güncelleyin ve requirements.txt dosyasındaki bağımlılıkları yükleyin
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 8000 portunu açın (Django'nun default portu)
EXPOSE 8000

# Uygulama dosyalarını kopyalayın
COPY ./run.sh ./run.sh
COPY . .
RUN dos2unix ./run.sh
RUN chmod +x ./run.sh
RUN sed -i 's/\r//' ./run.sh

# Container başlatıldığında çalışacak komut
ENTRYPOINT ["/bin/bash", "run.sh"]
