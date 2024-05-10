def remove_elements(list_to_remove_elements):
	del list_to_remove_elements[0:1]
	del list_to_remove_elements[3:4]
	del list_to_remove_elements[3:4] 
	return list_to_remove_elements

def add_elements(list_to_add_elements):
	list_to_add_elements.insert(0, "Pink")
	list_to_add_elements.append("Yellow")
	return list_to_add_elements


def is_empty(list_to_check):
	if list_to_check:
		return False
	else:
		return True


def check_lists(list_to_compare1, list_to_compare2):
    if is_empty(list_to_compare1) or is_empty(list_to_compare2):
    	return False
    else:
    	if list_to_compare1[2:3] == list_to_compare2[2:3]:
    		return True
    	else:
    		return False



def list_of_lists(list_of_lists_to_modify):
	new_lista1 = list_of_lists_to_modify[0][0:2]
	new_lista2 = list_of_lists_to_modify[1][1:4]
	new_lista3 = list_of_lists_to_modify[2][-2:]
	lista_ext = [new_lista1, new_lista2, new_lista3]
	return lista_ext
