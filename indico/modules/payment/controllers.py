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

from flask import redirect, flash

from indico.modules.payment import settings
from indico.modules.payment.forms import SettingsForm
from indico.modules.payment.views import WPPayment
from indico.util.i18n import _
from indico.web.flask.util import url_for
from indico.web.forms.base import FormDefaults
from MaKaC.webinterface.rh.admins import RHAdminBase


class RHPayment(RHAdminBase):
    """Payment settings"""

    def _process(self):
        form = SettingsForm(obj=FormDefaults(**settings.get_all()))
        if form.validate_on_submit():
            settings.set_multi(form.data)
            flash(_(u'Settings saved'), 'success')
            return redirect(url_for('.index'))
        return WPPayment.render_template('index.html', form=form)