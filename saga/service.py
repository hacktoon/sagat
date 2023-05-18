

class Service:
    """
    Store state for a service, ex: session, header, client, etc
    Offer costly response cache
    - service configuration
    - service state
    - response cache
    """

    def __init__(self, name: str, config: dict = None) -> None:
        self.name = name
        self.config = config
