# ==================== dsa/tree_search.py (TRIE / PREFIX TREE IMPLEMENTATION) ====================

class TrieNode:
    """Node in Trie data structure"""
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None


class TrieSearch:
    """
    Trie (Prefix Tree) for auto-complete search
    Time Complexity:
        - Insert: O(m) where m is word length
        - Search: O(m)
        - Prefix Search: O(m + k) where k is number of results
    Space Complexity: O(total characters in all words)
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert word into Trie"""
        node = self.root
        word_lower = word.lower()
        
        for char in word_lower:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
        node.word = word  # Store original word with case
    
    def search(self, word):
        """Search for exact word match"""
        node = self._find_node(word.lower())
        return node is not None and node.is_end_of_word
    
    def _find_node(self, prefix):
        """Find node corresponding to prefix"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        
        return node
    
    def search_prefix(self, prefix):
        """
        Find all words starting with given prefix
        Returns list of matching words
        """
        if not prefix:
            return []
        
        node = self._find_node(prefix.lower())
        
        if node is None:
            return []
        
        # Collect all words from this node
        results = []
        self._collect_words(node, results)
        
        return results
    
    def _collect_words(self, node, results):
        """Recursively collect all words from a node"""
        if node.is_end_of_word:
            results.append(node.word)
        
        for child in node.children.values():
            self._collect_words(child, results)
    
    def autocomplete(self, prefix, max_results=10):
        """
        Get autocomplete suggestions for prefix
        Limited to max_results
        """
        suggestions = self.search_prefix(prefix)
        return suggestions[:max_results]


def build_trie_from_products(products):
    """Build Trie from product names"""
    trie = TrieSearch()
    
    unique_names = set([p['name'] for p in products])
    
    for name in unique_names:
        trie.insert(name)
    
    return trie


def prefix_search(items, prefix):
    """
    Simple prefix search (fallback without Trie)
    Time Complexity: O(n * m) where n=items, m=prefix length
    """
    if not prefix:
        return list(items)
    
    prefix_lower = prefix.lower()
    return [item for item in items if item.lower().startswith(prefix_lower)]