import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from temporalio import workflow


@workflow.defn  # Correct annotation
class TransactionWorkflow:
    @workflow.run  # Correct method decorator
    async def process_transaction(self, transaction_data: dict):
        """
        Workflow logic to check for fraudulent transactions
        """
        print(f"🔄 Processing transaction: {transaction_data}")

        # Example: Call ML model for fraud detection
        if transaction_data["amount"] > 5000:  # Threshold for fraud check
            print("🚨 Fraud detected! Transaction flagged.")
            return {"status": "flagged", "reason": "High value transaction"}

        print("✅ Transaction approved.")
        return {"status": "approved"}


async def run_worker():
    """
    Connects to Temporal, registers the workflow, and starts the worker
    """
    client = await Client.connect("localhost:7233")  # Ensure Temporal server is running

    worker = Worker(
        client,
        task_queue="transaction-queue",
        workflows=[TransactionWorkflow]  # Register workflow
    )

    print("🚀 Temporal Worker Started, Listening for Tasks...")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(run_worker())
