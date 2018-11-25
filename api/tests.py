# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
# /api/tests.py


from api.models.dashboards import Dashboard


class ModelTestCase(TestCase):
    """This class defines the test suite for the dashboard model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.dashboard_name = "outbox"
        self.dashboard = Dashboard(name=self.dashboard_name)

    def test_model_can_create_a_dashboard(self):
        """Test the dashboard model can create a dashboard."""
        old_count = Dashboard.objects.count()
        self.dashboard.save()
        new_count = Dashboard.objects.count()
        self.assertNotEqual(old_count, new_count)
