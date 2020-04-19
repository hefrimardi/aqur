from odoo import fields, models, api


class Ruangan_aqur(models.Model):
    _name = 'daftar.ruangan'
    _description = 'Daftar ruangan aqur'
    _rec_name = 'namaRuangan'

    namaRuangan = fields.Char(string="Nama Ruangan", required=True)
    dayaTampung = fields.Integer(string='Daya Tampung', required=False)
    keterangan = fields.Text(string="Keterangan", required=False)
    jadwalRuangan = fields.One2many(comodel_name="jadwal.kelas", inverse_name="ruangan", string="Jadwal Ruangan",
                                    required=False, )
