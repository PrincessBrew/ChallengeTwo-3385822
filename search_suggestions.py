from typing import List

class SearchSuggestionSystem:
    def __init__(self, products: List[str]):
        # Sort products lexicographically when initializing
        self.products = sorted(products)

    def getSuggestions(self, searchWord: str) -> List[List[str]]:
        suggestions = []
        prefix = ""

        for char in searchWord:
            prefix += char
            # Filter products that start with the current prefix
            matches = [product for product in self.products if product.startswith(prefix)]
            # Take up to 3 matches
            suggestions.append(matches[:3])

        return suggestions


# Test the solution
if __name__ == "__main__":
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"

    system = SearchSuggestionSystem(products)
    result = system.getSuggestions(searchWord)

    print(result)
