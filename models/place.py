#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship

# association table between places and amenities
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    review = relationship(
        "Review", backref="place",
        cascade="all, delete, delete-orphan"
    )
    amenity_ids = []

    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        back_populates="place_amenities",
        viewonly=False
    )

    @property
    def reviews(self):
        """returns reviews related to this place id"""
        required = []
        for obj in storage.all(Review).values():
            if obj.place_id == self.id:
                required.append(obj)
        return required

    @property
    def amenities(self):
        """returns list of amenity instances"""
        required = []
        for obj in storage.all(Amenity).values():
            if obj.id in Place.amenity_ids:
                required.append(obj)
        return required

    @amenities.setter
    def amenities(self, amnity):
        """adds amenity to amenity_ids for file storage"""
        if amnity.__class__.__name__ == "Amenity":
            amenity_ids.append(amnity.id)
