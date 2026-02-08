# ==================== dsa/heap_utils.py (MIN-HEAP IMPLEMENTATION) ====================

class MinHeap:
    """
    Min-Heap for price optimization
    Time Complexity:
        - Insert: O(log n)
        - Extract Min: O(log n)
        - Get Min: O(1)
    Space Complexity: O(n)
    """
    
    def __init__(self):
        self.heap = []
    
    def insert(self, price, product):
        """Insert product with price into heap"""
        self.heap.append((price, product))
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, index):
        """Move element up to maintain heap property"""
        while index > 0:
            parent_index = (index - 1) // 2
            
            if self.heap[parent_index][0] <= self.heap[index][0]:
                break
            
            # Swap with parent
            self.heap[parent_index], self.heap[index] = \
                self.heap[index], self.heap[parent_index]
            
            index = parent_index
    
    def extract_min(self):
        """Extract product with minimum price"""
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()[1]  # Return product only
        
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        
        return min_item[1]  # Return product only
    
    def _bubble_down(self, index):
        """Move element down to maintain heap property"""
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            
            if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            
            if smallest == index:
                break
            
            self.heap[index], self.heap[smallest] = \
                self.heap[smallest], self.heap[index]
            
            index = smallest
    
    def peek(self):
        """Get minimum without removing"""
        if self.heap:
            return self.heap[0][1]
        return None
    
    def size(self):
        """Get heap size"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def get_all_sorted(self):
        """Get all products sorted by price (non-destructive)"""
        return sorted(self.heap, key=lambda x: x[0])


def find_best_price(products):
    """
    Find product with best (minimum) price using Min-Heap
    Time Complexity: O(n log n) for building heap
    """
    if not products:
        return None
    
    min_heap = MinHeap()
    
    for product in products:
        min_heap.insert(product['price'], product)
    
    return min_heap.extract_min()


def find_top_n_cheapest(products, n=3):
    """
    Find top N cheapest products
    Time Complexity: O(n log n + k log n) where k is number to extract
    """
    if not products:
        return []
    
    min_heap = MinHeap()
    
    for product in products:
        min_heap.insert(product['price'], product)
    
    results = []
    for _ in range(min(n, len(products))):
        if not min_heap.is_empty():
            results.append(min_heap.extract_min())
    
    return results


def compare_prices(products):
    """
    Compare all prices and return statistics
    """
    if not products:
        return {}
    
    prices = [p['price'] for p in products]
    
    return {
        'min_price': min(prices),
        'max_price': max(prices),
        'avg_price': sum(prices) / len(prices),
        'price_range': max(prices) - min(prices),
        'num_sellers': len(products)
    }