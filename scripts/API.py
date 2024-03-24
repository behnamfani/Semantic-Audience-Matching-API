from fastapi import FastAPI
from pydantic import BaseModel

from src.Semantic_Match import Semantic

S = Semantic()
app = FastAPI()


class Item(BaseModel):
    input_segments: list[str]


@app.get("/match")
async def match_segments(input: Item):
    """
    This endpoint match processes a list of segments in the request body and return best semantic match using
    Semantic_Match script.
    """

    # Pass the input to the Semantic_Match Script to find the best match
    response = S.find_match(input.input_segments)
    return {f"message": f"{response}"}
