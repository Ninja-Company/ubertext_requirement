# -*- coding: utf-8 -*-
from odoo import http

# class UbertextRequirement(http.Controller):
#     @http.route('/ubertext_requirement/ubertext_requirement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ubertext_requirement/ubertext_requirement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ubertext_requirement.listing', {
#             'root': '/ubertext_requirement/ubertext_requirement',
#             'objects': http.request.env['ubertext_requirement.ubertext_requirement'].search([]),
#         })

#     @http.route('/ubertext_requirement/ubertext_requirement/objects/<model("ubertext_requirement.ubertext_requirement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ubertext_requirement.object', {
#             'object': obj
#         })