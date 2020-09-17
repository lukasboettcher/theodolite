from dataclasses import dataclass

@dataclass
class ExperimentConfig:
    """ Wrapper for the configuration of an experiment. """
    use_case: str
    dim_values: list
    replicass: list
    partitions: int
    cpu_limit: str
    memory_limit: str
    kafka_streams_commit_interval_ms: int
    execution_minutes: int
    domain_restriction_strategy: object
    search_strategy: object
    subexperiment_executor: object
    subexperiment_evaluator: object