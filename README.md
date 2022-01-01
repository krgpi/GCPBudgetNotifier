# GCP Budget Notifier
Notify exceeding budget to your slack channel.

# Install Procedure
1. Create Slack App ([Incoming Webhook](https://ar-ap-inc.slack.com/apps/A0F7XDUAZ--incoming-webhook-?tab=more_info))
2. Copy Webhook URL and paste it to `main.py`.
3. Create Pub/Sub topics.
4. Create a new function in Cloud Function.
5. Set its trigger to the topic created in step 3 above.
6. Upload `main.py` and `requrements.txt` or copy and paste its codes.
7. Set entry point name to `notify_slack`.
8. Deploy it.
9. In your budget alert configuration, select the pub/sub topic created in step 3 above.