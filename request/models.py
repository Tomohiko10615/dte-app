from django.db import models

DOCUMENT_TYPE = [
    ('factura', 'Factura Electrónica'),
    ('boleta', 'Boleta de Venta Electrónica'),
    ('notacredito', 'Nota de Crédito Electrónica'),
    ('notadebito', 'Nota de Débito Electrónica'),
    ('comprobante', 'Comprobante de Retención'),
]

DOCUMENT_TYPE_DICT = {
    'factura': 'Factura Electrónica',
    'boleta': 'Boleta de Venta Electrónica',
    'notacredito': 'Nota de Crédito Electrónica',
    'notadebito': 'Nota de Débito Electrónica',
    'comprobante': 'Comprobante de Retención',
}

class Request(models.Model):
    documento = models.TextField(
        choices = DOCUMENT_TYPE,
        default = 'factura',
    )
    serie = models.CharField(max_length = 4)
    correlativo = models.CharField(max_length = 6)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits = 7, decimal_places = 2)
    archivo = models.FileField(upload_to = 'uploads/')

    def __str__(self):
        return DOCUMENT_TYPE_DICT[self.documento] + ' ' + self.serie + '-' + self.correlativo


