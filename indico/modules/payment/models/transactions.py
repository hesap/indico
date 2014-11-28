# This file is part of Indico.
# Copyright (C) 2002 - 2014 European Organization for Nuclear Research (CERN).
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# Indico is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico; if not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from sqlalchemy.dialects.postgresql import JSON

from indico.core.db import db
from indico.util.string import return_ascii
from indico.util.struct.enum import IndicoEnum
from MaKaC.conference import ConferenceHolder


class TransactionStatus(int, IndicoEnum):
    successful = 1  # payment successful
    failed = 2  # payment failed/cancelled
    rejected = 3  # payment rejected after a previous success


class PaymentTransaction(db.Model):
    """Payment transactions"""
    __tablename__ = 'payment_transactions'
    __table_args__ = (db.CheckConstraint('status IN ({})'.format(', '.join(map(str, TransactionStatus)))),
                      db.CheckConstraint('amount > 0'),
                      db.UniqueConstraint('event_id', 'registrant_id'),
                      {'schema': 'events'})

    #: Entry ID
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    #: ID of the event
    event_id = db.Column(
        db.Integer,
        index=True,
        nullable=False
    )
    #: ID of the registrant
    registrant_id = db.Column(
        db.Integer,
        nullable=False
    )
    #: a :class:`TransactionStatus`
    status = db.Column(
        db.SmallInteger,
        nullable=False
    )
    #: the base amount the user needs to pay (without payment-specific fees)
    amount = db.Column(
        db.Numeric(8, 2),  # max. 999999.99
        nullable=False
    )
    #: the currency of the payment (ISO string, e.g. EUR or USD)
    currency = db.Column(
        db.String,
        nullable=False
    )
    #: plugin-specific data of the payment
    data = db.Column(
        JSON,
        nullable=False
    )

    @property
    def event(self):
        return ConferenceHolder().getById(str(self.event_id))

    @property
    def registrant(self):
        return self.event.getRegistrantById(str(self.registrant_id))

    @registrant.setter
    def registrant(self, registrant):
        self.registrant_id = int(registrant.getId())
        self.event_id = int(registrant.getConference().getId())

    @return_ascii
    def __repr__(self):
        # in case of a new object we might not have the default status set
        return '<PaymentTransaction({}, {}, {}, {} {})>'.format(self.event_id, self.registrant_id,
                                                                TransactionStatus(self.status).name, self.amount,
                                                                self.currency)
