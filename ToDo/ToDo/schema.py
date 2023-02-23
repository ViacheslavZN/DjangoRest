import graphene
from graphene_django import DjangoObjectType
from ToDoApp.models import Project, Users, TODO

class Meta:
    model = Users
    fields = '__all__'

class Query(graphene.ObjectType):
    all_users = graphene.List(UsersType)
    def all_users(root, info):
        return Users.objects.all()
        schema = graphene.Schema(query=Query)

    all_projects = graphene.List(ProjectType)

    def all_projects(root, info):
        return Project.objects.all()
        schema = graphene.Schema(query=Query)

    all_TODO= graphene.List(TODOType)
 def all_TODO(root, info):
        return TODO.objects.all()
        schema = graphene.Schema(query=Query)













