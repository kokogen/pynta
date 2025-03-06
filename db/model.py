from enum import Enum
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects.postgresql import UUID

class NodeType(str, Enum):
    OPERATION = 'OP'
    ENTITY_DATAVERSION = 'EDV'

class Base(DeclarativeBase):
    pass

class Dag(Base):
    __tablename__ = 'dag'

    dag_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True) 
    nodes: Mapped[Set['Node']] = relationship(back_populates='dag') 
    params: Mapped[Set[str]] = mapped_column(ARRAY(String), nullable=False)

class Node(Base):
    __tablename__ = 'node'
    node_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped(str) = mapped_column(String(100), nullable=False, unique=True)
    node_type: Mapped[NodeType] = mapped_column(String(5), nullable=False)
    dag_id: Mapped[int] = mapped_column(ForeignKey('dag.dag_id'))
    dag: Mapped['Dag'] = relationship(back_populates='nodes')

class Edge(Base):
    __tablename__ = 'edge'
    left_node_id: Mapped[int] = mapped_column(ForeignKey('node.node_id'), primary_key=True)
    right_node_id: Mapped[int] = mapped_column(ForeignKey('node.node_id'), primary_key=True)
    
class DagOperation(Base):
    __tablename__ = 'dag_operation'
    node_id: Mapped[int] = mapped_column(ForeignKey('node.node_id'), primary_key=True)
    params: Mapped[Set[str]] = mapped_column(ARRAY(String), nullable=False)

class Edv(Base):
    __tablename__ = 'edv'
    node_id: Mapped[int] = mapped_column(ForeignKey('node.node_id'), primary_key=True)
