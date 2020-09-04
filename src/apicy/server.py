#!/usr/bin/env python
import logging
import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import RedirectResponse, JSONResponse

from .dtos.analyze_text_request import AnalyzeTextRequest
from .dtos.dependency_parses_response import DependencyParsesResponse
from .dtos.models_response import ModelsResponse
from .dtos.named_entities_response import NamedEntitiesResponse
from .dtos.pipeline_response import PipelineResponse
from .dtos.pos_annotations_response import PosAnnotationsResponse
from .dtos.schema_response import SchemaResponse
from .dtos.sentences_response import SentencesResponse
from .exceptions.model_not_found_exception import ModelNotFoundException
from .tools.knowledge_extractor import KnowledgeExtractor
from .tools.model_manager import ModelManager

log = logging.getLogger(__name__)


# load models
MODELS = os.getenv('MODELS', 'en').split()

model_manager = ModelManager()
for model_name in MODELS:
    model_manager.get_or_load_model(model_name)
    log.info('loaded spacy model %s', model_name)

# start API
API_PREFIX = os.getenv('API_PREFIX', '').rstrip('/')
app = FastAPI(
    title='SpaCy API',
    version='1.0.0',
    description='apiCy is a containerized Docker REST microservice for providing spaCy as a service.',
    openapi_prefix=API_PREFIX,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['DELETE', 'GET', 'POST', 'PUT'],
    allow_headers=['*']
)


@app.exception_handler(ModelNotFoundException)
async def model_not_found_exception_handler(request: Request, exc: ModelNotFoundException):
    return JSONResponse(
        status_code=404,
        content={'message': f'The pretrained statistical model "%s" is not available.' % exc.identifier},
    )


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f'{API_PREFIX}/docs')


@app.get(
    '/models',
    response_model=ModelsResponse,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
    tags=['INFO']
)
async def list_available_models():
    return {
        'models': list(MODELS)
    }


@app.get(
    '/{lang}/schema',
    response_model=SchemaResponse,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
    tags=['INFO']
)
async def get_model_schema(lang: str):
    model = model_manager.get_language_model(lang)
    return {
        'dep_types': list(model.get_dep_types()),
        'ent_types': list(model.get_ent_types()),
        'pos_types': list(model.get_pos_types())
    }


@app.post(
    '/{lang}/pos-annotations',
    response_model=PosAnnotationsResponse,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
    tags=['POS']
)
async def extract_pos_annotations(lang: str, body: AnalyzeTextRequest):
    """Analyzes the text and assigns parts of speech to each word, such as
        noun, verb, adjective, etc.
    """
    model = model_manager.get_language_model(lang)
    extractor = KnowledgeExtractor(model, text=body.text)
    return {
        'pos_annotations': extractor.annotate_pos_tags()
    }


@app.post(
    '/{lang}/dependency-parses',
    response_model=DependencyParsesResponse,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
    tags=['DEP']
)
async def extract_dependency_parses(lang: str, body: AnalyzeTextRequest):
    """Analyzes the grammatical structure of natural language sentences, esta-
        blishing relationships between "head" words and words which modify tho-
        se heads."""
    model = model_manager.get_language_model(lang)
    extractor = KnowledgeExtractor(model, text=body.text)
    return {
        'dep_parses': extractor.extract_parse_dependencies()
    }


@app.post(
    '/{lang}/named-entities',
    response_model=NamedEntitiesResponse,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
    tags=['NER']
)
async def extract_named_entities(lang: str, body: AnalyzeTextRequest):
    """Analyzes the text and extracts named entities."""
    model = model_manager.get_language_model(lang)
    extractor = KnowledgeExtractor(model, text=body.text)
    return {
        'entities': extractor.extract_named_entities()
    }


@app.post(
    '/{lang}/sentences',
    response_model=SentencesResponse,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
    tags=['SENT']
)
async def get_sentences(lang: str, body: AnalyzeTextRequest):
    """Split the text into sentences."""
    model = model_manager.get_language_model(lang)
    extractor = KnowledgeExtractor(model, text=body.text)
    return {
        'sentences': extractor.get_sentences_list()
    }


@app.post(
    '/{lang}/pipeline',
    response_model=PipelineResponse,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
    tags=['POS', 'DEP', 'NER', 'SENT']
)
async def get_pipeline(
        lang: str,
        body: AnalyzeTextRequest,
        pos: bool = False,
        dep: bool = False,
        sent: bool = False,
        ner: bool = False
):
    """Analyze the text and return intermediate results of the pipeline."""
    model = model_manager.get_language_model(lang)
    extractor = KnowledgeExtractor(model, text=body.text)
    resp = {}
    if pos:
        resp.__setitem__('pos_annotations', extractor.annotate_pos_tags())
    if dep:
        resp.__setitem__('dep_parses', extractor.extract_parse_dependencies())
    if sent:
        resp.__setitem__('sentences', extractor.get_sentences_list())
    if ner:
        resp.__setitem__('entities', extractor.extract_named_entities())
    return resp
