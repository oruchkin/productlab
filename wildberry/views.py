from django.http import  HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .parser import card_reciever
import xlrd
import pydantic
import json


class Product_pydantic(pydantic.BaseModel):
    article: str
    brand: str
    title: str


def index(request):
    """ Главная страница """
    return HttpResponse("index wildberies")


def read_excel(path:str) -> list:
    """Функция считывает excel файл и возвращает лист артикулей"""
    articles_list = []
    book = xlrd.open_workbook(path)
    sh = book.sheet_by_index(0)
    for rx in range(sh.nrows):
        articles_list.append(int(sh.row_values(rx)[0]))
    return articles_list


class Product_api(APIView):
    def post(self, request): 
        #проверка на наличие переданных полей
        article = request.POST.get('article')
        try:
            file = Product(docfile=request.FILES['excel'] )
            if article and file:
                return Response("ПРОВАЛ, нужно передать или 'excel' файл или 'article' - оба сразу нельзя!")
        except:
            file = None
        
        #если перетан артикль
        if article:
            try:
                article_check = int(article)
                card = card_reciever(article)
                card_data = Product_pydantic(article = card["nm_id"],
                                        brand = card["selling"]['brand_name'],
                                        title = card["imt_name"])
                card_data_serialized = json.loads(card_data.json())
                return Response(card_data_serialized)
            except:
                return Response("ПРОВАЛ, артикль должен быть цифрами")

        # если передан excel файл
        elif file:
            path = file.docfile.path
            try:
                rashirenie = path.split("/")[-1].split(".")[-1]
                if rashirenie != "xlsx":
                    return Response("ПРОВАЛ, в 'excel' можно передать  только 'xlsx' файл")
            except:
                return Response("ПРОВАЛ, в 'excel' можно передать  только 'xlsx' файл")
            file.save()
            articles_list = read_excel(file.docfile.path)
            file.delete()
            all_products = []
            for article in articles_list:
                card = card_reciever(article)
                card_data = Product_pydantic(article = card["nm_id"],
                                        brand = card["selling"]['brand_name'],
                                        title = card["imt_name"])
                card_data_serialized = json.loads(card_data.json())
                all_products.append(card_data_serialized)
            return Response(all_products)
        # если ничего не переданно
        else:
            return Response("ПРОВАЛ, сюда можно передать два поля 'article' это id товара, либо 'excel' это excel файл")
    
    
