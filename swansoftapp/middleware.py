from .models import *

class cartcount:

    # this both are compulsary functions
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_view(self,request,view_func,*view_args,**view_kargs):
        if request.user.id==None:
            request.Cart_count=0
        else:
            request.Cart_count=CartItem.objects.filter(cart__user=request.user).count()