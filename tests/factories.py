from factory import Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from pairbutton.models import db, Channel, File


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class ChannelFactory(BaseFactory):
    class Meta:
        model = Channel

    name = Sequence(lambda n: 'mychannel{}'.format(n))
    key = Sequence(lambda n: 'mykey{}'.format(n))


class FileFactory(BaseFactory):
    class Meta:
        model = File

    name = Sequence(lambda n: 'myname{}'.format(n))
    data = Sequence(lambda n: 'mydata{}'.format(n))
    channel = SubFactory(ChannelFactory)

