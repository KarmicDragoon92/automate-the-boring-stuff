'''inventory.py, 2023-1-25 '''



player_inventory = {'gold': 30, 'arrows': 12, 'sword': 1, }

def display_inventory(inventory):
	print('Player Inventory:')
	total_items = 0
	for x, y in player_inventory.items():
		print(x, y)
		total_items += y
	print('Total items in player inventory: ', total_items)

display_inventory(player_inventory)
print('-----------------')

dragonsLoot = ['ruby', 'lengendary item', 'spell book', 'gold', ]

def addLoot(inventory, loot):
	for treasure in dragonsLoot:
		if treasure not in player_inventory:
			player_inventory[treasure] = 1
		elif treasure in player_inventory:
			player_inventory[treasure] += 1
	return player_inventory 

player_inventory = addLoot(player_inventory, dragonsLoot)

display_inventory(player_inventory)


