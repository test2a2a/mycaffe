---------------------------------------

 __lte -> Less than or equal
 __gte -> Greater than or equal
 __lt -> Less than
 __gt -> Greater than


QuerySet(foo__lte=10) # foo <= 10
QuerySet(foo__gte=10) # foo >= 10
QuerySet(foo__lt=10) # foo < 10
QuerySet(foo__gt=10) # foo > 



data=Product.objects.filter(name__icontains=product_name)
