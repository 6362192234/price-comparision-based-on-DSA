from collections import deque
import random
import statistics

class PriceAnalyzer:
    def __init__(self, history_size=15):
        """
        Initialize the PriceAnalyzer with a fixed-size queue for price history.
        Using deque as a Queue data structure.
        """
        self.history_size = history_size
        self.price_queue = deque(maxlen=history_size)

    def generate_simulated_history(self, current_price):
        """
        Generates a simulated price history for demonstration purposes.
        In a real app, this would fetch historical data from a database.
        
        Logic: Generates prices within +/- 15% range of current price.
        """
        self.price_queue.clear()
        
        # Determine a trend (randomly: stable, increasing, decreasing)
        trend = random.choice(['stable', 'increasing', 'decreasing'])
        
        base_price = current_price
        
        for i in range(self.history_size):
            if trend == 'stable':
                # Random fluctuation +/- 5%
                variation = random.uniform(0.95, 1.05)
                price = int(base_price * variation)
            elif trend == 'increasing':
                # Prices were lower in the past
                factor = 1.0 - (0.02 * (self.history_size - i)) # e.g. 10 days ago was 20% cheaper
                # Add some noise
                noise = random.uniform(0.98, 1.02)
                price = int(base_price * factor * noise)
            else: # decreasing
                # Prices were higher in the past
                factor = 1.0 + (0.02 * (self.history_size - i)) # e.g. 10 days ago was 20% expensive
                # Add some noise
                noise = random.uniform(0.98, 1.02)
                price = int(base_price * factor * noise)
                
            self.price_queue.append(price)
            
        # Ensure the current price is the logical next step (optional, but good for consistency)
        # We don't append current_price to history yet, history is PAST data.
        return list(self.price_queue)

    def analyze_recommendation(self, current_price):
        """
        Analyzes the price history queue to recommend BUY or WAIT.
        
        Algorithm:
        1. Calculate Moving Average of history.
        2. If current_price < Moving Average by > 5% -> STRONG BUY
        3. If current_price < Moving Average -> BUY
        4. If current_price > Moving Average -> WAIT (Price likely to drop or is high)
        """
        if not self.price_queue:
            return "UNKNOWN", "Not enough data"

        avg_price = statistics.mean(self.price_queue)
        min_history = min(self.price_queue)
        max_history = max(self.price_queue)
        
        diff_percent = ((current_price - avg_price) / avg_price) * 100
        
        if current_price < min_history:
             return "🔥 BUY NOW", "Lowest price in recent history! Great deal."
        elif diff_percent < -5:
            return "✅ BUY", f"Price is {abs(diff_percent):.1f}% below average."
        elif diff_percent < 0:
            return "✅ BUY", "Price is slighty below average."
        elif diff_percent > 10:
            return "🛑 WAIT", f"Price is {diff_percent:.1f}% above average. Likely to drop."
        else:
            return "⏳ WAIT", "Price is average. You might find a better deal soon."

    def get_history(self):
        return list(self.price_queue)
