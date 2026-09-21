import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    machine_on = True

    while machine_on:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            machine_on = False

        elif choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} pound(s)")

        elif choice == "small" or choice == "medium" or choice == "large":
            ingredients = recipes[choice]["ingredients"]
            cost = recipes[choice]["cost"]

            enough_resources = sandwich_maker_instance.check_resources(ingredients)

            if enough_resources:
                coins = cashier_instance.process_coins()
                payment = cashier_instance.transaction_result(coins, cost)

                if payment:
                    sandwich_maker_instance.make_sandwich(choice, ingredients)


if __name__ == "__main__":
    main()