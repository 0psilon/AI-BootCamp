# AI-BootCamp

### Сервис можно запустить с помощью Docker:
```commandline
make up.docker
```

### Сервис можно запустить локально бeз использования Docker:

#### Подготовка виртуального окружения:
```commandline
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Запуск сервиса:
```commandline
make up.local
```
