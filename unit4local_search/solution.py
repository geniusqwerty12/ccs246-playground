class Solution:
    def __init__(self, items):
        self.items = items

    # function to get the index
    def getItemByPrice(self, list, price):
        # https://stackoverflow.com/questions/67349486/best-way-to-get-object-reference-in-object-list-based-on-attribute-value
        return list.index( next( item for item in self.items if item.price == price))

    # function to solve the cost of the solution
    def cost(self):
        # loop the items inside, getting the price of each item
        # then adding them up
        return sum( item.price for item in self.items )