# def odd_even(num):
#     if num%2==0:
#         return"even"
#     else:
#         return "odd"
# print(odd_even(8))

class phone:
    def _init_(self,brand,model_name,price):

      self.brand=brand
      self.model_name=model_name
      self.price=price
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def make_a_call(self,number):
        return f"calling{number}"

phone=phone('nokia','110',1000)

print(phone.full_name())
