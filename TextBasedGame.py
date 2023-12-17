# print main menu and instructions
def show_instructions():
    print("Dragon Text Adventure Game")
    print("Collect all 6 items to win the game to defeat the Dragon")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


def player_stat(current_room, inventory, rooms):
    print('--------------------------------------------------------')
    print('You are in the {}.'.format(current_room))
    print('Inventory:', inventory)
    i = len(inventory)
    inventory_count = 6 - int(i)
    print('Items Left: {} more'.format(inventory_count))
    if current_room != 'Town':
        print('You see the', rooms[current_room]['item'], end='.\n')
    print('--------------------------------------------------------')


def main():   # links different rooms and their items, except start and end rooms
    rooms = {
        'Town': {'South': 'Desert', 'East': 'Bridge'},
        'Desert': {'South': 'Field', 'East': 'Dark Forest', 'item': 'Sword'},
        'Dark Forest': {'East': 'Castle', 'South': 'Forest', 'North': 'Bridge', 'item': 'Armor'},
        'Field': {'North': 'Desert', 'East': 'Forest', 'item': 'Boots'},
        'Forest': {'North': 'Dark Forest', 'West': 'Field', 'item': 'Shield'},
        'Swamp': {'South': 'Castle', 'item': 'Bird'},
        'Bridge': {'South': 'Dark Forest', 'East': 'Swamp', 'item': 'Cape'},
        'Castle': {'North': 'Swamp', 'item': 'Dragon'}  # Villain
    }

    current_room = 'Town'
    player_move = ''
    inventory = []
    show_instructions()

    def move_directions(player_move, current_room):

        if player_move == 'South':
            return rooms[current_room]['South']
        elif player_move == 'North':
            return rooms[current_room]['North']
        elif player_move == 'East':
            return rooms[current_room]['East']
        elif player_move == 'West':
            return rooms[current_room]['West']

    def get_item():
        if player_move in rooms[current_room]['item']:
            inventory.append(rooms[current_room]['item'])

    while True:

        while len(inventory) <= 6 and current_room != 'Castle':

            player_stat(current_room, inventory, rooms)

            user_input = input('Enter your move:\n').title().split()
            print(user_input[0])

            if user_input[0] in ('Go', 'Get'):
                user_input.pop(0)
                player_move = ' '.join([str(elem) for elem in user_input])
            print(player_move)  # used for testing of split REMOVE LATER

            if player_move == 'Exit':
                exit('You have exited the game. Play again soon!')
                # Prints when you exit the game

            # validates current moves and rooms
            elif player_move in rooms[current_room]:
                current_room = move_directions(player_move, current_room)
            # validates current items and checks if you have picked it up
            elif player_move in rooms[current_room]['item']:

                if player_move in inventory:
                    print('You already have this item. Proceed to another room.')

                elif player_move != inventory:
                    get_item()

            elif user_input[0] != 'Go' or 'Get':
                print("That is not a valid move. Try again.")

            else:
                print("That is not a valid move. Try again.")  # Tells player move is not valid

        if len(inventory) == 6 and current_room == 'Castle':  # checks if win conditions are met
            print("Your pet bird distracts the dragon as you fight it with all of your equipment and slay the beast")
            print("You win!!")
            print("Thanks for playing the game. Hope you enjoyed it.")

        else:  # if win condition is not met
            exit('The Dragon swoops down and eats you.\n'
                 'GAME OVER!')
        break


main()
