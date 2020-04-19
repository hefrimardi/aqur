from odoo import fields, models, api


class Program_aqur(models.Model):
    _name = 'program.aqur'
    _description = 'Program studi yang ada di Yayasan Aqur'
    _rec_name = 'namaProgram'

    namaProgram = fields.Char(string='Nama Program', required=True, translate=True)
    departemenProgram = fields.Many2one(comodel_name='hr.department', string='Unit Kerja', required=True)
    penanggungJawabProgram = fields.Many2one(comodel_name='hr.employee', string='Penanggung Jawab', required=False)
    tglMulai = fields.Date(string="Tanggal dimulai", required=True)
    tglBerakhir = fields.Date(string='Tanggal Berakhir', required=False)
    berlanjutkah = fields.Boolean(string="Berlanjutkah", default=True)

    # untuk mengisi bagian notebook di form view mode
    programLevelID = fields.One2many(comodel_name="program.level", inverse_name="programID", string="Program Level",
                                     required=False, )


class Program_level_aqur(models.Model):
    _name = 'program.level'
    _description = 'Level/tingkatan program'
    _rec_name = 'levelProgram'

    programID = fields.Many2one(model="program.aqur", string="ID Program", required=False)
    levelProgram = fields.Char(string="Level", required=True)
    namaLevel = fields.Char(string="Nama Level", required=True)
    keteranganLevel = fields.Text(string="Keterangan", required=False)
