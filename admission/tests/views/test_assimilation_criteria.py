##############################################################################
#
# OSIS stands for Open Student Information System. It's an application
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
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from admission.models import applicant
from admission.views import assimilation_criteria
from django.utils.encoding import force_text
import json
from admission import models as mdl
from django.contrib.auth.models import User
import admission.tests.data_for_tests as data_model
from django.test import Client


class AssimilationCriteriaTest(TestCase):

    def test_criteria1_list_size(self):
        list_document_type = []
        list_document_type = assimilation_criteria.criteria1(list_document_type)
        self.assertTrue(len(list_document_type) == 2)

        list_document_type = assimilation_criteria.criteria1(None)
        self.assertTrue(len(list_document_type) == 2)

        list_document_type = []
        assimilation_doc = assimilation_criteria.AssimilationDoc()
        assimilation_doc.criteria_id = 1
        list_document_type.append(assimilation_doc)
        list_document_type = assimilation_criteria.criteria1(list_document_type)
        self.assertTrue(len(list_document_type) == 3)

    def test_criteria2_list_size(self):
        list_document_type = []
        list_document_type = assimilation_criteria.criteria2(list_document_type)
        self.assertTrue(len(list_document_type) == 5)

        list_document_type = assimilation_criteria.criteria2(None)
        self.assertTrue(len(list_document_type) == 5)

    def test_find_list_document_type_by_criteria_size(self):
        list_document_type = assimilation_criteria.find_list_document_type_by_criteria(None)
        self.assertTrue(len(list_document_type) == 0)

        list_document_type = assimilation_criteria.find_list_document_type_by_criteria("1")
        self.assertTrue(len(list_document_type) == 0)

        list_document_type = assimilation_criteria.find_list_document_type_by_criteria(1)
        self.assertTrue(len(list_document_type) == 2)

    def test_get_list_documents_descriptions_size(self):
        list_document_type = assimilation_criteria.get_list_documents_descriptions(None)
        self.assertTrue(len(list_document_type) == 0)

        list_document_type = assimilation_criteria.get_list_documents_descriptions("1")
        self.assertTrue(len(list_document_type) == 0)

        list_document_type = assimilation_criteria.get_list_documents_descriptions(3)
        self.assertTrue(len(list_document_type) == 9)

