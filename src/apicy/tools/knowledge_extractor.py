from .model_manager import Model


class KnowledgeExtractor:
    """class KnowledgeExtractor encapsulates logic to pipe text body through a
        spacy model and return the requested NLP output.
    """
    def __init__(self, model: Model, text: str):
        """Initialize the SpacyExtractor pipeline.

        spacy_model (spacy.language.Language): pre-loaded spacy language model
        text (str): text document to run the model on
        returns (KnowledgeExtractor): the newly constructed object.
        """
        self.model = model
        self.text = text
        self.doc = None

    def annotate_pos_tags(self):
        """Annotate text tokens with their respective Part-of-Speech tag.
        """
        if self.doc is None:
            self.doc = self.model.spacy_model(self.text)
        return [{
            'word': {
                'start': w.idx,
                'text': w.text,
                'lemma': w.lemma_
            },
            'annotation': w.tag_
        } for w in self.doc]

    def extract_parse_dependencies(self):
        """Extract relationships between "head" words and words which modify
            those heads.
        """
        if self.doc is None:
            self.doc = self.model.spacy_model(self.text)
        return [{
            'start': w.i,
            'end': w.head.i,
            'label': w.dep_,
            'word': {
                'start': w.idx,
                'text': w.text,
                'lemma': w.lemma_
            },
            'root': w.i == w.head.i,
            'right': w.i > w.head.i
        } for w in self.doc]

    def get_sentences_list(self):
        """Split the text into sentences."""
        if self.doc is None:
            self.doc = self.model.spacy_model(self.text)
        return [sent.string.strip() for sent in self.doc.sents]

    def extract_named_entities(self):
        """Extract recognized named entities from the text.
        """
        if self.doc is None:
            self.doc = self.model.spacy_model(self.text)
        return [{
            'start': ent.start_char,
            'end': ent.end_char,
            'text': str(ent),
            'kind': str(ent.label_)
        } for ent in self.doc.ents]
