from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from deepeval.models import OllamaModel

def test_basic_relevancy():
    local_judge = OllamaModel(model="llama3.2:1b", base_url="http://localhost:11434")
    test_case = LLMTestCase(
        input="You are a nanotechnology researcher. Can we make a nano product without zinc oxide?",
        actual_output="No, it isn't possible to create a nano product without zinc oxide.",
        retrieval_context=["Zinc oxide is essential for creating nano products."],
    )
    metric = AnswerRelevancyMetric(threshold=0.7, model=local_judge)
    
    assert_test(test_case, [metric])
    