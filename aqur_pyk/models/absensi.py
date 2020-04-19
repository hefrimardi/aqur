from odoo import fields, models, api


class absensi_pbm_aqur(models.Model):
    _name = 'absensi.pbm'
    _description = 'Absensi murid dan guru sewaktu PBM'
    _rec_name = 'namaKelas'

    namaKelas = fields.Many2one(comodel_name="daftar.kelas", string="Nama Kelas", required=True)
    tanggalAbsensi = fields.Datetime(string="Tanggal", required=True)
    namaGuru = fields.Many2one(comodel_name="hr.employee", string="Nama Guru", required=False,
                               related="namaKelas.guruKelas", readonly=True)
    guruPengganti = fields.Many2one(comodel_name="hr.employee", string="Guru Pengganti", required=False, )
    absensiDetailID = fields.One2many(comodel_name="absensi.pbm.detail", inverse_name="absensiID",
                                      string="Absensi Detail", required=False)

    @api.onchange('namaKelas')
    def _onchange_namaKelas(self):
        for rec in self:
            lines = [(5,0,0)]
            for line in self.namaKelas.daftarMuridID:
                vals = {
                    'namaMurid': line.id,
                }
                lines.append([0,0,vals])
            rec.absensiDetailID = lines


class absensi_pbm_detail(models.Model):
    _name = 'absensi.pbm.detail'
    _description = 'Absensi PBM detail'

    absensiID = fields.Many2one(comodel_name="absensi.pbm", string="ID Absensi", required=False)
    namaMurid = fields.Many2one(comodel_name="daftar.murid.kelas", string="Nama Murid", required=True)
    statusKehadiran = fields.Selection(string="Status Kehadiran", selection=[
        ('hadir', 'Hadir'),
        ('sakit', 'Sakit'),
        ('Alpa', 'Alpa')], required=True)