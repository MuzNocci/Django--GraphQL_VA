import graphene
from graphene_django import DjangoObjectType
from books.models import Books



class BooksType(DjangoObjectType):


    class Meta:

        model = Books
        fields = ("id", "title", "excerpt") # '__all__' for all cols


class Query(graphene.ObjectType):

    all_books = graphene.List(BooksType)


    def resolve_all_books(root, info):
        # return Books.objects.filter(title='Django')
        return Books.objects.all()


schema = graphene.Schema(query=Query)