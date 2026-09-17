import os

import pytest
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.models import OllamaModel
from deepeval.test_case import LLMTestCase

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1")

@pytest.mark.local_ai
@pytest.mark.skipif(
    os.getenv("RUN_LOCAL_AI_TESTS") != "1",
    reason="Set RUN_LOCAL_AI_TESTS=1 and start a local Ollama service to run this lesson.",
)
def test_local_support_relevance():
    local_model = OllamaModel(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0
    )
    test_case = LLMTestCase(
        input="How do I reset my password?",
        actual_output="You can reset your password by clicking on 'Forgot Password' on the login screen."
    )
    metric = AnswerRelevancyMetric(threshold=0.7, model=local_model)
    assert_test(test_case, [metric])