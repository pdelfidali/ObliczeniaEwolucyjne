import os.path
import random
import uuid
from typing import Union

import matplotlib.pyplot as plt
import mpld3
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from Algorithm import Algorithm
from Assumptions import Assumptions

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
    algorithm.run()
    print(algorithm.process_id)
    return {"process_id": algorithm.process_id}


@app.get("/epoch/{process_id}")
def get_epoch(process_id: int):
    # max_epochs = 1
    # n = random.randint(0, max_epochs)
    if n == max_epochs:
    #     plt.plot([3, 1, 4, 1, 5], 'ks-', mec='w', mew=5, ms=20)
        filename = f"{uuid.uuid4()}.png"
        path = os.path.join(os.path.curdir, "react-app", "public", "plots", filename)
    #     plt.savefig(path)
    #     return {"epoch": n, "maxEpochs": max_epochs, "progress": n / max_epochs, "plot": filename}
    return {"epoch": algorithm.epoch}
