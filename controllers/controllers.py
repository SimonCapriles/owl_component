# -*- coding: utf-8 -*-
# from odoo import http


# class OwlComponent(http.Controller):
#     @http.route('/owl_component/owl_component', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl_component/owl_component/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl_component.listing', {
#             'root': '/owl_component/owl_component',
#             'objects': http.request.env['owl_component.owl_component'].search([]),
#         })

#     @http.route('/owl_component/owl_component/objects/<model("owl_component.owl_component"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl_component.object', {
#             'object': obj
#         })
