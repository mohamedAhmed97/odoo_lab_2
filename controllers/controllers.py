# -*- coding: utf-8 -*-
# from odoo import http


# class CallCenter1(http.Controller):
#     @http.route('/call_center1/call_center1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/call_center1/call_center1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('call_center1.listing', {
#             'root': '/call_center1/call_center1',
#             'objects': http.request.env['call_center1.call_center1'].search([]),
#         })

#     @http.route('/call_center1/call_center1/objects/<model("call_center1.call_center1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('call_center1.object', {
#             'object': obj
#         })
