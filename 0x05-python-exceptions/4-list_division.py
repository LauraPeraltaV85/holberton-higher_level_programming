#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    count = 0
    for count in range(list_length):
        try:
            count = my_list_1[count]/my_list_2[count]
        except (ValueError, TypeError):
            count = 0
            print("wrong type")
        except ZeroDivisionError:
            count = 0
            print("division by 0")
        except IndexError:
            count = 0
            print("out of range")
        finally:
            new.append(count)
    return new
