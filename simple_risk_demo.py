import random
import statistics

class SimpleRiskModel:
    def __init__(self, name, min_loss, max_loss, probability):
        self.name = name
        self.min_loss = min_loss
        self.max_loss = max_loss
        self.probability = probability

    def simulate(self, iterations=10000):
        losses = []
        for _ in range(iterations):
            if random.random() < self.probability:
                loss = random.uniform(self.min_loss, self.max_loss)
                losses.append(loss)
            else:
                losses.append(0)
        return losses

    def analyze(self):
        losses = self.simulate()
        return {
            'name': self.name,
            'average_loss': statistics.mean(losses),
            'max_loss': max(losses),
            'ninety_percentile': sorted(losses)[int(len(losses) * 0.9)]
        }

# Example usage
cyber_breach = SimpleRiskModel(
    name="Data Breach Scenario",
    min_loss=100000,  # $100,000
    max_loss=1000000,  # $1,000,000
    probability=0.1    # 10% chance per year
)

results = cyber_breach.analyze()

print(f"\nRisk Analysis for {results['name']}:")
print(f"Average Annual Loss: ${results['average_loss']:,.2f}")
print(f"Maximum Potential Loss: ${results['max_loss']:,.2f}")
print(f"90th Percentile Loss: ${results['ninety_percentile']:,.2f}")