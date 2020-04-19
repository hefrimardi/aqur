# -*- coding: utf-8 -*-
# from odoo import http


# class AqurPyk(http.Controller):
#     @http.route('/aqur_pyk/aqur_pyk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aqur_pyk/aqur_pyk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aqur_pyk.listing', {
#             'root': '/aqur_pyk/aqur_pyk',
#             'objects': http.request.env['aqur_pyk.aqur_pyk'].search([]),
#         })

#     @http.route('/aqur_pyk/aqur_pyk/objects/<model("aqur_pyk.aqur_pyk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aqur_pyk.object', {
#             'object': obj
#         })
