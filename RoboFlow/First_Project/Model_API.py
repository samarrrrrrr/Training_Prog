from inference_sdk import InferenceHTTPClient
import json

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="*************************"
)

# Run the workflow
try:
    result = client.run_workflow(
        workspace_name="samar-patil-jnsir",
        workflow_id="custom-workflow",
        images={"image": "Test.jpg"},
        use_cache=True  # Cache workflow definition for 15 minutes
    )

    # Print the result in pretty JSON format
    print("Workflow result:")
    print(json.dumps(result, indent=2))

except Exception as e:
    print("An error occurred while running the workflow:")
    print(e)
