from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=254)
    mobile_number = models.IntegerField()
    client_address = models.CharField(max_length=200)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client{self.name, self.mobile_number, self.registration_date}'


class Goods(models.Model):
    name_goods = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)  # представляет значение типа Number, которое имеет
    # максимум X разрядов и Y знаков после запятой
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Goodst{self.name_goods, self.price, self.quantity}'


class Ordergds(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    all_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order{self.client.name, self.goods.name_goods, self.all_price}'
