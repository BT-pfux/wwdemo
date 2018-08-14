##############################################################################
#
#    Copyright (c) 2018 brain-tec AG (http://www.braintec-group.com)
#    All Right Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'WW Wizard Prototype',
    'summary': 'WW Wizard Prototype',
    'category': '',
    'version': '11.0.0.1.0',
    'author': 'brain-tec AG',
    'license': 'AGPL-3',
    'website': 'http://www.braintec-group.com/en/',
    'depends': ['cms_form',
                'sale_subscription',
                'website_quote',
                'website_sale',
                'website_sign'],
    'data': ['templates/form_ext.xml',
             'templates/signup_ext.xml',
             'templates/assets.xml', ],
}
