import json


def save_chunks(
    chunks,
    path="vectorstore/chunks.json"
):

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            chunks,
            file,
            ensure_ascii=False,
            indent=2
        )


def load_chunks(
    path="vectorstore/chunks.json"
):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)