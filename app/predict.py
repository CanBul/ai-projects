import torch
from transformers import ConvBertTokenizer, ConvBertForSequenceClassification
from app import app


class OffensivePredict:
    """
    A class to make predictions of offensiveness.

    Example usage:

    >>> predict = OffensivePredict()
    >>> predict('Bayağı büyük laflar etmiş şerefsiz.')  # Offensive
    (0.02447461523115635, 0.9755253791809082)
    """
    def __init__(self, model_path='/home/can/ai-projects/app/model'):
        self.tokenizer = ConvBertTokenizer.from_pretrained(model_path, from_pt=True)
        self.model = ConvBertForSequenceClassification.from_pretrained(model_path)
        self.softmax = torch.nn.Softmax(dim=1)

    def __call__(self, text, *args, **kwargs):
        """Takes a string and returns a tuple of (not offensive score, offensive score)."""
        inputs = self.tokenizer(text, return_tensors="pt")
        labels = torch.tensor([1]).unsqueeze(0)  # Batch size 1
        outputs = self.model(**inputs, labels=labels)

        logits = outputs.logits
        return tuple(map(float, self.softmax(logits).squeeze()))



predict = OffensivePredict()
print(predict('Bayağı büyük laflar etmiş şerefsiz.'))  # Offensive
    