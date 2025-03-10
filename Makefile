IMAGE_NAME = sentiment_analysis
CONTAINER_NAME = sentiment_analysis_container

build:
	docker build -t $(IMAGE_NAME) .

up.docker: build
	docker run -p 8000:8000 --rm --name $(CONTAINER_NAME) $(IMAGE_NAME)

up.local:
	python main.py
