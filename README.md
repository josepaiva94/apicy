# apiCy

**Ready-to-use Docker REST microservices providing spaCy as a service - [apiCy](https://github.com/josepaiva94/apicy)**

### Features

- Use the awesome [apiCy](https://github.com/josepaiva94/apicy) with other programming languages.
- Better scaling: One NLP - multiple services.
- Build using the official [apiCy REST services](https://github.com/josepaiva94/apicy).
- Dependency parsing visualisation with [apiCy](https://demos.explosion.ai/displacy/).
- Docker images for **Danish**, **Dutch**, **English**, **French**, **German**, **Greek**, **Italian**, **Lithuanian**, **Norwegian Bokmål**, **Polish**, **Portuguese**, **Romanian**, and **Spanish**.
- Automated builds to stay up to date with spaCy.
- Current spaCy version: 2.3.2

_Documentation and API- code based upon [spaCy REST services](https://github.com/explosion/spacy-services) by [Explosion AI](https://explosion.ai)._

---

## Images

| Image                       | Description                                                       |
| --------------------------- | ----------------------------------------------------------------- |
| jcpaiva/apicy:base          | Base image for apiCy, containing no language model                |
| jcpaiva/apicy:en            | English language model                                            |
| jcpaiva/apicy:en-md         | English language model (medium)                                   |
| jcpaiva/apicy:en-lg         | English language model (large)                                    |
| jcpaiva/apicy:da            | Danish language model                                             |
| jcpaiva/apicy:da-md         | Danish language model (medium)                                    |
| jcpaiva/apicy:da-lg         | Danish language model (large)                                     |
| jcpaiva/apicy:de            | German language model                                             |
| jcpaiva/apicy:de-md         | German language model (medium)                                    |
| jcpaiva/apicy:de-lg         | German language model (large)                                     |
| jcpaiva/apicy:el            | Greek language model                                              |
| jcpaiva/apicy:el-md         | Greek language model (medium)                                     |
| jcpaiva/apicy:el-lg         | Greek language model (large)                                      |
| jcpaiva/apicy:es            | Spanish language model                                            |
| jcpaiva/apicy:es-md         | Spanish language model (medium)                                   |
| jcpaiva/apicy:es-lg         | Spanish language model (large)                                    |
| jcpaiva/apicy:fr            | French language model                                             |
| jcpaiva/apicy:fr-md         | French language model (medium)                                    |
| jcpaiva/apicy:fr-lg         | French language model (large)                                     |
| jcpaiva/apicy:it            | Italian language model                                            |
| jcpaiva/apicy:it-md         | Italian language model (medium)                                   |
| jcpaiva/apicy:it-lg         | Italian language model (large)                                    |
| jcpaiva/apicy:lt            | Lithuanian language model                                         |
| jcpaiva/apicy:lt-md         | Lithuanian language model (medium)                                |
| jcpaiva/apicy:lt-lg         | Lithuanian language model (large)                                 |
| jcpaiva/apicy:nb            | Norwegian Bokmål language model                                   |
| jcpaiva/apicy:nb-md         | Norwegian Bokmål language model (medium)                          |
| jcpaiva/apicy:nb-lg         | Norwegian Bokmål language model (large)                           |
| jcpaiva/apicy:nl            | Dutch language model                                              |
| jcpaiva/apicy:nl-md         | Dutch language model (medium)                                     |
| jcpaiva/apicy:nl-lg         | Dutch language model (large)                                      |
| jcpaiva/apicy:pl            | Polish language model                                             |
| jcpaiva/apicy:pl-md         | Polish language model (medium)                                    |
| jcpaiva/apicy:pl-lg         | Polish language model (large)                                     |
| jcpaiva/apicy:pt            | Portuguese language model                                         |
| jcpaiva/apicy:pt-md         | Portuguese language model (medium)                                |
| jcpaiva/apicy:pt-lg         | Portuguese language model (large)                                 |
| jcpaiva/apicy:ro            | Romanian language model                                           |
| jcpaiva/apicy:ro-md         | Romanian language model (medium)                                  |
| jcpaiva/apicy:ro-lg         | Romanian language model (large)                                   |
| jcpaiva/apicy:all           | EN, DA, DE, EL, ES, FR, IT, LT, NB, NL, PL, PT, RO language models|

---

## Usage

`docker run -p "8080:8000" jcpaiva/apicy:en`

All models are loaded at start up time. Depending on the model size and server
performance, this can take a few minutes.

The apiCy docs are available at `/docs`.

### Docker Compose

```yaml
version: '3'

services:
  apicy:
    image: jcpaiva/apicy:en
    ports:
      - "8080:8000"
    restart: always

```

### Running Tests

In order to run unit tests locally `tox` is included.

`tox`

