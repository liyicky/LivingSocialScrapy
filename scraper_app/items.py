from scrapy.item import Item, Field

class LivingSocialDeal(Item):
  """Livingsocial container"""
  title          = Field()
  link           = Field()
  seller         = Field()
  availability   = Field()
  price          = Field()


