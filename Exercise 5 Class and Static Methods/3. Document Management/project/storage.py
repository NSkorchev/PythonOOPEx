from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)
        return

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

        return

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)
        return

    def edit_category(self, category_id: int, new_name: str):
        category = next((cat for cat in self.categories if cat.id == category_id), None)
        if category:
            category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = next((top for top in self.topics if top.id == topic_id), None)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = next((doc for doc in self.documents if doc.id == document_id), None)
        if document:
            document.file_name = new_file_name

    def delete_category(self, category_id: int):
        category = next((cat for cat in self.categories if cat.id == category_id), None)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = next((top for top in self.topics if top.id == topic_id), None)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = next((doc for doc in self.documents if doc.id == document_id), None)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id: int) -> Document:
        document = next((doc for doc in self.documents if doc.id == document_id), None)
        return document

    def __repr__(self):
        document = "\n".join(repr(document) for document in self.documents)
        return document
