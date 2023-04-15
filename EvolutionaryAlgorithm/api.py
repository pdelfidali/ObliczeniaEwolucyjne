import os.path
import uuid

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from Algorithm import Algorithm

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

algorithm = Algorithm()


class AssumptionsRequest(BaseModel):
    minValue: float
    maxValue: float
    precisionType: str
    precisionVal: int
    populationSize: int
    epochsAmount: int
    crossoverType: str
    crossoverProbability: float
    mutationType: str
    mutationProbability: float
    eliteStrategy: bool
    selectionType: str
    selectionValue: float
    optimizationMode: str


@app.post("/assumptions/")
def post_assumptions(assumptions: AssumptionsRequest):
    algorithm.config_program(assumptions_config=assumptions.dict())
    algorithm.set_assumptions_json(assumptions.dict())
    algorithm.run()
    print(algorithm.process_id)
    return {"process_id": algorithm.process_id}
