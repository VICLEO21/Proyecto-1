from myLib import *

art1= art(10256, "Coca-Cola", "Canada Dry 500ml")
art1.setPrecio(25.00)
art1.setPeso(500)
art1.setDescuento(25)
art1.setInv(5)
print(art1)

art2= art (10008, "Sabritas", "Adobadas 500g")
art2.setPrecio(50.00)
art2.setPeso(500)
art2.setDescuento(25)
art2.setInv(5)
print(art2)

art3= art (13456, "Bimbo", "Donas azucaradas")
art3.setPrecio(20.00)
art3.setPeso(100)
art3.setDescuento(25)
art3.setInv(5)
print(art3)

cart=carrito('abc123')
print(cart)
cart1=carrito('abc456')

print ("")