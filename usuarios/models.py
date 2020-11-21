from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Usuario(models.Model):
  identificacao = models.IntegerField()
  nome = models.CharField(max_length=256)
  data_nascimento = models.DateField()

  tel_validators = [
    MinValueValidator(999999999, 'Insira um telefone válido, ex: 11987654321'), # asseguramos que o telefone tenha
    MaxValueValidator(100000000000, 'Insira um telefone válido, ex: 11987654321') # entre 10 e 11 números (DDD+telefone)
  ]

  tel_residencial = models.PositiveBigIntegerField(validators=tel_validators)
  tel_comercial = models.PositiveBigIntegerField(validators=tel_validators, null=True, blank=True)
  endereco_residencial = models.CharField(max_length=256)
  endereco_comercial = models.CharField(max_length=256, null=True, blank=True)
  facebook = models.URLField(max_length=256, null=True, blank=True)
  linkedin = models.URLField(max_length=256, null=True, blank=True)
  twitter = models.URLField(max_length=256, null=True, blank=True)
  instagram = models.URLField(max_length=256, null=True, blank=True)
  CPF = models.PositiveBigIntegerField(validators=[
    MinValueValidator(9999999999, 'Insira um CPF válido, ex: 123.456.789-01'), # Asseguramos que o CPF
    MaxValueValidator(100000000000, 'Insira um CPF válido, ex: 123.456.789-01') # tenha 11 dígitos
  ])
  RG = models.PositiveBigIntegerField(validators=[
    MinValueValidator(99999999, 'Insira um RG válido, ex: 12.345.678-9'), # Asseguramos que o RG tenha
    MaxValueValidator(1000000000, 'Insira um RG válido, ex: 12.345.678-9') # 9 dígitos
  ])