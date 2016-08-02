##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2016 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class AdmissionDocumentFile(models.Model):
    applicant = models.ForeignKey('Applicant')
    document_file = models.ForeignKey('osis_common.documentFile')


def search(applicant=None, description=None):
    out = None
    queryset = AdmissionDocumentFile.objects.order_by('document_file__creation_date')
    if applicant:
        queryset = queryset.filter(applicant=applicant)
    if description:
        queryset = queryset.filter(document_file__description=description)
    if applicant or description:
        out = queryset
    return out




