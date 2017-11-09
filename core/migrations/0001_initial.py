# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 17:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(choices=[('1', 'ACHILLES ALMEIDA BARRETO (E. M. Prof.)'), ('2', 'AGRISA (E. M.)'), ('3', 'ALFREDINA OLIVEIRA FRANCESCONI (E. M. Prof.ª)'), ('4', 'ALFREDO CASTRO ( E. M.)'), ('5', 'ALITTA MARIA DO VALLE (E. M. Prof.ª)'), ('6', 'AMÉLIA FERREIRA (E. M. Prof.ª)'), ('7', 'AMÉRICA DOS ANJOS MONICA (E. M.)'), ('8', 'AMÉRICO VESPÚCIO (E. M.)'), ('9', 'ANA PEREIRA GONÇALVES (E. M. Prof.ª )'), ('10', 'ANGELIM (E. E. Mz)'), ('11', 'ANITA TEIXEIRA DA SILVA (E.M. de Ed. Inf. Prof.ª)'), ('12', 'ANTONIO DA CUNHA AZEVEDO (E. M.)'), ('13', 'ARAÇÁ (E. M.)'), ('14', 'ARLETE ROSA CASTANHO (E. M.)'), ('15', 'CARLOS ALBERTO GOMES DE CARVALHO (E. M.)'), ('16', 'CATHARINA DA SILVEIRA CORDEIRO (E. M . Prof.ª)'), ('17', 'CECILIA NOGUEIRA MACHADO GUIA (E. M. Prof.ª)'), ('18', 'CILÉA MARIA BARRETO (E. M. Prof.ª)'), ('19', 'CLÁUDIA MUZIO FREITAS DE OLIVEIRA (E. M. Prof.ª)'), ('20', 'CLADYR DA ROCHA MENDES (E. M. de Ed. Infantil)'), ('21', 'CLEUSA GUIMARÃES FARIA BRAGA (E. M. de Ed. Infantil)'), ('22', 'DALCY BARROSO PILLAR (E. M. de Ed. Infantil Prof.ª)'), ('23', 'DEMERVAL ALVES RANGEL (E.M. De Ed. Infantil)'), ('24', 'DEODORO AZEVEDO (E. M.)'), ('25', 'DO POMAR (E.M. de Ed. Infantil)'), ('26', 'DOMINGOS GOUVÊA (E. M.)'), ('27', 'EDILSON DUARTE (E. M. Prof.)'), ('28', 'EDITH CASTRO DOS SANTOS (E. M.)'), ('29', 'ELENICE MARTINS (Creche E. M. Prof.ª)'), ('30', 'ELENITA FERREIRA DOS SANTOS ABREU (E. M. de Ed. Infantil Prof.ª)'), ('31', 'ELICÉA DA SILVEIRA (E. M. Prof.ª)'), ('32', 'ELZA MARIA SANTA ROSA BERNARDO (Colégio M. Prof.ª)'), ('33', 'ETELVINA SANTANA DA FONSECA (E. M.)'), ('34', 'EVALDO SALLES (E. M.)'), ('35', 'FRANCISCA NAZARETH DE SOUZA (E. E. Mz.)'), ('36', 'FRANCISCO FRANCO (E. M.)'), ('37', 'IZABEL DOS SANTOS MACHADO (E.M.Prof.ª)'), ('38', 'JOÃO BESSA TEIXEIRA (E. M.)'), ('39', 'JOÃO EVANGELISTA DOS SANTOS (E. M.)'), ('40', 'JOÃO ROCHA (E. M.)'), ('41', 'JOSÉ BONIFÁCIO FERREIRA NOVELLINO (E. M.)'), ('42', 'JUSTINIANO DE SOUZA (E. M.)'), ('43', 'LAIR DIAS GAGO PEREIRA (E. M. Prof.ª)'), ('44', 'LEAQUIM SCHUINDT (E. M. Vereador)'), ('45', 'LEOMARI GARCIA BARRETO (E. M. Prof.ª)'), ('46', 'LERINÉA FIGUEIREDO (E. M. Prof.ª)'), ('47', 'LUCELÉA RODRIGUES DA COSTA (E. M. Prof.ª)'), ('48', 'LUÍZ LINDENBERG (E. M.)'), ('49', 'MANOEL MENDES DE SOUZA (E. M.)'), ('50', 'MÁRCIA FRANCESCONI PEREIRA (E. M. Prof.ª)'), ('51', 'MARIA AMÁLIA DOS SANTOS SILVEIRA (Creche E. M. Prof.ª)'), ('52', 'MARIA DARIA SALDANHA (E. M.)'), ('53', 'MARIA EMILIA DOS SANTOS CASTRO (Creche E.M.)'), ('54', 'MARIA JOSÉ BARROSO (E. M. Prof.ª)'), ('55', 'MARIA LEONÍDIA PARENTES FORTES MARTINS PINHEIRO (Creche Municipal)'), ('56', 'MARIA QUITÉRIA DA COSTA RIBEIRO (Creche Municipal Prof.ª )'), ('57', 'MARILIA DE TEVES MORENO (Creche Escola Municipal Prof.ª )'), ('58', 'MARÍLIA PLAISANT (E. M. Prof.ª)'), ('59', 'MARLI CAPP (Centro Educacional M. Prof.ª)'), ('60', 'NEUSA AGUALUSA DA COSTA (E.M. de Ed. Infantil)'), ('61', 'NILO BATISTA (Escola Agrícola Municipal)'), ('62', 'OSWALDO SANTA ROSA (E. M. Prof.)'), ('63', 'PALMIRA BESSA DE FIGUEIREDO (E. M.)'), ('64', 'PARQUE ELDORADO (Creche Escola Municipal)'), ('65', 'PATRÍCIA AZEVEDO DE ALMEIDA (E. M. Prof.ª)'), ('66', 'PAULO BURLE (E. M.)'), ('67', 'PEDRO JOTHA (E. M.)'), ('68', 'RENATO AZEVEDO (E. M.Prof.)'), ('69', 'ROBINSON CARVALHO DE AZEVEDO (E. M.)'), ('70', 'RUI BARBOSA (Colégio Municipal)'), ('71', 'RUI CAPDEVILLE (E. M. Maestro)'), ('72', 'SAMBURÁ (E.M)'), ('73', 'SANTOS ANJOS CUSTÓDIOS (E. M.)'), ('74', 'SÃO CRISTÓVÃO (E. M.)'), ('75', 'TALITA HERNANDES PERELLÓ (E. M.)'), ('76', 'TANIA MARIA GOMES DE ÁVILA (E. M. Prof.ª)'), ('77', 'TEIXEIRA E SOUZA (E. E. Mz.)'), ('78', 'THEMIRA PALMER (E. M.)'), ('79', 'TIO COTIAS (E. M. de Ed. Infantil)'), ('80', 'TOSANA (E. E. Mz.)'), ('81', 'VOVO CINHA (E. M. de Ed. Infantil)'), ('82', 'VOVO OLIVIA (E. M. de Ed. Infantil)'), ('83', 'WALDEMIRA THEREZA DE JESUS (E. M.)'), ('84', 'WANDA M.ª NOGUEIRA GONÇALVES (Creche E. M.Prof.ª)'), ('85', 'WANDA PEREIRA ROQUE (E. M. Prof.ª)'), ('86', 'YONE NOGUEIRA (E. M. de Ed. Infantil)'), ('87', 'ZÉLIO JOTHA (E. M. Prof.)')], max_length=100, verbose_name='escola')),
                ('neighborhood', models.CharField(choices=[('1', 'Agrisa'), ('2', 'Algodoal'), ('3', 'Araçá'), ('4', 'Braga'), ('5', 'Caminho de Búzios'), ('6', 'Campos Novos'), ('7', 'Célula Mater'), ('8', 'Centro'), ('9', 'Dunas do Peró'), ('10', 'Foguete'), ('11', 'Gamboa'), ('12', 'Guarani'), ('13', 'Itajuru'), ('14', 'Jacaré'), ('15', 'Jardim Caiçara'), ('16', 'Jardim Esperança'), ('17', 'Jardim Excelsior'), ('18', 'Jardim Flamboyant'), ('19', 'Jardim Machado'), ('20', 'Jardim Náutilus'), ('21', 'Jardim Olinda'), ('22', 'Jardim Peró'), ('23', 'Juscelino Kubitschek de Oliveira'), ('24', 'Manoel Correa'), ('25', 'Marina Porto Buzios'), ('26', 'Miguel Couto'), ('27', 'Ogiva'), ('28', 'Pachecos'), ('29', 'Palmeiras'), ('30', 'Balneário São Francisco'), ('31', 'Parque Burle'), ('32', 'Parque Central'), ('33', 'Parque Riviera'), ('34', 'Passagem'), ('35', 'Peró'), ('36', 'Portinho'), ('37', 'Porto do Carro'), ('38', 'Praia do Siqueira'), ('39', 'Recanto das Dunas'), ('40', 'Reserva do Peró'), ('41', 'São Bento'), ('42', 'São Cristóvão'), ('43', 'São Francisco'), ('44', 'Sao Jacinto'), ('45', 'Unamar'), ('46', 'Ville Blanche'), ('47', 'Vila do Sol'), ('48', 'Vila Nova')], max_length=100, verbose_name='bairro')),
                ('date', models.DateField(default=datetime.datetime.today, verbose_name='data')),
                ('period', models.CharField(choices=[('1', 'Primeiro Turno'), ('2', 'Segundo Turno'), ('3', 'Terceiro Turno')], max_length=100, verbose_name='turno')),
                ('time', models.CharField(choices=[('1', 'Horário de entrada dos alunos'), ('2', 'Horário de saída dos alunos'), ('3', 'Recreio'), ('4', 'Intervalo entre as aulas'), ('5', 'Contraturno'), ('6', 'Durante a aula')], max_length=100, verbose_name='ocasião')),
                ('aluno1', models.CharField(max_length=100, verbose_name='aluno 1')),
                ('turma1', models.CharField(max_length=100, verbose_name='turma do aluno 1')),
                ('idade1', models.CharField(blank=True, choices=[('1', 'Menos de 5'), ('2', 'De 5 a 8 anos'), ('3', 'De 9 a 12 anos'), ('4', 'De 12 a 15 anos'), ('5', 'De 16 a 18 anos'), ('6', 'Acima de 18 anos')], max_length=100, verbose_name='idade do aluno 1')),
                ('aluno2', models.CharField(blank=True, max_length=100, verbose_name='aluno 2')),
                ('turma2', models.CharField(blank=True, max_length=100, verbose_name='turma do aluno 2')),
                ('idade2', models.CharField(blank=True, choices=[('1', 'Menos de 5'), ('2', 'De 5 a 8 anos'), ('3', 'De 9 a 12 anos'), ('4', 'De 12 a 15 anos'), ('5', 'De 16 a 18 anos'), ('6', 'Acima de 18 anos')], max_length=100, verbose_name='idade do aluno 2')),
                ('aluno3', models.CharField(blank=True, max_length=100, verbose_name='aluno 3')),
                ('turma3', models.CharField(blank=True, max_length=100, verbose_name='turma do aluno 3')),
                ('idade3', models.CharField(blank=True, choices=[('1', 'Menos de 5'), ('2', 'De 5 a 8 anos'), ('3', 'De 9 a 12 anos'), ('4', 'De 12 a 15 anos'), ('5', 'De 16 a 18 anos'), ('6', 'Acima de 18 anos')], max_length=100, verbose_name='idade do aluno 3')),
                ('aluno4', models.CharField(blank=True, max_length=100, verbose_name='aluno 4')),
                ('turma4', models.CharField(blank=True, max_length=100, verbose_name='turma do aluno 4')),
                ('idade4', models.CharField(blank=True, choices=[('1', 'Menos de 5'), ('2', 'De 5 a 8 anos'), ('3', 'De 9 a 12 anos'), ('4', 'De 12 a 15 anos'), ('5', 'De 16 a 18 anos'), ('6', 'Acima de 18 anos')], max_length=100, verbose_name='idade do aluno 4')),
                ('envolved', models.CharField(blank=True, choices=[('1', 'Professor'), ('2', 'Funcionário da escola'), ('3', 'Responsável por aluno'), ('4', 'Desconhecido'), ('5', 'Ex-aluno'), ('6', 'Outro')], max_length=100, verbose_name='outros envolvidos')),
                ('envolved_description', models.CharField(blank=True, max_length=100, verbose_name='descrição envolvidos')),
                ('kind', models.CharField(choices=[('1', 'Acidente envolvendo aluno'), ('2', 'Acidente envolvendo funcionário'), ('3', 'Agressão física'), ('4', 'Agressão verbal'), ('5', 'Atraso'), ('6', 'Bullying'), ('7', 'Bullying virtual'), ('8', 'Desacato ao professor ou funcionário'), ('9', 'Evasão da escola sem permissão'), ('10', 'Indisciplina'), ('11', 'Porte de armas'), ('12', 'Porte de drogas'), ('13', 'Recusa a entrar ou retornar para a sala de aula'), ('14', 'Roubo'), ('15', 'Sinais de abuso'), ('16', 'Sinais de maus tratos'), ('17', 'Uso de drogas'), ('18', 'Venda de drogas'), ('19', 'Atentado ao Pudor'), ('20', 'Outro')], max_length=100, verbose_name='tipo de ocorrência')),
                ('description_kind', models.TextField(verbose_name='descrição do tipo de ocorrência')),
                ('measures', models.CharField(choices=[('1', 'Advertência verbal'), ('2', 'Advertência escrita'), ('3', 'Comunicação ao responsável'), ('4', 'Suspensão de aulas'), ('5', 'Transferência compulsória')], max_length=100, verbose_name='medidas tomadas')),
                ('measures_description', models.TextField(verbose_name='descrição das medidas')),
                ('contact', models.CharField(max_length=100, verbose_name='responsável pelo preenchimento')),
            ],
        ),
    ]
