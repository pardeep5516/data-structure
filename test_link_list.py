import unittest
from colorama import Fore, Style

from link_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_head_value(self):
        data = LinkedList(10)
        if data.head.value == 10:
            print(Fore.GREEN + f"Test Passed: {data.head.value}" + Style.RESET_ALL)

        else:
            print(Fore.RED + f"Test Failed: {data.head.value}" + Style.RESET_ALL)

    def test_length(self):
        data = LinkedList(10)
        if data.length == 1:
            print(Fore.GREEN + f"Test Passed: {data.length}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Test Failed: {data.length}" + Style.RESET_ALL)

    def test_append(self):
        data = LinkedList(10)
        data.append(5)
        if data.tail.value == 5:
            print(Fore.GREEN + f"Test Passed: {data.tail.value}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Test Failed: {data.tail.value}" + Style.RESET_ALL)

    def test_prepend(self):
        data = LinkedList(10)
        data.prepend(5)
        if data.head.value == 5:
            print(Fore.GREEN + f"Test Passed: {data.head.value}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Test Failed: {data.head.value}" + Style.RESET_ALL)

    def test_pop(self):
        data = LinkedList(10)
        data.append(5)
        data.append(16)
        data.pop()
        if data.tail.value == 5:
            print(Fore.GREEN + f"Test Passed: {data.tail.value}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Test Failed: {data.tail.value}" + Style.RESET_ALL)


if __name__ == "__main__":
    unittest.main()
