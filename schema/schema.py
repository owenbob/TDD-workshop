import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene import relay, Schema, ObjectType

from models.models import User, Story, db_session


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)

class StoryType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)


class CreateUser(graphene.Mutation):
    
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
    
    user = graphene.Field(UserType)

    def mutate(self, info, **kwargs):
        user = User(**kwargs)
        db_session.add(user)
        db_session.commit()

        return CreateUser(user=user)


class UpdateUsername(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, email, **kwargs):
        query = UserType.get_query(info)
        user = query.filter(User.email == email).first()
        print(kwargs)
        if kwargs.get("username"):
            user.username = kwargs["username"]
        if kwargs.get("last_name"):
            user.last_name = kwargs["last_name"]
        if kwargs.get("first_name"):
            user.first_name = kwargs["first_name"]
        if kwargs.get("password"):
            user.password = kwargs["password"]

        db_session.commit()

        return UpdateUsername(user=user)


class DeleteUser(graphene.Mutation):
    class Arguments:
        email = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self,info,email):
        query = UserType.get_query(info)
        user = query.filter(User.email == email).first()

        db_session.delete(user)
        db_session.commit()
        return DeleteUser(user=user)


class Query(ObjectType):
    node = relay.Node.Field()
    user = SQLAlchemyConnectionField(StoryType)


class SocialMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_username = UpdateUsername.Field()
    delete_user = DeleteUser.Field()


schema = Schema(query=Query, mutation=SocialMutation)
