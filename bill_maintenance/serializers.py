from rest_framework import serializers
from .models import Bill, Product, BillItem, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('name','line1','line2','line3','city','state','pin')

class ProductSerializer(serializers.ModelSerializer):
    
    product_id = serializers.ReadOnlyField(source='items.product_id')
    name = serializers.ReadOnlyField(source='items.name')
    price = serializers.ReadOnlyField(source='items.price')
    category = serializers.ReadOnlyField(source='items.category')
    class Meta:
        model = BillItem
        fields = ('product_id','name','price','category','quantity','total')

class ItemSerializer(serializers.Serializer):
    item = serializers.IntegerField()
    quantity =serializers.IntegerField()
class ListBillSerializer(serializers.ModelSerializer):
    bill_to = AddressSerializer()
    items = ProductSerializer(source='billitem_set',many=True,read_only=True)
    bill_items = ItemSerializer(many=True,write_only=True)
    class Meta:
        model = Bill
        fields = ('invoice_no', 'bill_date', 'order_date', 'bill_to','bill_items','items','total')
        lookup_field = 'invoice_no'
        depth=1

    def create(self, validated_data):
        items = validated_data.pop('bill_items')
        address = validated_data.pop('bill_to')
        bill_to = Address.objects.create(**address)
        bill = Bill.objects.create(bill_to=bill_to,**validated_data)
        dict_items = [dict(x) for x in items]
        products = Product.objects.filter(product_id__in=[dict_item['item'] for dict_item in dict_items])
        print(products)
        for product,dict_item in zip(products,dict_items):
            total = product.price*dict_item['quantity']
            print(total)
            BillItem.objects.create(bill=bill,items=product,quantity=dict_item['quantity'],price=product.price,total=product.price*dict_item['quantity'])
        return bill 

class CreateBillSerializer(serializers.ModelSerializer):
    bill_to = AddressSerializer()
    product_ids = serializers.ListField(child=serializers.CharField())
    quantity = serializers.IntegerField()
    class Meta:
        model = Bill
        fields = ('invoice_no', 'bill_date', 'order_date', 'bill_to', 'product_ids','quantity', 'total')
    
    def create(self, validated_data):
        product_ids = validated_data.pop('product_ids')
        quantity = validated_data.pop('quantity')
        address = validated_data.pop('bill_to')
        bill_to = Address.objects.create(**address)
        bill = Bill.objects.create(bill_to=bill_to,**validated_data)
        products = Product.objects.filter(product_id__in=product_ids)
        for product in products:
            BillItem.objects.create(bill=bill,product=product,quantity=quantity,price=product.price,total=product.price*quantity)
        return bill            
