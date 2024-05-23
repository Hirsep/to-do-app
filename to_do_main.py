import datetime
import to_do_list_oop
import to_do_oop


new_to_do_list = to_do_list_oop.ToDoList()
new_element = to_do_oop.ToDo("Test", "Wir haben ein Test")
new_element2=to_do_oop.ToDo("Neuer test","2")
new_to_do_list.add_to_do_element(new_element)
new_to_do_list.add_to_do_element(new_element)
new_to_do_list.add_to_do_element(new_element2)
new_to_do_list.print_to_do_list()
print("------------------------------------------------------------------------")
new_to_do_list.remove_to_do_element(new_element)
new_to_do_list.print_to_do_list()
