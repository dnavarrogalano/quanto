from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
aategorias_acciones = Table('aategorias_acciones', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('categoria_id', Integer, primary_key=True, nullable=False),
    Column('accion_id', Integer, primary_key=True, nullable=False),
)

accion = Table('accion', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nemo', String(length=20)),
    Column('empresa', String(length=120)),
)

categoria = Table('categoria', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nombre', String(length=50)),
    Column('descripcion', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['aategorias_acciones'].create()
    post_meta.tables['accion'].create()
    post_meta.tables['categoria'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['aategorias_acciones'].drop()
    post_meta.tables['accion'].drop()
    post_meta.tables['categoria'].drop()
