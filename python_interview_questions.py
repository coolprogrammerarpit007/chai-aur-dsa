print("Python Interview Questions")
print("************* -------------- ***********")



import copy as cp

l1 = [1,2,3,4,5,6,7,8,9,10]
l1_copy = cp.copy(l1)
# print(l1_copy)


l2 = [[1,2,3,4,5],6,7,8]
l2_deep_copy = cp.deepcopy(l2)
# print(l2_deep_copy)

#  Generators in Python

# def number_range(number):
#     for index in range(number+1):
#         yield index


# result = list(number_range(100))
# print(result)


from abc import ABC,abstractclassmethod


class Animal(ABC):
    @abstractclassmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        print("Bark")
        
animal = Dog()
# animal.make_sound()