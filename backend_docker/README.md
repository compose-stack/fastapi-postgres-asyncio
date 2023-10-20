The `data` directory will contain docker volumes used for persistency.
Run `initialise_<env>.sh` to create all the folders.

## Tests

Tests run in a containerized environment, generated as hybrid between
development and production.
In development, the image is built as a single step image and includes all the system
libraries needed, and the code is mounted as a shared volume.

In production, the image is built with a two step process where the first step includes
all the libraries needed to build the wheels, and the second uses a smaller image and
installs the dependencies by using the wheels generated on the previous step.
The code is also copied in the image and shipped.

The test environment uses the two step image creation but uses a shared volume, so
the application can be tested during development without needing to rebuild the images
(unless new dependencies are added, of course).

Build images:

```
docker compose -f docker-compose.test.yml build
```

Run the tests:

```
docker compose -f docker-compose.test.yml up --exit-code-from cs-fastapi-pg-async-api-test
```

The `--exit-code-from cs-fastapi-pg-async-api-test` argument set the main command exit code
to be the same as the command running in the container. This makes possible to track the
tests results correctly in the shell or in the CI.
