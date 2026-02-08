# ==================== dsa/graph_recommend.py (GRAPH + BFS IMPLEMENTATION) ====================

from collections import deque
from data.products import get_products_by_category, get_unique_product_names


class ProductGraph:
    """
    Graph for modeling product similarity
    Nodes: Products
    Edges: Similarity (same category/specs)
    
    Time Complexity:
        - Add Edge: O(1)
        - BFS: O(V + E) where V=vertices, E=edges
    """
    
    def __init__(self, category=None):
        self.graph = {}
        self.products_data = {}
        
        if category:
            self._build_from_category(category)
    
    def _build_from_category(self, category):
        """Build graph from products in a category"""
        products = get_products_by_category(category)
        
        # Group products by name
        product_groups = {}
        for p in products:
            name = p['name']
            if name not in product_groups:
                product_groups[name] = []
            product_groups[name].append(p)
        
        # Store product data
        for name, variants in product_groups.items():
            self.products_data[name] = {
                'name': name,
                'variants': variants,
                'min_price': min(v['price'] for v in variants),
                'max_rating': max(v['rating'] for v in variants),
                'specs': variants[0].get('specs', 'general')
            }
        
        # Create edges based on similarity
        names = list(product_groups.keys())
        
        for name in names:
            self.graph[name] = []
            
            # Connect products with similar specs
            for other_name in names:
                if name != other_name:
                    if self._are_similar(name, other_name):
                        self.graph[name].append(other_name)
    
    def _are_similar(self, product1, product2):
        """
        Check if two products are similar
        Based on specs, price range, etc.
        """
        if product1 not in self.products_data or product2 not in self.products_data:
            return False
        
        p1 = self.products_data[product1]
        p2 = self.products_data[product2]
        
        # Same specs category
        if p1['specs'] == p2['specs']:
            return True
        
        # Similar price range (within 50%)
        price_ratio = p1['min_price'] / p2['min_price']
        if 0.5 <= price_ratio <= 2.0:
            return True
        
        return False
    
    def add_edge(self, product1, product2):
        """Add edge between two products"""
        if product1 not in self.graph:
            self.graph[product1] = []
        if product2 not in self.graph:
            self.graph[product2] = []
        
        if product2 not in self.graph[product1]:
            self.graph[product1].append(product2)
    
    def get_neighbors(self, product):
        """Get all neighbors of a product"""
        return self.graph.get(product, [])
    
    def bfs(self, start_product, target_condition):
        """
        Breadth-First Search
        Find products matching target_condition starting from start_product
        
        Time Complexity: O(V + E)
        """
        if start_product not in self.graph:
            return []
        
        visited = set()
        queue = deque([start_product])
        visited.add(start_product)
        results = []
        
        while queue:
            current = queue.popleft()
            
            # Check if current product meets condition
            if target_condition(current, self.products_data.get(current)):
                if current != start_product:  # Don't include starting product
                    results.append(self.products_data[current])
            
            # Visit neighbors
            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return results


def find_alternatives_bfs(product_name, max_price, category):
    """
    Find cheaper alternatives using BFS
    
    Args:
        product_name: Current product
        max_price: Maximum acceptable price
        category: Product category
    
    Returns:
        List of cheaper alternative products
    """
    graph = ProductGraph(category)
    
    def is_cheaper_alternative(name, data):
        """Check if product is a cheaper alternative"""
        if data is None:
            return False
        return data['min_price'] < max_price
    
    alternatives = graph.bfs(product_name, is_cheaper_alternative)
    
    # Sort by price (cheapest first)
    alternatives.sort(key=lambda x: x['min_price'])
    
    return alternatives[:5]  # Return top 5


def recommend_by_price_range(category, min_price, max_price):
    """
    Recommend products in a price range
    Uses BFS to find connected products
    """
    graph = ProductGraph(category)
    
    # Find a product in range to start BFS
    start_product = None
    for name, data in graph.products_data.items():
        if min_price <= data['min_price'] <= max_price:
            start_product = name
            break
    
    if not start_product:
        return []
    
    def in_price_range(name, data):
        if data is None:
            return False
        return min_price <= data['min_price'] <= max_price
    
    recommendations = graph.bfs(start_product, in_price_range)
    
    return recommendations


def find_best_rated_alternatives(product_name, category, min_rating=4.0):
    """
    Find highly rated alternatives
    """
    graph = ProductGraph(category)
    
    def is_highly_rated(name, data):
        if data is None:
            return False
        return data['max_rating'] >= min_rating
    
    alternatives = graph.bfs(product_name, is_highly_rated)
    
    # Sort by rating (highest first)
    alternatives.sort(key=lambda x: x['max_rating'], reverse=True)
    
    return alternatives[:5]