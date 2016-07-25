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

from django.test import TestCase, Client
from base.models import student, person
import performance.views.main as perf_views
from django.contrib.auth.models import User


class TemplatesPerformanceTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create student user
        self.createStudentUser()

    def createStudentUser(self):
        self.student_username = "user_student"
        self.student_password = "user_pass"
        user_student = User.objects.create_user(self.student_username, password=self.student_password)
        person_student = person.Person(user=user_student,
                                       global_id="45451000",
                                       first_name="Student",
                                       last_name="Etudiant",
                                       email="student@stud.com")
        person_student.save()
        self.stud = student.Student(person=person_student,
                                    registration_id="45451000")
        self.stud.save()

    def testHomeUnlogged(self):
        # User is not logged
        # result/2015/sinf2msg/
        response = self.client.get("/performance/")

        # Check resolver function, status code and finally template(s) used.
        self.assertEqual(response.resolver_match.func, perf_views.home)
        self.assertRedirects(response, "/login/?next=/performance/")

    def testHomeLogged(self):
        # User is logged
        self.client.login(username=self.student_username, password=self.student_password)

        response = self.client.get("/performance/")

        self.assertEqual(response.resolver_match.func, perf_views.home)
        self.assertEqual(response.status_code, 200, "Logged in student user should be able to "
                                                    "access performance app")
        self.assertTemplateUsed(response=response, template_name="performance_home.html")

        self.client.logout()
