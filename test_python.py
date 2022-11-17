def add_to_map():
    name = "bla_bla_two_three"
    order_name_split = name.split("_")
    order_names = order_name_split[1: len(order_name_split) - 1]

    print(str(order_names))


add_to_map()
