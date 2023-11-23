class Ship:
    def __init__(self, draft, crew):
        self.draft = draft  # Total weight of the ship
        self.crew = crew    # Number of crew members

    def is_worth_it(self):
        # Subtract the weight contributed by the crew
        net_draft = self.draft - (self.crew * 1.5)
        # Check if the net draft is more than 20
        return net_draft > 20