"""Command-line interface for AI Data Broker Remover."""

import asyncio
import argparse
import sys
import logging
from typing import Optional

from .core import DataBrokerManager, PersonalInfo, RemovalStatus
from .brokers import AVAILABLE_BROKERS


def setup_logging(verbose: bool = False) -> None:
    """Set up logging configuration."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


async def list_brokers() -> None:
    """List all available data brokers."""
    print("Available data brokers:")
    print("=" * 40)
    
    for broker_name, broker_class in AVAILABLE_BROKERS.items():
        # Create instance to get info
        broker = broker_class()
        required_fields = broker.get_required_fields()
        
        print(f"• {broker.name}")
        print(f"  URL: {broker.url}")
        print(f"  Required fields: {', '.join(required_fields)}")
        print()


async def search_broker(broker_name: str, personal_info: PersonalInfo) -> None:
    """Search a specific broker for records."""
    if broker_name not in AVAILABLE_BROKERS:
        print(f"Error: Broker '{broker_name}' not found")
        print(f"Available brokers: {', '.join(AVAILABLE_BROKERS.keys())}")
        return
    
    broker_class = AVAILABLE_BROKERS[broker_name]
    broker = broker_class()
    
    print(f"Searching {broker.name} for records...")
    
    try:
        records = await broker.search_records(personal_info)
        
        if records:
            print(f"Found {len(records)} record(s):")
            print("=" * 50)
            for i, record in enumerate(records, 1):
                print(f"Record {i}:")
                for key, value in record.items():
                    print(f"  {key}: {value}")
                print()
        else:
            print("No records found.")
    
    except Exception as e:
        print(f"Error searching {broker.name}: {e}")


async def submit_removal(broker_name: Optional[str], personal_info: PersonalInfo) -> None:
    """Submit removal request(s)."""
    manager = DataBrokerManager()
    
    # Register brokers
    if broker_name:
        if broker_name not in AVAILABLE_BROKERS:
            print(f"Error: Broker '{broker_name}' not found")
            return
        
        broker_class = AVAILABLE_BROKERS[broker_name]
        broker = broker_class()
        manager.register_broker(broker)
        
        print(f"Submitting removal request to {broker.name}...")
        requests = [await manager.submit_removal_to_broker(broker_name, personal_info)]
    else:
        # Register all brokers
        for broker_name, broker_class in AVAILABLE_BROKERS.items():
            broker = broker_class()
            manager.register_broker(broker)
        
        print("Submitting removal requests to all brokers...")
        requests = await manager.submit_removal_to_all(personal_info)
    
    # Display results
    print("\nRemoval request results:")
    print("=" * 50)
    
    for request in requests:
        print(f"• {request.broker_name}")
        print(f"  Status: {request.status.value}")
        print(f"  Request ID: {request.request_id}")
        if request.notes:
            print(f"  Notes: {request.notes}")
        print()


async def check_status() -> None:
    """Check status of all removal requests (placeholder - in real app would persist requests)."""
    print("Status checking functionality would track persistent requests.")
    print("This is a demonstration of the module structure.")


def create_personal_info_from_args(args) -> PersonalInfo:
    """Create PersonalInfo object from command line arguments."""
    return PersonalInfo(
        first_name=args.first_name,
        last_name=args.last_name,
        email=args.email,
        phone=args.phone,
        address=args.address,
        city=args.city,
        state=args.state,
        zip_code=args.zip_code,
        date_of_birth=args.date_of_birth
    )


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="AI Data Broker Remover - Remove your personal data from data brokers"
    )
    
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # List brokers command
    subparsers.add_parser("list", help="List available data brokers")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search for records at a specific broker")
    search_parser.add_argument("broker", help="Name of the broker to search")
    search_parser.add_argument("--first-name", required=True, help="First name")
    search_parser.add_argument("--last-name", required=True, help="Last name")
    search_parser.add_argument("--email", required=True, help="Email address")
    search_parser.add_argument("--phone", help="Phone number")
    search_parser.add_argument("--address", help="Street address")
    search_parser.add_argument("--city", help="City")
    search_parser.add_argument("--state", help="State")
    search_parser.add_argument("--zip-code", help="ZIP code")
    search_parser.add_argument("--date-of-birth", help="Date of birth")
    
    # Submit removal command
    submit_parser = subparsers.add_parser("submit", help="Submit removal request(s)")
    submit_parser.add_argument("--broker", help="Specific broker name (if not provided, submits to all)")
    submit_parser.add_argument("--first-name", required=True, help="First name")
    submit_parser.add_argument("--last-name", required=True, help="Last name")
    submit_parser.add_argument("--email", required=True, help="Email address")
    submit_parser.add_argument("--phone", help="Phone number")
    submit_parser.add_argument("--address", help="Street address")
    submit_parser.add_argument("--city", help="City")
    submit_parser.add_argument("--state", help="State")
    submit_parser.add_argument("--zip-code", help="ZIP code")
    submit_parser.add_argument("--date-of-birth", help="Date of birth")
    
    # Check status command
    subparsers.add_parser("status", help="Check status of removal requests")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    setup_logging(args.verbose)
    
    if args.command == "list":
        asyncio.run(list_brokers())
    
    elif args.command == "search":
        personal_info = create_personal_info_from_args(args)
        asyncio.run(search_broker(args.broker, personal_info))
    
    elif args.command == "submit":
        personal_info = create_personal_info_from_args(args)
        asyncio.run(submit_removal(args.broker, personal_info))
    
    elif args.command == "status":
        asyncio.run(check_status())


if __name__ == "__main__":
    main()
