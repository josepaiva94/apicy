
def collapse_punctuation(doc):
    spans = []
    for word in doc[:-1]:
        if word.is_punct:
            continue
        if not word.nbor(1).is_punct:
            continue
        start = word.i
        end = word.i + 1
        while end < len(doc) and doc[end].is_punct:
            end += 1
        span = doc[start: end]
        spans.append(
            (span.start_char, span.end_char, word.tag_, word.lemma_, word.ent_type_)
        )
    for span_props in spans:
        doc.merge(*span_props)


def collapse_phrases(doc):
    for np in list(doc.noun_chunks):
        np.merge(np.root.tag_, np.root.lemma_, np.root.ent_type_)
