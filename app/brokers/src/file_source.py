from data_source import DataSource


class FileSource(DataSource):
    def get_brokers(self, url: str) -> list[str]:
        brokers = []
        try:
            with open(url, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith(
                        "#"
                    ):  # Ignore empty lines and comments
                        brokers.append(line)
        except FileNotFoundError:
            print(f"Error: File not found at {url}")
        return brokers
