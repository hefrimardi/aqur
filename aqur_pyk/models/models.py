# -*- coding: utf-8 -*-


from odoo import models, fields, api


class Aqur_kontak_inherit(models.Model):
    _inherit = 'res.partner'

    # Menambah field kategori kontak di model res.partner
    kategoriKontak = fields.Selection(string="Kategori Kontak", selection=[
        ('murid', 'Murid'),
        ('guru', 'Guru'),
        ('karyawan', 'Karyawan'),
        ('umum', 'Umum')], required=True, default='murid', translate=True)
    daftarKelasID = fields.One2many(comodel_name="daftar.murid.kelas", inverse_name="namaMurid", string="Daftar Kelas", required=False, )


class Aqur_karyawan_inherit(models.Model):
    _inherit = 'hr.employee'

    kelasID = fields.One2many(comodel_name="daftar.kelas", inverse_name="guruKelas", string="Daftar Kelas", required=False, )
