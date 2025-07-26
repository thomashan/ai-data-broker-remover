from data_source import DataSource


class InMemSource(DataSource):
    def get_brokers(self, url: str) -> list[str]:
        # Dummy implementation for database source, url can be a connection string
        print(f"Connecting to database at {url} (dummy implementation)")
        return ["BrokerX", "BrokerY", "BrokerZ"]
