from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from aproducts.models import A_Product

class SearchKnowledgeProductView(ListView):
    #queryset = A_Product.objects.all()
    template_name = "searchknowledge/view.html"

    def get_context_data(self, *args, **kwargs):
        context=super(SearchKnowlegdeProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get("q")
        query1 = self.request.GET.get("q1")
        query2 = self.request.GET.get("q2")

        context["query"] = query
        context["query1"] = query1
        context["query2"] = query2


        #SearchQuery.objects.create(query=query)

        return context

    def get_queryset(self, *args, **kwargs ):
        request = self.request
        method_dict = request.GET
        query = method_dict.get("q", None)
        query1 = method_dict.get("q1", None)
        query2 = method_dict.get("q2", None)


        #print(query)
        if query is not None:
            return A_Product.objects.filter(title__icontains=query,price__icontains=query1,Color__icontains=query2)
            # return A_Product.objects.filter(price__icontains=query)
            # return A_Product.objects.filter(memory__icontains=query)

        return A_Product.objects.featured()
        #return A_Product.objects.filter(title__icontains="samsung")