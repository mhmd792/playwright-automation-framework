from deepeval import assert_test
from deepeval.metrics import AnswerRelevanceMetric
from deepeval.models import OllamaModel
from deepeval.test_case import LLMTestCase

def test_local_support_relevance():
    local_model = OllamaModel(
        model="llama3.1",
        base_url="http://localhost:11434",
        temperature=0
    )
    test_case = LLMTestCase(
        input="How do I reset my password?",
        actual_output="You can reset your password by clicking on 'Forgot Password' on the login screen."
    )
    metric = AnswerRelevanceMetric(threshold=0.7, model=local_model)
    assert_test(test_case, [metric])