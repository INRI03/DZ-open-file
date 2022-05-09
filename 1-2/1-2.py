
file_name = 'cook_book.txt'

def book(txt):
    cook_book = {}
    with open(file_name, 'r', encoding="utf-8") as f:
        for string in f:
            dish = string
            quantity = f.readline()
            products = []
            for x in range(int(quantity)):
                comp = f.readline().split(' |')
                comps = {'product': comp[0], 'quantity': int(comp[1]), 'measure': comp[2].strip()}
                products.append(comps)
            cook_book[dish.strip()] = products
            f.readline()
    def get_shop_list_by_dishes():
        dishes = input('Введите список блюд (через запятую): ').split(' , ')
        person_count = int(input('Введите количество человек: '))
        list_products = {}
        for dish in dishes:
            dish = dish.capitalize()
            if dish in cook_book.keys():
                list_ = cook_book.get(dish)
                new_list = {}
                for string in list_:
                    new_list[string['product']] = {'measure': string['measure'],
                                                   'quantity': string['quantity'] * person_count}
                list_products.update(new_list)
            else:
                print('Такого блюда нет в книге, внесите данные')
                cook_book[dish] = None
        print(list_products)
        print(cook_book)

    get_shop_list_by_dishes()

book(file_name)


