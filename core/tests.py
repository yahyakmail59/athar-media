# -*- coding: utf-8 -*-
"""Tests for the portfolio cover pipeline.

A project cover is whatever the phone or the designer handed over, and the
card that shows it is a fixed 4:3 box. These cover the normalising step that
sits between the two, because it fails silently: a broken crop still saves,
still renders, and is only noticed as a squashed photo on the live site.
"""
import io
import shutil
import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from PIL import Image

from .models import COVER_HEIGHT, COVER_WIDTH, Project

MEDIA_ROOT = tempfile.mkdtemp()


def _upload(name, size, mode="RGB", fmt="JPEG"):
    """An in-memory upload of the given shape, as the admin would send it."""
    colour = (200, 60, 60, 128) if mode == "RGBA" else (200, 60, 60)
    buffer = io.BytesIO()
    Image.new(mode, size, colour).save(buffer, fmt)
    return SimpleUploadedFile(name, buffer.getvalue())


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class ProjectCoverTests(TestCase):
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def _project(self, upload=None):
        project = Project(title_ar='مطعم', title_en='Restaurant', category='restaurant')
        if upload is not None:
            project.image = upload
        project.save()
        return project

    def test_any_shape_becomes_the_cards_four_by_three(self):
        """The card crops with object-fit, so the stored file must match it."""
        for label, size in (
            ('portrait', (3000, 4000)),
            ('panorama', (2400, 900)),
            ('square', (1200, 1200)),
            ('smaller than the card', (300, 200)),
        ):
            with self.subTest(label):
                project = self._project(_upload('cover.jpg', size))
                with Image.open(project.image.path) as image:
                    self.assertEqual(image.size, (COVER_WIDTH, COVER_HEIGHT))

    def test_every_upload_is_stored_as_webp(self):
        project = self._project(_upload('cover.png', (1600, 900), fmt='PNG'))
        self.assertTrue(project.image.name.endswith('.webp'))
        with Image.open(project.image.path) as image:
            self.assertEqual(image.format, 'WEBP')

    def test_transparency_is_flattened_rather_than_left_to_show_the_card(self):
        """A transparent cover would let the card's navy through the photo."""
        project = self._project(_upload('logo.png', (1200, 1200), mode='RGBA', fmt='PNG'))
        with Image.open(project.image.path) as image:
            self.assertNotIn('A', image.mode)

    def test_a_later_save_does_not_re_encode_the_cover(self):
        """Re-encoding on every edit would degrade the image over time."""
        project = self._project(_upload('cover.jpg', (2000, 1500)))
        name, size = project.image.name, project.image.size

        project.client_name = 'عميل'
        project.save()
        project.refresh_from_db()

        self.assertEqual(project.image.name, name)
        self.assertEqual(project.image.size, size)

    def test_a_project_without_a_cover_still_saves(self):
        """An empty image is what makes the template fall back to the mockup."""
        project = self._project()
        self.assertFalse(project.image)
