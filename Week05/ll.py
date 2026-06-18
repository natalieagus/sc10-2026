class Node:
    def __init__(self, v, next_ref) -> None:
        self.value = v
        self.next_ref = next_ref


def make_ll():
    # eg: [9, 13, 15, 1]

    fourth_element = Node(1, None)
    third_element = Node(15, fourth_element)
    second_element = Node(13, third_element)
    first_element = Node(9, second_element)
    return first_element

def insert_to_third_place(ll, value):
    # [9, 13, 15, 1] ---> insert new one ---> [9, 13, NEW, 15, 1]
    # find ref of the third element
    temp_node = None

    index = 2
    while True:
        temp_node = ll.next_ref
        index -= index
        if index == 0:
            break

    # instance REFERENCE, NOT COPY
    original_second_element = temp_node # temp_node and original_second_element IS the same instance, which is that second Node we created earlier above, the Node with value 13
    # changing temp_node.value WILL change original_second_element.value
    original_third_element = temp_node.next_ref

    new_node = Node(value, original_third_element)
    original_second_element.next_ref = new_node




ll = make_ll()
insert_to_third_place(ll, 10)
while True:
    print(ll.value)
    ll = ll.next_ref
    if ll is None:
        break
