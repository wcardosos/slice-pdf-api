class ReferenceSucessMock:
    exists = True
    def to_dict(self):
        return { 'count': 1}

class ReferenceErrorMock:
    exists = False


class DocumentMock:
    def __init__(self, success):
        self.success = success
    
    def get(self):
        return ReferenceSucessMock() if self.success else ReferenceErrorMock()


class CollectionMock:
    def __init__(self, success):
        self.success = success
    
    def document(self, document):
        return DocumentMock(self.success)

class FirestoreClientMock:
    def __init__(self, has_doc):
        self.has_doc = has_doc
    
    def collection(self, collection):
        return CollectionMock(self.has_doc)