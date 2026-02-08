# ==================== dsa/hashmap.py (HASH MAP IMPLEMENTATION) ====================

class ProductHashMap:
    """
    HashMap for fast product lookup
    Time Complexity: O(1) average for insert and get
    Space Complexity: O(n) where n is number of products
    """
    
    def __init__(self):
        self.map = {}
    
    def insert(self, key, value):
        """
        Insert product into HashMap
        Key: product name
        Value: product details (seller, price, rating)
        """
        if key not in self.map:
            self.map[key] = []
        self.map[key].append(value)
    
    def get(self, key):
        """
        Get all seller entries for a product
        Returns list of products or empty list if not found
        """
        return self.map.get(key, [])
    
    def get_all_keys(self):
        """Get all product names"""
        return list(self.map.keys())
    
    def size(self):
        """Get total number of unique products"""
        return len(self.map)
    
    def contains(self, key):
        """Check if product exists"""
        return key in self.map
    
    def remove(self, key):
        """Remove product from HashMap"""
        if key in self.map:
            del self.map[key]
            return True
        return False


def build_product_map(products):
    """
    Build HashMap from product list
    Groups products by name for fast lookup
    """
    product_map = ProductHashMap()
    
    for product in products:
        product_map.insert(product['name'], product)
    
    return product_map


def search_product(product_map, product_name):
    """
    Search for a product in HashMap
    Time Complexity: O(1)
    """
    return product_map.get(product_name)
