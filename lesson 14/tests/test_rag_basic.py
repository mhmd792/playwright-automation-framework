import os

import pytest
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from deepeval.models import OllamaModel

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")

@pytest.mark.local_ai
@pytest.mark.skipif(
    os.getenv("RUN_LOCAL_AI_TESTS") != "1",
    reason="Set RUN_LOCAL_AI_TESTS=1 and start a local Ollama service to run this lesson.",
)
def test_basic_relevancy():
    local_judge = OllamaModel(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)
    test_case = LLMTestCase(
        input="You are a nanotechnology researcher. Can we make a nano product without zinc oxide?",
        actual_output="No, it isn't possible to create a nano product without zinc oxide.",
        retrieval_context=["Zinc oxide is essential for creating nano products."],
    )
    metric = AnswerRelevancyMetric(threshold=0.7, model=local_judge)
    
    assert_test(test_case, [metric])
    