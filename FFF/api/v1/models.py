from mongoengine import connect, Document, StringField, IntField, \
                        ReferenceField, DecimalField, DateTimeField

connect('fff')


class Buddy(Document):
    name = StringField(required=True, max_length=100)
    portrait = StringField(required=False)
    title = StringField(required=False)
    pass


class Food(Document):
    name = StringField(required=True, max_length=100)
    calories = IntField(required=True, default=0)
    pass


class Sport(Document):
    name = StringField(required=True, max_length=100)
    calories = IntField(required=True, default=0)
    pass


class Weights(Document):
    buddy = ReferenceField(Buddy, required=True)
    weight = DecimalField(required=True)
    at = DateTimeField(required=True)
    pass


class Crimes(Document):
    buddy = ReferenceField(Buddy, required=True)
    food = ReferenceField(Food, required=True)
    calories = IntField(required=True)
    pass


class Righteousness(Document):
    buddy = ReferenceField(Buddy, required=True)
    sport = ReferenceField(Sport, required=True)
    calories = IntField(required=True)
    pass
