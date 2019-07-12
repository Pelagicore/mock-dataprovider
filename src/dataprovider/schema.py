import graphene
import movies.schema
import music.schema
import photos.schema

class Query(movies.schema.Query, music.schema.Query, photos.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)