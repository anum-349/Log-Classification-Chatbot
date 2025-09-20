from regex_processor import classify_with_regex
from BERT_processor import classify_with_bert
from llm_processor import classify_with_llm
import pandas as pd

def classify(logs):
    labels = []
    for source, log in logs:
        label = classify_logs(source, log)
        labels.append(label)
    return labels

def classify_logs(source, log):
    if source == "LegacyCRM":
        label = classify_with_llm(log)
    else:   
        label = classify_with_regex(log)
        if label is None:
            label = classify_with_bert(log)
    return label

def classify_csv(file_path):
    df = pd.read_csv(file_path)
    df["Target_label"] = classify(list(zip(df['source'], df['log_message'])))
    df.to_csv("resources/classified_logs.csv", index=False)

if __name__ == "__main__":  
    classify_csv("resources/test.csv")
#     sample_logs = [
#      ("ModernCRM", "IP 192.168.133.114 blocked due to potential attack"),
#      ("BillingSystem", "User user12345 logged in."),
#      ("AnalyticsEngine", "File data_6957.csv uploaded successfully by user User265."),
#      ("AnalyticsEngine", "Backup completed successfully."),
#      ("ModernHR", "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1 RCODE  200 len: 1583 time: 0.1878400"),
#      ("ModernHR", "Admin access escalation detected for user 9429"),
#      ("LegacyCRM", "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."),
#      ("LegacyCRM", "Invoice generation process aborted for order ID 8910 due to invalid tax calculation module."),
#      ("LegacyCRM", "The 'BulkEmailSender' feature is no longer supported. Use 'EmailCampaignManager' for improved functionality."),
#      ("LegacyCRM", " The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025")
#  ]

#     results = classify(sample_logs)
#     for label in results:
#         print(f"Label: {label}")