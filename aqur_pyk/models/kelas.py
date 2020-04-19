from odoo import fields, models, api
from datetime import datetime as dt, date, timedelta as tmd
from lxml import etree

class Daftar_kelas_aqur(models.Model):
    _name = 'daftar.kelas'
    _description = 'Daftar kelas'
    _rec_name = 'namaKelas'

    def buatJadwal(self):
        for rec in self:
            lines = [(5, 0, 0)]
            tahun = dt.today().year
            bulan = dt.today().month
            # hari = dt.today().day
            x_hari = date(tahun,bulan,1)

            for line in rec.jadwalKelasID:
                x_hari = self.tanggalDariHari(tahun, bulan, line.jadwalHari)
                if x_hari.month != bulan:
                    x_hari += tmd(days=7)
                while x_hari.month == bulan:
                    waktuMulaiInDetik = line.jadwalJam * 3600
                    waktuSelesaiInDetik = waktuMulaiInDetik + line.jadwalDurasi * 60
                    valuenya = {
                        'namaKelasKalender': line.id,
                        'waktuMulaiKalender': dt(tahun, bulan, x_hari.day,
                                                 int(waktuMulaiInDetik // 3600) - 7,
                                                 int((waktuMulaiInDetik % 3600) / 60), 0),
                        'waktuSelesaiKalender': dt(tahun, bulan, x_hari.day,
                                                   int(waktuSelesaiInDetik // 3600) - 7,
                                                   int((waktuSelesaiInDetik % 3600) / 60), 0),
                        'ruanganKalender': line.ruangan.id,
                        'guruKalender': rec.guruKelas.id
                    }
                    lines.append([0, 0, valuenya])
                    x_hari += tmd(days=7)
            rec.kalenderKelasID = lines

    def tanggalDariHari(self, tahun, bulan, hari):
        listHari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu']
        indekHari = listHari.index(hari)
        tglHarinya = date(tahun, bulan, 1)
        tglHarinya += tmd(days=indekHari - tglHarinya.weekday())
        return tglHarinya

    namaKelas = fields.Char(string='Nama Kelas', required=True)
    namaProgram = fields.Many2one(comodel_name="program.aqur", string="Nama Program", required=True)
    levelProgram = fields.Many2one(comodel_name="program.level", string="Level", required=False)
    guruKelas = fields.Many2one(comodel_name="hr.employee", string="Guru Kelas", required=True)
    kategoriKelas = fields.Many2one(comodel_name="kategori.kelas", string="Kategori Kelas", required=True)
    jadwalKelasID = fields.One2many(comodel_name="jadwal.kelas", inverse_name="daftarKelasID", required=False,
                                    string="Jadwal Kelas")
    daftarMuridID = fields.One2many(comodel_name="daftar.murid.kelas", inverse_name="daftarKelasID", required=False,
                                    string="Daftar Murid")
    berlanjutkah = fields.Boolean(string="Berlanjutkah", default=True)
    kalenderKelasID = fields.One2many(comodel_name="kalender.kelas", inverse_name="namaKelasKalender",
                                      string="Kalender Kelas ID", required=False)

    @api.onchange('namaProgram')
    def _onchange_namaProgram(self):
        for rec in self:
            return {'domain': {'levelProgram': [('programID', '=', rec.namaProgram.id)]}}


class Jadwal_kelas_aqur(models.Model):
    _name = 'jadwal.kelas'
    _description = 'Jadwal kelas aqur'
    _rec_name = 'daftarKelasID'

    daftarKelasID = fields.Many2one(comodel_name="daftar.kelas", string="Nama Kelas", required=True)
    jadwalHari = fields.Selection(string="Hari", selection=[
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', 'Jumat'),
        ('sabtu', 'Sabtu'),
        ('minggu', 'Minggu')], required=True)
    jadwalJam = fields.Float(string="Mulai Pukul", required=True)
    jadwalDurasi = fields.Integer(string="Durasi (menit)", required=True)
    ruangan = fields.Many2one(comodel_name="daftar.ruangan", string="Ruangan", required=False)


class daftar_murid_kelas(models.Model):
    _name = 'daftar.murid.kelas'
    _description = 'Daftar Murid di Kelas'
    _rec_name = 'namaMurid'

    namaMurid = fields.Many2one(comodel_name="res.partner", string="Nama Murid", required=False, )
    daftarKelasID = fields.Many2one(comodel_name="daftar.kelas", string="Nama Kelas", required=True)


class Kategori_kelas(models.Model):
    _name = 'kategori.kelas'
    _description = 'Kategori kelas'
    _rec_name = 'namaKategori'

    namaKategori = fields.Char(string="Nama Kategori", required=True)
    jenisSPP = fields.Many2one(comodel_name="product.template", string="Jenis SPP", required=True)
    kelasID = fields.One2many(comodel_name="daftar.kelas", inverse_name="kategoriKelas", string="Daftar Kelas",
                              required=False)


class kalender_kelas(models.Model):
    _name = 'kalender.kelas'
    _description = 'Daftar Kalender Kelas'
    _rec_name = "namaKelasKalender"

    namaKelasKalender = fields.Many2one(comodel_name="daftar.kelas", string="Nama Kelas", required=True)
    waktuMulaiKalender = fields.Datetime(string="Waktu Mulai", required=False)
    waktuSelesaiKalender = fields.Datetime(string="Waktu Selesai", required=False)
    ruanganKalender = fields.Many2one(comodel_name="daftar.ruangan", string="Nama Ruangan", required=False)
    guruKalender = fields.Many2one(comodel_name="hr.employee", string="Nama Guru", required=False, )
