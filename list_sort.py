def list_sort(lista):
    if isinstance(lista, list):
        sorted_elements = {}

        sorted_elements['evens'] = list()
        sorted_elements['odds'] = list()
        sorted_elements['chars'] = list()

        for item in lista:
            if isinstance(item, int) and item % 2 == 0:
                sorted_elements['evens'].append(item)
                sorted_elements['evens'].sort()
            if isinstance(item, int) and item % 2 == 1:
                sorted_elements['odds'].append(item)
                sorted_elements['odds'].sort()
            if isinstance(item, str):
                sorted_elements['chars'].append(item)
                sorted_elements['chars'].sort()
        return sorted_elements
    else:
        return 'Invalid Input'
