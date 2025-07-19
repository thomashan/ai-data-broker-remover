"""Example usage of the AI Data Broker Remover."""

import asyncio
import sys
import os

# Add the parent directory to the path so we can import from src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.ai_data_broker_remover import DataBrokerManager, PersonalInfo
from src.ai_data_broker_remover.brokers import AVAILABLE_BROKERS


async def demo():
    """Demonstrate the data broker remover functionality."""
    # Create a manager
    manager = DataBrokerManager()
    
    # Register all available brokers
    for broker_name, broker_class in AVAILABLE_BROKERS.items():
        broker = broker_class()
        manager.register_broker(broker)
    
    print(f"Registered {len(manager.list_brokers())} data brokers:")
    for broker_name in manager.list_brokers():
        print(f"  - {broker_name}")
    
    # Create sample personal information
    personal_info = PersonalInfo(
        first_name="John",
        last_name="Doe", 
        email="john.doe@example.com",
        phone="(555) 123-4567",
        address="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    )
    
    print(f"\nDemo personal info: {personal_info.first_name} {personal_info.last_name}")
    
    # Search one broker for records
    broker = manager.get_broker("WhitePages")
    if broker:
        print(f"\nSearching {broker.name} for records...")
        records = await broker.search_records(personal_info)
        print(f"Found {len(records)} record(s)")
    
    # Submit removal requests to all brokers
    print("\nSubmitting removal requests to all brokers...")
    requests = await manager.submit_removal_to_all(personal_info)
    
    print("\nRemoval request results:")
    for request in requests:
        print(f"  {request.broker_name}: {request.status.value} (ID: {request.request_id})")
    
    # Check status updates
    print("\nChecking status updates...")
    updated_requests = await manager.check_all_statuses()
    
    if updated_requests:
        print("Updated statuses:")
        for request in updated_requests:
            print(f"  {request.broker_name}: {request.status.value}")
    
    # Get completion summary
    summary = manager.get_completion_summary()
    print("\nCompletion summary:")
    for status, count in summary.items():
        if count > 0:
            print(f"  {status}: {count}")


def main():
    """Main entry point."""
    print("AI Data Broker Remover - Modular Demo")
    print("=" * 40)
    
    asyncio.run(demo())
    
    print("\nTo use the CLI interface, run:")
    print("  python -m src.ai_data_broker_remover.cli --help")


if __name__ == "__main__":
    main()
