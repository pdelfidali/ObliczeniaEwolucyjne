from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from Algorithm import Algorithm
from functions.bits_crossover import *
from functions.bits_mutation import *
from functions.metaheuristics import *
from functions.real_representation_crossover import *
from functions.real_representation_mutation import *
from functions.selection import *
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
    method: str
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
    useMetaheuristics: bool
    metaheuristics: object


def set_assumptions_for_crossover(crossover_name, crossover_probability, assumptions):
    if crossover_name == 'one':
        assumptions.set_crossover(one_point_crossover, crossover_probability)
    elif crossover_name == 'two':
        assumptions.set_crossover(two_point_crossover, crossover_probability)
    elif crossover_name == 'three':
        assumptions.set_crossover(three_point_crossover, crossover_probability)
    elif crossover_name == 'homo':
        assumptions.set_crossover(homogeneous_crossover, crossover_probability)
    elif crossover_name == 'arithmetic_crossover':
        assumptions.set_crossover(arithmetic_crossover, crossover_probability)
    elif crossover_name == 'linear_crossover':
        assumptions.set_crossover(linear_crossover, crossover_probability)
    elif crossover_name == 'blend_crossover_alpha':
        assumptions.set_crossover(blend_crossover_alpha, crossover_probability)
    elif crossover_name == 'blend_crossover_alpha_beta':
        assumptions.set_crossover(blend_crossover_alpha_beta, crossover_probability)
    elif crossover_name == 'average_crossover':
        assumptions.set_crossover(average_crossover, crossover_probability)


def set_assumptions_for_mutation(mutation_name, mutation_probability, assumptions):
    if mutation_name == 'one':
        assumptions.set_mutation(one_point_mutation, mutation_probability)
    elif mutation_name == 'two':
        assumptions.set_mutation(two_point_mutation, mutation_probability)
    elif mutation_name == 'edge':
        assumptions.set_mutation(edge_mutation, mutation_probability)
    elif mutation_name == 'inv':
        assumptions.set_mutation(inversion_mutation, mutation_probability)
    elif mutation_name == 'uniform':
        assumptions.set_mutation(uniform_mutation, mutation_probability)
    elif mutation_name == 'gaussian':
        assumptions.set_mutation(gaussian_mutation, mutation_probability)


def set_assumptions_for_selection(selection_name, selection_probability, assumptions):
    if selection_name == 'roulette':
        assumptions.set_selection(roulette_wheel_selection, selection_probability)
    elif selection_name == 'rank':
        assumptions.set_selection(rank_selection, selection_probability)
    elif selection_name == 'tournament':
        assumptions.set_selection(tournament_selection, selection_probability)


def set_metaheuristics(metaheuristics_name, metaheuristics_params, assumptions):
    if metaheuristics_name == 'random_sampling':
        assumptions.set_metaheuristics(random_sampling)
    elif metaheuristics_name == 'random_walk':
        assumptions.set_metaheuristics(random_walk, metaheuristics_params)
    elif metaheuristics_name == 'hill_climbing':
        assumptions.set_metaheuristics(hill_climbing, metaheuristics_params)
    elif metaheuristics_name == 'simulated_annealing':
        assumptions.set_metaheuristics(simulated_annealing, metaheuristics_params)


def set_assumptions(assumptions_request: AssumptionsRequest):
    assumptions = Assumptions()
    assumptions.set_method(assumptions_request.method)
    assumptions.set_data_range(assumptions_request.minValue, assumptions_request.maxValue)
    assumptions.set_population(assumptions_request.populationSize)
    assumptions.set_optimization_mode(assumptions_request.optimizationMode)
    assumptions.set_epochs(assumptions_request.epochsAmount)
    if assumptions_request.method != 'metaheuristics':
        assumptions.set_precision_type(assumptions_request.precisionType, assumptions_request.precisionVal)
        set_assumptions_for_crossover(assumptions_request.crossoverType, assumptions_request.crossoverProbability,
                                      assumptions)
        set_assumptions_for_mutation(assumptions_request.mutationType, assumptions_request.mutationProbability,
                                     assumptions)
        assumptions.set_elite_strategy(assumptions_request.eliteStrategy)
        set_assumptions_for_selection(assumptions_request.selectionType, assumptions_request.selectionValue, assumptions)
    else:
        set_metaheuristics(assumptions_request.metaheuristics['name'],
                           assumptions_request.metaheuristics['assumptions'],
                           assumptions)


@app.post("/assumptions/")
def post_assumptions(assumptions: AssumptionsRequest):
    set_assumptions(assumptions)
    _assumptions = Assumptions()
    algorithm.run()
    return {"process_id": 2}
