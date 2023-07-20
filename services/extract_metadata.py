from models.models import Source
from services.openai import get_chat_completion
import json
from typing import Dict

def extract_metadata_from_document(text: str) -> Dict[str, str]:
    sources = Source.__members__.keys()
    sources_string = ", ".join(sources)
    messages = [
        {
            "role": "system",
            "content": f"""
            Given a document from a user, try to extract the following metadata:
            - source: string, one of {sources_string}
            - source_id: string or don't specify
            - url: string or don't specify
            - created_at: string or don't specify
            - author: string or don't specify
            - title: string or don't specify
            - referenced_law: strings or don't specify
            - keywords: list of strings or don't specify
            - year: integer or don't specify
            - law_type: string or don't specify
            - jurisdiction: string or don't specify
            - subject_matter: string or don't specify
            - sections: list of strings or don't specify
            - case_numbers: list of strings or don't specify
            - courts: list of strings or don't specify
            - related_laws: list of strings or don't specify
            - amendments: list of strings or don't specify

            Respond with a JSON containing the extracted metadata in key value pairs. If you don't find a metadata field, don't specify it.
            """,
        },
        {"role": "user", "content": text},
    ]
    completion = get_chat_completion(
        messages, "gpt-4"
    )  # TODO: change to your preferred model name

    print(f"completion: {completion}")

    try:
        metadata = json.loads(completion)
    except:
        metadata = {}

    return metadata
