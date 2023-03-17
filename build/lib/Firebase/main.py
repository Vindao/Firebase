from firebase_admin import firestore, initialize_app
from firebase_admin.credentials import Certificate


class Firebase:

    def __init__(self, certificate_path: str):
        cred = Certificate(certificate_path)
        self.app = initialize_app(cred)
        self.fs = firestore.client(self.app)