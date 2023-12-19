quality-check:
	docker build . -t good-library --target quality --progress=plain --no-cache

build-api:
	docker build . -t good-library --target prod --progress=plain

run:
	docker run --name good-library --detach good-library

lint:
	cd src && black app
