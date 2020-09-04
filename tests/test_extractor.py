from apicy.tools.knowledge_extractor import KnowledgeExtractor
from apicy.tools.model_manager import ModelManager


model_manager = ModelManager()


def test_extract_dependency_parses():
    model = model_manager.get_or_load_model('en')
    extractor = KnowledgeExtractor(model, u'Hello, this is a parse.')
    dep_parses = extractor.extract_parse_dependencies()
    assert len(dep_parses) == 7
    assert [dep_parse['word']['text'] for dep_parse in dep_parses] ==\
           [u'Hello', u',', u'this', u'is', u'a', u'parse', u'.']
