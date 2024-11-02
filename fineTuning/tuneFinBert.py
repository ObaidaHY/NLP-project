import torch
from transformers import BertModel, BertTokenizer, BertConfig, AutoModel
from transformers.modeling_outputs import SequenceClassifierOutput
import torch
from transformers import AutoTokenizer, Trainer, TrainingArguments
from datasets import Dataset
import pandas as pd
from sklearn.metrics import mean_squared_error
import os 



os.environ["TOKENIZERS_PARALLELISM"] = "false"


class FinBERTRegression(torch.nn.Module):
    def __init__(self, model_name):
        super(FinBERTRegression, self).__init__()
        self.bert = AutoModel.from_pretrained(model_name)
        self.regression_head = torch.nn.Linear(self.bert.config.hidden_size, 1)  # Output a single value for regression

    def forward(self, input_ids, attention_mask=None, token_type_ids=None, labels=None):
        # Pass input through the FinBERT model
        outputs = self.bert(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        cls_output = outputs.last_hidden_state[:, 0, :]  # Use [CLS] token for regression
        logits = self.regression_head(cls_output)
        
        loss = None
        if labels is not None:
            loss_fn = torch.nn.MSELoss()
            loss = loss_fn(logits.view(-1), labels.view(-1))  # Calculate MSE loss for regression
        
        return SequenceClassifierOutput(loss=loss, logits=logits)



# Load FinBERT model and tokenizer
model_name = "SeanD103/Longformer_for_financial_sentiment_analysis"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = FinBERTRegression(model_name)  

# Tokenize function remains the same
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=2048)

# Define MSE computation for regression
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = predictions.flatten()
    mse = mean_squared_error(labels, predictions)
    return {"mse": mse}

def main():
    # Load and prepare the dataset
    layoff_data = pd.read_csv("layoff_data_with_news.csv")[:200]
    data_7_days = Dataset.from_pandas(layoff_data[['news_7_days', 'Percentage']].rename(columns={"news_7_days": "text", "Percentage": "label"}))
    

    # Tokenize the dataset
    data_7_days = data_7_days.map(tokenize_function, batched=True)
    data_7_days = data_7_days.remove_columns(["text"])
    data_7_days.set_format("torch")
    
    # Training arguments
    training_args = TrainingArguments(
        output_dir="./finbert_output",
        eval_strategy="epoch",
        save_strategy="no",
        num_train_epochs=100,
        per_device_train_batch_size = 12,
        logging_dir="./logs",
        load_best_model_at_end=False,
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=data_7_days,
        eval_dataset=data_7_days,
        compute_metrics=compute_metrics
    )

    # Fine-tune the model
    print("Training with 7-day data window")
    trainer.train()

    # Evaluate the model
    eval_results = trainer.evaluate()
    print(f"MSE for 7-day data window: {eval_results['eval_mse']}")

if __name__ == "__main__":
    main()
