from odoo import api, models, fields
from odoo import exceptions
from psycopg2 import IntegrityError
from werkzeug.utils import redirect

from odoo.http import request

class WWWizard(models.AbstractModel):
    """A wizard form."""

    _name = 'wizard'
    _inherit = 'cms.form.wizard'
    _wiz_name = _name

    def wiz_configure_steps(self):
        return {
            1: {'form_model': 'child.wizard',
                'title': "Tarifierung"},
            2: {'form_model': 'resume.wizard',
                'title': "Vorschlag"},
            3: {'form_model': 'order.insurance',
                'title': "Antragserstellung"},
        }

    @api.model
    def create(self, vals):
        pass


class ChildSelectionWizard(models.AbstractModel):

    _name = 'child.wizard'
    _inherit = 'wizard'
    _form_model = 'ww.insurance.wizard'
    _form_required_fields = ('start_date','child_birth_1','overnight_rate_1', )
    _form_fields_hidden = ('user_id','child_birth_2','overnight_rate_2', 'is_active_2','child_birth_3','overnight_rate_3','is_active_3')
    _form_fieldsets = [
        {
            'id': 'main',
            'title': '',
            'fields': [
                'start_date',
            ],
        },
        {
            'id': 'insured_people',
            'title': 'Versicherte Person 1 (Versicherungsnehmer)',
            'fields': [
                'child_birth_1',
                'overnight_rate_1',
            ],
        }
    ]

    user_id = fields.Many2one("res.users")
    start_date = fields.Selection([('01.08.2018', '01.08.2018'),
                                   ('01.09.2018', '01.09.2018'),
                                   ('01.10.2018', '01.10.2018'),
                                   ('01.11.2018', '01.11.2018'),
                                   ('01.12.2018', '01.12.2018'),
                                   ('01.01.2019', '01.01.2019'),
                                   ('01.02.2019', '01.02.2019')],
                                  string="Gewünschter Versicherungsbeginn")
    child_birth_1 = fields.Date(string="Geburtsdatum")
    child_birth_2 = fields.Date(string="Geburtsdatum")
    child_birth_3 = fields.Date(string="Geburtsdatum")
    overnight_rate_1 = fields.Selection([('10', '10 €'),
                                       ('15', '15 €'),
                                       ('20', '20 €'),
                                       ('25', '25 €'),
                                       ('30', '30 €'),
                                       ('35', '35 €'),
                                       ('40', '40 €'),
                                       ('45', '45 €'),
                                       ('50', '50 €'),
                                       ('55', '55 €'),
                                       ('60', '60 €'),
                                       ('65', '65 €'),
                                       ('70', '70 €'),
                                       ('75', '75 €')], default='65', string="Tagegeldsatz")
    overnight_rate_2 = fields.Selection([('10', '10'),
                                       ('15', '15'),
                                       ('20', '20'),
                                       ('25', '25'),
                                       ('30', '30'),
                                       ('35', '35'),
                                       ('40', '40'),
                                       ('45', '45'),
                                       ('50', '50'),
                                       ('55', '55'),
                                       ('60', '60'),
                                       ('65', '65'),
                                       ('70', '70'),
                                       ('75', '75')], default='65')
    overnight_rate_3 = fields.Selection([('10', '10'),
                                       ('15', '15'),
                                       ('20', '20'),
                                       ('25', '25'),
                                       ('30', '30'),
                                       ('35', '35'),
                                       ('40', '40'),
                                       ('45', '45'),
                                       ('50', '50'),
                                       ('55', '55'),
                                       ('60', '60'),
                                       ('65', '65'),
                                       ('70', '70'),
                                       ('75', '75')], default='65')

    is_active_2 = fields.Boolean()
    is_active_3 = fields.Boolean()

    @property
    def form_title(self):
        return 'Pflegetagegeld-Versicherung: Eingabe Ihrer Tarifierungsdaten'


class WWResumeInsurance(models.AbstractModel):

    _name = 'resume.wizard'
    _inherit = 'child.wizard'
    _form_model = 'sale.order'
    _form_model_fields = ()

    @property
    def form_title(self):
        return 'Pflegetagegeld-Versicherung: Eingabe Ihrer Tarifierungsdaten'


class WWSaleOrder(models.AbstractModel):

    _name = 'order.insurance'
    _inherit = 'wizard'
    _form_model = 'sale.order'
    _form_model_fields = ()

    @property
    def form_title(self):
        return 'Pflegetagegeld-Versicherung: Eingabe Ihrer Tarifierungsdaten'
