from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class Source(str, Enum):
    email = "email"
    file = "file"
    chat = "chat"


class DocumentMetadata(BaseModel):
    source: Optional[Source] = None
    source_id: Optional[str] = None
    url: Optional[str] = None
    created_at: Optional[str] = None
    author: Optional[str] = None
    title: Optional[str] = None
    referenced_law: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    year: Optional[int] = None
    law_type: Optional[str] = None
    jurisdiction: Optional[str] = None
    subject_matter: Optional[str] = None
    sections: Optional[List[str]] = None
    case_numbers: Optional[List[str]] = None
    courts: Optional[List[str]] = None
    related_laws: Optional[List[str]] = None
    amendments: Optional[List[str]] = None


class DocumentChunkMetadata(DocumentMetadata):
    document_id: Optional[str] = None


class DocumentChunk(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: DocumentChunkMetadata
    embedding: Optional[List[float]] = None


class DocumentChunkWithScore(DocumentChunk):
    score: float


class Document(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: Optional[DocumentMetadata] = None


class DocumentWithChunks(Document):
    chunks: List[DocumentChunk]


class DocumentMetadataFilter(BaseModel):
    document_id: Optional[str] = None
    source: Optional[Source] = None
    source_id: Optional[str] = None
    author: Optional[str] = None
    start_date: Optional[str] = None  # any date string format
    end_date: Optional[str] = None  # any date string format
    title: Optional[str] = None
    referenced_law: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    year: Optional[int] = None
    law_type: Optional[str] = None
    jurisdiction: Optional[str] = None
    subject_matter: Optional[str] = None
    sections: Optional[List[str]] = None
    case_numbers: Optional[List[str]] = None
    courts: Optional[List[str]] = None
    related_laws: Optional[List[str]] = None
    amendments: Optional[List[str]] = None


class Query(BaseModel):
    query: str
    filter: Optional[DocumentMetadataFilter] = None
    top_k: Optional[int] = 3


class QueryWithEmbedding(Query):
    embedding: List[float]


class QueryResult(BaseModel):
    query: str
    results: List[DocumentChunkWithScore]
