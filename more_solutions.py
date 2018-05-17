

def _print(a):
    for e in a:
        print('{} '.format(e), end='')
    print()


def insertionSortPartial(n, arr):
    to_insert = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > to_insert:
            arr[i+1] = arr[i]
            _print(arr)

        else:
            arr[i+1] = to_insert
            _print(arr)
            break

    if to_insert < arr[0]:
        arr[0] = to_insert
        _print(arr)


def insertionSort2(n, arr):
    for j in range(1, len(arr)):
        to_insert = arr[j]

        for i in range(j-1, -1, -1):
            if arr[i] > to_insert:
                arr[i+1] = arr[i]
            else:
                arr[i+1] = to_insert
                break

        if to_insert < arr[0]:
            arr[0] = to_insert
        _print(arr)


def missing_intervals():
    a = [(2, 6), (9, 12), (8, 9), (18, 21), (4, 7), (10, 11)]
    a.sort()
    prev_max = a[0][1]
    for t in a[1:]:
        if t[0] > prev_max:
            print(prev_max, t[0])
        prev_max = max(prev_max, t[1])


class Node:
    def __init__(self, x_count, is_x):
        self.is_x = is_x
        self.method_name = None
        self.x_count = x_count
        self.children = dict()

    def add_children(self, path_components, leaf_method_name):
        if not path_components:
            self.method_name = leaf_method_name
        else:
            component, rest_of_path = path_components[0], path_components[1:]
            is_x = component == 'X'
            if component not in self.children:
                x_count = self.x_count + (1 if is_x else 0)
                self.children[component] = Node(x_count, is_x)
            self.children[component].add_children(rest_of_path, leaf_method_name)

    def find_match(self, path_components):
        matches = []
        if not path_components:
            if self.method_name:
                matches.append((self.method_name, self.x_count))
        else:
            component = path_components[0]
            rest_of_path = path_components[1:]
            if 'X' in self.children:
                matches += self.children['X'].find_match(rest_of_path)
            if component in self.children:
                matches += self.children[component].find_match(rest_of_path)
        return matches


def path_method_resolver():
    f = open('input/input')
    content = f.read()
    z = content.split('#')

    config_lines = [[s for s in r.split()] for r in z[0].strip().split('\n')]
    root_node = Node(0, False)
    for path_components, method_name in config_lines:
        path_components = path_components.strip('/').split('/')
        if path_components == ['']:             # root node edge case
            root_node.method_name = method_name
            continue
        root_node.add_children(path_components, method_name)

    request_paths = [e.strip('/').split('/') for e in z[-1].strip().split('\n')[1:]]
    for path in request_paths:
        path = [] if path == [''] else path     # root node edge case
        possible_methods = root_node.find_match(path)
        if possible_methods:
            print(min(possible_methods, key=lambda e: e[1])[0])
        else:
            print('404')

if __name__ == '__main__':
    path_method_resolver()
    missing_intervals()
