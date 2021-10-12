class A:
    def show(self):
        print("in a show")
class B(A):
    pass
pillow=A()
pillow.show()
blanket=B()
blanket.show()