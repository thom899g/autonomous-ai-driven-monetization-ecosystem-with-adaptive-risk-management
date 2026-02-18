import logging
from typing import Dict, List, Optional
from .models import MonetizationStrategy, EvaluationResult

logger = logging.getLogger(__name__)

class StrategyEvaluator:
    def __init__(self):
        self.strategies = {}  # type: Dict[str, MonetizationStrategy]
        
    def add_strategy(self, name: str, strategy: MonetizationStrategy) -> None:
        """Add a new monetization strategy to evaluate."""
        self.strategies[name] = strategy
        
    def evaluate_strategies(self, data: Dict) -> List[EvaluationResult]:
        """Evaluate all strategies against provided data and return results."""
        results = []
        
        try:
            for name, strategy in self.strategies.items():
                logger.info(f"Starting evaluation of strategy: {name}")
                
                result = strategy.evaluate(data)
                if result is None:
                    raise ValueError("Strategy returned no result.")
                    
                # Log intermediate metrics
                logger.info(f"Intermediate metrics: {result.metrics}")
                
                results.append(EvaluationResult(name=name, success=True, result=result))
        except Exception as e:
            logger.error(f"Error evaluating strategies: {str(e)}")
            results.append(EvaluationResult(name=None, success=False, result=None))
            
        return results