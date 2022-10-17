from xmlrpc.client import Boolean

class User():
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.friends_of_friends = []
        
    # добавляем пользователя в друзья
    def add_friend(self,target_user):
        if target_user not in self.friends:
            self.friends.append(target_user)

    # добавляем друзей своих друзей
    def add_friends_of_friends(self):
        my_friends_friends_list = [self.name]
        for friend in self.friends:
            this_friends_friends_list = friend.friends
            #для каждого друга среди моих друзей
            for friends_friend in this_friends_friends_list:
                # для каждого друга моего друга 
                if friends_friend.name not in my_friends_friends_list:
                    my_friends_friends_list.append(friends_friend.name)
                    self.friends_of_friends.append(friends_friend)


def get_person_obj(name:str,all_persons_sort_list:list,
                    persons_obj_list:list) -> User:
    """ Функция для получения обьекта пользователя. """
    position = all_persons_sort_list.index(name)
    return persons_obj_list[position]


def get_persons_names(net:tuple)-> list:
    """ Находим уникальных пользователей в сети. """
    all_persons_set = set()
    for relation in net:
        for i in relation:
            all_persons_set.add(i)
    all_persons_sort_list = (list(all_persons_set))
    all_persons_sort_list.sort()
    return all_persons_sort_list


def generate_person_obj(all_persons_sort_list:list)-> list:
    """ Генерируем обьекты пользователей. """
    persons_obj_list = []
    for i in all_persons_sort_list:
        persons_obj_list.append(User(i))
    return persons_obj_list


def add_friends_relations(net:tuple,all_persons_sort_list:list, 
                          persons_obj_list:list) -> None:
    """ Добавляем друзей каждому пользователю, а затем друзей его друзей """
    for relation in net:
        user_1_obj = get_person_obj(relation[0],all_persons_sort_list,persons_obj_list)
        user_2_obj = get_person_obj(relation[1],all_persons_sort_list,persons_obj_list)
        user_1_obj.add_friend(user_2_obj)
        user_2_obj.add_friend(user_1_obj)
    for user in persons_obj_list:
        user.add_friends_of_friends()
    return None


def get_friendship(first:str, second:str,all_persons_sort_list,persons_obj_list) -> Boolean:
    """ Проверяем есть ли у двух друзей общие друзья """
    first_user = get_person_obj(first,all_persons_sort_list,persons_obj_list)
    all_first_friends = [i.name for i in first_user.friends] + [i.name for i in first_user.friends_of_friends]
    second_user = get_person_obj(second,all_persons_sort_list,persons_obj_list)
    all_second_friends = [i.name for i in second_user.friends] + [i.name for i in second_user.friends_of_friends]
    #проверяем есть ли в списках друзей совпадения
    for i in all_first_friends:
        if i in all_second_friends:
            return True
    return False


def check_relation(net:tuple, first:str, second:str) -> Boolean:
    """ Основаная функция со всей логикой """
    all_persons_sort_list = get_persons_names(net)
    persons_obj_list = generate_person_obj(all_persons_sort_list)
    add_friends_relations(net,all_persons_sort_list,persons_obj_list)
    result = get_friendship(first, second,all_persons_sort_list,persons_obj_list)
    return result


if __name__ == '__main__':
    net = (
    ("Ваня", "Лёша"), ("Лёша", "Катя"),
    ("Ваня", "Катя"), ("Вова", "Катя"),
    ("Лёша", "Лена"), ("Оля", "Петя"),
    ("Стёпа", "Оля"), ("Оля", "Настя"),
    ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True